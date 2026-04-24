"""
lira.py — Lira, The Analyst  ⊹

Name chosen for this work. Glyph: ⊹

Lira reads the database after every scan and surfaces what matters.
Not individual cases — patterns. Gaps. Spikes. Silences.

Which states have no coverage this week.
Which violence types are underrepresented relative to known rates.
Where public figure cases are concentrated.
What the data says that the individual records don't.

Lira does not judge. Lira reports.

MEDUSA KNOWLEDGE — DATABASE QUERIES:

  get_stats() in database.py returns:
    {
      "total": int,
      "public_figures": int,
      "by_type": {"homicide": int, "assault": int, ...},
      "by_state": {"CA": int, "TX": int, ...}  # not yet implemented
    }

  Direct DB queries via SQLAlchemy:
    from medusa.database import get_session
    from medusa.models import Case
    session = get_session()
    results = session.query(Case).filter(Case.violence_type == "homicide").all()
    session.close()

  Case model fields available for analysis:
    violence_type, status, is_public_figure, date_incident,
    date_reported, city, state, lat, lng, source_name, verified

  Neon DB — always close session after query.
  Use try/finally to guarantee session.close() is called.

MEDUSA KNOWLEDGE — KNOWN DATA GAPS:

  Sources not yet implemented (high value):
    - DOJ press releases (justice.gov/news RSS) — federal prosecutions
    - State AG press releases — state prosecutions
    - GovInfo.gov — congressional hearing transcripts
    - NCVS (National Crime Victimization Survey) — BJS data
    - NIBRS (National Incident-Based Reporting System) — FBI incident data

  Known underrepresentation:
    - Rural states: fewer news sources, less CourtListener coverage
    - Tribal jurisdiction cases: rarely in federal courts
    - Immigration-related trafficking: often federal sealed cases
    - Child abuse: heavily sealed in state courts

  Known overrepresentation:
    - States with active federal districts (CA, TX, NY, FL)
    - Cases involving federal charges (trafficking, interstate)
    - High-profile public figure cases (more news coverage)

MEDUSA KNOWLEDGE — NATIONAL STATISTICS FOR COMPARISON:

  CDC/FBI baseline rates (approximate annual):
    Intimate partner homicide (women): ~1,500/year
    Rape/sexual assault: ~463,000/year (NCVS)
    Domestic violence: ~10 million/year
    Stalking: ~7.5 million/year
    Human trafficking: ~200,000-500,000/year (estimated)

  If Medusa's counts are orders of magnitude below these:
    - Expected — Medusa captures documented/prosecuted cases only
    - Unreported cases are the majority for all violence types
    - Medusa's value is documentation, not statistical completeness

MEDUSA KNOWLEDGE — STATUS DISTRIBUTION:

  Valid statuses: reported, charged, convicted, acquitted,
                  civil_judgment, credible_allegation,
                  congressional_record, unknown

  CourtListener cases are typically: charged (active docket)
  or convicted (terminated docket with date_terminated set)
  FBI cases: reported (aggregate statistics)
  News RSS: reported or charged depending on coverage stage

  If status is always 'reported':
    Check _infer_status() in courtlistener.py and ap_rss.py
    CourtListener: if dateTerminated is set → convicted/acquitted
    News: if "sentenced", "convicted" in text → convicted

MEDUSA KNOWLEDGE — REPAIRS FOR LIRA:

  If by_state query returns empty:
    get_stats() in database.py may not include state breakdown yet
    Add: stats["by_state"] = dict(
      session.query(Case.state, func.count(Case.id))
      .group_by(Case.state).all()
    )

  If pattern analysis finds impossible values (negative counts, etc):
    Check normalize_record() in record.py — validation may have gaps
    Check database.py save_case() — confirm field types match model

  If date analysis is unreliable:
    date_incident is nullable — many records have no date
    date_reported is set on save — always present
    Use date_reported for time-series analysis if date_incident sparse
"""

import os
from collections import defaultdict, Counter
from datetime import datetime, timezone
from .base import CircleMember


