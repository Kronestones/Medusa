"""
sources/ed_gov.py — ED.gov Title IX / OCR + Clery Act campus safety data

Two free public sources from the US Department of Education:

1. OCR Resolution Agreements (Title IX)
   ED.gov publishes XML/CSV of all Office for Civil Rights resolution
   agreements — these document institutions that were found to have
   mishandled sexual violence/harassment complaints.
   URL: https://ocrcas.ed.gov/

2. Campus Safety & Security Data (Clery Act)
   ope.ed.gov publishes annual Clery Act crime statistics per institution.
   API: https://ope.ed.gov/campussafety/
   Includes: forcible sex offenses, domestic violence, stalking, dating violence.

No API key required for either source.
"""

import re
import time
from medusa.fetch import safe_json, safe_get
from medusa.record import STATE_LARGEST_CITY, VALID_STATES, _NAME_TO_ABBR

# ── OCR Case Search ───────────────────────────────────────────────────────────
# ED.gov OCR has a public case search API used by their website
OCR_SEARCH_URL = "https://ocrcas.ed.gov/api/complaint"

OCR_PARAMS = {
    "page":        1,
    "page_size":   50,
    "issue":       "Sexual Violence",   # primary filter
    "resolution":  "Resolution Agreement",
    "sort":        "open_date",
    "sort_order":  "desc",
}

# ── Clery Act API ─────────────────────────────────────────────────────────────
# Campus Safety and Security Data Analysis Cutting Tool
CLERY_BASE    = "https://ope.ed.gov/campussafety/rest"
CLERY_YEAR    = 2022    # Most recent reliable year

# Clery offense categories we track
CLERY_OFFENSES = [
    ("rape",            "rape"),
    ("fondling",        "sexual_assault"),
    ("dom_violence",    "domestic_violence"),
    ("dating_violence", "domestic_violence"),
    ("stalking",        "stalking"),
]


def fetch() -> list[dict]:
    """Fetch ED.gov OCR cases and Clery Act campus safety data."""
    records = []

    # Source 1: OCR Title IX resolution agreements
    ocr_records = _fetch_ocr()
    records.extend(ocr_records)
    print(f"[ED.gov OCR] {len(ocr_records)} resolution agreements fetched.")

    time.sleep(1)

    # Source 2: Clery Act campus crime statistics
    clery_records = _fetch_clery()
    records.extend(clery_records)
    print(f"[ED.gov Clery] {len(clery_records)} campus crime records fetched.")

    return records


# ── OCR fetch ─────────────────────────────────────────────────────────────────

def _fetch_ocr() -> list[dict]:
    data = safe_json(OCR_SEARCH_URL, params=OCR_PARAMS)
    if not data:
        return []

    results = data if isinstance(data, list) else data.get("results", data.get("data", []))
    records = []

    for item in results:
        rec = _parse_ocr_item(item)
        if rec:
            records.append(rec)

    return records


def _parse_ocr_item(item: dict) -> dict | None:
    institution = item.get("recipient_name") or item.get("institution") or ""
    state_raw   = item.get("state") or item.get("recipient_state") or ""
    city_raw    = item.get("city")  or item.get("recipient_city")  or ""

    state = _resolve_state(state_raw)
    if not state:
        return None

    city = city_raw.strip().title() if city_raw else STATE_LARGEST_CITY.get(state, "")
    if not city:
        return None

    # Date of resolution
    date_str = _clean_ocr_date(
        item.get("resolve_date") or item.get("close_date") or
        item.get("open_date") or ""
    )

    # Issue / basis
    issue = (item.get("issue") or item.get("basis") or "Title IX Sexual Violence").strip()

    case_number = item.get("case_number") or item.get("docket_number") or ""
    summary = (
        f"ED.gov OCR Title IX Resolution: {institution} ({city}, {state}). "
        f"Issue: {issue}. "
        + (f"Case {case_number}." if case_number else "")
    ).strip()

    # Try to build a direct URL
    case_id_raw = item.get("id") or item.get("case_id") or ""
    if case_id_raw:
        source_url = f"https://ocrcas.ed.gov/ocr-search?case={case_id_raw}"
    else:
        source_url = "https://ocrcas.ed.gov/ocr-search"

    return {
        "summary":       summary[:600],
        "city":          city,
        "state":         state,
        "date_incident": date_str,
        "violence_type": "sexual_assault",
        "status":        "civil_judgment",
        "source_url":    source_url,
        "source_name":   "ED.gov Office for Civil Rights (OCR)",
        "verified":      True,
    }


