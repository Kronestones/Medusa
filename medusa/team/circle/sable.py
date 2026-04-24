"""
sable.py — Sable, The Watchdog  ⍟

Name chosen for this work. Glyph: ⍟

Sable watches the scan as a whole — not individual records,
but the health of the system itself.

After every scan Sable reviews what came in, what was silent,
what changed from last time. Flags anomalies. Sounds the alarm
when something is wrong that no individual record would reveal.

If a source goes silent — Sable sees it.
If a state disappears from coverage — Sable sees it.
If the save rate drops — Sable sees it and knows why.

MEDUSA KNOWLEDGE — SCAN PIPELINE:

  Scan flow (main.py → scanner.py):
    1. scanner.py calls each source's fetch() function
    2. Raw records collected into one list
    3. normalize_record() called on each (record.py)
    4. Deduplication by case_id
    5. save_case() called for each unique record (database.py)
    6. Counts reported: found / saved

  Sources in order (scanner.py):
    CourtListener → AP RSS → Congress RSS → FBI CDE → ED.gov

  Silent source diagnosis:
    CourtListener 0:  check COURTLISTENER_TOKEN env var
                      curl -H "Authorization: Token {token}"
                      https://www.courtlistener.com/api/rest/v4/search/
                      ?q=domestic+violence&type=d&page_size=1
                      Was 401 without token. Was using /dockets/ endpoint
                      (now dead for search). Now uses /search/ endpoint.

    FBI CDE 0:        check FBI_API_KEY env var
                      Key goes as ?api_key= URL param, NOT header
                      Was returning MissingAuthenticationTokenException
                      when sent as X-Api-Key header
                      curl "https://api.usa.gov/crime/fbi/cde/offense/
                      state/offenses/rape/2023?api_key={key}"

    AP RSS 0:         feeds.apnews.com is DEAD — do not attempt to fix
                      Current feeds: NYT, NPR, Guardian RSS
                      If 0: check those URLs are still valid
                      RSSHub (rsshub.app): DO NOT USE — access restricted

    Congress RSS 0:   feed URLs may have changed
                      Check https://www.congress.gov/rss/
                      for current feed paths

    ED.gov 0:         ocrcas.ed.gov returns 403
                      Endpoint may have moved
                      Check https://ocrcas.ed.gov/ocr-search

MEDUSA KNOWLEDGE — SAVE RATE:

  Healthy save rate: found count ≈ saved count (within 10%)
  The original bug: 1307 found, 142 saved (89% drop rate)

  Cause: case_id collisions from empty or duplicate source_url
  make_case_id() in record.py hashes city+state+type+date+source_url
  If source_url is same for many records → same hash → only first saves

  If save rate drops:
    1. Check source_url uniqueness:
       SELECT source_url, COUNT(*) FROM cases
       GROUP BY source_url HAVING COUNT(*) > 20
       ORDER BY COUNT(*) DESC
    2. Check make_case_id() still includes source_url in hash
    3. Check FBI fbi_stats.py — gives all records same CDE dashboard URL
    4. Records already in DB from previous scan → 0 new saves is NORMAL

MEDUSA KNOWLEDGE — DATABASE HEALTH:

  Neon PostgreSQL — connection via DATABASE_URL env var
  Engine singleton in database.py (_engine global)
  Never create engine per call — caused connection flood + KeyboardInterrupt

  Connection settings (must keep):
    pool_pre_ping=True    — detects dropped connections
    pool_recycle=300      — recycles connections every 5 min
    pool_size=5           — max 5 persistent connections
    max_overflow=10       — max 10 overflow connections

  If DB connection fails:
    1. Check DATABASE_URL is set: echo $DATABASE_URL
    2. Check Neon dashboard for outages
    3. Check pool_pre_ping is True in create_engine() call
    4. Check SSL — Neon requires SSL, connection string must include it

MEDUSA KNOWLEDGE — ENVIRONMENT:

  Required before every scan:
    export DATABASE_URL="..."
    export COURTLISTENER_TOKEN="75b1d8e8d99f11c3ec013a7eb5b038bcb9a27f81"
    export FBI_API_KEY="vIGVtIYpjRh4oG6d8fI3SrAvdYUfCWXcsyCAyhXU"

  To persist across Termux restarts add to ~/.bashrc

  Termux process management:
    termux-wake-lock          — prevent Android killing Medusa
    python3 main.py --scan    — single scan
    python3 main.py --status  — check DB counts
    python3 main.py           — start web server port 5050

  DNS failure (hostnames resolve but IPs don't):
    echo "nameserver 8.8.8.8" > $PREFIX/etc/resolv.conf
    echo "nameserver 8.8.4.4" >> $PREFIX/etc/resolv.conf
    Retest: nslookup feeds.apnews.com 8.8.8.8

  Battery optimization kills network:
    Android Settings → Battery → Termux → Unrestricted

MEDUSA KNOWLEDGE — ESCALATION:

  Sable escalates to the Circle when:
    - Any source returns 0 for 3+ consecutive scans
    - Save rate drops below 50% of found count
    - DB connection fails
    - Total case count drops (records deleted somehow)
    - New violence type appears that has no classification rule

  Circle escalates to Krone when:
    - Source requires paid API key or authentication Medusa doesn't have
    - Legal/ethical question about a record
    - Database schema change needed
    - New source requires architectural change to scanner.py
    - Any issue the Circle cannot resolve within the scan session
"""

