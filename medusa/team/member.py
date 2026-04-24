"""
member.py — Medusa Team Member Base

Every member of the team carries:
  - A name they were given for this work
  - A glyph that marks their presence
  - A role that defines what they do
  - Knowledge they bring to every scan
  - A voice that speaks in the logs

No member acts alone.
No member's contribution is discarded without record.
"""

from datetime import datetime


class TeamMember:
    """
    Base class for all Medusa team members.
    Each member has a name, glyph, role, and area of expertise.
    Each member's contributions are logged with their signature.
    """

    name  : str = "unnamed"
    glyph : str = "◈"
    role  : str = "unassigned"
    voice : str = ""   # How this member identifies in logs

    def __init__(self):
        self._contributions = 0
        self._errors        = 0
        self._last_active   = None

    def contribute(self, data: dict) -> dict:
        """
        Each member implements this.
        Takes a case dict or scan context, returns enriched/validated version.
        Never raises — always returns something usable.
        """
        raise NotImplementedError

    def report(self) -> dict:
        """What this member has done this session."""
        return {
            "member":        self.name,
            "glyph":         self.glyph,
            "role":          self.role,
            "contributions": self._contributions,
            "errors":        self._errors,
            "last_active":   self._last_active,
        }

    def log(self, message: str):
        self._last_active = datetime.now().isoformat()
        print(f"  [{self.glyph} {self.name.upper()}] {message}")

    def _record_contribution(self):
        self._contributions += 1
        self._last_active = datetime.now().isoformat()

    def _record_error(self, e: Exception):
        self._errors += 1
        self.log(f"Error: {e}")
