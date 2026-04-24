"""
record.py — Medusa unified record format

Every source module produces a MedusaRecord dict.
Shape is locked here. DB layer reads this shape. Nothing else.

Also contains:
  - make_case_id()
  - detect_public_figure()
  - FEDERAL_DISTRICT_CITY  — deterministic district → city lookup
  - normalize_record()     — validates and fills defaults
"""

import hashlib
from typing import TypedDict

# ── Unified record shape ──────────────────────────────────────────────────────

VIOLENCE_TYPES = {
    "homicide", "assault", "sexual_assault", "stalking",
    "trafficking", "domestic_violence", "rape", "harassment",
    "attempted_murder", "child_abuse", "coercive_control",
}

STATUSES = {
    "reported", "charged", "convicted", "acquitted",
    "civil_judgment", "credible_allegation", "congressional_record", "unknown",
}

class MedusaRecord(TypedDict, total=False):
    case_id:          str           # MEDUSA-YYYY-XXXXXXXX  (set by normalize)
    summary:          str           # factual; no victim name
    city:             str
    state:            str           # 2-letter US abbrev
    date_incident:    str           # YYYY-MM-DD | YYYY-MM | YYYY
    violence_type:    str           # one of VIOLENCE_TYPES
    status:           str           # one of STATUSES
    source_url:       str
    source_name:      str
    is_public_figure: bool          # set by normalize
    verified:         bool
    lat:              float | None
    lng:              float | None


# ── Federal district → city (all 94 districts) ───────────────────────────────
# Key: lowercase normalized district abbreviation or partial name
# Used by CourtListener and DOJ source parsers.