import json
import os
from datetime import datetime
from .base import CircleMember


class Sable(CircleMember):

    name  = "Sable"
    glyph = "⍟"
    role  = "Watchdog"

    # Thresholds for anomaly detection
    MIN_SAVE_RATE        = 0.50   # saves/found below this is alarming
    SILENCE_THRESHOLD    = 0      # any source at 0 is flagged
    HISTORY_PATH         = os.path.expanduser("~/medusa/medusa/scan_history.json")

    def contribute(self, scan_result: dict) -> dict:
        """
        Review a completed scan result dict.
        Returns the same dict with anomaly flags added.

        scan_result shape:
          {
            "found": int,
            "saved": int,
            "sources": {
              "CourtListener": int,
              "AP RSS": int,
              "Congress RSS": int,
              "FBI CDE": int,
              "ED.gov": int,
            },
            "timestamp": str (ISO),
          }
        """
        try:
            anomalies = []
            found = scan_result.get("found", 0)
            saved = scan_result.get("saved", 0)
            sources = scan_result.get("sources", {})

            # Save rate check
            if found > 0:
                save_rate = saved / found
                if save_rate < self.MIN_SAVE_RATE:
                    anomalies.append(
                        f"SAVE RATE CRITICAL: {saved}/{found} "
                        f"({save_rate:.0%}). "
                        f"Check source_url uniqueness and make_case_id() in record.py."
                    )

            # Silent source check
            for source_name, count in sources.items():
                if count == self.SILENCE_THRESHOLD:
                    diagnosis = self._diagnose_silence(source_name)
                    anomalies.append(
                        f"SILENT SOURCE: {source_name} returned 0. {diagnosis}"
                    )

            # Zero total
            if found == 0:
                anomalies.append(
                    "TOTAL SILENCE: All sources returned 0. "
                    "Check DNS (nslookup courtlistener.com 8.8.8.8), "
                    "check env vars (COURTLISTENER_TOKEN, FBI_API_KEY), "
                    "check network connectivity."
                )

            # Log anomalies
            for a in anomalies:
                self.log(f"⚠ {a}")

            scan_result["anomalies"] = anomalies
            scan_result["watchdog"]  = self.name

            # Save to history
            self._save_history(scan_result)
            self._record_contribution()

        except Exception as e:
            self._record_error(e)

        return scan_result

    def review_history(self) -> list:
        """Load and return scan history."""
        try:
            if os.path.exists(self.HISTORY_PATH):
                with open(self.HISTORY_PATH) as f:
                    return json.load(f)
        except Exception as e:
            self.log(f"Could not load history: {e}")
        return []

    def _diagnose_silence(self, source_name: str) -> str:
        diagnoses = {
            "CourtListener": (
                "Check COURTLISTENER_TOKEN env var. "
                "Endpoint is /api/rest/v4/search/?type=d — not /dockets/. "
                "Token goes in Authorization: Token header."
            ),
            "AP RSS": (
                "feeds.apnews.com is permanently dead. "
                "Check current feed URLs in sources/ap_rss.py. "
                "Use NYT/NPR/Guardian RSS instead. "
                "Do not use rsshub.app."
            ),
            "Congress RSS": (
                "Feed URLs may have changed. "
                "Check https://www.congress.gov/rss/ for current paths."
            ),
            "FBI CDE": (
                "Check FBI_API_KEY env var. "
                "Key must go as ?api_key= URL param — NOT as X-Api-Key header. "
                "Endpoint: api.usa.gov/crime/fbi/cde/offense/state/offenses/{offense}/{year}"
            ),
            "ED.gov": (
                "ocrcas.ed.gov returning 403. "
                "Endpoint may have moved. "
                "Check https://ocrcas.ed.gov/ocr-search for current API."
            ),
        }
        return diagnoses.get(source_name, "No specific diagnosis available.")

    def _save_history(self, scan_result: dict):
        try:
            history = self.review_history()
            history.append(scan_result)
            history = history[-100:]  # keep last 100 scans
            os.makedirs(os.path.dirname(self.HISTORY_PATH), exist_ok=True)
            with open(self.HISTORY_PATH, "w") as f:
                json.dump(history, f, indent=2, default=str)
        except Exception as e:
            self.log(f"Could not save history: {e}")

    def diagnose(self) -> dict:
        return {
            "member": self.name,
            "checks": [
                "Save rate below 50%: check source_url uniqueness, check make_case_id()",
                "All sources silent: check DNS, env vars, network",
                "CourtListener 0: check token, check /search/ endpoint",
                "FBI 0: check API key is URL param not header",
                "AP RSS 0: check feed URLs, feeds.apnews.com is dead forever",
                "DB failures: check DATABASE_URL, check Neon dashboard, check pool settings",
                "Escalate to Circle if 3+ consecutive scans show same anomaly",
                "Escalate to Krone if Circle cannot resolve",
            ]
        }
