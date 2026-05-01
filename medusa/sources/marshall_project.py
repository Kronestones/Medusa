"""
sources/marshall_project.py — The Marshall Project + DOJ CEOS press releases

The Marshall Project (themarshallproject.org):
  Nonprofit criminal justice newsroom. Publishes RSS.
  Focus: incarcerated people, courts, policing — includes violence convictions.
  RSS: https://www.themarshallproject.org/feeds/news.rss

DOJ CEOS (Child Exploitation and Obscenity Section):
  https://www.justice.gov/criminal/criminal-ceos/press-releases
  DOJ publishes press releases for every federal child exploitation conviction.
  We access via DOJ JSON API filtered by CEOS component.

No API key required.
"""

import re
from medusa.fetch import safe_rss, safe_json, safe_get
from medusa.record import normalize_violence_type, normalize_status, VALID_STATES

# Marshall Project RSS
MARSHALL_RSS = "https://www.themarshallproject.org/feeds/news.rss"

# DOJ JSON API — CEOS press releases
DOJ_CEOS_URL = "https://www.justice.gov/api/node/press_release"
DOJ_CEOS_PARAMS = {
    "sort": "-field_pr_date",
    "page[limit]": 50,
    "filter[field_pr_component.name]": "Criminal Division",
}

# Also try direct scrape of CEOS page
DOJ_CEOS_DIRECT = "https://www.justice.gov/criminal/criminal-ceos/press-releases"

INCLUDE_KEYWORDS = [
    "domestic violence", "sexual assault", "rape", "stalking",
    "trafficking", "intimate partner", "femicide", "murder", "homicide",
    "child abuse", "child pornography", "child exploitation", "molestation",
    "sex offense", "sex offender", "coercive", "assault", "harassment",
    "attempted murder", "strangled", "beaten",
]

EXCLUDE_KEYWORDS = [
    "ukraine", "israel", "gaza", "russia", "china", "iran",
    "robbery", "drug trafficking", "cartel", "money laundering",
    "bank fraud", "tax", "corruption",   # avoid non-violence stories
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

_CITY_STATE_RE = re.compile(r"([A-Z][a-zA-Z\s\-]{2,25}),\s*([A-Z]{2})\b")
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
    records = []
    seen_urls = set()

    # Marshall Project RSS
    mp_records = _fetch_marshall(seen_urls)
    records.extend(mp_records)
    print(f"[Marshall Project] {len(mp_records)} records.")

    # DOJ CEOS
    ceos_records = _fetch_ceos(seen_urls)
    records.extend(ceos_records)
    print(f"[DOJ CEOS] {len(ceos_records)} records.")

    return records


def _fetch_marshall(seen_urls: set) -> list[dict]:
    entries = safe_rss(MARSHALL_RSS)
    records = []
    for entry in entries:
        url = entry.get("link") or ""
        if url in seen_urls:
            continue
        rec = _parse_rss_entry(entry, "The Marshall Project")
        if rec:
            seen_urls.add(url)
            records.append(rec)
    return records


def _fetch_ceos(seen_urls: set) -> list[dict]:
    # Try DOJ JSON API filtered by Criminal Division, keyword=child exploitation
    url = DOJ_CEOS_URL
    params = dict(DOJ_CEOS_PARAMS)
    data = safe_json(url, params=params)
    records = []

    if data:
        items = data if isinstance(data, list) else data.get("data", [])
        for item in items:
            attrs = item.get("attributes", item)
            title = attrs.get("title", "") or ""
            body  = attrs.get("body", {})
            if isinstance(body, dict):
                body = body.get("value", "") or ""
            text = f"{title} {body}".lower()

            # Must match child exploitation / sex offense keywords
            ceos_kws = [
                "child", "minor", "exploitation", "pornography",
                "sex trafficking", "sexual assault", "molestation",
                "rape", "grooming",
            ]
            if not any(kw in text for kw in ceos_kws):
                continue

            link = attrs.get("field_pr_url", {})
            if isinstance(link, dict):
                link = link.get("uri", "") or ""
            link = str(link)
            if link in seen_urls:
                continue

            city, state = _extract_location(f"{title} {body}")
            if not state:
                city, state = "Washington", "DC"

            date_str = _parse_date(attrs.get("field_pr_date", "") or "")
            clean    = _clean_text(title, str(body))
            vtype    = _infer_type(text)

            records.append({
                "summary":       clean,
                "city":          city,
                "state":         state,
                "date_incident": date_str,
                "violence_type": vtype,
                "status":        "convicted",   # CEOS only announces convictions
                "source_url":    link or DOJ_CEOS_DIRECT,
                "source_name":   "DOJ CEOS (Child Exploitation)",
                "verified":      True,
            })
            seen_urls.add(link)

    return records


def _parse_rss_entry(entry, source_name: str) -> dict | None:
    title   = entry.get("title") or ""
    summary = entry.get("summary") or entry.get("description") or ""
    text    = f"{title} {summary}".lower()

    if not any(kw in text for kw in INCLUDE_KEYWORDS):
        return None
    if any(kw in text for kw in EXCLUDE_KEYWORDS):
        return None

    vtype  = _infer_type(text)
    status = _infer_status(text)
    city, state = _extract_location(f"{title} {summary}")
    if not state:
        return None   # Marshall Project — skip if we can't locate it

    date_str = _parse_date(entry.get("published") or entry.get("updated") or "")
    clean    = _clean_text(title, summary)

    return {
        "summary":       clean,
        "city":          city or state,
        "state":         state,
        "date_incident": date_str,
        "violence_type": vtype,
        "status":        status,
        "source_url":    entry.get("link") or "",
        "source_name":   source_name,
        "verified":      True,
    }


def _infer_type(text: str) -> str:
    if any(x in text for x in ["murder", "homicide", "killed", "femicide"]):
        return "homicide"
    if any(x in text for x in ["attempted murder", "tried to kill"]):
        return "attempted_murder"
    if any(x in text for x in ["rape", "raped"]):
        return "rape"
    if any(x in text for x in ["sexual assault", "sex assault", "sex offense",
                                 "child pornography", "exploitation", "grooming",
                                 "molestation"]):
        return "sexual_assault"
    if "trafficking" in text:
        return "trafficking"
    if "stalking" in text:
        return "stalking"
    if any(x in text for x in ["domestic violence", "intimate partner", "dating violence"]):
        return "domestic_violence"
    if any(x in text for x in ["child abuse"]):
        return "child_abuse"
    if "coercive" in text:
        return "coercive_control"
    if "harassment" in text:
        return "harassment"
    return "assault"


def _infer_status(text: str) -> str:
    if any(x in text for x in ["convicted", "sentenced", "guilty plea",
                                 "pleaded guilty", "found guilty"]):
        return "convicted"
    if any(x in text for x in ["charged", "indicted", "arrested"]):
        return "charged"
    return "reported"


def _extract_location(text: str) -> tuple[str, str]:
    m = _CITY_STATE_RE.search(text)
    if m:
        city  = m.group(1).strip().title()
        state = m.group(2).upper()
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
    return ""


def _clean_text(title: str, body: str) -> str:
    clean = re.sub(r"<[^>]+>", "", body).strip()
    sentences = re.split(r"(?<=[.!?])\s+", clean)
    first = sentences[0] if sentences else ""
    if first and first.strip() != title.strip():
        return f"{title} {first}"[:600]
    return title[:600]