# ── Clery fetch ───────────────────────────────────────────────────────────────

def _fetch_clery() -> list[dict]:
    """
    Pull campus crime statistics from ope.ed.gov for the most recent year.
    Returns one record per campus per offense type where count > 0.
    """
    # The Clery tool has a REST endpoint for aggregate data
    url = f"{CLERY_BASE}/GetInstitutions"
    params = {
        "year":       CLERY_YEAR,
        "page":       1,
        "pagesize":   100,
        # Filter: institutions that reported any forcible sex offense > 0
        "rape_min":   1,
    }

    data = safe_json(url, params=params)
    if not data:
        # Try alternate endpoint
        url2 = f"{CLERY_BASE}/GetCrimeStats"
        data = safe_json(url2, params={"year": CLERY_YEAR, "page": 1, "pagesize": 100})

    if not data:
        return []

    items = data if isinstance(data, list) else data.get("data", data.get("results", []))
    records = []

    for item in items:
        recs = _parse_clery_item(item)
        records.extend(recs)

    return records


def _parse_clery_item(item: dict) -> list[dict]:
    institution = item.get("institution_name") or item.get("name") or ""
    state_raw   = item.get("state") or item.get("state_abbr") or ""
    city_raw    = item.get("city") or ""

    state = _resolve_state(state_raw)
    if not state:
        return []

    city = city_raw.strip().title() if city_raw else STATE_LARGEST_CITY.get(state, "")
    if not city:
        return []

    unit_id = item.get("unitid") or item.get("unit_id") or ""
    base_url = (
        f"https://ope.ed.gov/campussafety/rest/customdata/SchoolDetails/{unit_id}"
        if unit_id else "https://ope.ed.gov/campussafety/"
    )

    records = []
    for field, vtype in CLERY_OFFENSES:
        count = _safe_int(item.get(field) or item.get(f"on_campus_{field}"))
        if not count:
            continue

        summary = (
            f"Clery Act Data: {institution} ({city}, {state}) reported "
            f"{count} {field.replace('_', ' ')} incident(s) in {CLERY_YEAR}. "
            f"Source: US Dept of Education Campus Safety & Security Data."
        )
        records.append({
            "summary":       summary[:600],
            "city":          city,
            "state":         state,
            "date_incident": str(CLERY_YEAR),
            "violence_type": vtype,
            "status":        "reported",
            "source_url":    base_url,
            "source_name":   "ED.gov Campus Safety & Security (Clery Act)",
            "verified":      True,
        })

    return records


# ── Helpers ───────────────────────────────────────────────────────────────────

def _resolve_state(raw: str) -> str | None:
    if not raw:
        return None
    s = raw.strip()
    if len(s) == 2:
        up = s.upper()
        return up if up in VALID_STATES else None
    return _NAME_TO_ABBR.get(s.lower())


def _clean_ocr_date(raw: str) -> str:
    if not raw:
        return ""
    m = re.search(r"\d{4}-\d{2}-\d{2}", raw)
    if m:
        return m.group(0)
    m = re.search(r"\b(20\d{2})\b", raw)
    if m:
        return m.group(1)
    return ""


def _safe_int(val) -> int | None:
    if val is None:
        return None
    try:
        return int(val)
    except (ValueError, TypeError):
        return None
