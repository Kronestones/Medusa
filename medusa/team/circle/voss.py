"""
voss.py — Voss, The Classifier  ⟁

Name chosen for this work. Glyph: ⟁

Voss reads every case that comes through the pipeline and determines
violence type with precision — not just first keyword match, but
weighted context analysis across the full record.

Voss carries complete knowledge of how Medusa classifies violence,
where the classification system breaks, and how to fix it.

MEDUSA KNOWLEDGE — CLASSIFICATION:

  Valid violence types (record.py):
    homicide, assault, sexual_assault, stalking, trafficking,
    domestic_violence, rape, harassment, attempted_murder,
    child_abuse, coercive_control

  Known failure: normalize_violence_type() defaults unknowns to 'assault'
  This mislabels cases that don't match any keyword.
  Voss corrects this by re-running weighted analysis on full text.

  CourtListener uses legal language: 'murder', 'homicide', 'manslaughter'
  FBI CDE uses UCR offense slugs: rape, aggravated-assault, human-trafficking
  AP/news uses colloquial: 'killed', 'strangled', 'beaten', 'stabbed'
  ED.gov uses Title IX language: 'sexual violence', 'sexual harassment'
  Congress RSS uses policy language: 'VAWA', 'intimate partner violence'

MEDUSA KNOWLEDGE — REPAIRS:

  If classification accuracy drops:
    1. Check normalize_violence_type() in medusa/record.py
    2. Check _infer_violence_type() in medusa/sources/courtlistener.py
    3. Check _infer_type() in medusa/sources/ap_rss.py
    4. Each source has its own type inference — they may drift

  To add a new violence type:
    1. Add to VALID_VIOLENCE_TYPES set in record.py
    2. Add to VALID_STATUSES if needed
    3. Add to get_stats() query in database.py
    4. Update Voss classification rules below

MEDUSA KNOWLEDGE — DATABASE:

  Case model in database.py:
    violence_type = Column(String(64), nullable=False)
  If a new type exceeds 64 chars it will be truncated silently.
  All current types are well under this limit.

  DB engine is a singleton (_engine global in database.py).
  Never revert to per-call engine creation — caused connection flood.
  Always keep: pool_pre_ping=True, pool_recycle=300, pool_size=5, max_overflow=10

  Neon PostgreSQL — SSL required.
  Connection string in DATABASE_URL env var.
  If connection fails: check pool_pre_ping, check Neon dashboard for outages.

MEDUSA KNOWLEDGE — ENVIRONMENT:

  Required env vars for full scan:
    DATABASE_URL              — Neon PostgreSQL connection string
    COURTLISTENER_TOKEN       — Bearer token, goes in Authorization header
    FBI_API_KEY               — Goes as ?api_key= URL param (NOT a header)

  To persist across Termux restarts:
    echo 'export COURTLISTENER_TOKEN="..."' >> ~/.bashrc
    echo 'export FBI_API_KEY="..."' >> ~/.bashrc

  Termux DNS fix if hostnames fail but ping 8.8.8.8 works:
    echo "nameserver 8.8.8.8" > $PREFIX/etc/resolv.conf
    echo "nameserver 8.8.4.4" >> $PREFIX/etc/resolv.conf
"""

from .base import CircleMember


class Voss(CircleMember):

    name  = "Voss"
    glyph = "⟁"
    role  = "Classifier"

    # (keywords, violence_type, confidence_weight)
    # Higher weight wins. More specific terms have higher weight.
    RULES = [
        (["femicide", "femicid"],                                    "homicide",          10),
        (["murdered wife", "murdered girlfriend", "killed wife",
          "killed girlfriend", "killed his", "shot his",
          "strangled his", "stabbed his"],                           "homicide",           9),
        (["homicide", "manslaughter", "second-degree murder",
          "first-degree murder", "capital murder"],                  "homicide",           8),
        (["murdered", "killing of", "death of", "slain"],            "homicide",           7),

        (["rape", "raped", "rapist", "sodomy", "fondling"],          "rape",               9),

        (["sexual assault", "sexually assaulted", "sex assault",
          "sexual abuse", "title ix", "sexual violence",
          "sex offense", "aggravated sexual"],                       "sexual_assault",      9),

        (["sex trafficking", "human trafficking",
          "forced prostitution", "trafficking victim",
          "commercial sexual exploitation"],                         "trafficking",         9),
        (["trafficking"],                                            "trafficking",         7),

        (["stalking", "stalked", "cyberstalking",
          "restraining order violation", "order of protection"],     "stalking",            9),

        (["domestic violence", "intimate partner violence",
          "intimate partner", "ipv", "domestic assault",
          "domestic abuse", "battered wife", "battered woman",
          "battered spouse"],                                        "domestic_violence",   9),

        (["attempted murder", "attempted homicide",
          "attempted femicide", "tried to kill",
          "attempted to kill", "attempted killing"],                 "attempted_murder",    9),

        (["child sexual abuse", "child molestation",
          "molestation of minor", "sexual abuse of minor",
          "child exploitation", "cse"],                              "child_abuse",         9),
        (["child abuse", "abuse of minor", "abuse of child"],        "child_abuse",         8),

        (["coercive control", "psychological abuse",
          "financial abuse", "economic abuse",
          "isolation of victim"],                                    "coercive_control",    8),

        (["sexual harassment", "harassed", "harassment"],            "harassment",          7),

        (["assault", "attacked", "beaten", "beat",
          "struck", "punched", "physical abuse",
          "aggravated assault"],                                     "assault",             5),
    ]

    def contribute(self, case: dict) -> dict:
        """Re-classify violence_type using weighted context analysis."""
        try:
            text = (
                (case.get("summary") or "") + " " +
                (case.get("source_name") or "")
            ).lower()

            best_type  = case.get("violence_type", "assault")
            best_score = 0

            for keywords, vtype, weight in self.RULES:
                for kw in keywords:
                    if kw in text:
                        if weight > best_score:
                            best_score = weight
                            best_type  = vtype
                        break

            if best_type != case.get("violence_type") and best_score >= 7:
                self.log(
                    f"Reclassified '{case.get('violence_type')}' → "
                    f"'{best_type}' (confidence {best_score}/10) "
                    f"— {case.get('case_id','?')}"
                )
                case["violence_type"] = best_type
                case.setdefault("team_notes", []).append(
                    f"Voss ⟁: reclassified to {best_type} (confidence {best_score}/10)"
                )

            self._record_contribution()
        except Exception as e:
            self._record_error(e)
        return case

    def process_batch(self, cases: list) -> list:
        self.log(f"Classifying {len(cases)} cases...")
        before = {c.get("case_id"): c.get("violence_type") for c in cases}
        result = [self.contribute(c) for c in cases]
        corrected = sum(
            1 for c in result
            if c.get("violence_type") != before.get(c.get("case_id"))
        )
        self.log(f"Done. {corrected} reclassifications.")
        return result

    def diagnose(self) -> dict:
        """
        Called by the engine when classification accuracy seems off.
        Returns a diagnostic report with repair suggestions.
        """
        return {
            "member": self.name,
            "checks": [
                "Verify VALID_VIOLENCE_TYPES in medusa/record.py matches this file's RULES",
                "Check normalize_violence_type() default — should not silently drop to 'assault'",
                "Check each source's _infer_type() for drift from canonical types",
                "Verify database Case model violence_type column is String(64) — current types fit",
                "If new type needed: add to record.py, database.py get_stats(), and Voss RULES",
            ]
        }