FEDERAL_DISTRICT_CITY: dict[str, tuple[str, str]] = {
    # Alabama
    "n.d. ala.":    ("Birmingham",   "AL"),
    "m.d. ala.":    ("Montgomery",   "AL"),
    "s.d. ala.":    ("Mobile",       "AL"),
    # Alaska
    "d. alaska":    ("Anchorage",    "AK"),
    # Arizona
    "d. ariz.":     ("Phoenix",      "AZ"),
    # Arkansas
    "e.d. ark.":    ("Little Rock",  "AR"),
    "w.d. ark.":    ("Fort Smith",   "AR"),
    # California
    "n.d. cal.":    ("San Francisco","CA"),
    "e.d. cal.":    ("Sacramento",   "CA"),
    "c.d. cal.":    ("Los Angeles",  "CA"),
    "s.d. cal.":    ("San Diego",    "CA"),
    # Colorado
    "d. colo.":     ("Denver",       "CO"),
    # Connecticut
    "d. conn.":     ("New Haven",    "CT"),
    # Delaware
    "d. del.":      ("Wilmington",   "DE"),
    # DC
    "d.d.c.":       ("Washington",   "DC"),
    "d. d.c.":      ("Washington",   "DC"),
    # Florida
    "n.d. fla.":    ("Pensacola",    "FL"),
    "m.d. fla.":    ("Tampa",        "FL"),
    "s.d. fla.":    ("Miami",        "FL"),
    # Georgia
    "n.d. ga.":     ("Atlanta",      "GA"),
    "m.d. ga.":     ("Macon",        "GA"),
    "s.d. ga.":     ("Savannah",     "GA"),
    # Hawaii
    "d. haw.":      ("Honolulu",     "HI"),
    # Idaho
    "d. idaho":     ("Boise",        "ID"),
    # Illinois
    "n.d. ill.":    ("Chicago",      "IL"),
    "c.d. ill.":    ("Springfield",  "IL"),
    "s.d. ill.":    ("East St. Louis","IL"),
    # Indiana
    "n.d. ind.":    ("Hammond",      "IN"),
    "s.d. ind.":    ("Indianapolis", "IN"),
    # Iowa
    "n.d. iowa":    ("Cedar Rapids", "IA"),
    "s.d. iowa":    ("Des Moines",   "IA"),
    # Kansas
    "d. kan.":      ("Wichita",      "KS"),
    # Kentucky
    "e.d. ky.":     ("Lexington",    "KY"),
    "w.d. ky.":     ("Louisville",   "KY"),
    # Louisiana
    "e.d. la.":     ("New Orleans",  "LA"),
    "m.d. la.":     ("Baton Rouge",  "LA"),
    "w.d. la.":     ("Shreveport",   "LA"),
    # Maine
    "d. me.":       ("Portland",     "ME"),
    # Maryland
    "d. md.":       ("Baltimore",    "MD"),
    # Massachusetts
    "d. mass.":     ("Boston",       "MA"),
    # Michigan
    "e.d. mich.":   ("Detroit",      "MI"),
    "w.d. mich.":   ("Grand Rapids", "MI"),
    # Minnesota
    "d. minn.":     ("Minneapolis",  "MN"),
    # Mississippi
    "n.d. miss.":   ("Oxford",       "MS"),
    "s.d. miss.":   ("Jackson",      "MS"),
    # Missouri
    "e.d. mo.":     ("St. Louis",    "MO"),
    "w.d. mo.":     ("Kansas City",  "MO"),
    # Montana
    "d. mont.":     ("Billings",     "MT"),
    # Nebraska
    "d. neb.":      ("Omaha",        "NE"),
    # Nevada
    "d. nev.":      ("Las Vegas",    "NV"),
    # New Hampshire
    "d.n.h.":       ("Concord",      "NH"),
    "d. n.h.":      ("Concord",      "NH"),
    # New Jersey
    "d.n.j.":       ("Newark",       "NJ"),
    "d. n.j.":      ("Newark",       "NJ"),
    # New Mexico
    "d.n.m.":       ("Albuquerque",  "NM"),
    "d. n.m.":      ("Albuquerque",  "NM"),
    # New York
    "n.d.n.y.":     ("Albany",       "NY"),
    "n.d. n.y.":    ("Albany",       "NY"),
    "e.d.n.y.":     ("Brooklyn",     "NY"),
    "e.d. n.y.":    ("Brooklyn",     "NY"),
    "s.d.n.y.":     ("New York",     "NY"),
    "s.d. n.y.":    ("New York",     "NY"),
    "w.d.n.y.":     ("Buffalo",      "NY"),
    "w.d. n.y.":    ("Buffalo",      "NY"),
    # North Carolina
    "e.d.n.c.":     ("Raleigh",      "NC"),
    "e.d. n.c.":    ("Raleigh",      "NC"),
    "m.d.n.c.":     ("Greensboro",   "NC"),
    "m.d. n.c.":    ("Greensboro",   "NC"),
    "w.d.n.c.":     ("Charlotte",    "NC"),
    "w.d. n.c.":    ("Charlotte",    "NC"),
    # North Dakota
    "d.n.d.":       ("Bismarck",     "ND"),
    "d. n.d.":      ("Bismarck",     "ND"),
    # Ohio
    "n.d. ohio":    ("Cleveland",    "OH"),
    "s.d. ohio":    ("Columbus",     "OH"),
    # Oklahoma
    "n.d. okla.":   ("Tulsa",        "OK"),
    "e.d. okla.":   ("Muskogee",     "OK"),
    "w.d. okla.":   ("Oklahoma City","OK"),
    # Oregon
    "d. or.":       ("Portland",     "OR"),
    # Pennsylvania
    "e.d. pa.":     ("Philadelphia", "PA"),
    "m.d. pa.":     ("Scranton",     "PA"),
    "w.d. pa.":     ("Pittsburgh",   "PA"),
    # Rhode Island
    "d.r.i.":       ("Providence",   "RI"),
    "d. r.i.":      ("Providence",   "RI"),
    # South Carolina
    "d.s.c.":       ("Columbia",     "SC"),
    "d. s.c.":      ("Columbia",     "SC"),
    # South Dakota
    "d.s.d.":       ("Sioux Falls",  "SD"),
    "d. s.d.":      ("Sioux Falls",  "SD"),
    # Tennessee
    "e.d. tenn.":   ("Knoxville",    "TN"),
    "m.d. tenn.":   ("Nashville",    "TN"),
    "w.d. tenn.":   ("Memphis",      "TN"),
    # Texas
    "n.d. tex.":    ("Dallas",       "TX"),
    "e.d. tex.":    ("Beaumont",     "TX"),
    "s.d. tex.":    ("Houston",      "TX"),
    "w.d. tex.":    ("San Antonio",  "TX"),
    # Utah
    "d. utah":      ("Salt Lake City","UT"),
    # Vermont
    "d. vt.":       ("Burlington",   "VT"),
    # Virginia
    "e.d. va.":     ("Alexandria",   "VA"),
    "w.d. va.":     ("Roanoke",      "VA"),
    # Washington
    "e.d. wash.":   ("Spokane",      "WA"),
    "w.d. wash.":   ("Seattle",      "WA"),
    # West Virginia
    "n.d.w. va.":   ("Clarksburg",   "WV"),
    "n.d. w. va.":  ("Clarksburg",   "WV"),
    "s.d.w. va.":   ("Charleston",   "WV"),
    "s.d. w. va.":  ("Charleston",   "WV"),
    # Wisconsin
    "e.d. wis.":    ("Milwaukee",    "WI"),
    "w.d. wis.":    ("Madison",      "WI"),
    # Wyoming
    "d. wyo.":      ("Cheyenne",     "WY"),
}

