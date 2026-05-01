"""
record.py — Medusa unified record format

Every source module returns raw dicts.
normalize_record() validates and standardizes them into the
locked CaseRecord schema before the orchestrator geocodes and saves.

Key guarantees:
  - state is always a valid 2-letter US abbreviation (or record is dropped)
  - city is always a real string (never "Federal", "Unknown", etc.)
  - violence_type is always a valid enum value
  - status is always a valid enum value
  - case_id is deterministic and collision-resistant
"""

import hashlib
import re
from datetime import datetime

# ── Enums ─────────────────────────────────────────────────────────────────────

VALID_VIOLENCE_TYPES = {
    "homicide", "assault", "sexual_assault", "stalking", "trafficking",
    "domestic_violence", "rape", "harassment", "attempted_murder",
    "child_abuse", "coercive_control",
}

VALID_STATUSES = {
    "reported", "charged", "convicted", "acquitted",
    "civil_judgment", "credible_allegation", "congressional_record", "unknown",
}

# ── State validation ──────────────────────────────────────────────────────────

VALID_STATES = {
    "AL","AK","AZ","AR","CA","CO","CT","DE","FL","GA",
    "HI","ID","IL","IN","IA","KS","KY","LA","ME","MD",
    "MA","MI","MN","MS","MO","MT","NE","NV","NH","NJ",
    "NM","NY","NC","ND","OH","OK","OR","PA","RI","SC",
    "SD","TN","TX","UT","VT","VA","WA","WV","WI","WY","DC",
}

# Full state name → abbreviation
_NAME_TO_ABBR = {
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
    "district of columbia":"DC","d.c.":"DC","washington dc":"DC","washington d.c.":"DC",
}

# Strings that are NOT valid city names
_INVALID_CITIES = {
    "", "federal", "national", "unknown", "n/a", "na", "none",
    "united states", "us", "usa", "various", "multiple",
}


def validate_state(raw: str) -> str | None:
    """
    Return a valid 2-letter US state abbreviation, or None if invalid.
    Accepts full names ('California') or abbreviations ('CA').
    Rejects non-US territories (PR, GU, VI, etc.) — US 50 + DC only.
    """
    if not raw:
        return None
    s = raw.strip()

    # Already a 2-letter abbr?
    if len(s) == 2:
        up = s.upper()
        return up if up in VALID_STATES else None

    # Full name lookup
    return _NAME_TO_ABBR.get(s.lower())


def validate_city(raw: str) -> str | None:
    """
    Return a cleaned city string or None if invalid.
    """
    if not raw:
        return None
    clean = raw.strip().title()
    if clean.lower() in _INVALID_CITIES:
        return None
    # Must be at least 2 chars, mostly letters/spaces/hyphens
    if len(clean) < 2:
        return None
    return clean


def normalize_violence_type(raw: str) -> str:
    """Map raw string to a valid violence_type enum. Defaults to 'assault'."""
    if not raw:
        return "assault"
    r = raw.strip().lower().replace(" ", "_").replace("-", "_")
    if r in VALID_VIOLENCE_TYPES:
        return r
    # Common aliases
    aliases = {
        "murder": "homicide", "femicide": "homicide", "manslaughter": "homicide",
        "rape": "rape", "sexual_abuse": "sexual_assault", "sex_assault": "sexual_assault",
        "dv": "domestic_violence", "intimate_partner": "domestic_violence",
        "human_trafficking": "trafficking", "sex_trafficking": "trafficking",
        "attempted_homicide": "attempted_murder", "attempted_killing": "attempted_murder",
        "molestation": "child_abuse", "child_sexual_abuse": "child_abuse",
        "coercion": "coercive_control", "abuse": "assault",
    }
    return aliases.get(r, "assault")


