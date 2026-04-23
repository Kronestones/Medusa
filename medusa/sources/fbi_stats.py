"""
sources/fbi_stats.py — FBI Crime Data Explorer (CDE) API

Free, no API key required.
Base URL: https://cde.ucr.cjis.gov/LATEST/webapp/#/pages/explorer/crime/crime-trend

REST API endpoint (undocumented but public):
  https://api.usa.gov/crime/fbi/cde/

NOTE: FBI data is aggregated statistics, NOT individual case records.
We use it to generate summary records per state showing documented
violence statistics. These appear on the map as state-level data points
with counts rather than named individual cases.

Offenses tracked:
  - Rape (legacy + revised definition)
  - Aggravated assault (female victims)
  - Homicide (female victims)
  - Human trafficking
"""

import time
from medusa.fetch import safe_json
from medusa.record import STATE_LARGEST_CITY, VALID_STATES

FBI_BASE = "https://api.usa.gov/crime/fbi/cde"

# Most recent year we can reliably pull
DATA_YEAR = 2022

# Offense codes we care about
OFFENSES = [
    ("rape-legacy",       "rape",              "Rape (FBI UCR)"),
    ("aggravated-assault","assault",            "Aggravated Assault (FBI UCR)"),
    ("homicide",          "homicide",           "Homicide (FBI UCR)"),
    ("human-trafficking", "trafficking",        "Human Trafficking (FBI UCR)"),
]


def fetch() -> list[dict]:
    """
    Pull FBI CDE aggregate stats by state.
    Returns one summary record per state per offense type where data exists.
    These are statistical/aggregate records, not individual cases.
    """
    records = []

    for offense_slug, vtype, offense_label in OFFENSES:
        state_records = _fetch_offense_by_state(offense_slug, vtype, offense_label)
        records.extend(state_records)
        time.sleep(0.5)   # be polite to the API

    print(f"[FBI CDE] {len(records)} aggregate state records fetched.")
    return records


def _fetch_offense_by_state(offense_slug: str, vtype: str,
                             offense_label: str) -> list[dict]:
    """Fetch a single offense type across all states for DATA_YEAR."""
    url = f"{FBI_BASE}/estimate/national/{offense_slug}/{DATA_YEAR}/{DATA_YEAR}"
    data = safe_json(url)

    if not data:
        # Try alternate endpoint structure
        url2 = f"{FBI_BASE}/offense/state/run/{offense_slug}/{DATA_YEAR}/{DATA_YEAR}"
        data = safe_json(url2)

    if not data:
        return []

    records = []

    # FBI API returns either a list of state objects or a dict with nested data
    items = data if isinstance(data, list) else data.get("data", data.get("results", []))

    for item in items:
        state_abbr = _extract_state(item)
        if not state_abbr or state_abbr not in VALID_STATES:
            continue

        count = _extract_count(item)
        if count is None or count == 0:
            continue

        city = STATE_LARGEST_CITY.get(state_abbr, "")
        if not city:
            continue

        summary = (
            f"FBI UCR Data: {count:,} {offense_label} incidents reported in "
            f"{state_abbr} ({DATA_YEAR}). This is aggregate law enforcement "
            f"reporting data — individual cases within this count may appear "
            f"separately from other sources."
        )

        records.append({
            "summary":       summary,
            "city":          city,
            "state":         state_abbr,
            "date_incident": str(DATA_YEAR),
            "violence_type": vtype,
            "status":        "reported",
            "source_url":    f"https://cde.ucr.cjis.gov/",
            "source_name":   "FBI Crime Data Explorer (UCR)",
            "verified":      True,
        })

    return records


def _extract_state(item: dict) -> str | None:
    """Extract 2-letter state abbreviation from FBI API response item."""
    # Try common field names
    for key in ("state_abbr", "state_id", "state", "StateAbbr", "abbr"):
        val = item.get(key)
        if val and len(str(val)) == 2:
            return str(val).upper()

    # Try state name
    for key in ("state_name", "StateName", "name"):
        val = item.get(key)
        if val:
            from medusa.record import validate_state, _NAME_TO_ABBR
            abbr = _NAME_TO_ABBR.get(str(val).lower().strip())
            if abbr:
                return abbr

    return None


def _extract_count(item: dict) -> int | None:
    """Extract numeric count from FBI API response item."""
    for key in ("value", "count", "actual", "reported", "total",
                "offenses", "incidents", "rape", "homicide"):
        val = item.get(key)
        if val is not None:
            try:
                return int(val)
            except (ValueError, TypeError):
                pass
    return None
