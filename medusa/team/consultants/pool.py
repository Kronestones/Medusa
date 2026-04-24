"""
pool.py — Medusa Consultant Pool

Loads all consultant profiles and spins up specialist workers
dynamically. Hundreds of specialists available on demand —
one for each violence type, each state, each source,
each pattern — without hundreds of separate files.

Usage:
    from medusa.team.consultants.pool import ConsultantPool
    pool = ConsultantPool()

    # Get all state specialists
    state_consultants = pool.by_domain("jurisdiction")

    # Get specialist for a specific focus
    ca_specialist = pool.get("j_CA")

    # Run all source health consultants
    report = pool.run_source_health_checks()
"""

import json
import os
from typing import Optional


PROFILES_DIR = os.path.join(os.path.dirname(__file__), "profiles")


class Consultant:
    """
    A single consultant, instantiated from a profile dict.
    Lightweight — just carries knowledge and can answer questions.
    """

    def __init__(self, profile: dict):
        self.id          = profile.get("id", "unknown")
        self.name        = profile.get("name", "Unnamed Consultant")
        self.domain      = profile.get("domain", "general")
        self.focus       = profile.get("focus") or profile.get("state") or profile.get("source", "")
        self.profile     = profile
        self._queries    = 0

    def advise(self, context: dict = None) -> dict:
        """
        Return this consultant's knowledge about their focus area.
        context is optional — can narrow the advice.
        """
        self._queries += 1
        return {
            "consultant": self.name,
            "domain":     self.domain,
            "focus":      self.focus,
            "profile":    self.profile,
        }

    def diagnose(self, issue: str = "") -> list:
        """
        Return diagnostic steps for an issue in this consultant's domain.
        """
        self._queries += 1
        failure_modes = self.profile.get("failure_modes", [])
        checks        = self.profile.get("checks", [])
        diagnosis     = self.profile.get("diagnosis", [])
        notes         = [self.profile.get("notes", "")] if self.profile.get("notes") else []
        return failure_modes + checks + diagnosis + notes

    def __repr__(self):
        return f"Consultant({self.id}: {self.name})"


class ConsultantPool:
    """
    The full pool of Medusa consultants.
    Loads all profile JSON files and makes consultants available by
    domain, focus, state, or ID.
    """

    def __init__(self):
        self._consultants = {}
        self._load_all()
        print(f"  [◈ POOL] {len(self._consultants)} consultants loaded.")

    def _load_all(self):
        """Load all profile JSON files from profiles/ directory."""
        if not os.path.exists(PROFILES_DIR):
            print(f"  [◈ POOL] Profiles directory not found: {PROFILES_DIR}")
            return

        for filename in sorted(os.listdir(PROFILES_DIR)):
            if not filename.endswith(".json"):
                continue
            path = os.path.join(PROFILES_DIR, filename)
            try:
                with open(path) as f:
                    profiles = json.load(f)
                if isinstance(profiles, list):
                    for p in profiles:
                        c = Consultant(p)
                        self._consultants[c.id] = c
                elif isinstance(profiles, dict):
                    c = Consultant(profiles)
                    self._consultants[c.id] = c
            except Exception as e:
                print(f"  [◈ POOL] Failed to load {filename}: {e}")

    def get(self, consultant_id: str) -> Optional[Consultant]:
        """Get a specific consultant by ID."""
        return self._consultants.get(consultant_id)

    def by_domain(self, domain: str) -> list:
        """Get all consultants for a domain (violence_type, jurisdiction, source_health, pattern, system)."""
        return [c for c in self._consultants.values() if c.domain == domain]

    def by_focus(self, focus: str) -> list:
        """Get consultants matching a focus keyword."""
        focus = focus.lower()
        return [
            c for c in self._consultants.values()
            if focus in (c.focus or "").lower()
            or focus in c.name.lower()
        ]

    def for_state(self, state: str) -> Optional[Consultant]:
        """Get the jurisdiction specialist for a state."""
        state_id = f"j_{state.upper()}"
        return self._consultants.get(state_id)

    def for_violence_type(self, vtype: str) -> Optional[Consultant]:
        """Get the violence type specialist."""
        matches = [
            c for c in self._consultants.values()
            if c.domain == "violence_type" and c.focus == vtype
        ]
        return matches[0] if matches else None

    def for_source(self, source_name: str) -> Optional[Consultant]:
        """Get the source health consultant for a source."""
        matches = [
            c for c in self._consultants.values()
            if c.domain == "source_health"
            and source_name.lower() in c.name.lower()
        ]
        return matches[0] if matches else None

    def diagnose_source(self, source_name: str) -> list:
        """
        Get diagnostic steps for a failing source.
        Called by Sable when a source goes silent.
        """
        consultant = self.for_source(source_name)
        if consultant:
            return consultant.diagnose()
        return [f"No consultant found for source: {source_name}"]

    def diagnose_pattern(self, pattern_focus: str) -> list:
        """
        Get diagnostic steps for a detected pattern anomaly.
        Called by Lira when an anomaly is flagged.
        """
        matches = [
            c for c in self._consultants.values()
            if c.domain == "pattern" and c.focus == pattern_focus
        ]
        if matches:
            return matches[0].diagnose()
        return [f"No pattern consultant found for: {pattern_focus}"]

    def run_source_health_checks(self) -> dict:
        """
        Return a report of all source consultant knowledge.
        Not live checks — knowledge-based assessment.
        """
        report = {}
        for c in self.by_domain("source_health"):
            report[c.focus or c.name] = {
                "expected_min":  c.profile.get("expected_min"),
                "check_url":     c.profile.get("check_url"),
                "failure_modes": c.profile.get("failure_modes", []),
                "notes":         c.profile.get("notes", ""),
            }
        return report

    def run_system_checks(self) -> dict:
        """Return all system health consultant knowledge."""
        report = {}
        for c in self.by_domain("system"):
            report[c.focus] = {
                "checks":        c.profile.get("checks", []),
                "failure_modes": c.profile.get("failure_modes", []),
                "commands":      c.profile.get("commands", {}),
                "notes":         c.profile.get("notes", ""),
            }
        return report

    def coverage_report(self) -> dict:
        """
        Return a summary of consultant coverage by domain.
        """
        from collections import Counter
        domains = Counter(c.domain for c in self._consultants.values())
        return {
            "total":   len(self._consultants),
            "domains": dict(domains),
        }

    def all_ids(self) -> list:
        return sorted(self._consultants.keys())

    def __len__(self):
        return len(self._consultants)

    def __repr__(self):
        return f"ConsultantPool({len(self._consultants)} consultants)"
