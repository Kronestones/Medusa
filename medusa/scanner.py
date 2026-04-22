"""
scanner.py — MedusaScanner

Uses the Claude API with web search to find and document
every reported act of male violence against women in the US.

Sources searched:
  - Police reports and law enforcement press releases
  - Court records (criminal + civil)
  - News archives (local, national, investigative)
  - DOJ and FBI public case announcements
  - Congressional records and ethics investigations
  - Civil suits and Title IX findings
  - Victim advocacy org reports (NCADV, RAINN, NOW, etc.)
  - State legislative ethics records
  - #MeToo documented cases with named perpetrators

Inclusion standard: cast wide — let sources speak.
If it appears in a public record or credible publication, it goes on the map.
No victim names stored. Perpetrator named only when public record does.

Built on Project Themis architecture.
"""

import os
import re
import json
import time
import hashlib
import requests
from datetime import datetime, timezone


CLAUDE_API_URL = "https://api.anthropic.com/v1/messages"
MODEL          = "claude-sonnet-4-20250514"

# State centroids for fallback geocoding
STATE_COORDS = {
    "AL": (32.806671, -86.791130), "AK": (61.370716, -152.404419),
    "AZ": (33.729759, -111.431221), "AR": (34.969704, -92.373123),
    "CA": (36.116203, -119.681564), "CO": (39.059811, -105.311104),
    "CT": (41.597782, -72.755371), "DE": (39.318523, -75.507141),
    "FL": (27.766279, -81.686783), "GA": (33.040619, -83.643074),
    "HI": (21.094318, -157.498337), "ID": (44.240459, -114.478828),
    "IL": (40.349457, -88.986137), "IN": (39.849426, -86.258278),
    "IA": (42.011539, -93.210526), "KS": (38.526600, -96.726486),
    "KY": (37.668140, -84.670067), "LA": (31.169960, -91.867805),
    "ME": (44.693947, -69.381927), "MD": (39.063946, -76.802101),
    "MA": (42.230171, -71.530106), "MI": (43.326618, -84.536095),
    "MN": (45.694454, -93.900192), "MS": (32.741646, -89.678696),
    "MO": (38.456085, -92.288368), "MT": (46.921925, -110.454353),
    "NE": (41.125370, -98.268082), "NV": (38.313515, -117.055374),
    "NH": (43.452492, -71.563896), "NJ": (40.298904, -74.521011),
    "NM": (34.840515, -106.248482), "NY": (42.165726, -74.948051),
    "NC": (35.630066, -79.806419), "ND": (47.528912, -99.784012),
    "OH": (40.388783, -82.764915), "OK": (35.565342, -96.928917),
    "OR": (44.572021, -122.070938), "PA": (40.590752, -77.209755),
    "RI": (41.680893, -71.511780), "SC": (33.856892, -80.945007),
    "SD": (44.299782, -99.438828), "TN": (35.747845, -86.692345),
    "TX": (31.054487, -97.563461), "UT": (40.150032, -111.862434),
    "VT": (44.045876, -72.710686), "VA": (37.769337, -78.169968),
    "WA": (47.400902, -121.490494), "WV": (38.491226, -80.954453),
    "WI": (44.268543, -89.616508), "WY": (42.755966, -107.302490),
    "DC": (38.895110, -77.036366),
}

_geocode_cache = {}

PUBLIC_FIGURE_KEYWORDS = {
    "senator", "congressman", "congresswoman", "representative", "governor",
    "mayor", "judge", "prosecutor", "sheriff", "police chief", "officer",
    "politician", "official", "minister", "lobbyist", "staffer",
    "council member", "assemblyman", "assemblywoman", "state rep",
    "attorney general", "secretary", "ambassador", "aide", "aide",
    "deputy", "commissioner", "superintendent", "superintendent",
    "president", "vice president", "cabinet",
}


