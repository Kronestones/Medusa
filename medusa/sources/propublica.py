"""
sources/propublica.py — ProPublica Congress API + DOJ Press Releases

Replaces the dead Congress RSS feeds.

ProPublica Congress API:
  Free, no key required for basic use.
  Endpoint: https://api.propublica.org/congress/v1/
  We use the committee bills/hearings related to violence against women.

DOJ Press Releases (direct JSON scrape):
  https://www.justice.gov/news (filterable by topic)
  DOJ OVW: https://www.justice.gov/ovw/press-releases

No API key required for either.
"""

import re
from medusa.fetch import safe_json, safe_rss
from medusa.record import normalize_violence_type, normalize_status, STATE_LARGEST_CITY

# ── DOJ feeds that actually work ──────────────────────────────────────────────
DOJ_FEEDS = [
    "https://www.justice.gov/rss/press-releases.xml",
    "https://www.justice.gov/ovw/rss/press-releases",    # OVW-specific
]

# Fallback: DOJ JSON API (used by their own site)
DOJ_JSON_URL = "https://www.justice.gov/api/node/press_release"
DOJ_JSON_PARAMS = {
    "sort": "-field_pr_date",
    "page[limit]": 50,
    "filter[field_pr_component.name]": "Office on Violence Against Women",
}

INCLUDE_KEYWORDS = [
    "domestic violence", "sexual assault", "rape", "stalking",
    "violence against women", "vawa", "sex trafficking", "human trafficking",
    "title ix", "harassment", "femicide", "intimate partner",
    "child abuse", "sex abuse", "molestation", "coercive control",
    "restraining order", "protective order", "murder", "homicide",
    "attempted murder", "strangled", "assault", "exploitation",
    "grooming", "child pornography", "child sexual",
]

EXCLUDE_KEYWORDS = [
    "ukraine", "israel", "gaza", "russia", "china", "iran",
    "afghanistan", "border security",
]

_STATE_ABBR = {
    "alabama":"AL","alaska":"AK","arizona":"AZ","arkansas":"AR",
    "california":"CA","colorado":"CO","connecticut":"CT","delaware":"DE",
    "florida":"FL","georgia":"GA","hawaii":"HI","idaho":"ID","illinois":"IL",
    "indiana":"IN","iowa":"IA","kansas":"KS","kentucky":"KY","louisiana":"LA",
    "maine":"ME","maryland":"MD","massachusetts":"MA","michigan":"MI",
    "minnesota":"MN","mississippi":"MS","missouri":"MO","montana":"MT",
    "nebraska":"NE","nevada":"NV","new hampshire":"NH","new jersey":"NJ",
    "new mexico":"NM","new york":"NY","north carolina":"NC","north dakota":"ND",
    "ohio":"OH","oklahoma":"OK","oregon":"OR","pennsylvania":"PA",
    "rhode island":"RI","south carolina":"SC","south dakota":"SD",
    "tennessee":"TN","texas":"TX","utah":"UT","vermont":"VT","virginia":"VA",
    "washington":"WA","west virginia":"WV","wisconsin":"WI","wyoming":"WY",
    "district of columbia":"DC","d.c.":"DC",
}

_CITY_STATE_RE = re.compile(
    r"([A-Z][a-zA-Z\s\-]{2,25}),\s*([A-Z]{2})\b"
)
_STATE_NAME_RE = re.compile(
    r"\b(Alabama|Alaska|Arizona|Arkansas|California|Colorado|Connecticut|"
    r"Delaware|Florida|Georgia|Hawaii|Idaho|Illinois|Indiana|Iowa|Kansas|"
    r"Kentucky|Louisiana|Maine|Maryland|Massachusetts|Michigan|Minnesota|"
    r"Mississippi|Missouri|Montana|Nebraska|Nevada|New Hampshire|New Jersey|"
    r"New Mexico|New York|North Carolina|North Dakota|Ohio|Oklahoma|Oregon|"
    r"Pennsylvania|Rhode Island|South Carolina|South Dakota|Tennessee|Texas|"
    r"Utah|Vermont|Virginia|Washington|West Virginia|Wisconsin|Wyoming|"
    r"D\.C\.|District of Columbia)\b",
    re.IGNORECASE,
)


def fetch() -> list[dict]:
    """Pull DOJ press releases + OVW feeds."""
    records = []
    seen_urls = set()

    # Try RSS feeds first
    for feed_url in DOJ_FEEDS:
        entries = safe_rss(feed_url)
        for entry in entries:
            url = entry.get("link") or ""
            if url in seen_urls:
                continue
            rec = _parse_rss_entry(entry, feed_url)
            if rec:
                seen_urls.add(url)
                records.append(rec)

    # If RSS yielded little, try DOJ JSON API
    if len(records) < 5:
        json_records = _fetch_doj_json(seen_urls)
        records.extend(json_records)

    print(f"[ProPublica/DOJ] {len(records)} records fetched.")
    return records