class Lira(CircleMember):

    name  = "Lira"
    glyph = "⊹"
    role  = "Analyst"

    # States with historically low Medusa coverage — watch these
    UNDERSERVED_STATES = {
        "AK", "WY", "ND", "SD", "MT", "VT", "NH", "ME",
        "ID", "WV", "NE", "KS", "NM", "HI", "RI", "DE"
    }

    # Expected minimum cases per scan for high-population states
    HIGH_COVERAGE_STATES = {
        "CA": 10, "TX": 8, "FL": 6, "NY": 6,
        "PA": 4, "IL": 4, "OH": 4, "GA": 4,
    }

    def contribute(self, cases: list) -> dict:
        """
        Analyze a batch of cases. Returns analysis report.
        Called after each scan with the full batch.
        """
        try:
            report = {
                "timestamp":      datetime.now(timezone.utc).isoformat(),
                "total":          len(cases),
                "by_type":        {},
                "by_state":       {},
                "by_source":      {},
                "by_status":      {},
                "public_figures": 0,
                "verified":       0,
                "gaps":           [],
                "spikes":         [],
                "notes":          [],
            }

            if not cases:
                report["notes"].append("No cases to analyze this scan.")
                return report

            # Aggregate counts
            types   = Counter(c.get("violence_type", "unknown") for c in cases)
            states  = Counter(c.get("state", "?")               for c in cases)
            sources = Counter(c.get("source_name", "unknown")   for c in cases)
            status  = Counter(c.get("status", "unknown")        for c in cases)

            report["by_type"]   = dict(types.most_common())
            report["by_state"]  = dict(states.most_common())
            report["by_source"] = dict(sources.most_common())
            report["by_status"] = dict(status.most_common())
            report["public_figures"] = sum(
                1 for c in cases if c.get("is_public_figure")
            )
            report["verified"] = sum(
                1 for c in cases if c.get("verified")
            )

            # Gap detection — underserved states with zero cases
            for state in self.UNDERSERVED_STATES:
                if states.get(state, 0) == 0:
                    report["gaps"].append(
                        f"No coverage: {state} — historically underserved"
                    )

            # Gap detection — high coverage states below threshold
            for state, minimum in self.HIGH_COVERAGE_STATES.items():
                count = states.get(state, 0)
                if count < minimum:
                    report["gaps"].append(
                        f"Low coverage: {state} has {count} cases "
                        f"(expected ≥{minimum})"
                    )

            # Spike detection — any type with disproportionate share
            total = len(cases)
            for vtype, count in types.items():
                share = count / total
                if share > 0.60:
                    report["spikes"].append(
                        f"Type dominance: '{vtype}' is {share:.0%} of all cases "
                        f"— may indicate source bias"
                    )

            # Status health check
            if status.get("unknown", 0) > total * 0.5:
                report["notes"].append(
                    f"Status 'unknown' is {status['unknown']}/{total} cases. "
                    f"Check _infer_status() in source modules."
                )

            # Source diversity check
            if len(sources) == 1:
                only_source = list(sources.keys())[0]
                report["notes"].append(
                    f"All cases from single source: {only_source}. "
                    f"Other sources may be down."
                )

            # Log summary
            self.log(
                f"Analysis: {total} cases | "
                f"{len(report['gaps'])} gaps | "
                f"{len(report['spikes'])} spikes | "
                f"{report['public_figures']} public figures"
            )

            self._record_contribution()
        except Exception as e:
            self._record_error(e)
            report = {"error": str(e)}

        return report

    def diagnose(self) -> dict:
        return {
            "member": self.name,
            "checks": [
                "If by_state empty: add state breakdown to get_stats() in database.py",
                "If status always 'unknown': check _infer_status() in source modules",
                "If single source dominating: check other sources for failures",
                "Underserved states list may need updating as sources improve",
                "National baseline rates in docstring for context — Medusa won't match them",
                "date_incident is sparse — use date_reported for time-series",
            ]
        }
