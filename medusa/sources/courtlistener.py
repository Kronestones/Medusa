"""
sources/courtlistener.py — CourtListener REST API

CourtListener (courtlistener.com) provides free, no-key public access to:
  - Federal dockets (PACER mirror)
  - Court opinions
  - Audio arguments

Rate limit: ~5,000 requests/day unauthenticated.
We query the /api/rest/v4/dockets/ endpoint with violence-related search terms.

API docs: https://www.courtlistener.com/help/api/rest/
"""

import re
from datetime import datetime
from medusa.fetch import safe_json
from medusa.record import district_to_city, normalize_violence_type, STATE_LARGEST_CITY

BASE = "https://www.courtlistener.com/api/rest/v4"

# Search terms → violence_type hint
QUERIES = [
    ("domestic violence assault intimate partner",      "domestic_violence"),
    ("sexual assault rape conviction sentence",          "sexual_assault"),
    ("stalking harassment restraining order violation",  "stalking"),
    ("femicide murder intimate partner women",           "homicide"),
    ("sex trafficking women forced prostitution",        "trafficking"),
    ("attempted murder girlfriend wife assault",         "attempted_murder"),
    ("sexual abuse minor child molestation",             "child_abuse"),
    ("rape conviction sentence women",                   "rape"),
]

# Only pull criminal cases from district courts
COURT_TYPE_FILTER = "fd"    # federal district courts
PAGE_SIZE = 20              # results per query (keep low — wide queries)


def fetch() -> list[dict]:
    """Query CourtListener for recent criminal cases involving violence against women."""
    records = []
    seen_dockets = set()

    for search_term, vtype_hint in QUERIES:
        results = _search_dockets(search_term, vtype_hint)
        for r in results:
            docket_id = r.get("_docket_id")
            if docket_id and docket_id in seen_dockets:
                continue
            if docket_id:
                seen_dockets.add(docket_id)
            records.append(r)

    print(f"[CourtListener] {len(records)} records fetched.")
    return records


def _search_dockets(search_term: str, vtype_hint: str) -> list[dict]:
    """Search dockets endpoint, return normalized partial records."""
    data = safe_json(
        f"{BASE}/search/",
        params={
            "q":         search_term,
            "type":      "d",
            "order_by":  "score desc",
            "page_size": PAGE_SIZE,
        },
        extra_headers={"Accept": "application/json"},
    )
    if not data:
        return []

    results = data.get("results", [])
    records = []

    for item in results:
        rec = _parse_docket(item, vtype_hint)
        if rec:
            records.append(rec)

    return records


def _parse_docket(item: dict, vtype_hint: str) -> dict | None:
    """Convert a CourtListener docket object to a partial MedusaRecord."""
    case_name = item.get("caseName") or item.get("case_name") or ""
    if not case_name:
        return None

    # Skip civil/bankruptcy/appellate — we want criminal
    nature_of_suit = (item.get("nature_of_suit") or "").lower()
    if any(x in nature_of_suit for x in ["contract", "property", "bankruptcy",
                                           "civil rights — employment", "patent"]):
        return None

    court_str = item.get("court_citation_string") or item.get("court") or ""
    city, state = _resolve_location(item, court_str)
    if not city or not state:
        return None

    # Date
    date_filed = item.get("dateFiled") or item.get("date_filed") or ""
    date_str = _clean_date(date_filed)

    # Build summary from available fields
    docket_number = item.get("docketNumber") or item.get("docket_number") or ""
    summary = _build_summary(case_name, court_str, docket_number, nature_of_suit)

    # Determine violence type from case name + hint
    vtype = _infer_violence_type(case_name, nature_of_suit, vtype_hint)

    # Status from available fields
    status = _infer_status(item)

    absolute_url = item.get("docket_absolute_url") or item.get("absolute_url") or ""
    source_url = f"https://www.courtlistener.com{absolute_url}" if absolute_url else ""

    return {
        "summary":       summary,
        "city":          city,
        "state":         state,
        "date_incident": date_str,
        "violence_type": vtype,
        "status":        status,
        "source_url":    source_url,
        "source_name":   "CourtListener / PACER",
        "verified":      True,
        "_docket_id":    item.get("id"),    # dedup key, stripped before DB
    }


