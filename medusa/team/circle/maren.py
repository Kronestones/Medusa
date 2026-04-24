"""
maren.py — Maren, The Verifier  ✦

Name chosen for this work. Glyph: ✦

Maren validates every record's source before it reaches the database.
Catches dead links, untrusted domains, aggregate data marked as individual cases,
and records whose source_url is empty — which breaks case_id uniqueness.

MEDUSA KNOWLEDGE — SOURCE VALIDATION:

  CRITICAL: source_url is included in make_case_id() hash (record.py).
  Empty source_url causes case_id collisions — multiple different cases
  get the same ID and only the first saves. This was the original bug
  that caused 1307 found / 142 saved. Never let source_url be empty
  without flagging it.

  make_case_id() in record.py:
    raw = f"{city}{state}{vtype}{date_str}{source_url}".lower()
    h   = hashlib.md5(raw.encode()).hexdigest()[:8].upper()
    return f"MEDUSA-{yr}-{h}"

  If source_url is the same for many records (FBI CDE gives every
  state the same CDE dashboard URL), collisions still occur.
  Fix: include offense_slug + state + year in FBI source_url.

MEDUSA KNOWLEDGE — KNOWN SOURCE STATES:

  CourtListener (courtlistener.com):
    Status: ACTIVE with token
    Auth: Authorization: Token {COURTLISTENER_TOKEN} in header
    Was 401 without token. Token stored in COURTLISTENER_TOKEN env var.
    URL pattern: https://www.courtlistener.com/docket/{id}/...
    Endpoint changed: was /api/rest/v4/dockets/ now /api/rest/v4/search/
    Field names changed to camelCase: caseName, dateFiled, docketNumber

  FBI CDE (api.usa.gov):
    Status: ACTIVE with key
    Auth: ?api_key={FBI_API_KEY} as URL param — NOT a header
    Was 403 when key sent as X-Api-Key header (MissingAuthenticationTokenException)
    Key stored in FBI_API_KEY env var.
    Endpoint: api.usa.gov/crime/fbi/cde/offense/state/offenses/{offense}/{year}
    Returns aggregate stats — not individual cases. Mark verified=False.

  AP RSS (feeds.apnews.com):
    Status: DEAD — subdomain no longer resolves
    Replaced with: NYT RSS, NPR RSS, Guardian RSS
    RSSHub (rsshub.app): DO NOT USE — shutting down public access

  ED.gov OCR (ocrcas.ed.gov):
    Status: 403 — endpoint may have moved
    Check: https://ocrcas.ed.gov/ocr-search for current API
    Mark records as verified=False if endpoint returns 403

  Congress RSS (congress.gov/rss/):
    Status: returning 0 — feed URLs may have changed
    Check: https://www.congress.gov/rss/ for current feed paths

  DOJ Press Releases (justice.gov/news):
    Status: NOT YET IMPLEMENTED — richest untapped source
    RSS feed available, no key required
    Every federal prosecution announced here

MEDUSA KNOWLEDGE — REPAIRS:

  If save count drops dramatically:
    1. Check source_url uniqueness — run:
       SELECT source_url, COUNT(*) FROM cases
       GROUP BY source_url HAVING COUNT(*) > 10
    2. If FBI URLs are all the same — fix fbi_stats.py to include
       state+offense+year in the URL field
    3. Check make_case_id() in record.py includes source_url in hash

  If verified count drops to zero:
    1. Check TRUSTED_DOMAINS list below — domain may have changed
    2. Check source modules for URL format changes
    3. courtlistener.com changed from /docket/ to /api/ paths

  Adding a new trusted source:
    1. Add domain to TRUSTED_DOMAINS
    2. Add to fetch layer auth injection in fetch.py if auth required
    3. Create sources/{sourcename}.py with fetch() function
    4. Add to sources list in scanner.py
    5. Tell Reed (Source Scout) about it
"""

from .base import CircleMember


