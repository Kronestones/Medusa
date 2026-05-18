"""
seed_sexual_coercion_study.py — Medusa

Peer-reviewed study: Journal of Interpersonal Violence
95.1% of surveyed men admitted using calculated tactics to coerce
non-consenting women into sex. 2,689 men aged 18-34, US and Canada.

Run:
    cd ~/medusa && python3 seed_sexual_coercion_study.py
"""

import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from medusa.database import init_db, save_case

CASES = [
    {
        "case_id":        "stat_jiv_sexual_coercion_95pct_study",
        "violence_type":  "sexual_assault",
        "status":         "congressional_record",
        "summary": (
            "A peer-reviewed study published in the Journal of Interpersonal "
            "Violence surveyed 2,689 men aged 18 to 34 in the United States "
            "and Canada using fully anonymous surveys, guaranteeing no fear of "
            "social or legal consequences, to obtain honest self-reporting. "
            "The study focused on men's use of calculated strategies to obtain "
            "sex from women they knew did not want to engage in sexual activity "
            "and had not consented. "
            "Key findings: "
            "95.1% of respondents reported having recently used at least one "
            "calculated strategy to pressure, coerce, or force a non-consenting "
            "woman into sex. "
            "Of those attempts, 65% resulted in successfully coercing or forcing "
            "the woman into sex. "
            "Researchers identified 36 distinct coercive strategies from "
            "formative research — all 36 were reported as having been used by "
            "at least some men. The average man in the sample had used 8.94 "
            "different strategies. "
            "Tactics ranged from persistent verbal pressure, manipulation, and "
            "emotional coercion at the lower end, to physical restraint and "
            "overt physical force at the higher end. The most commonly reported "
            "were consistent physical pressure and verbal coercion. "
            "The women targeted were individuals with whom the men had no prior "
            "romantic or sexual history — these were not relationship disputes "
            "but encounters with near-strangers. "
            "This study is among the most significant self-report studies of "
            "sexual coercion ever conducted. Its findings — that sexual coercion "
            "of non-consenting women is not a behavior confined to a small "
            "minority of predators, but reported by the vast majority of the "
            "anonymous male sample — have profound implications for understanding "
            "rape culture, consent education, and the gap between reported and "
            "actual rates of sexual violence. "
            "Source: Journal of Interpersonal Violence (peer-reviewed). "
            "Study methodology: anonymous survey, 2,689 men ages 18–34, "
            "United States and Canada."
        ),
        "city":           "Washington",
        "state":          "DC",
        "lat":            38.9072,
        "lng":            -77.0369,
        "source_url":     "https://journals.sagepub.com/home/jiv",
        "source_name":    "Journal of Interpersonal Violence",
        "verified":       True,
        "is_public_figure": False,
        "date_incident":  "2024-01-01",
    },
]


def main():
    print("\n  [Medusa] Seeding sexual coercion study...\n")
    try:
        init_db()
    except Exception as e:
        print(f"  [DB] Warning: {e}")

    saved = 0
    skipped = 0
    for case in CASES:
        if save_case(case):
            saved += 1
            print(f"  + {case['case_id']}")
        else:
            skipped += 1
            print(f"  ~ skipped (exists): {case['case_id']}")

    print(f"\n  Done. {saved} saved, {skipped} skipped.\n")


if __name__ == "__main__":
    main()