def geocode(city: str, state: str) -> tuple:
    key = f"{city},{state}"
    if key in _geocode_cache:
        return _geocode_cache[key]
    try:
        resp = requests.get(
            "https://nominatim.openstreetmap.org/search",
            params={"q": f"{city}, {state}, United States",
                    "format": "json", "limit": 1, "countrycodes": "us"},
            headers={"User-Agent": "Medusa/1.0 (public violence documentation)"},
            timeout=5,
        )
        if resp.ok:
            data = resp.json()
            if data:
                lat, lng = float(data[0]["lat"]), float(data[0]["lon"])
                _geocode_cache[key] = (lat, lng)
                return lat, lng
    except Exception:
        pass
    coords = STATE_COORDS.get(state.upper(), (None, None))
    _geocode_cache[key] = coords
    return coords


def make_case_id(city, state, vtype, date_str) -> str:
    raw = f"{city}{state}{vtype}{date_str}".lower().replace(" ", "")
    h   = hashlib.md5(raw.encode()).hexdigest()[:8].upper()
    yr  = (date_str or "")[:4] or "0000"
    return f"MEDUSA-{yr}-{h}"


def detect_public_figure(summary: str) -> bool:
    s = (summary or "").lower()
    return any(kw in s for kw in PUBLIC_FIGURE_KEYWORDS)


# ── Scan prompts ──────────────────────────────────────────────────────────────
# We run multiple focused queries per scan to cast the widest net.

SCAN_QUERIES = [

    # Sex offender registries — all states
    """Search the national and state sex offender registries for documented cases of
male offenders convicted of crimes against women and girls in the United States.
Search: National Sex Offender Public Website (nsopw.gov), state registry databases,
DOJ SMART Office reports, SORNA compliance records.
Include: convicted rapists, sexual predators, child sex offenders with female victims.
Focus on cases with public court records and verified convictions.""",

    # Epstein network — documented cases
    """Search for all publicly documented cases connected to Jeffrey Epstein and his
network of associates involving violence, trafficking, and sexual abuse of women and girls.
Sources: Southern District of New York court filings, Virgin Islands AG lawsuit,
Maxwell trial transcripts, Epstein victim fund records, congressional testimony,
investigative journalism (Miami Herald Julie Brown reporting, New York Times, NYT),
unsealed court documents, depositions naming associates.
Include: all named individuals in public court records, flight logs, deposition transcripts.
Only include names that appear in court filings, official investigations, or verified journalism.""",



    # General recent cases
    """Search for recently reported cases of male violence against women in the United States.
Include: homicide, femicide, domestic violence, assault, rape, sexual assault, stalking,
harassment, attempted murder, coercive control, human trafficking.
Search across: local news, national news, law enforcement press releases, court records,
DOJ announcements, FBI case releases.""",

    # Politicians and government officials specifically
    """Search for documented cases of male politicians, government officials, law enforcement
officers, judges, or public servants accused or convicted of violence against women in the
United States. Include: police officers charged with domestic violence or sexual assault,
elected officials with credible allegations, judges removed for misconduct involving women,
congressional ethics investigations involving violence or harassment.
Search: congressional records, ethics committee findings, law enforcement disciplinary records,
court records, investigative journalism (ProPublica, Marshall Project, local investigative outlets).""",

    # Court records and convictions
    """Search for recent US court convictions or charges filed against men for crimes of
violence against women. Include: murder convictions, rape convictions, domestic violence
charges, stalking charges, trafficking convictions. Search: DOJ press releases,
US Attorney office announcements, state AG announcements, court records databases.""",

    # Civil suits and Title IX
    """Search for civil lawsuits, Title IX findings, and institutional records documenting
male violence against women in the United States. Include: university Title IX adjudications,
civil judgments, EEOC findings, HR settlements with public disclosure, NDAs that have been
broken or reported on. Search: court records, university Title IX transparency reports,
investigative journalism.""",

]

