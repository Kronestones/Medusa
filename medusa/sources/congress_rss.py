"""
sources/congress_rss.py — Congressional records via RSS (no API key)

Congress.gov and related government feeds publish Judiciary Committee
hearing summaries, press releases, and bill tracking via RSS.

We pull hearings related to violence against women, ethics investigations,
and VAWA-related legislation as documentary evidence.

No API key required. congress.gov has a free API key option but the
RSS feeds are fully public and sufficient for our purposes.
"""

import re
from medusa.fetch import safe_rss
from medusa.record import normalize_violence_type, normalize_status

# Public RSS feeds — no key required
CONGRESS_FEEDS = [
    # Senate Judiciary Committee news
    "https://www.judiciary.senate.gov/rss/press-releases",
    # House Judiciary Committee
    "https://judiciary.house.gov/news/rss.aspx",
    # DOJ press releases — federal prosecutions
    "https://www.justice.gov/rss/press-releases.xml",
    # DOJ Office on Violence Against Women
    "https://www.justice.gov/ovw/rss-news",
    # Senate press releases (filtered below)
    "https://www.congress.gov/rss/most-viewed-bills.xml",
]

INCLUDE_KEYWORDS = [
    "domestic violence", "sexual assault", "rape", "stalking",
    "violence against women", "vawa", "sex trafficking", "human trafficking",
    "title ix", "harassment", "femicide", "intimate partner",
    "child abuse", "sex abuse", "molestation", "coercive control",
    "restraining order", "protective order",
]

EXCLUDE_KEYWORDS = [
    "ukraine", "israel", "gaza", "russia", "china", "iran",
    "afghanistan", "border security", "immigration enforcement",
    # Skip pure budget/appropriations unless tied to VAWA
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
    r"([A-Z][a-zA-Z\s]{2,25}),\s*([A-Z]{2})\b"
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
    """Pull congressional and DOJ RSS feeds, filter for violence against women."""
    records = []
    seen_urls = set()

    for feed_url in CONGRESS_FEEDS:
        entries = safe_rss(feed_url)
        for entry in entries:
            url = entry.get("link") or ""
            if url in seen_urls:
                continue
            rec = _parse_entry(entry, feed_url)
            if rec:
                seen_urls.add(url)
                records.append(rec)

    print(f"[Congress RSS] {len(records)} records fetched.")
    return records


def _parse_entry(entry, feed_url: str) -> dict | None:
    title   = entry.get("title") or ""
    summary = entry.get("summary") or entry.get("description") or ""
    text    = f"{title} {summary}".lower()

    if not any(kw in text for kw in INCLUDE_KEYWORDS):
        return None
    if any(kw in text for kw in EXCLUDE_KEYWORDS):
        return None

    vtype  = _infer_type(text)
    status = _infer_status(text, feed_url)

    city, state = _extract_location(f"{title} {summary}")
    # Congressional records default to DC if no specific location
    if not state:
        city  = "Washington"
        state = "DC"

    date_str = _parse_date(entry.get("published") or entry.get("updated") or "")

    clean = _clean_summary(title, summary)

    return {
        "summary":       clean,
        "city":          city,
        "state":         state,
        "date_incident": date_str,
        "violence_type": vtype,
        "status":        status,
        "source_url":    entry.get("link") or "",
        "source_name":   _source_name(feed_url),
        "verified":      True,
    }


def _infer_type(text: str) -> str:
    if any(x in text for x in ["murder", "homicide", "killed", "femicide"]):
        return "homicide"
    if any(x in text for x in ["rape", "raped"]):
        return "rape"
    if any(x in text for x in ["sexual assault", "sex assault", "sex abuse"]):
        return "sexual_assault"
    if "trafficking" in text:
        return "trafficking"
    if "stalking" in text:
        return "stalking"
    if any(x in text for x in ["domestic violence", "intimate partner"]):
        return "domestic_violence"
    if any(x in text for x in ["child abuse", "molestation"]):
        return "child_abuse"
    if "harassment" in text:
        return "harassment"
    if "coercive" in text:
        return "coercive_control"
    return "assault"


def _infer_status(text: str, feed_url: str) -> str:
    if "doj" in feed_url or "justice.gov" in feed_url:
        # DOJ press releases usually announce charges or convictions
        if any(x in text for x in ["convicted", "sentenced", "guilty plea",
                                     "pleaded guilty", "found guilty"]):
            return "convicted"
        if any(x in text for x in ["charged", "indicted", "arrested"]):
            return "charged"
        return "charged"   # DOJ default: if they're announcing it, charges exist
    if any(x in text for x in ["convicted", "sentenced", "guilty"]):
        return "convicted"
    if any(x in text for x in ["charged", "indicted"]):
        return "charged"
    return "congressional_record"


def _extract_location(text: str) -> tuple[str, str]:
    # Try "City, ST" first
    m = _CITY_STATE_RE.search(text)
    if m:
        city  = m.group(1).strip().title()
        state = m.group(2).upper()
        from medusa.record import VALID_STATES
        if state in VALID_STATES:
            return city, state

    # Fall back to state name
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


def _clean_summary(title: str, body: str) -> str:
    clean = re.sub(r"<[^>]+>", "", body).strip()
    sentences = re.split(r"(?<=[.!?])\s+", clean)
    first = sentences[0] if sentences else ""
    if first and first != title:
        return f"{title} {first}"[:600]
    return title[:600]


def _source_name(feed_url: str) -> str:
    if "justice.gov/ovw" in feed_url:
        return "DOJ Office on Violence Against Women"
    if "justice.gov" in feed_url:
        return "US Department of Justice"
    if "judiciary.senate.gov" in feed_url:
        return "Senate Judiciary Committee"
    if "judiciary.house.gov" in feed_url:
        return "House Judiciary Committee"
    if "congress.gov" in feed_url:
        return "Congress.gov"
    return "Congressional Record"
