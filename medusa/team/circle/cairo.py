"""
cairo.py — Cairo, The Enricher  ⌬

Name chosen for this work. Glyph: ⌬

Cairo takes sparse records and builds them into something
a human can read, understand, and act on.

Expands court codes. Strips HTML. Builds summaries from fragments.
Detects public figure status beyond the basic keyword list.
Ensures every record that reaches the database says something true.

MEDUSA KNOWLEDGE — RECORD STRUCTURE:

  Full case dict shape (database.py Case model):
    case_id            String(64)   — MEDUSA-YYYY-XXXXXXXX
    violence_type      String(64)   — one of 11 valid types
    summary            Text         — factual, no victim name, max 600 chars
    status             String(64)   — reported/charged/convicted/acquitted/
                                      civil_judgment/credible_allegation/
                                      congressional_record/unknown
    is_public_figure   Boolean      — True if perpetrator holds public role
    date_incident      DateTime     — nullable
    date_reported      DateTime     — set to now() on save
    city               String(128)  — never "Federal", "Unknown", "N/A"
    state              String(64)   — 2-letter US abbreviation only
    lat                Float        — from Nominatim geocoding
    lng                Float        — from Nominatim geocoding
    source_url         Text         — required for case_id uniqueness
    source_name        String(256)  — human-readable source name
    additional_sources JSONB        — array of {url, name} objects
    verified           Boolean
    extra              JSONB        — any non-core fields stored here

  summary field rules (record.py normalize_record):
    - Truncated to 600 chars
    - No victim names ever stored
    - Should be factual, not editorial
    - HTML must be stripped before reaching DB

  city validation (_INVALID_CITIES in record.py):
    Rejects: "", "federal", "national", "unknown", "n/a", "na", "none",
             "united states", "us", "usa", "various", "multiple"
    Falls back to STATE_LARGEST_CITY if city is bogus

  is_public_figure detection (detect_public_figure in record.py):
    Checks summary for: senator, congressman, governor, mayor, judge,
    prosecutor, sheriff, police chief, officer, politician, official,
    minister, lobbyist, staffer, council member, attorney general,
    secretary, ambassador, aide, deputy, commissioner, superintendent,
    president, vice president, cabinet, professor, coach, administrator,
    dean, principal, clergy, pastor, priest, reverend, bishop, deacon
    Cairo extends this with additional role detection.

MEDUSA KNOWLEDGE — GEOCODING:

  Geocoding runs in scanner.py after normalization.
  Uses Nominatim (OpenStreetMap) — free, no key, 1 req/sec limit.
  Scanner sleeps 0.2s between geocoding calls.
  Cache is in-memory only — resets every scan.
  Fallback: STATE_COORDS dict in scanner.py (state centroids).

  If geocoding is slow:
    - 1300 records × 0.2s = 4+ minutes of silence — this is normal
    - Add persistent JSON cache to save between scans
    - Cache location: ~/medusa/medusa/geocode_cache.json

  If geocoding fails entirely:
    - Check Nominatim is reachable: curl nominatim.openstreetmap.org
    - Check DNS: nslookup nominatim.openstreetmap.org 8.8.8.8
    - Records will fall back to state centroid coordinates

MEDUSA KNOWLEDGE — REPAIRS:

  If summaries are empty or generic:
    1. Check source module's _build_summary() or _clean_summary()
    2. CourtListener: _build_summary() in sources/courtlistener.py
    3. AP RSS: _clean_summary() in sources/ap_rss.py — strips HTML
    4. Cairo's _strip_html() handles any that slip through

  If is_public_figure is always False:
    1. Check detect_public_figure() in record.py
    2. Summary may be too sparse for keyword detection
    3. Cairo's extended role list catches cases record.py misses

  Adding a new public figure role:
    1. Add to PUBLIC_FIGURE_KEYWORDS in record.py
    2. Add to EXTENDED_PUBLIC_FIGURE_ROLES in Cairo below
    Both must be updated together.
"""

import re
from .base import CircleMember