# Verbose name fragments → lookup (for CourtListener "court_full_name" field)
DISTRICT_NAME_FRAGMENTS: dict[str, tuple[str, str]] = {
    "northern district of alabama":     ("Birmingham",    "AL"),
    "middle district of alabama":       ("Montgomery",    "AL"),
    "southern district of alabama":     ("Mobile",        "AL"),
    "district of alaska":               ("Anchorage",     "AK"),
    "district of arizona":              ("Phoenix",       "AZ"),
    "eastern district of arkansas":     ("Little Rock",   "AR"),
    "western district of arkansas":     ("Fort Smith",    "AR"),
    "northern district of california":  ("San Francisco", "CA"),
    "eastern district of california":   ("Sacramento",    "CA"),
    "central district of california":   ("Los Angeles",   "CA"),
    "southern district of california":  ("San Diego",     "CA"),
    "district of colorado":             ("Denver",        "CO"),
    "district of connecticut":          ("New Haven",     "CT"),
    "district of delaware":             ("Wilmington",    "DE"),
    "district of columbia":             ("Washington",    "DC"),
    "northern district of florida":     ("Pensacola",     "FL"),
    "middle district of florida":       ("Tampa",         "FL"),
    "southern district of florida":     ("Miami",         "FL"),
    "northern district of georgia":     ("Atlanta",       "GA"),
    "middle district of georgia":       ("Macon",         "GA"),
    "southern district of georgia":     ("Savannah",      "GA"),
    "district of hawaii":               ("Honolulu",      "HI"),
    "district of idaho":                ("Boise",         "ID"),
    "northern district of illinois":    ("Chicago",       "IL"),
    "central district of illinois":     ("Springfield",   "IL"),
    "southern district of illinois":    ("East St. Louis","IL"),
    "northern district of indiana":     ("Hammond",       "IN"),
    "southern district of indiana":     ("Indianapolis",  "IN"),
    "northern district of iowa":        ("Cedar Rapids",  "IA"),
    "southern district of iowa":        ("Des Moines",    "IA"),
    "district of kansas":               ("Wichita",       "KS"),
    "eastern district of kentucky":     ("Lexington",     "KY"),
    "western district of kentucky":     ("Louisville",    "KY"),
    "eastern district of louisiana":    ("New Orleans",   "LA"),
    "middle district of louisiana":     ("Baton Rouge",   "LA"),
    "western district of louisiana":    ("Shreveport",    "LA"),
    "district of maine":                ("Portland",      "ME"),
    "district of maryland":             ("Baltimore",     "MD"),
    "district of massachusetts":        ("Boston",        "MA"),
    "eastern district of michigan":     ("Detroit",       "MI"),
    "western district of michigan":     ("Grand Rapids",  "MI"),
    "district of minnesota":            ("Minneapolis",   "MN"),
    "northern district of mississippi": ("Oxford",        "MS"),
    "southern district of mississippi": ("Jackson",       "MS"),
    "eastern district of missouri":     ("St. Louis",     "MO"),
    "western district of missouri":     ("Kansas City",   "MO"),
    "district of montana":              ("Billings",      "MT"),
    "district of nebraska":             ("Omaha",         "NE"),
    "district of nevada":               ("Las Vegas",     "NV"),
    "district of new hampshire":        ("Concord",       "NH"),
    "district of new jersey":           ("Newark",        "NJ"),
    "district of new mexico":           ("Albuquerque",   "NM"),
    "northern district of new york":    ("Albany",        "NY"),
    "eastern district of new york":     ("Brooklyn",      "NY"),
    "southern district of new york":    ("New York",      "NY"),
    "western district of new york":     ("Buffalo",       "NY"),
    "eastern district of north carolina":("Raleigh",      "NC"),
    "middle district of north carolina": ("Greensboro",   "NC"),
    "western district of north carolina":("Charlotte",    "NC"),
    "district of north dakota":         ("Bismarck",      "ND"),
    "northern district of ohio":        ("Cleveland",     "OH"),
    "southern district of ohio":        ("Columbus",      "OH"),
    "northern district of oklahoma":    ("Tulsa",         "OK"),
    "eastern district of oklahoma":     ("Muskogee",      "OK"),
    "western district of oklahoma":     ("Oklahoma City", "OK"),
    "district of oregon":               ("Portland",      "OR"),
    "eastern district of pennsylvania": ("Philadelphia",  "PA"),
    "middle district of pennsylvania":  ("Scranton",      "PA"),
    "western district of pennsylvania": ("Pittsburgh",    "PA"),
    "district of rhode island":         ("Providence",    "RI"),
    "district of south carolina":       ("Columbia",      "SC"),
    "district of south dakota":         ("Sioux Falls",   "SD"),
    "eastern district of tennessee":    ("Knoxville",     "TN"),
    "middle district of tennessee":     ("Nashville",     "TN"),
    "western district of tennessee":    ("Memphis",       "TN"),
    "northern district of texas":       ("Dallas",        "TX"),
    "eastern district of texas":        ("Beaumont",      "TX"),
    "southern district of texas":       ("Houston",       "TX"),
    "western district of texas":        ("San Antonio",   "TX"),
    "district of utah":                 ("Salt Lake City","UT"),
    "district of vermont":              ("Burlington",    "VT"),
    "eastern district of virginia":     ("Alexandria",    "VA"),
    "western district of virginia":     ("Roanoke",       "VA"),
    "eastern district of washington":   ("Spokane",       "WA"),
    "western district of washington":   ("Seattle",       "WA"),
    "northern district of west virginia":("Clarksburg",   "WV"),
    "southern district of west virginia":("Charleston",   "WV"),
    "eastern district of wisconsin":    ("Milwaukee",     "WI"),
    "western district of wisconsin":    ("Madison",       "WI"),
    "district of wyoming":              ("Cheyenne",      "WY"),
}


