"""
sources/fbi_stats.py — FBI Crime Data Explorer (CDE) API

The real working endpoints (verified 2025):
  https://cde.ucr.cjis.gov/LATEST/webapp/public/api/data/nibrs/...
  https://api.usa.gov/crime/fbi/cde/...  ← requires demo key OR use ucr below

Best free, no-key endpoints:
  UCR offense counts by state, year:
    GET https://ucr.fbi.gov/api/table/10/{year}?api_key=iiHnOKfno2Mgkt5AynpvPpUQTEyxE77jo1RU8PIv
    (the iiHn... key is the public demo key FBI publishes openly)

  Alternate: CDE public API, no key required for some routes:
    GET https://cde.ucr.cjis.gov/LATEST/webapp/public/api/data/nibrs/sex-offenses/sex-offenses/count/national/{year}
    GET https://cde.ucr.cjis.gov/LATEST/webapp/public/api/data/nibrs/human-trafficking/human-trafficking/count/national/{year}

FBI data is aggregate statistics per state, NOT individual cases.
We generate one summary record per state where count > 0.
"""

import time
from medusa.fetch import safe_json
from medusa.record import STATE_LARGEST_CITY, VALID_STATES

# FBI public demo API key (published openly in their documentation)
FBI_DEMO_KEY = "iiHnOKfno2Mgkt5AynpvPpUQTEyxE77jo1RU8PIv"

# Primary: UCR summary API
UCR_BASE = "https://ucr.fbi.gov/api"

# Fallback: CDE public API (no key)
CDE_BASE = "https://cde.ucr.cjis.gov/LATEST/webapp/public/api/data/nibrs"

# Most recent reliable year
DATA_YEAR = 2022

# (offense_param, violence_type, label, cde_path)
OFFENSES = [
    ("rape",                 "rape",             "Rape",                 "sex-offenses/sex-offenses"),
    ("aggravated-assault",   "assault",          "Aggravated Assault",   "aggravated-assault/aggravated-assault"),
    ("homicide",             "homicide",         "Homicide",             "homicide/homicide"),
    ("human-trafficking",    "trafficking",      "Human Trafficking",    "human-trafficking/human-trafficking"),
]

# All US state abbreviations for iteration
ALL_STATES = list(VALID_STATES - {"DC"})


def fetch() -> list[dict]:
    """
    Pull FBI aggregate stats. Returns one summary record per state per offense
    type where data exists.
    """
    records = []

    for offense_param, vtype, label, cde_path in OFFENSES:
        state_records = _fetch_offense(offense_param, vtype, label, cde_path)
        records.extend(state_records)
        time.sleep(0.5)

    print(f"[FBI CDE] {len(records)} aggregate state records fetched.")
    return records


def _fetch_offense(offense_param: str, vtype: str,
                   label: str, cde_path: str) -> list[dict]:
    """Try multiple FBI API endpoints for a given offense type."""

    # ── Attempt 1: UCR summary API with demo key ──────────────────────────────
    # Returns national + state breakdown
    ucr_url = f"{UCR_BASE}/table/10/{DATA_YEAR}"
    data = safe_json(ucr_url, params={"api_key": FBI_DEMO_KEY, "offense": offense_param})
    if data:
        results = _parse_ucr_table(data, vtype, label)
        if results:
            return results

    # ── Attempt 2: CDE public endpoint (count by state) ──────────────────────
    for state in ALL_STATES[:5]:   # sample a few states
        cde_url = f"{CDE_BASE}/{cde_path}/count/states/offense/{state}/{DATA_YEAR}/{DATA_YEAR}"
        data = safe_json(cde_url)
        if data:
            # If this works, fetch all states
            return _fetch_cde_all_states(cde_path, vtype, label)

    # ── Attempt 3: CDE national aggregate then attribute to state ─────────────
    cde_national = f"{CDE_BASE}/{cde_path}/count/national/{DATA_YEAR}/{DATA_YEAR}"
    data = safe_json(cde_national)
    if data:
        return _parse_cde_national(data, vtype, label)

    return []


