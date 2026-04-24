"""
sources/fbi_stats.py — FBI Crime Data Explorer API (no API key required)

The FBI CDE API at api.usa.gov/crime/fbi/cde/ is completely free and keyless.
It provides aggregated statistics — not individual case records.

We use it to:
  1. Pull state-level violent crime counts (as context/reference records)
  2. Identify states/years with high concentrations for targeted scanning

Note: This source produces AGGREGATE records, not individual cases.
      They are marked status="reported" and summarize FBI statistical data.
      They appear on the map as state-centroid markers.

API docs: https://cde.ucr.cjis.gov/LATEST/webapp/#/pages/docApi
"""

import re
from medusa.fetch import safe_json
from medusa.record import STATE_LARGEST_CITY

BASE = "https://api.usa.gov/crime/fbi/cde"

# Offense types relevant to violence against women
# FBI UCR offense codes
OFFENSE_MAP = {
    "rape":                    "rape",
    "aggravated-assault":      "assault",
    "human-trafficking":       "trafficking",
    "sex-offenses":            "sexual_assault",
    "fondling":                "sexual_assault",
    "sodomy":                  "rape",
    "sexual-assault-w-object": "sexual_assault",
}

# Pull last 3 years of data
YEARS = ["2021", "2022", "2023"]

# States to sample (all 50 + DC would be 150+ calls — sample top states by population)
SAMPLE_STATES = [
    "CA", "TX", "FL", "NY", "PA", "IL", "OH", "GA", "NC", "MI",
    "NJ", "VA", "WA", "AZ", "MA", "TN", "IN", "MO", "MD", "WI",
    "CO", "MN", "SC", "AL", "LA", "KY", "OR", "OK", "CT", "NV",
]


def fetch() -> list[dict]:
    """
    Pull FBI CDE aggregate offense data. Returns state-level summary records.
    These are statistical markers, not individual cases.
    """
    records = []

    for offense_slug, vtype in OFFENSE_MAP.items():
        for year in YEARS:
            data = safe_json(
                f"{BASE}/offense/state/offenses/{offense_slug}/{year}",
                params={"offense": offense_slug},
            )
            if not data:
                continue

            results = data if isinstance(data, list) else data.get("results", [])
            for item in results:
                rec = _parse_item(item, offense_slug, vtype, year)
                if rec:
                    records.append(rec)

    print(f"[FBI CDE] {len(records)} aggregate records fetched.")
    return records


def _parse_item(item: dict, offense_slug: str, vtype: str, year: str) -> dict | None:
    state = (item.get("state_abbr") or item.get("state") or "").strip().upper()
    if not state or len(state) != 2:
        return None

    count = item.get("actual") or item.get("count") or 0
    if not count:
        return None

    city = STATE_LARGEST_CITY.get(state, "")
    if not city:
        return None

    offense_label = offense_slug.replace("-", " ").title()
    summary = (
        f"FBI UCR data: {count:,} reported {offense_label} incidents in "
        f"{state} ({year}). Source: FBI Crime Data Explorer."
    )

    return {
        "summary":       summary,
        "city":          city,
        "state":         state,
        "date_incident": f"{year}-01-01",
        "violence_type": vtype,
        "status":        "reported",
        "source_url":    f"https://cde.ucr.cjis.gov/LATEST/webapp/#/pages/explorer/crime/crime-trend",
        "source_name":   "FBI Crime Data Explorer",
        "verified":      True,
    }