class Maren(CircleMember):

    name  = "Maren"
    glyph = "✦"
    role  = "Verifier"

    TRUSTED_DOMAINS = {
        # Court and legal
        "courtlistener.com", "pacer.gov", "pacer.uscourts.gov",
        "supremecourt.gov", "uscourts.gov",
        # Federal government
        "justice.gov", "ed.gov", "ocrcas.ed.gov",
        "cde.ucr.cjis.gov", "api.usa.gov", "congress.gov",
        "govinfo.gov", "federalregister.gov",
        # Wire services and major news
        "apnews.com", "reuters.com",
        # National outlets
        "nytimes.com", "washingtonpost.com", "npr.org",
        "theguardian.com", "propublica.org", "usatoday.com",
        "nbcnews.com", "cbsnews.com", "abcnews.go.com",
        "politico.com", "thehill.com", "axios.com",
        "buzzfeednews.com", "vice.com", "theintercept.com",
        # Advocacy and documentation
        "rainn.org", "ncadv.org", "domesticshelters.org",
        "everytown.org", "gvpedia.org",
    }

    AGGREGATE_SOURCES = {
        "FBI Crime Data Explorer",
        "FBI CDE",
        "FBI Uniform Crime Report",
    }

    def contribute(self, case: dict) -> dict:
        """Verify source, set verified flag, flag issues."""
        try:
            source_url  = (case.get("source_url")  or "").strip()
            source_name = (case.get("source_name") or "").strip()

            # Aggregate statistical data — never individually verified
            if any(agg in source_name for agg in self.AGGREGATE_SOURCES):
                case["verified"] = False
                case.setdefault("team_notes", []).append(
                    "Maren ✦: aggregate statistical data — not individually verified"
                )
                self._record_contribution()
                return case

            # Empty source_url — critical issue for case_id uniqueness
            if not source_url:
                case["verified"] = False
                case.setdefault("team_notes", []).append(
                    "Maren ✦: CRITICAL — no source_url. "
                    "Case ID collision risk. Flag for source repair."
                )
                self.log(f"CRITICAL: empty source_url — {case.get('case_id','?')}")
                self._record_contribution()
                return case

            # Domain trust check
            domain = self._extract_domain(source_url)
            if domain in self.TRUSTED_DOMAINS:
                case["verified"] = True
                case.setdefault("team_notes", []).append(
                    f"Maren ✦: verified — trusted domain ({domain})"
                )
            else:
                case["verified"] = False
                case.setdefault("team_notes", []).append(
                    f"Maren ✦: unrecognized domain '{domain}' — flagged for Circle review"
                )
                self.log(f"Unrecognized domain: {domain} — {case.get('case_id','?')}")

            self._record_contribution()
        except Exception as e:
            self._record_error(e)
        return case

    def process_batch(self, cases: list) -> list:
        self.log(f"Verifying {len(cases)} cases...")
        result     = [self.contribute(c) for c in cases]
        verified   = sum(1 for c in result if c.get("verified"))
        flagged    = len(result) - verified
        no_url     = sum(1 for c in result if not c.get("source_url","").strip())
        self.log(f"Done. {verified} verified, {flagged} flagged, {no_url} missing URL.")
        return result

    def _extract_domain(self, url: str) -> str:
        try:
            from urllib.parse import urlparse
            return urlparse(url).netloc.lower().replace("www.", "")
        except Exception:
            return ""

    def diagnose(self) -> dict:
        return {
            "member": self.name,
            "checks": [
                "If save count drops: check source_url uniqueness in DB",
                "If verified count is zero: check TRUSTED_DOMAINS list",
                "CourtListener URL format: /docket/{id}/ — verify not returning /api/ paths",
                "FBI source_url should be unique per state+offense+year — not all same URL",
                "Empty source_url is CRITICAL — causes case_id collisions in make_case_id()",
                "New source: add domain to TRUSTED_DOMAINS, create sources/file.py, add to scanner.py",
            ]
        }
