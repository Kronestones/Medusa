"""
engine.py — Medusa Team Engine

Coordinates the Circle and the Consultant Pool.
Called by scanner.py after each scan.

The engine:
  1. Runs Voss (Classifier) over all cases
  2. Runs Maren (Verifier) over all cases
  3. Runs Cairo (Enricher) over all cases
  4. Runs Lira (Analyst) to surface patterns
  5. Runs Sable (Watchdog) to check scan health
  6. Runs Reed (Source Scout) for recommendations
  7. Consults the pool for domain-specific advice
  8. Returns full team report

If any Circle member finds an issue they cannot resolve,
they escalate to the engine. The engine logs it for Krone.

Escalation to Krone:
  Issues that require Krone's attention are written to:
  ~/medusa/medusa/escalations.json
  Check this file after any scan with anomalies.
"""

import json
import os
from datetime import datetime, timezone

from .circle import CIRCLE, Voss, Maren, Cairo, Sable, Lira, Reed
from .consultants.pool import ConsultantPool


ESCALATION_PATH = os.path.expanduser(
    "~/medusa/medusa/escalations.json"
)


class TeamEngine:
    """
    The Medusa Team Engine.

    Instantiate once at scan start.
    Call run(cases, scan_result) after normalization.
    """

    def __init__(self):
        self.circle = {m.name: m for m in CIRCLE}
        self.pool   = ConsultantPool()
        self._voss  = self.circle["Voss"]
        self._maren = self.circle["Maren"]
        self._cairo = self.circle["Cairo"]
        self._sable = self.circle["Sable"]
        self._lira  = self.circle["Lira"]
        self._reed  = self.circle["Reed"]
        print(
            f"  [◈ ENGINE] Team active — "
            f"{len(self.circle)} Circle members, "
            f"{len(self.pool)} consultants."
        )

    def run(self, cases: list, scan_result: dict) -> dict:
        """
        Full team pipeline. Call after normalization, before DB save.

        Args:
          cases:       list of normalized case dicts
          scan_result: dict with found/saved/sources counts from scanner

        Returns:
          enriched cases list and full team report
        """
        print(f"\n  [◈ ENGINE] Running team pipeline on {len(cases)} cases...")

        # 1. Classification
        cases = self._voss.process_batch(cases)

        # 2. Verification
        cases = self._maren.process_batch(cases)

        # 3. Enrichment
        cases = self._cairo.process_batch(cases)

        # 4. Analysis
        analysis = self._lira.contribute(cases)

        # 5. Watchdog
        scan_result["sources"] = scan_result.get("sources", {})
        scan_result = self._sable.contribute(scan_result)

        # 6. Source scout recommendations
        scan_result = self._reed.contribute(scan_result)

        # 7. Consult pool for any anomalies
        pool_notes = []
        for anomaly in scan_result.get("anomalies", []):
            for source_name in ["CourtListener", "AP RSS", "Congress RSS", "FBI CDE", "ED.gov"]:
                if source_name in anomaly:
                    steps = self.pool.diagnose_source(source_name)
                    if steps:
                        pool_notes.append({
                            "source":    source_name,
                            "diagnosis": steps,
                        })

        # 8. Check for escalations
        escalations = self._check_escalations(scan_result, analysis)
        if escalations:
            self._write_escalations(escalations)
            print(f"\n  [◈ ENGINE] ⚠ {len(escalations)} issue(s) escalated to Krone.")
            print(f"  [◈ ENGINE] See: {ESCALATION_PATH}")

        # Build team report
        team_report = {
            "timestamp":       datetime.now(timezone.utc).isoformat(),
            "cases_processed": len(cases),
            "analysis":        analysis,
            "watchdog":        scan_result.get("anomalies", []),
            "recommendations": scan_result.get("scout_recommendations", []),
            "pool_notes":      pool_notes,
            "escalations":     escalations,
            "circle_reports":  [m.report() for m in CIRCLE],
            "pool_coverage":   self.pool.coverage_report(),
        }

        print(f"  [◈ ENGINE] Team pipeline complete.\n")
        return cases, team_report

    def _check_escalations(self, scan_result: dict, analysis: dict) -> list:
        """
        Determine what needs to go to Krone.
        These are issues the Circle cannot resolve on their own.
        """
        escalations = []

        # All sources silent for full scan
        sources = scan_result.get("sources", {})
        all_silent = all(v == 0 for v in sources.values()) if sources else False
        if all_silent:
            escalations.append({
                "severity": "HIGH",
                "issue":    "Total scan silence — all sources returned 0",
                "action":   (
                    "Check DNS, env vars, and network. "
                    "Test: nslookup courtlistener.com 8.8.8.8. "
                    "Check: echo $COURTLISTENER_TOKEN"
                ),
            })

        # Save rate critical
        found = scan_result.get("found", 0)
        saved = scan_result.get("saved", 0)
        if found > 0 and (saved / found) < 0.30:
            escalations.append({
                "severity": "HIGH",
                "issue":    f"Critical save rate: {saved}/{found} ({saved/found:.0%})",
                "action":   (
                    "Check make_case_id() includes source_url in hash. "
                    "Check source_url uniqueness in DB. "
                    "Run: SELECT source_url, COUNT(*) FROM cases "
                    "GROUP BY source_url HAVING COUNT(*) > 20"
                ),
            })

        # Unrecognized domains flagged by Maren
        maren = self.circle.get("Maren")
        if maren and maren._errors > 5:
            escalations.append({
                "severity": "MEDIUM",
                "issue":    f"Maren logged {maren._errors} errors — new unrecognized domains",
                "action":   "Review Maren's TRUSTED_DOMAINS list. Add new legitimate sources.",
            })

        return escalations

    def _write_escalations(self, escalations: list):
        """Write escalations to file for Krone to review."""
        try:
            existing = []
            if os.path.exists(ESCALATION_PATH):
                with open(ESCALATION_PATH) as f:
                    existing = json.load(f)

            record = {
                "timestamp":   datetime.now(timezone.utc).isoformat(),
                "escalations": escalations,
                "resolved":    False,
            }
            existing.append(record)
            existing = existing[-50:]  # keep last 50

            os.makedirs(os.path.dirname(ESCALATION_PATH), exist_ok=True)
            with open(ESCALATION_PATH, "w") as f:
                json.dump(existing, f, indent=2)
        except Exception as e:
            print(f"  [◈ ENGINE] Could not write escalations: {e}")

    def status(self) -> dict:
        """Quick status report for all Circle members."""
        return {
            "circle":     [m.report() for m in CIRCLE],
            "pool":       self.pool.coverage_report(),
            "escalations": self._load_escalations(),
        }

    def _load_escalations(self) -> list:
        try:
            if os.path.exists(ESCALATION_PATH):
                with open(ESCALATION_PATH) as f:
                    return [
                        e for e in json.load(f)
                        if not e.get("resolved")
                    ]
        except Exception:
            pass
        return []