def _resolve_location(item: dict, court_str: str) -> tuple[str, str]:
    """Resolve city/state from court name. Returns ("", "") if unresolvable."""
    # Try court citation string first (e.g. "W.D. Tex.")
    if court_str:
        loc = district_to_city(court_str)
        if loc:
            return loc

    # Try full court name from nested court object
    court_obj = item.get("court_full_name") or ""
    if court_obj:
        loc = district_to_city(court_obj)
        if loc:
            return loc

    # Try court URL slug (e.g. "txwd" → western district texas)
    court_slug = ""
    court_ref = item.get("court") or ""
    if isinstance(court_ref, str) and "/" in court_ref:
        # e.g. "/api/rest/v4/courts/txwd/"
        court_slug = court_ref.strip("/").split("/")[-1]
    elif isinstance(court_ref, str):
        court_slug = court_ref

    if court_slug:
        loc = _slug_to_city(court_slug)
        if loc:
            return loc

    return "", ""


# Common court slugs → (city, state)
_SLUG_MAP = {
    "alnd": ("Birmingham",    "AL"), "almd": ("Montgomery",   "AL"), "alsd": ("Mobile",        "AL"),
    "akd":  ("Anchorage",     "AK"), "azd":  ("Phoenix",      "AZ"),
    "ared": ("Little Rock",   "AR"), "arwd": ("Fort Smith",   "AR"),
    "cand": ("San Francisco", "CA"), "caed": ("Sacramento",   "CA"),
    "cacd": ("Los Angeles",   "CA"), "casd": ("San Diego",    "CA"),
    "cod":  ("Denver",        "CO"), "ctd":  ("New Haven",    "CT"),
    "ded":  ("Wilmington",    "DE"), "dcd":  ("Washington",   "DC"),
    "flnd": ("Pensacola",     "FL"), "flmd": ("Tampa",        "FL"), "flsd": ("Miami",         "FL"),
    "gand": ("Atlanta",       "GA"), "gamd": ("Macon",        "GA"), "gasd": ("Savannah",      "GA"),
    "hid":  ("Honolulu",      "HI"), "idd":  ("Boise",        "ID"),
    "ilnd": ("Chicago",       "IL"), "ilcd": ("Springfield",  "IL"), "ilsd": ("East St. Louis","IL"),
    "innd": ("Hammond",       "IN"), "insd": ("Indianapolis", "IN"),
    "iand": ("Cedar Rapids",  "IA"), "iasd": ("Des Moines",   "IA"),
    "ksd":  ("Wichita",       "KS"),
    "kyed": ("Lexington",     "KY"), "kywd": ("Louisville",   "KY"),
    "laed": ("New Orleans",   "LA"), "lamd": ("Baton Rouge",  "LA"), "lawd": ("Shreveport",    "LA"),
    "med":  ("Portland",      "ME"), "mdd":  ("Baltimore",    "MD"), "mad":  ("Boston",        "MA"),
    "mied": ("Detroit",       "MI"), "miwd": ("Grand Rapids", "MI"),
    "mnd":  ("Minneapolis",   "MN"),
    "msnd": ("Oxford",        "MS"), "mssd": ("Jackson",      "MS"),
    "moed": ("St. Louis",     "MO"), "mowd": ("Kansas City",  "MO"),
    "mtd":  ("Billings",      "MT"), "ned":  ("Omaha",        "NE"), "nvd":  ("Las Vegas",     "NV"),
    "nhd":  ("Concord",       "NH"), "njd":  ("Newark",       "NJ"), "nmd":  ("Albuquerque",   "NM"),
    "nynd": ("Albany",        "NY"), "nyed": ("Brooklyn",     "NY"),
    "nysd": ("New York",      "NY"), "nywd": ("Buffalo",      "NY"),
    "nced": ("Raleigh",       "NC"), "ncmd": ("Greensboro",   "NC"), "ncwd": ("Charlotte",     "NC"),
    "ndd":  ("Bismarck",      "ND"),
    "ohnd": ("Cleveland",     "OH"), "ohsd": ("Columbus",     "OH"),
    "oknd": ("Tulsa",         "OK"), "oked": ("Muskogee",     "OK"), "okwd": ("Oklahoma City", "OK"),
    "ord":  ("Portland",      "OR"),
    "paed": ("Philadelphia",  "PA"), "pamd": ("Scranton",     "PA"), "pawd": ("Pittsburgh",    "PA"),
    "rid":  ("Providence",    "RI"),
    "scd":  ("Columbia",      "SC"),
    "sdd":  ("Sioux Falls",   "SD"),
    "tned": ("Knoxville",     "TN"), "tnmd": ("Nashville",    "TN"), "tnwd": ("Memphis",       "TN"),
    "txnd": ("Dallas",        "TX"), "txed": ("Beaumont",     "TX"),
    "txsd": ("Houston",       "TX"), "txwd": ("San Antonio",  "TX"),
    "utd":  ("Salt Lake City","UT"), "vtd":  ("Burlington",   "VT"),
    "vaed": ("Alexandria",    "VA"), "vawd": ("Roanoke",      "VA"),
    "waed": ("Spokane",       "WA"), "wawd": ("Seattle",      "WA"),
    "wvnd": ("Clarksburg",    "WV"), "wvsd": ("Charleston",   "WV"),
    "wied": ("Milwaukee",     "WI"), "wiwd": ("Madison",      "WI"),
    "wyd":  ("Cheyenne",      "WY"),
}