def district_to_city(court_name: str) -> tuple[str, str] | None:
    """
    Given a court name string (any format), return (city, state) or None.
    Tries abbreviated form first, then verbose fragment matching.
    """
    if not court_name:
        return None
    s = court_name.lower().strip()

    # Try abbreviated
    if s in FEDERAL_DISTRICT_CITY:
        return FEDERAL_DISTRICT_CITY[s]

    # Try verbose fragment
    for fragment, loc in DISTRICT_NAME_FRAGMENTS.items():
        if fragment in s:
            return loc

    return None


# ── Public figure detection ───────────────────────────────────────────────────

PUBLIC_FIGURE_KEYWORDS = {
    "senator", "congressman", "congresswoman", "representative", "governor",
    "mayor", "judge", "prosecutor", "sheriff", "police chief", "officer",
    "politician", "official", "minister", "lobbyist", "staffer",
    "council member", "assemblyman", "assemblywoman", "state rep",
    "attorney general", "secretary", "ambassador", "aide",
    "deputy", "commissioner", "superintendent",
    "president", "vice president", "cabinet", "professor", "coach",
    "administrator", "dean", "principal", "clergy", "pastor", "priest",
    "reverend", "bishop", "deacon",
}


def detect_public_figure(summary: str) -> bool:
    s = (summary or "").lower()
    return any(kw in s for kw in PUBLIC_FIGURE_KEYWORDS)


# ── Case ID ───────────────────────────────────────────────────────────────────

def make_case_id(city: str, state: str, vtype: str, date_str: str, source_url: str = "") -> str:
    raw = f"{city}{state}{vtype}{date_str}{source_url}".lower().replace(" ", "")
    h   = hashlib.md5(raw.encode()).hexdigest()[:8].upper()
    yr  = (date_str or "")[:4] or "0000"
    return f"MEDUSA-{yr}-{h}"


# ── Record normalizer ─────────────────────────────────────────────────────────

_BOGUS_CITIES = {
    "federal", "national", "unknown", "n/a", "na", "none",
    "us", "usa", "united states", "washington dc",   # DC ok only if actually DC
}

