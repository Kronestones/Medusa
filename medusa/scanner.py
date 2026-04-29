"""
scanner.py — Medusa orchestrator (v1.2)

Coordinates all free public API source modules.
No Claude API calls. No web search API. Sources speak directly.

Sources:
  CourtListener  — federal docket mirror, free REST API, no key
  AP News RSS    — wire service crime/justice feeds, no key
  Congress RSS   — Judiciary committee hearings, no key
  FBI CDE        — aggregate crime statistics, no key
  ED.gov         — Title IX / OCR resolution agreements, no key

Flow:
  1. Each source module fetches and returns partial MedusaRecord dicts
  2. Orchestrator normalizes, deduplicates, geocodes
  3. Returns enriched list to main.py for DB persistence

All geocoding via Nominatim (OpenStreetMap) — free, no key.
"""

import time
import hashlib
from datetime import datetime, timezone

import requests

from medusa.meta import ScanHistory, ScanRecord
from medusa.purpose import MISSION, CREATED_FOR
from medusa.watchdog import SourceWatchdog
from medusa.record import (
    normalize_record, make_case_id,
    STATE_LARGEST_CITY,
)

# Source modules
from medusa.sources import courtlistener
from medusa.sources import ap_rss
from medusa.sources import congress_rss
from medusa.sources import fbi_stats
from medusa.sources import ed_gov
from medusa.sources import ag_press
from medusa.sources import wiki_homicides


# State centroids — fallback when Nominatim fails
STATE_COORDS = {
    "AL": (32.806671, -86.791130), "AK": (61.370716,-152.404419),
    "AZ": (33.729759,-111.431221), "AR": (34.969704, -92.373123),
    "CA": (36.116203,-119.681564), "CO": (39.059811,-105.311104),
    "CT": (41.597782, -72.755371), "DE": (39.318523, -75.507141),
    "FL": (27.766279, -81.686783), "GA": (33.040619, -83.643074),
    "HI": (21.094318,-157.498337), "ID": (44.240459,-114.478828),
    "IL": (40.349457, -88.986137), "IN": (39.849426, -86.258278),
    "IA": (42.011539, -93.210526), "KS": (38.526600, -96.726486),
    "KY": (37.668140, -84.670067), "LA": (31.169960, -91.867805),
    "ME": (44.693947, -69.381927), "MD": (39.063946, -76.802101),
    "MA": (42.230171, -71.530106), "MI": (43.326618, -84.536095),
    "MN": (45.694454, -93.900192), "MS": (32.741646, -89.678696),
    "MO": (38.456085, -92.288368), "MT": (46.921925,-110.454353),
    "NE": (41.125370, -98.268082), "NV": (38.313515,-117.055374),
    "NH": (43.452492, -71.563896), "NJ": (40.298904, -74.521011),
    "NM": (34.840515,-106.248482), "NY": (42.165726, -74.948051),
    "NC": (35.630066, -79.806419), "ND": (47.528912, -99.784012),
    "OH": (40.388783, -82.764915), "OK": (35.565342, -96.928917),
    "OR": (44.572021,-122.070938), "PA": (40.590752, -77.209755),
    "RI": (41.680893, -71.511780), "SC": (33.856892, -80.945007),
    "SD": (44.299782, -99.438828), "TN": (35.747845, -86.692345),
    "TX": (31.054487, -97.563461), "UT": (40.150032,-111.862434),
    "VT": (44.045876, -72.710686), "VA": (37.769337, -78.169968),
    "WA": (47.400902,-121.490494), "WV": (38.491226, -80.954453),
    "WI": (44.268543, -89.616508), "WY": (42.755966,-107.302490),
    "DC": (38.895110, -77.036366),
}

_geocode_cache: dict[str, tuple] = {}