def _slug_to_city(slug: str) -> tuple[str, str] | None:
    return _SLUG_MAP.get(slug.lower())


def _clean_date(raw: str) -> str:
    if not raw:
        return ""
    # Already YYYY-MM-DD
    if re.match(r"\d{4}-\d{2}-\d{2}", raw):
        return raw[:10]
    # Try parsing
    for fmt in ("%Y-%m-%dT%H:%M:%S", "%Y-%m-%d", "%m/%d/%Y"):
        try:
            return datetime.strptime(raw[:len(fmt)], fmt).strftime("%Y-%m-%d")
        except Exception:
            pass
    return raw[:10] if len(raw) >= 10 else raw


def _build_summary(case_name: str, court_str: str, docket_number: str,
                   nature_of_suit: str) -> str:
    parts = [f"Court case: {case_name}."]
    if court_str:
        parts.append(f"Filed in {court_str}.")
    if docket_number:
        parts.append(f"Docket {docket_number}.")
    return " ".join(parts)


def _infer_violence_type(case_name: str, nos: str, hint: str) -> str:
    text = (case_name + " " + nos).lower()
    if any(x in text for x in ["murder", "homicide", "kill", "manslaughter"]):
        return "homicide"
    if any(x in text for x in ["rape", "sexual assault", "sex assault"]):
        return "sexual_assault"
    if "trafficking" in text:
        return "trafficking"
    if "stalking" in text:
        return "stalking"
    if "domestic" in text or "intimate partner" in text:
        return "domestic_violence"
    if "attempted murder" in text or "attempted homicide" in text:
        return "attempted_murder"
    if any(x in text for x in ["child", "minor", "abuse"]):
        return "child_abuse"
    return normalize_violence_type(hint)


def _infer_status(item: dict) -> str:
    # CourtListener doesn't always expose verdict — use date_terminated as proxy
    if item.get("dateTerminated"):
        return "convicted"     # case closed; approximate
    if item.get("dateFiled") or item.get("date_filed"):
        return "charged"
    return "reported"
