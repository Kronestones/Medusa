"""
consultants/ — The Medusa Consultant Pool

Hundreds of specialists loaded from profile files.
Available on demand. No individual files per consultant.

Domains:
  violence_type   — 11 specialists, one per violence type
  jurisdiction    — 51 specialists, one per US state + DC
  source_health   — one per data source
  pattern         — anomaly and health pattern monitors
  system          — infrastructure and environment monitors
"""

from .pool import ConsultantPool
