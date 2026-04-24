"""
sources/ed_gov.py — ED.gov Title IX & Clery Act data (no API key required)

The US Department of Education Office for Civil Rights (OCR) publishes:
  - Title IX resolution agreements (named institutions)
  - OCR complaint resolutions
  - Campus safety data (Clery Act) via ope.ed.gov

All public, no authentication required.

Primary endpoint: https://ocrcas.ed.gov/ocr-search
  Returns resolution agreements searchable by issue type, state, institution.
  Issue type 14 = Sexual Violence / Title IX
  Issue type 11 = Sexual Harassment

Clery data: https://ope.ed.gov/campussafety/
"""

import re
from medusa.fetch import safe_json, safe_rss
from medusa.record import STATE_LARGEST_CITY, normalize_state

# OCR Case Activity System — public search API
OCR_SEARCH_BASE = "https://ocrcas.ed.gov/ocr-search/searchocr"

# Issue type codes relevant to sexual violence / Title IX
ISSUE_TYPES = [
    "14",   # Sexual Violence
    "11",   # Sexual Harassment
    "20",   # Title IX — Athletics (sometimes covers assault)
]

# ED.gov OCR blog/news RSS — publishes major resolution announcements
ED_RSS_FEEDS = [
    "https://www.ed.gov/rss/ed-blog.xml",
    "https://www.ed.gov/rss/ed-press-releases.xml",
]

INCLUDE_KEYWORDS = [
    "title ix", "sexual violence", "sexual assault", "sexual harassment",
    "rape", "domestic violence", "clery", "campus safety",
]


def fetch() -> list[dict]:
    """Pull ED.gov Title IX resolution records and OCR search results."""
    records = []

    # Pull OCR case search
    ocr_records = _fetch_ocr_cases()
    records.extend(ocr_records)

    # Pull ED press release RSS for major announcements
    rss_records = _fetch_ed_rss()
    records.extend(rss_records)

    print(f"[ED.gov] {len(records)} records fetched.")
    return records


def _fetch_ocr_cases() -> list[dict]:
    """Query the OCR Case Activity System for Title IX resolutions."""
    records = []

    for issue_type in ISSUE_TYPES:
        data = safe_json(
            OCR_SEARCH_BASE,
            params={
                "issue":      issue_type,
                "page":       1,
                "per-page":   25,
                "sort":       "open-date",
                "order":      "desc",
                "recipient_type": "2",   # 2 = postsecondary (colleges)
            },
        )
        if not data:
            continue

        items = data if isinstance(data, list) else (
            data.get("data") or data.get("results") or []
        )

        for item in items:
            rec = _parse_ocr_item(item, issue_type)
            if rec:
                records.append(rec)

    return records


def _parse_ocr_item(item: dict, issue_type: str) -> dict | None:
    # Institution info
    institution = (item.get("recipient_name") or
                   item.get("institution") or
                   item.get("name") or "")
    if not institution:
        return None

    city  = (item.get("city") or "").strip().title()
    state = normalize_state(item.get("state") or item.get("state_abbr") or "")
    if not state:
        return None
    if not city:
        city = STATE_LARGEST_CITY.get(state, "")

    date_opened = item.get("open_date") or item.get("date") or ""
    date_str    = _clean_date(date_opened)

    case_num = item.get("case_number") or item.get("case_id") or ""
    issue_label = {
        "14": "Sexual Violence (Title IX)",
        "11": "Sexual Harassment (Title IX)",
        "20": "Title IX Athletics",
    }.get(issue_type, "Title IX")

    summary = (
        f"ED.gov OCR {issue_label} resolution at {institution}, {city}, {state}. "
        f"Case {case_num}. Federal investigation under Title IX."
        if case_num else
        f"ED.gov OCR {issue_label} resolution at {institution}, {city}, {state}. "
        f"Federal investigation under Title IX."
    )

    case_url = (
        item.get("resolution_url") or
        item.get("url") or
        f"https://ocrcas.ed.gov/ocr-search"
    )

    vtype = "sexual_assault" if issue_type in ("14",) else "harassment"
    status = "civil_judgment" if item.get("resolution_date") else "reported"

    return {
        "summary":       summary[:600],
        "city":          city,
        "state":         state,
        "date_incident": date_str,
        "violence_type": vtype,
        "status":        status,
        "source_url":    case_url,
        "source_name":   "ED.gov / Office for Civil Rights",
        "verified":      True,
    }


def _fetch_ed_rss() -> list[dict]:
    """Pull ED.gov press release RSS for Title IX announcements."""
    records = []
    seen = set()

    for feed_url in ED_RSS_FEEDS:
        entries = safe_rss(feed_url)
        for entry in entries:
            url = entry.get("link") or ""
            if url in seen:
                continue

            title   = entry.get("title") or ""
            summary = entry.get("summary") or ""
            text    = f"{title} {summary}".lower()

            if not any(kw in text for kw in INCLUDE_KEYWORDS):
                continue

            state = _extract_state(f"{title} {summary}")
            if not state:
                # ED press releases about national policy → DC
                state = "DC"
            city = STATE_LARGEST_CITY.get(state, "Washington")

            date_str = _parse_rss_date(
                entry.get("published") or entry.get("updated") or ""
            )

            vtype = "sexual_assault" if any(
                x in text for x in ["sexual violence", "sexual assault", "rape"]
            ) else "harassment"

            clean = re.sub(r"<[^>]+>", " ", f"{title}. {summary}").strip()[:600]

            records.append({
                "summary":       clean,
                "city":          city,
                "state":         state,
                "date_incident": date_str,
                "violence_type": vtype,
                "status":        "civil_judgment",
                "source_url":    url,
                "source_name":   "ED.gov",
                "verified":      True,
            })
            seen.add(url)

    return records


_STATE_MAP = {
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


def _extract_state(text: str) -> str:
    m = _STATE_PATTERN.search(text)
    if m:
        return _STATE_MAP.get(m.group(0).lower(), "")
    return ""


def _clean_date(raw: str) -> str:
    if not raw:
        return ""
    m = re.match(r"(\d{4}-\d{2}-\d{2})", raw)
    if m:
        return m.group(1)
    m = re.match(r"(\d{2})/(\d{2})/(\d{4})", raw)
    if m:
        return f"{m.group(3)}-{m.group(1)}-{m.group(2)}"
    return ""


def _parse_rss_date(raw: str) -> str:
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