def geocode(city: str, state: str) -> tuple:
    key = f"{city},{state}"
    if key in _geocode_cache:
        return _geocode_cache[key]
    try:
        resp = requests.get(
            "https://nominatim.openstreetmap.org/search",
            params={
                "q":            f"{city}, {state}, United States",
                "format":       "json",
                "limit":        1,
                "countrycodes": "us",
            },
            headers={"User-Agent": "Medusa/1.2 (sentinel.commons@gmail.com)"},
            timeout=5,
        )
        if resp.ok:
            data = resp.json()
            if data:
                lat = float(data[0]["lat"])
                lng = float(data[0]["lon"])
                _geocode_cache[key] = (lat, lng)
                return lat, lng
    except Exception:
        pass
    coords = STATE_COORDS.get(state.upper(), (None, None))
    _geocode_cache[key] = coords
    return coords



# ── Scope filter ──────────────────────────────────────────────────────────────
# Medusa documents male violence against women and children ONLY.
# This gate runs after normalization and drops anything outside that mission.

# Female perpetrator indicators — drop these cases entirely
_FEMALE_PERP_TERMS = [
    "woman pleads", "woman convicted", "woman sentenced", "woman arrested",
    "woman charged", "woman indicted", "woman guilty",
    "female suspect", "female defendant", "female perpetrator",
    "mother convicted", "mother pleads", "mother sentenced", "mother charged",
    "wife convicted", "wife pleads", "wife sentenced",
    "girlfriend convicted", "girlfriend sentenced",
]

# Out-of-scope subject matter — not male violence against women/children
_OUT_OF_SCOPE_TERMS = [
    "animal crush", "animal cruelty", "monkey", "dog fighting",
    "drug trafficking", "drug possession", "drug distribution",
    "tax fraud", "tax evasion", "financial fraud", "bank fraud",
    "immigration violation", "border crossing",
    "terrorism", "bomb threat",
    "death sentence reinstated",     # AG press releases re: old cases
    "attorney general announces",    # press releases, not incidents
    "for immediate release",         # press release boilerplate
    "for press inquiries",
]

# Must contain at least one victim-context term to confirm relevance
_VICTIM_TERMS = [
    "woman", "women", "female", "girl", "girls", "daughter",
    "wife", "girlfriend", "mother", "victim", "survivor",
    "child", "children", "minor", "juvenile", "infant", "baby",
    "domestic violence", "sexual assault", "rape", "stalking",
    "trafficking", "abuse", "exploitation", "harassment",
    "intimate partner", "dating violence",
    "transgender woman", "transgender girl", "transgender female",
    "trans woman", "trans girl", "transfeminine",
]


def _is_in_scope(record: dict) -> bool:
    """
    Returns True only if record is male violence against women/children.

    Court records (CourtListener, AG Press) get a lighter touch —
    case names like "State v. Johnson" have no victim terms even when
    the case is domestic violence. We trust the violence_type inference
    for court sources and only apply strict victim filtering to news.
    """
    text = " ".join([
        str(record.get("title", "")),
        str(record.get("summary", "")),
        str(record.get("description", "")),
        str(record.get("detail", "")),
    ]).lower()

    # Drop female perpetrators always
    if any(term in text for term in _FEMALE_PERP_TERMS):
        return False

    # Drop out-of-scope subject matter always
    if any(term in text for term in _OUT_OF_SCOPE_TERMS):
        return False

    # Court sources — trust violence_type inference, skip victim term check
    court_sources = {"courtlistener", "pacer", "court", "attorney general",
                     "ag press", "doj", "justice.gov"}
    source = str(record.get("source_name", "")).lower()
    if any(cs in source for cs in court_sources):
        vtype = str(record.get("violence_type", ""))
        if vtype and vtype != "unknown":
            return True

    # News sources — require victim context terms
    if not any(term in text for term in _VICTIM_TERMS):
        return False

    return True

    # Drop out-of-scope subject matter
    if any(term in text for term in _OUT_OF_SCOPE_TERMS):
        return False

    # Must have victim context
    if not any(term in text for term in _VICTIM_TERMS):
        return False

    return True