def normalize_status(raw: str) -> str:
    """Map raw string to a valid status enum. Defaults to 'reported'."""
    if not raw:
        return "reported"
    r = raw.strip().lower()
    if r in VALID_STATUSES:
        return r
    aliases = {
        "guilty plea": "convicted", "pleaded guilty": "convicted",
        "sentenced": "convicted", "found guilty": "convicted",
        "arrested": "charged", "indicted": "charged", "faces charges": "charged",
        "not guilty": "acquitted", "charges dropped": "acquitted",
        "dismissed": "acquitted",
        "civil judgment": "civil_judgment", "judgment": "civil_judgment",
        "allegation": "credible_allegation", "alleged": "credible_allegation",
        "congressional": "congressional_record",
    }
    for k, v in aliases.items():
        if k in r:
            return v
    return "reported"


# ── Largest city fallback per state ──────────────────────────────────────────

STATE_LARGEST_CITY = {
    "AL":"Birmingham","AK":"Anchorage","AZ":"Phoenix","AR":"Little Rock",
    "CA":"Los Angeles","CO":"Denver","CT":"Bridgeport","DE":"Wilmington",
    "FL":"Jacksonville","GA":"Atlanta","HI":"Honolulu","ID":"Boise",
    "IL":"Chicago","IN":"Indianapolis","IA":"Des Moines","KS":"Wichita",
    "KY":"Louisville","LA":"New Orleans","ME":"Portland","MD":"Baltimore",
    "MA":"Boston","MI":"Detroit","MN":"Minneapolis","MS":"Jackson",
    "MO":"Kansas City","MT":"Billings","NE":"Omaha","NV":"Las Vegas",
    "NH":"Manchester","NJ":"Newark","NM":"Albuquerque","NY":"New York",
    "NC":"Charlotte","ND":"Fargo","OH":"Columbus","OK":"Oklahoma City",
    "OR":"Portland","PA":"Philadelphia","RI":"Providence","SC":"Columbia",
    "SD":"Sioux Falls","TN":"Memphis","TX":"Houston","UT":"Salt Lake City",
    "VT":"Burlington","VA":"Virginia Beach","WA":"Seattle","WV":"Charleston",
    "WI":"Milwaukee","WY":"Cheyenne","DC":"Washington",
}


# ── Federal district → (city, state) ─────────────────────────────────────────
# Called by courtlistener.py and any source dealing with federal courts.

