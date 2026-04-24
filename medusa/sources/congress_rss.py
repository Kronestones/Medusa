"""
sources/congress_rss.py — Congress.gov RSS feeds (no API key required)

Congress.gov publishes committee hearing and legislation RSS feeds.
We pull Judiciary committee feeds to find:
  - Hearings on VAWA, domestic violence, sexual assault
  - Named perpetrators in congressional records
  - Ethics investigations involving violence against women

RSS feeds: https://www.congress.gov/rss/  (public, no auth)
"""

import re
from medusa.fetch import safe_rss
from medusa.record import normalize_violence_type

# Congress.gov committee hearing RSS feeds — no key required
CONGRESS_FEEDS = [
    # Senate Judiciary
    "https://www.congress.gov/rss/committee-activity/ssju00.xml",
    # House Judiciary
    "https://www.congress.gov/rss/committee-activity/hsju00.xml",
    # Senate HELP (Health, Education, Labor — Title IX)
    "https://www.congress.gov/rss/committee-activity/sshr00.xml",
    # House Education & Workforce
    "https://www.congress.gov/rss/committee-activity/hsed00.xml",
    # General legislation RSS (bills introduced)
    "https://www.congress.gov/rss/legislation/bills-introduced.xml",
]

INCLUDE_KEYWORDS = [
    "violence against women", "vawa", "domestic violence", "sexual assault",
    "rape", "trafficking", "title ix", "sexual harassment",
    "intimate partner", "femicide", "stalking", "sex crimes",
    "abuse", "exploitation",
]

EXCLUDE_KEYWORDS = [
    "gun", "immigration", "border", "tax", "budget", "infrastructure",
    "climate", "trade", "foreign", "military", "defense",
]


def fetch() -> list[dict]:
    """Pull Congress.gov RSS feeds, filter relevant hearings/bills."""
    records = []
    seen = set()

    for feed_url in CONGRESS_FEEDS:
        entries = safe_rss(feed_url)
        for entry in entries:
            url = entry.get("link") or entry.get("id") or ""
            if url in seen:
                continue
            rec = _parse_entry(entry)
            if rec:
                seen.add(url)
                records.append(rec)

    print(f"[Congress RSS] {len(records)} records fetched.")
    return records


def _parse_entry(entry) -> dict | None:
    title   = entry.get("title") or ""
    summary = entry.get("summary") or entry.get("description") or ""
    text    = f"{title} {summary}".lower()

    if not any(kw in text for kw in INCLUDE_KEYWORDS):
        return None
    if any(kw in text for kw in EXCLUDE_KEYWORDS):
        return None

    # Congressional records are DC-located unless a specific incident is named
    city, state = _extract_location(f"{title} {summary}")

    vtype = _infer_type(text)
    date_str = _parse_date(entry.get("published") or entry.get("updated") or "")
    clean_summary = _clean_html(f"{title}. {summary}")[:600]

    return {
        "summary":       clean_summary,
        "city":          city,
        "state":         state,
        "date_incident": date_str,
        "violence_type": vtype,
        "status":        "congressional_record",
        "source_url":    entry.get("link") or "",
        "source_name":   "Congress.gov",
        "verified":      True,
    }


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
    "district of columbia":"DC",
}

_STATE_PATTERN = re.compile(
    r"\b(Alabama|Alaska|Arizona|Arkansas|California|Colorado|Connecticut|"
    r"Delaware|Florida|Georgia|Hawaii|Idaho|Illinois|Indiana|Iowa|Kansas|"
    r"Kentucky|Louisiana|Maine|Maryland|Massachusetts|Michigan|Minnesota|"
    r"Mississippi|Missouri|Montana|Nebraska|Nevada|New Hampshire|New Jersey|"
    r"New Mexico|New York|North Carolina|North Dakota|Ohio|Oklahoma|Oregon|"
    r"Pennsylvania|Rhode Island|South Carolina|South Dakota|Tennessee|Texas|"
    r"Utah|Vermont|Virginia|Washington|West Virginia|Wisconsin|Wyoming)\b",
    re.IGNORECASE,
)


def _extract_location(text: str) -> tuple[str, str]:
    """Congressional items default to DC unless a specific state is mentioned."""
    # Named state in the text → use that state's capital/largest city
    from medusa.record import STATE_LARGEST_CITY
    match = _STATE_PATTERN.search(text)
    if match:
        state = _STATE_ABBR.get(match.group(0).lower(), "")
        if state:
            return STATE_LARGEST_CITY.get(state, ""), state
    # Default: Washington DC — hearing location
    return "Washington", "DC"


def _infer_type(text: str) -> str:
    if any(x in text for x in ["murder", "homicide", "femicide", "killed"]):
        return "homicide"
    if "rape" in text:
        return "rape"
    if any(x in text for x in ["sexual assault", "sex assault"]):
        return "sexual_assault"
    if "trafficking" in text:
        return "trafficking"
    if "stalking" in text:
        return "stalking"
    if "domestic violence" in text or "intimate partner" in text:
        return "domestic_violence"
    if "harassment" in text:
        return "harassment"
    return "assault"


def _parse_date(raw: str) -> str:
    if not raw:
        return ""
    m = re.match(r"(\d{4}-\d{2}-\d{2})", raw)
    if m:
        return m.group(1)
    import email.utils
    try:
        t = email.utils.parsedate(raw)
        if t:
            from datetime import date
            return date(*t[:3]).isoformat()
    except Exception:
        pass
    return ""


def _clean_html(text: str) -> str:
    return re.sub(r"<[^>]+>", " ", text).strip()