def _fetch_cde_all_states(cde_path: str, vtype: str, label: str) -> list[dict]:
    records = []
    for state in ALL_STATES:
        url = (
            f"{CDE_BASE}/{cde_path}/count/states/offense"
            f"/{state}/{DATA_YEAR}/{DATA_YEAR}"
        )
        data = safe_json(url)
        if not data:
            continue
        count = _extract_count_from_cde(data)
        if not count:
            continue
        city = STATE_LARGEST_CITY.get(state, "")
        if not city:
            continue
        records.append(_make_record(city, state, vtype, label, count))
        time.sleep(0.15)
    return records


def _parse_ucr_table(data, vtype: str, label: str) -> list[dict]:
    """Parse UCR /table/10 response — returns list per state."""
    records = []
    items = data if isinstance(data, list) else data.get("data", data.get("results", []))

    for item in items:
        state_abbr = _get_state(item)
        if not state_abbr or state_abbr not in VALID_STATES:
            continue
        count = _get_count(item)
        if not count:
            continue
        city = STATE_LARGEST_CITY.get(state_abbr, "")
        if not city:
            continue
        records.append(_make_record(city, state_abbr, vtype, label, count))

    return records


def _parse_cde_national(data, vtype: str, label: str) -> list[dict]:
    """Parse a national aggregate response — make one national record."""
    total = _get_count(data if isinstance(data, dict) else (data[0] if data else {}))
    if not total:
        # Try summing items
        items = data if isinstance(data, list) else data.get("data", [])
        total = sum(_get_count(i) or 0 for i in items)
    if not total:
        return []

    return [{
        "summary": (
            f"FBI UCR Data: {total:,} {label} incidents reported nationally "
            f"({DATA_YEAR}). Aggregate law enforcement reporting data."
        ),
        "city":          "Washington",
        "state":         "DC",
        "date_incident": str(DATA_YEAR),
        "violence_type": vtype,
        "status":        "reported",
        "source_url":    "https://cde.ucr.cjis.gov/",
        "source_name":   "FBI Crime Data Explorer (UCR)",
        "verified":      True,
    }]


def _make_record(city: str, state: str, vtype: str, label: str, count: int) -> dict:
    return {
        "summary": (
            f"FBI UCR Data: {count:,} {label} incidents reported in "
            f"{state} ({DATA_YEAR}). Aggregate law enforcement reporting data — "
            f"individual cases within this count may appear separately from other sources."
        ),
        "city":          city,
        "state":         state,
        "date_incident": str(DATA_YEAR),
        "violence_type": vtype,
        "status":        "reported",
        "source_url":    "https://cde.ucr.cjis.gov/",
        "source_name":   "FBI Crime Data Explorer (UCR)",
        "verified":      True,
    }


def _get_state(item: dict) -> str | None:
    for key in ("state_abbr", "state_id", "state", "StateAbbr", "abbr"):
        val = item.get(key)
        if val and len(str(val)) == 2:
            return str(val).upper()
    for key in ("state_name", "StateName", "name"):
        val = item.get(key)
        if val:
            from medusa.record import _NAME_TO_ABBR
            abbr = _NAME_TO_ABBR.get(str(val).lower().strip())
            if abbr:
                return abbr
    return None


def _get_count(item: dict) -> int | None:
    if not isinstance(item, dict):
        return None
    for key in ("value", "count", "actual", "reported", "total",
                "offenses", "incidents", "rape", "homicide", "data_value"):
        val = item.get(key)
        if val is not None:
            try:
                return int(float(str(val)))
            except (ValueError, TypeError):
                pass
    return None


def _extract_count_from_cde(data) -> int | None:
    if isinstance(data, list):
        total = 0
        for item in data:
            c = _get_count(item) if isinstance(item, dict) else None
            if c:
                total += c
        return total if total else None
    if isinstance(data, dict):
        return _get_count(data)
    return None