class MedusaScanner:

    def __init__(self):
        self.last_scan   = None
        self.total_found = 0
        self._history    = ScanHistory()
        self._watchdog   = SourceWatchdog()

    def scan(self) -> list[dict]:
        """
        Run all source modules. Returns enriched, deduplicated case dicts.
        """
        print("[Medusa] Starting free-source public records scan...")
        print(f"[Medusa] Mission: {MISSION}")
        print(f"[Medusa] For: {CREATED_FOR}")
        print("[Medusa] Sources: CourtListener · AP RSS · Congress RSS · FBI CDE · ED.gov")

        raw_records: list[dict] = []

        # ── Collect from each source ──────────────────────────────────────────
        sources = [
            ("CourtListener", courtlistener.fetch),
            ("AP News RSS",   ap_rss.fetch),
            ("Congress RSS",  congress_rss.fetch),
            ("FBI CDE",       fbi_stats.fetch),
            ("ED.gov",        ed_gov.fetch),
            ("AG Press",      ag_press.fetch),
            ("Wiki Homicides", wiki_homicides.fetch),
        ]

        from concurrent.futures import ThreadPoolExecutor, as_completed

        def _fetch_source(name, fetch_fn):
            try:
                results = fetch_fn()
                print(f"[Medusa] {name}: {len(results)} raw records")
                return results
            except Exception as e:
                print(f"[Medusa] {name} ERROR: {e}")
                return []

        with ThreadPoolExecutor(max_workers=4) as executor:
            futures = {executor.submit(_fetch_source, name, fn): name for name, fn in sources}
            for future in as_completed(futures):
                raw_records.extend(future.result())

        print(f"[Medusa] Total raw records: {len(raw_records)}")

        # ── Watchdog — record source health ──────────────────────
        try:
            source_counts = {}
            for name, _ in sources:
                source_counts[name] = len([r for r in raw_records
                                          if r.get("source_name","").startswith(name.split()[0])])
            self._watchdog.record_scan(source_counts)
            print(self._watchdog.health_report())
        except Exception as e:
            print(f"[Watchdog] Error: {e}")

        # ── Normalize ─────────────────────────────────────────────────────────
        normalized = []
        for r in raw_records:
            # Strip internal-only keys before normalize
            r.pop("_docket_id", None)
            cleaned = normalize_record(r)
            if cleaned:
                normalized.append(cleaned)

        print(f"[Medusa] After normalization: {len(normalized)} valid records")

        # ── Relevance filter — male violence against women/children ONLY ──────
        normalized = [r for r in normalized if _is_in_scope(r)]
        print(f"[Medusa] After scope filter: {len(normalized)} in-scope records")

        # ── Deduplicate by case_id and summary fingerprint ─────────────────────
        import hashlib as _hl
        seen_ids    : set[str] = set()
        seen_prints : set[str] = set()
        unique      : list[dict] = []

        for r in normalized:
            cid        = r.get("case_id", "")
            summary_fp = _hl.sha1(str(r.get("summary","")).lower().strip()[:120].encode()).hexdigest()[:16]

            if cid in seen_ids or summary_fp in seen_prints:
                continue
            seen_ids.add(cid)
            seen_prints.add(summary_fp)
            unique.append(r)

        print(f"[Medusa] After dedup: {len(unique)} unique records")

        # ── Geocode — batched by city/state to avoid redundant calls ───────────
        geo_cache = {}
        for r in unique:
            key = f"{r.get('city','')},{r.get('state','')}"
            if key not in geo_cache:
                geo_cache[key] = geocode(r["city"], r["state"])
                time.sleep(0.2)
            r["lat"], r["lng"] = geo_cache[key]
        print(f"[Medusa] Geocoded {len(geo_cache)} unique locations for {len(unique)} records.")

        # ── Finalize ──────────────────────────────────────────────────────────
        self.last_scan    = datetime.now(timezone.utc).isoformat()
        self.total_found += len(unique)

        print(f"[Medusa] Scan complete. {len(unique)} cases ready.")

        # ── Meta-analysis ─────────────────────────────────────────
        try:
            scan_rec = ScanRecord.build(
                found = len(raw_records),
                saved = len(unique),
                cases = unique,
            )
            self._history.record(scan_rec)
            print(self._history.report())
        except Exception as e:
            print(f"[Medusa Meta] Error: {e}")

        return unique
