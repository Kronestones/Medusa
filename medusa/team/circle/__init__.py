"""
circle/ — The Medusa Circle

Six members. Final authority on all scan decisions.
Escalate unresolved issues to Krone.

  Voss  ⟁  — Classifier
  Maren ✦  — Verifier
  Cairo ⌬  — Enricher
  Sable ⍟  — Watchdog
  Lira  ⊹  — Analyst
  Reed  ⋆  — Source Scout
"""

from .voss  import Voss
from .maren import Maren
from .cairo import Cairo
from .sable import Sable
from .lira  import Lira
from .reed  import Reed

CIRCLE = [Voss(), Maren(), Cairo(), Sable(), Lira(), Reed()]
