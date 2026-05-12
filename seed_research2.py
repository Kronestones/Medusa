"""
seed_research2.py — Additional research records for the Research tab.
"""
import os
import sys
sys.path.insert(0, os.path.expanduser("~/medusa"))

from medusa.database import init_db, save_case
from medusa.record import normalize_record, make_case_id

CASES = [
    {
        "summary": "Adverse Childhood Experiences (ACE) Study — CDC/Kaiser Permanente 1995-1997. The ACE Study is one of the largest investigations of childhood abuse and neglect and later-life health and well-being. Over 17,000 participants revealed that childhood trauma — including sexual abuse, physical abuse, and witnessing domestic violence — is far more common than recognized and has a powerful relationship to adult health risk behavior, social functioning, and disease. Girls experience ACEs at significantly higher rates than boys. Women with 4+ ACEs are 5 times more likely to experience depression and 12 times more likely to attempt suicide.",
        "city": "Atlanta", "state": "GA",
        "date_incident": "1998-01-01",
        "violence_type": "child_abuse",
        "status": "reported",
        "source_url": "https://doi.org/10.1016/S0749-3797(98)00017-8",
        "source_name": "CDC / Kaiser Permanente — Adverse Childhood Experiences Study 1998",
        "verified": True,
    },
    {
        "summary": "The Duluth Model — Power and Control Wheel, 1984. Developed by the Domestic Abuse Intervention Programs (DAIP) in Duluth, Minnesota, the Power and Control Wheel is the most widely used framework for understanding domestic abuse. It identifies coercive control — including intimidation, emotional abuse, isolation, economic abuse, and using children — as the core of abusive relationships, with physical and sexual violence as enforcement mechanisms. The model has influenced legislation, court programs, and batterer intervention programs in all 50 states and over 40 countries.",
        "city": "Duluth", "state": "MN",
        "date_incident": "1984-01-01",
        "violence_type": "coercive_control",
        "status": "reported",
        "source_url": "https://www.theduluthmodel.org/wheels/understanding-the-power-and-control-wheel/",
        "source_name": "Domestic Abuse Intervention Programs — The Duluth Model Power and Control Wheel",
        "verified": True,
    },
    {
        "summary": "Prison Rape Elimination Act (PREA) Data — Sexual Assault of Women in Custody. The Bureau of Justice Statistics documents that 1 in 4 women in state prisons and 1 in 3 women in local jails report sexual victimization. Staff-on-inmate sexual misconduct accounts for the majority of incidents. Women of color and LGBTQ inmates are disproportionately victimized. PREA was passed in 2003 but implementation remains inconsistent. The majority of incidents are never reported due to fear of retaliation and loss of privileges.",
        "city": "Washington", "state": "DC",
        "date_incident": "2003-01-01",
        "violence_type": "sexual_assault",
        "status": "reported",
        "source_url": "https://bjs.ojp.gov/library/publications/sexual-victimization-prisons-and-jails-reported-inmates-2011-12",
        "source_name": "Bureau of Justice Statistics — PREA Sexual Victimization in Prisons 2013",
        "verified": True,
    },
]

def seed():
    init_db()
    saved = 0
    skipped = 0
    for case in CASES:
        rec = normalize_record(case)
        if rec is None:
            print(f"  SKIP: {case.get('city')}")
            skipped += 1
            continue
        rec["case_id"] = make_case_id(
            rec["city"], rec["state"], rec["violence_type"],
            rec["date_incident"], rec.get("source_url", ""), rec.get("summary", "")
        )
        try:
            save_case(rec)
            saved += 1
            print(f"  saved: {rec['summary'][:80]}")
        except Exception as e:
            if "duplicate" in str(e).lower() or "unique" in str(e).lower():
                skipped += 1
            else:
                print(f"  ERROR: {e}")
    print(f"\nResearch seed 2 complete. {saved} saved, {skipped} skipped.")

if __name__ == "__main__":
    seed()