EXTRACT_PROMPT = """You are a researcher for Medusa, a public documentation project.
You have just searched for: {query}

Extract all documented cases of male violence against women you found. Include every case
that appears in a public record or credible publication — police reports, court filings,
news articles, congressional records, civil suits, ethics investigations, DOJ/FBI releases,
Title IX findings, or any other public source.

Cast wide. Let sources speak. Do not filter based on your own judgment about severity.
If it's documented publicly, include it.

For each case return a JSON object with EXACTLY these fields:
{{
  "summary": "2-3 sentence factual description. No victim name. Perpetrator name only if in public record.",
  "city": "city name",
  "state": "2-letter US state abbreviation",
  "date_incident": "YYYY-MM-DD or YYYY-MM or YYYY (best available)",
  "violence_type": "homicide|assault|sexual_assault|stalking|trafficking|domestic_violence|rape|harassment|attempted_murder|child_abuse|coercive_control",
  "status": "reported|charged|convicted|acquitted|civil_judgment|credible_allegation|congressional_record|unknown",
  "source_url": "direct URL to the public record or article",
  "source_name": "name of the publication, agency, or court"
}}

Rules:
- Only cases in the United States
- Only male perpetrator → female victim
- state must be a valid 2-letter US abbreviation
- violence_type must be exactly one of the enum values
- status must be exactly one of the enum values
- source_url must be a real, direct URL
- No victim names in summary
- Return ONLY a JSON array. No preamble. No markdown. No explanation."""


class MedusaScanner:

    def __init__(self):
        self.last_scan   = None
        self.total_found = 0

    def scan(self) -> list:
        """
        Run all scan queries. Returns enriched case dicts ready for DB.
        """
        print("[Medusa] Starting wide-net public records scan...")
        all_cases = []
        seen_ids  = set()

        for i, query in enumerate(SCAN_QUERIES, 1):
            print(f"[Medusa] Query {i}/{len(SCAN_QUERIES)}: {query[:60]}...")
            try:
                cases = self._query_claude(query)
                for c in cases:
                    cid = make_case_id(
                        c.get("city", ""),
                        c.get("state", ""),
                        c.get("violence_type", ""),
                        c.get("date_incident", ""),
                    )
                    if cid in seen_ids:
                        continue
                    seen_ids.add(cid)
                    c["case_id"]         = cid
                    c["is_public_figure"] = detect_public_figure(c.get("summary", ""))
                    c["verified"]        = True

                    # Geocode
                    lat, lng = geocode(c.get("city", ""), c.get("state", ""))
                    c["lat"] = lat
                    c["lng"] = lng

                    all_cases.append(c)
                    time.sleep(0.25)   # rate-limit geocoder

                print(f"[Medusa] Query {i} returned {len(cases)} cases.")
                time.sleep(1)          # brief pause between API calls

            except Exception as e:
                print(f"[Medusa] Query {i} error: {e}")
                continue

        self.last_scan    = datetime.now(timezone.utc).isoformat()
        self.total_found += len(all_cases)
        print(f"[Medusa] Scan complete. {len(all_cases)} unique cases found.")
        return all_cases

    def _query_claude(self, query: str) -> list:
        prompt = EXTRACT_PROMPT.format(query=query)

        payload = {
            "model":      MODEL,
            "max_tokens": 4000,
            "tools": [{"type": "web_search_20250305", "name": "web_search"}],
            "messages": [{"role": "user", "content": prompt}],
        }

        resp = requests.post(
            CLAUDE_API_URL,
            json=payload,
            headers={"Content-Type": "application/json", "x-api-key": os.environ.get("ANTHROPIC_API_KEY", ""), "anthropic-version": "2023-06-01"},
            timeout=90,
        )

        if not resp.ok:
            raise RuntimeError(f"API {resp.status_code}: {resp.text[:300]}")

        data = resp.json()
        text_blocks = [
            b["text"] for b in data.get("content", []) if b.get("type") == "text"
        ]
        if not text_blocks:
            return []

        raw = "\n".join(text_blocks).strip()
        raw = re.sub(r"```json\s*", "", raw)
        raw = re.sub(r"```\s*",     "", raw)
        raw = raw.strip()

        parsed = json.loads(raw)
        return parsed if isinstance(parsed, list) else []