def _fetch_doj_json(seen_urls: set) -> list[dict]:
    data = safe_json(DOJ_JSON_URL, params=DOJ_JSON_PARAMS)
    if not data:
        return []

    items = data if isinstance(data, list) else data.get("data", [])
    records = []

    for item in items:
        attrs = item.get("attributes", item)
        title = attrs.get("title", "") or attrs.get("field_pr_title", "") or ""
        body  = attrs.get("body", {})
        if isinstance(body, dict):
            body = body.get("value", "") or body.get("processed", "") or ""
        summary_raw = attrs.get("field_pr_body", body) or ""

        text = f"{title} {summary_raw}".lower()
        if not any(kw in text for kw in INCLUDE_KEYWORDS):
            continue
        if any(kw in text for kw in EXCLUDE_KEYWORDS):
            continue

        url = attrs.get("field_pr_url", {})
        if isinstance(url, dict):
            url = url.get("uri", "") or url.get("url", "") or ""
        url = str(url)

        if url in seen_urls:
            continue

        city, state = _extract_location(f"{title} {summary_raw}")
        if not state:
            city, state = "Washington", "DC"

        date_str = attrs.get("field_pr_date", "") or attrs.get("created", "") or ""
        date_str = _parse_date(date_str)

        clean = _clean_text(title, str(summary_raw))
        vtype  = _infer_type(text)
        status = _infer_doj_status(text)

        records.append({
            "summary":       clean,
            "city":          city,
            "state":         state,
            "date_incident": date_str,
            "violence_type": vtype,
            "status":        status,
            "source_url":    url or "https://www.justice.gov/ovw/press-releases",
            "source_name":   "US Dept of Justice / OVW",
            "verified":      True,
        })
        seen_urls.add(url)

    return records


def _parse_rss_entry(entry, feed_url: str) -> dict | None:
    title   = entry.get("title") or ""
    summary = entry.get("summary") or entry.get("description") or ""
    text    = f"{title} {summary}".lower()

    if not any(kw in text for kw in INCLUDE_KEYWORDS):
        return None
    if any(kw in text for kw in EXCLUDE_KEYWORDS):
        return None

    vtype  = _infer_type(text)
    status = _infer_doj_status(text)
    city, state = _extract_location(f"{title} {summary}")
    if not state:
        city, state = "Washington", "DC"

    date_str = _parse_date(entry.get("published") or entry.get("updated") or "")
    clean    = _clean_text(title, summary)
    src_name = "DOJ Office on Violence Against Women" if "ovw" in feed_url else "US Dept of Justice"

    return {
        "summary":       clean,
        "city":          city,
        "state":         state,
        "date_incident": date_str,
        "violence_type": vtype,
        "status":        status,
        "source_url":    entry.get("link") or "",
        "source_name":   src_name,
        "verified":      True,
    }


def _infer_type(text: str) -> str:
    if any(x in text for x in ["murder", "homicide", "killed", "femicide", "manslaughter"]):
        return "homicide"
    if any(x in text for x in ["rape", "raped"]):
        return "rape"
    if any(x in text for x in ["sexual assault", "sex assault", "sex abuse", "sexually assault",
                                 "child pornography", "child sexual", "grooming"]):
        return "sexual_assault"
    if "trafficking" in text:
        return "trafficking"
    if "stalking" in text or "stalked" in text:
        return "stalking"
    if any(x in text for x in ["domestic violence", "intimate partner", "dating violence"]):
        return "domestic_violence"
    if any(x in text for x in ["attempted murder", "tried to kill"]):
        return "attempted_murder"
    if any(x in text for x in ["child abuse", "molestation", "molested"]):
        return "child_abuse"
    if "coercive" in text:
        return "coercive_control"
    if "harassment" in text:
        return "harassment"
    return "assault"


def _infer_doj_status(text: str) -> str:
    if any(x in text for x in ["sentenced", "convicted", "guilty plea",
                                 "pleaded guilty", "found guilty"]):
        return "convicted"
    if any(x in text for x in ["charged", "indicted", "arrested", "complaint filed"]):
        return "charged"
    return "charged"   # DOJ default: they announce charges or convictions


def _extract_location(text: str) -> tuple[str, str]:
    m = _CITY_STATE_RE.search(text)
    if m:
        city  = m.group(1).strip().title()
        state = m.group(2).upper()
        from medusa.record import VALID_STATES
        if state in VALID_STATES:
            return city, state

    m = _STATE_NAME_RE.search(text)
    if m:
        state = _STATE_ABBR.get(m.group(0).lower(), "")
        return "", state

    return "", ""


def _parse_date(raw: str) -> str:
    if not raw:
        return ""
    import email.utils
    try:
        t = email.utils.parsedate(raw)
        if t:
            from datetime import date
            return date(*t[:3]).isoformat()
    except Exception:
        pass
    m = re.search(r"\d{4}-\d{2}-\d{2}", raw)
    if m:
        return m.group(0)
    m = re.search(r"\b(20\d{2})\b", raw)
    if m:
        return m.group(1)
    return ""


def _clean_text(title: str, body: str) -> str:
    clean = re.sub(r"<[^>]+>", "", body).strip()
    sentences = re.split(r"(?<=[.!?])\s+", clean)
    first = sentences[0] if sentences else ""
    if first and first.strip() != title.strip():
        return f"{title} {first}"[:600]
    return title[:600]