_DISTRICT_PATTERNS = [
    # Patterns: match court strings like "W.D. Tex.", "S.D.N.Y.", "N.D. Cal."
    (re.compile(r"S\.?D\.?\s*N\.?Y\.?",    re.I), ("New York",      "NY")),
    (re.compile(r"E\.?D\.?\s*N\.?Y\.?",    re.I), ("Brooklyn",      "NY")),
    (re.compile(r"N\.?D\.?\s*N\.?Y\.?",    re.I), ("Albany",        "NY")),
    (re.compile(r"W\.?D\.?\s*N\.?Y\.?",    re.I), ("Buffalo",       "NY")),
    (re.compile(r"N\.?D\.?\s*Cal\.?",      re.I), ("San Francisco", "CA")),
    (re.compile(r"E\.?D\.?\s*Cal\.?",      re.I), ("Sacramento",    "CA")),
    (re.compile(r"C\.?D\.?\s*Cal\.?",      re.I), ("Los Angeles",   "CA")),
    (re.compile(r"S\.?D\.?\s*Cal\.?",      re.I), ("San Diego",     "CA")),
    (re.compile(r"N\.?D\.?\s*Tex\.?",      re.I), ("Dallas",        "TX")),
    (re.compile(r"S\.?D\.?\s*Tex\.?",      re.I), ("Houston",       "TX")),
    (re.compile(r"W\.?D\.?\s*Tex\.?",      re.I), ("San Antonio",   "TX")),
    (re.compile(r"E\.?D\.?\s*Tex\.?",      re.I), ("Beaumont",      "TX")),
    (re.compile(r"N\.?D\.?\s*Ill\.?",      re.I), ("Chicago",       "IL")),
    (re.compile(r"N\.?D\.?\s*Ohio",        re.I), ("Cleveland",     "OH")),
    (re.compile(r"S\.?D\.?\s*Ohio",        re.I), ("Columbus",      "OH")),
    (re.compile(r"E\.?D\.?\s*Mich\.?",     re.I), ("Detroit",       "MI")),
    (re.compile(r"W\.?D\.?\s*Mich\.?",     re.I), ("Grand Rapids",  "MI")),
    (re.compile(r"N\.?D\.?\s*Ga\.?",       re.I), ("Atlanta",       "GA")),
    (re.compile(r"S\.?D\.?\s*Fla\.?",      re.I), ("Miami",         "FL")),
    (re.compile(r"M\.?D\.?\s*Fla\.?",      re.I), ("Tampa",         "FL")),
    (re.compile(r"N\.?D\.?\s*Fla\.?",      re.I), ("Pensacola",     "FL")),
    (re.compile(r"E\.?D\.?\s*Pa\.?",       re.I), ("Philadelphia",  "PA")),
    (re.compile(r"W\.?D\.?\s*Pa\.?",       re.I), ("Pittsburgh",    "PA")),
    (re.compile(r"D\.?\s*Colo\.?",         re.I), ("Denver",        "CO")),
    (re.compile(r"D\.?\s*Ariz\.?",         re.I), ("Phoenix",       "AZ")),
    (re.compile(r"D\.?\s*N\.?J\.?",        re.I), ("Newark",        "NJ")),
    (re.compile(r"D\.?\s*Md\.?",           re.I), ("Baltimore",     "MD")),
    (re.compile(r"D\.?\s*Mass\.?",         re.I), ("Boston",        "MA")),
    (re.compile(r"D\.?\s*Conn\.?",         re.I), ("New Haven",     "CT")),
    (re.compile(r"W\.?D\.?\s*Wash\.?",     re.I), ("Seattle",       "WA")),
    (re.compile(r"E\.?D\.?\s*Wash\.?",     re.I), ("Spokane",       "WA")),
    (re.compile(r"D\.?\s*Or\.?",           re.I), ("Portland",      "OR")),
    (re.compile(r"D\.?\s*Nev\.?",          re.I), ("Las Vegas",     "NV")),
    (re.compile(r"D\.?\s*D\.?C\.?",        re.I), ("Washington",    "DC")),
    (re.compile(r"District of Columbia",   re.I), ("Washington",    "DC")),
    # State name fallbacks
    (re.compile(r"\bTexas\b",              re.I), ("Houston",       "TX")),
    (re.compile(r"\bCalifornia\b",         re.I), ("Los Angeles",   "CA")),
    (re.compile(r"\bNew York\b",           re.I), ("New York",      "NY")),
    (re.compile(r"\bFlorida\b",            re.I), ("Jacksonville",  "FL")),
    (re.compile(r"\bIllinois\b",           re.I), ("Chicago",       "IL")),
]


def district_to_city(court_str: str) -> tuple[str, str] | None:
    """
    Given a court citation string (e.g. 'W.D. Tex.' or 'S.D.N.Y.'),
    return (city, state) or None.
    """
    for pattern, location in _DISTRICT_PATTERNS:
        if pattern.search(court_str):
            return location
    return None


# ── make_case_id ──────────────────────────────────────────────────────────────

def make_case_id(city: str, state: str, vtype: str, date_str: str,
                 source_url: str = "", summary: str = "") -> str:
    # Include source_url and first 80 chars of summary to prevent collisions
    # when multiple cases share city/state/type/date (common with AP + DOJ feeds)
    discriminator = (source_url or summary[:80] or "").lower().replace(" ", "")
    raw = f"{city}{state}{vtype}{date_str}{discriminator}".lower().replace(" ", "")
    h   = hashlib.md5(raw.encode()).hexdigest()[:10].upper()
    yr  = (date_str or "")[:4] or "0000"
    return f"MEDUSA-{yr}-{h}"


# ── PUBLIC_FIGURE detection ───────────────────────────────────────────────────

