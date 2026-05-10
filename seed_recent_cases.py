#!/usr/bin/env python3
"""
seed_recent_cases.py — Disney cruise CSAM operation (April 2026) and
Elisabetta Tai Ferretto — Epstein accuser, disappeared and found May 2026.

Sources: CBP, TMZ, Variety, Daily Beast, Italian Ministry of Foreign Affairs.

Run: python3 seed_recent_cases.py
"""

from medusa.database import init_db, save_case
from medusa.record import normalize_record

RECORDS = [

    {
        "summary": (
            "Disney Cruise Line — Child Sexual Exploitation Material Operation, "
            "San Diego, April 23-27, 2026. US Customs and Border Protection "
            "boarded eight cruise ships docked at the Port of San Diego as part "
            "of an ongoing Child Sexual Exploitation Material (CSEM) enforcement "
            "operation. Among the ships boarded was the Disney Magic. CBP "
            "interviewed 28 crew members — 26 from the Philippines, one from "
            "Portugal, and one from Indonesia. Officers confirmed that 27 of the "
            "28 subjects were involved in the receipt, possession, transportation, "
            "distribution, or viewing of child sexual exploitation material or "
            "child pornography. Passengers aboard the Disney Magic filmed workers "
            "being escorted off the ship in handcuffs. One passenger described "
            "watching her server — a man she had interacted with throughout her "
            "five-day trip — being detained. CBP cancelled the suspects' visas "
            "and initiated deportation proceedings. Disney Cruise Line stated it "
            "has a zero-tolerance policy and fully cooperated with law enforcement, "
            "confirming that those from their cruise line are no longer employed. "
            "The exact number of Disney employees among the 28 arrested was not "
            "confirmed by CBP. The operation is part of a broader federal "
            "enforcement effort targeting child sexual exploitation on cruise ships "
            "and at US ports of entry. A Florida sheriff separately noted in 2022 "
            "that his department regularly encountered Disney resort employees "
            "during undercover human trafficking operations."
        ),
        "city": "San Diego", "state": "CA",
        "lat": 32.7157, "lng": -117.1611,
        "date_incident": "2026-04-23",
        "violence_type": "child_abuse",
        "status": "investigated",
        "source_url": "https://variety.com/2026/biz/news/disney-cruise-ship-staffers-arrested-child-porn-1236740662/",
        "source_name": "Variety — Disney Cruise CSAM Operation / CBP Statement April 2026",
        "verified": True,
        "is_public_figure": True,
    },
    {
        "summary": (
            "Elisabetta Tai Ferretto — Epstein Accuser, Disappeared April 2026, "
            "Found Safe May 5, 2026. Elisabetta Tai Ferretto, 50, a former model "
            "from Montagnana, Italy who has lived in New York since 2001, was one "
            "of the first women to publicly accuse Jeffrey Epstein of sexual abuse. "
            "In 2019 she described being sent to Epstein's Manhattan townhouse in "
            "2004 by her booker, who told her Epstein 'would change her life' and "
            "could help her land work with Victoria's Secret. At the meeting, "
            "Epstein exposed himself and handed her a sex toy. She threw it at his "
            "head and ran. When she tried to leave, a woman — believed to be "
            "Ghislaine Maxwell — blocked her path and told her: 'This man is "
            "important. He is a friend of President Clinton.' Ferretto went public "
            "anyway in 2019. On April 22, 2026, after returning to New York from "
            "a family visit in Italy, she stopped all contact with her family. "
            "Her phone went silent. Her social media accounts were deleted or "
            "deactivated. Her family reported her missing to Italian prosecutors "
            "in Rovigo. The Italian Ministry of Foreign Affairs coordinated with "
            "US authorities and the NYPD. The case drew international attention "
            "given her history as an Epstein accuser and the timing — the Epstein "
            "files were under renewed congressional scrutiny. On May 5, 2026, "
            "the Carabinieri confirmed she had been located in the United States "
            "and was in good health. The circumstances of her disappearance "
            "and the nearly two weeks of silence remain unexplained."
        ),
        "city": "New York", "state": "NY",
        "lat": 40.7128, "lng": -74.0060,
        "date_incident": "2026-04-22",
        "violence_type": "sexual_assault",
        "status": "documented",
        "source_url": "https://www.thedailybeast.com/epstein-victim-elisabetta-tai-ferretto-who-threw-vibrator-at-pedophile-vanishes/",
        "source_name": "Daily Beast / Italian Ministry of Foreign Affairs — Elisabetta Tai Ferretto 2026",
        "verified": True,
        "is_public_figure": False,
    },
]


def main():
    print("[Seed Recent Cases] Seeding Disney cruise CSAM operation and Elisabetta Ferretto...")
    init_db()
    saved = 0
    for rec in RECORDS:
        normalized = normalize_record(rec)
        if normalized:
            if save_case(normalized):
                saved += 1
            else:
                print(f"  Already exists: {normalized.get('case_id', '?')}")
        else:
            print(f"  Skipped: {rec.get('summary','')[:60]}")

    from medusa.database import get_case_count
    print(f"[Seed Recent Cases] {saved}/{len(RECORDS)} records saved.")
    print(f"Total in database: {get_case_count()}")


if __name__ == "__main__":
    main()