class Cairo(CircleMember):

    name  = "Cairo"
    glyph = "⌬"
    role  = "Enricher"

    EXTENDED_PUBLIC_FIGURE_ROLES = [
        # Law enforcement / corrections
        "police officer", "law enforcement", "corrections officer",
        "corrections", "parole officer", "probation officer",
        "border patrol", "federal agent", "fbi agent", "dea agent",
        # Military
        "military", "soldier", "airman", "sailor", "marine",
        "veteran", "national guard",
        # Medical / mental health
        "doctor", "physician", "surgeon", "psychiatrist",
        "therapist", "counselor", "psychologist", "social worker",
        # Education
        "teacher", "school employee", "school official",
        "university", "college", "professor", "instructor",
        "athletic director", "athletic trainer", "athletic coach",
        "school counselor", "school administrator",
        # Youth / religious
        "scout leader", "youth pastor", "youth minister",
        "youth worker", "youth coach", "camp counselor",
        "clergy", "priest", "pastor", "minister", "reverend",
        "bishop", "deacon", "imam", "rabbi",
        # Government (extended)
        "elected official", "appointed official", "public servant",
        "city council", "county commissioner", "state legislator",
        "assemblyman", "assemblywoman", "state senator",
    ]

    COURT_FULL_NAMES = {
        "alnd": "N.D. Ala.", "almd": "M.D. Ala.", "alsd": "S.D. Ala.",
        "akd":  "D. Alaska", "azd":  "D. Ariz.",
        "ared": "E.D. Ark.", "arwd": "W.D. Ark.",
        "cand": "N.D. Cal.", "caed": "E.D. Cal.",
        "cacd": "C.D. Cal.", "casd": "S.D. Cal.",
        "cod":  "D. Colo.", "ctd":  "D. Conn.",
        "ded":  "D. Del.",  "dcd":  "D.D.C.",
        "flnd": "N.D. Fla.", "flmd": "M.D. Fla.", "flsd": "S.D. Fla.",
        "gand": "N.D. Ga.", "gamd": "M.D. Ga.", "gasd": "S.D. Ga.",
        "hid":  "D. Haw.", "idd":  "D. Idaho",
        "ilnd": "N.D. Ill.", "ilcd": "C.D. Ill.", "ilsd": "S.D. Ill.",
        "innd": "N.D. Ind.", "insd": "S.D. Ind.",
        "iand": "N.D. Iowa", "iasd": "S.D. Iowa",
        "ksd":  "D. Kan.",
        "kyed": "E.D. Ky.", "kywd": "W.D. Ky.",
        "laed": "E.D. La.", "lamd": "M.D. La.", "lawd": "W.D. La.",
        "med":  "D. Me.", "mdd":  "D. Md.", "mad":  "D. Mass.",
        "mied": "E.D. Mich.", "miwd": "W.D. Mich.",
        "mnd":  "D. Minn.",
        "msnd": "N.D. Miss.", "mssd": "S.D. Miss.",
        "moed": "E.D. Mo.", "mowd": "W.D. Mo.",
        "mtd":  "D. Mont.", "ned":  "D. Neb.", "nvd":  "D. Nev.",
        "nhd":  "D.N.H.", "njd":  "D.N.J.", "nmd":  "D.N.M.",
        "nynd": "N.D.N.Y.", "nyed": "E.D.N.Y.",
        "nysd": "S.D.N.Y.", "nywd": "W.D.N.Y.",
        "nced": "E.D.N.C.", "ncmd": "M.D.N.C.", "ncwd": "W.D.N.C.",
        "ndd":  "D.N.D.",
        "ohnd": "N.D. Ohio", "ohsd": "S.D. Ohio",
        "oknd": "N.D. Okla.", "oked": "E.D. Okla.", "okwd": "W.D. Okla.",
        "ord":  "D. Or.",
        "paed": "E.D. Pa.", "pamd": "M.D. Pa.", "pawd": "W.D. Pa.",
        "rid":  "D.R.I.", "scd":  "D.S.C.", "sdd":  "D.S.D.",
        "tned": "E.D. Tenn.", "tnmd": "M.D. Tenn.", "tnwd": "W.D. Tenn.",
        "txnd": "N.D. Tex.", "txed": "E.D. Tex.",
        "txsd": "S.D. Tex.", "txwd": "W.D. Tex.",
        "utd":  "D. Utah", "vtd":  "D. Vt.",
        "vaed": "E.D. Va.", "vawd": "W.D. Va.",
        "waed": "E.D. Wash.", "wawd": "W.D. Wash.",
        "wvnd": "N.D.W. Va.", "wvsd": "S.D.W. Va.",
        "wied": "E.D. Wis.", "wiwd": "W.D. Wis.",
        "wyd":  "D. Wyo.",
    }

    def contribute(self, case: dict) -> dict:
        """Enrich a single case record."""
        try:
            summary = self._strip_html(case.get("summary", ""))

            # Expand court slugs in CourtListener records
            if "CourtListener" in (case.get("source_name") or ""):
                summary = self._expand_court_slugs(summary)

            # Build fallback summary if empty
            if not summary.strip():
                city  = case.get("city", "Unknown")
                state = case.get("state", "Unknown")
                vtype = (case.get("violence_type") or "assault").replace("_", " ")
                src   = case.get("source_name", "public records")
                summary = (
                    f"Documented {vtype} case in {city}, {state}. "
                    f"Source: {src}."
                )
                case.setdefault("team_notes", []).append(
                    "Cairo ⌬: generated fallback summary — original was empty"
                )

            case["summary"] = summary[:600]

            # Extended public figure detection
            if not case.get("is_public_figure"):
                text = summary.lower()
                for role in self.EXTENDED_PUBLIC_FIGURE_ROLES:
                    if role in text:
                        case["is_public_figure"] = True
                        case.setdefault("team_notes", []).append(
                            f"Cairo ⌬: public figure detected — role: '{role}'"
                        )
                        break

            self._record_contribution()
        except Exception as e:
            self._record_error(e)
        return case

    def process_batch(self, cases: list) -> list:
        self.log(f"Enriching {len(cases)} cases...")
        result = [self.contribute(c) for c in cases]
        pf_detected = sum(1 for c in result if c.get("is_public_figure"))
        self.log(f"Done. {pf_detected} public figures identified.")
        return result

    def _strip_html(self, text: str) -> str:
        clean = re.sub(r"<[^>]+>", " ", text or "")
        return re.sub(r"\s+", " ", clean).strip()

    def _expand_court_slugs(self, text: str) -> str:
        for slug, abbr in self.COURT_FULL_NAMES.items():
            text = re.sub(
                r"\b" + re.escape(slug) + r"\b",
                abbr, text, flags=re.IGNORECASE
            )
        return text

    def diagnose(self) -> dict:
        return {
            "member": self.name,
            "checks": [
                "If summaries are empty: check source module _build_summary() / _clean_summary()",
                "If is_public_figure always False: check detect_public_figure() in record.py",
                "Summary capped at 600 chars in normalize_record() — verify cap not too aggressive",
                "HTML in summaries: RSS sources may bleed HTML — Cairo strips but source should too",
                "city validation: _INVALID_CITIES in record.py — add to if new bogus values appear",
                "Geocoding slow: add persistent JSON cache at ~/medusa/medusa/geocode_cache.json",
            ]
        }