_PUBLIC_FIGURE_KEYWORDS = {
    "senator", "congressman", "congresswoman", "representative", "governor",
    "mayor", "judge", "prosecutor", "sheriff", "police chief", "officer",
    "politician", "official", "minister", "lobbyist", "staffer",
    "council member", "assemblyman", "assemblywoman", "state rep",
    "attorney general", "secretary", "ambassador", "aide",
    "deputy", "commissioner", "superintendent", "president",
    "vice president", "cabinet", "professor", "coach",
    "administrator", "dean", "principal", "clergy", "pastor", "priest",
}


def detect_public_figure(summary: str) -> bool:
    s = (summary or "").lower()
    return any(kw in s for kw in _PUBLIC_FIGURE_KEYWORDS)


# ── normalize_record ──────────────────────────────────────────────────────────

def normalize_record(raw: dict) -> dict | None:
    """
    Validate and normalize a raw source dict into a complete MedusaRecord.
    Returns None if the record cannot be salvaged (invalid state, empty city, etc.).

    Input keys (all optional except noted):
        summary, city, state*, violence_type, status,
        date_incident, source_url, source_name, verified
    """
    # ── State (required) ─────────────────────────────────────────────────────
    state = validate_state(raw.get("state", ""))
    if not state:
        return None     # Can't place it in the US — drop

    # ── City ─────────────────────────────────────────────────────────────────
    city = validate_city(raw.get("city", ""))
    if not city:
        # Fall back to largest city in state rather than dropping
        city = STATE_LARGEST_CITY.get(state, "")
        if not city:
            return None

    # ── Violence type ─────────────────────────────────────────────────────────
    vtype = normalize_violence_type(raw.get("violence_type", ""))

    # ── Status ────────────────────────────────────────────────────────────────
    status = normalize_status(raw.get("status", ""))

    # ── Date ──────────────────────────────────────────────────────────────────
    date_incident = _clean_date(raw.get("date_incident", ""))

    # ── Summary ───────────────────────────────────────────────────────────────
    summary = (raw.get("summary") or "").strip()[:600]

    # ── Source ───────────────────────────────────────────────────────────────
    source_url  = (raw.get("source_url")  or "").strip()
    source_name = (raw.get("source_name") or "").strip()

    # ── Case ID ───────────────────────────────────────────────────────────────
    case_id = make_case_id(city, state, vtype, date_incident,
                           source_url=source_url, summary=summary)

    # ── Public figure ─────────────────────────────────────────────────────────
    is_public_figure = detect_public_figure(summary)

    return {
        "case_id":          case_id,
        "summary":          summary,
        "city":             city,
        "state":            state,
        "date_incident":    date_incident,
        "violence_type":    vtype,
        "status":           status,
        "source_url":       source_url,
        "source_name":      source_name,
        "verified":         bool(raw.get("verified", True)),
        "is_public_figure": is_public_figure,
        # lat/lng filled by scanner.py after geocoding
        "lat":              None,
        "lng":              None,
    }


def _clean_date(raw) -> str:
    if not raw:
        return ""
    s = str(raw).strip()
    # Already YYYY-MM-DD
    if re.match(r"\d{4}-\d{2}-\d{2}$", s):
        return s
    # YYYY-MM
    if re.match(r"\d{4}-\d{2}$", s):
        return s
    # YYYY
    if re.match(r"\d{4}$", s):
        return s
    # Try common formats
    for fmt in ("%Y-%m-%dT%H:%M:%S", "%Y-%m-%dT%H:%M:%SZ",
                "%m/%d/%Y", "%d %b %Y", "%B %d, %Y"):
        try:
            return datetime.strptime(s[:len(fmt)+5], fmt).strftime("%Y-%m-%d")
        except Exception:
            pass
    # Extract any YYYY-MM-DD substring
    m = re.search(r"\d{4}-\d{2}-\d{2}", s)
    if m:
        return m.group(0)
    # Extract just year
    m = re.search(r"\b(20\d{2})\b", s)
    if m:
        return m.group(1)
    return ""