# State field values that are not real US states — drop the record entirely
_BOGUS_STATES = {
    "us", "usa", "united states", "america", "federal", "national",
    "unknown", "n/a", "na", "none", "",
    # Full country names that might bleed in from sources
    "canada", "mexico", "uk", "england", "australia", "germany",
    "france", "spain", "italy", "brazil", "china", "japan", "india",
    "nigeria", "kenya", "south africa", "pakistan", "afghanistan",
}

_STATE_ABBREVS = {
    "AL","AK","AZ","AR","CA","CO","CT","DE","FL","GA","HI","ID","IL","IN",
    "IA","KS","KY","LA","ME","MD","MA","MI","MN","MS","MO","MT","NE","NV",
    "NH","NJ","NM","NY","NC","ND","OH","OK","OR","PA","RI","SC","SD","TN",
    "TX","UT","VT","VA","WA","WV","WI","WY","DC",
}

# State name → abbreviation fallback
_STATE_NAMES = {
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

# State abbreviation → largest city (last-resort geocoding fallback)
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


def normalize_state(raw: str) -> str | None:
    if not raw:
        return None
    # Reject anything that's clearly not a US state
    if raw.strip().lower() in _BOGUS_STATES:
        return None
    s = raw.strip().upper()
    if s in _STATE_ABBREVS:
        return s
    # Try full name
    abbr = _STATE_NAMES.get(raw.strip().lower())
    return abbr


def normalize_violence_type(raw: str) -> str:
    if not raw:
        return "assault"
    v = raw.lower().strip().replace(" ", "_").replace("-", "_")
    if v in VIOLENCE_TYPES:
        return v
    # Fuzzy map
    if "homicid" in v or "murder" in v or "femicid" in v or "kill" in v:
        return "homicide"
    if "rape" in v:
        return "rape"
    if "sexual" in v or "sex_assault" in v:
        return "sexual_assault"
    if "domestic" in v or "intimate" in v or "partner" in v:
        return "domestic_violence"
    if "stalking" in v or "stalk" in v:
        return "stalking"
    if "trafficking" in v or "traffick" in v:
        return "trafficking"
    if "harass" in v:
        return "harassment"
    if "attempted" in v or "attempt" in v:
        return "attempted_murder"
    if "child" in v or "minor" in v:
        return "child_abuse"
    if "coercive" in v or "control" in v:
        return "coercive_control"
    return "assault"


def normalize_status(raw: str) -> str:
    if not raw:
        return "unknown"
    s = raw.lower().strip()
    if s in STATUSES:
        return s
    if "convict" in s or "guilty" in s or "sentenced" in s:
        return "convicted"
    if "charg" in s or "arrest" in s or "indicted" in s:
        return "charged"
    if "acquit" in s or "not guilty" in s:
        return "acquitted"
    if "civil" in s or "judgment" in s or "settlement" in s:
        return "civil_judgment"
    if "congressional" in s or "testimony" in s or "hearing" in s:
        return "congressional_record"
    if "report" in s or "alleged" in s or "allegation" in s:
        return "reported"
    if "credible" in s:
        return "credible_allegation"
    return "unknown"


def normalize_record(r: dict) -> dict | None:
    """
    Validate and fill defaults. Returns None if record is unusable.
    Fixes bogus city values in place.
    """
    # State
    state = normalize_state(r.get("state", ""))
    if not state:
        return None
    r["state"] = state

    # City — fix "Federal", "National", etc.
    city = (r.get("city") or "").strip()
    if not city or city.lower() in _BOGUS_CITIES:
        city = STATE_LARGEST_CITY.get(state, "")
    r["city"] = city

    if not city:
        return None

    # Violence type
    r["violence_type"] = normalize_violence_type(r.get("violence_type", ""))

    # Status
    r["status"] = normalize_status(r.get("status", ""))

    # Booleans
    r.setdefault("verified", True)
    r["is_public_figure"] = detect_public_figure(r.get("summary", ""))

    # Case ID
    r["case_id"] = make_case_id(
        r["city"], r["state"],
        r["violence_type"], r.get("date_incident", ""),
        r.get("source_url", "")
    )

    # Defaults
    r.setdefault("summary", "")
    r.setdefault("source_url", "")
    r.setdefault("source_name", "")
    r.setdefault("lat", None)
    r.setdefault("lng", None)

    return r
