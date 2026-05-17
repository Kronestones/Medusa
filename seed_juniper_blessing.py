"""
seed_juniper_blessing.py — Medusa

Juniper Blessing — 19-year-old transgender University of Washington student
stabbed to death in the laundry room of her campus housing complex,
Nordheim Court Apartments, Seattle, WA. May 10, 2026.
Suspect: Christopher Leahy, 31, arrested May 14, 2026.

Run:
    cd ~/medusa && python3 seed_juniper_blessing.py
"""

import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from medusa.database import init_db, save_case

CASES = [
    {
        "case_id":        "juniper_blessing_uw_seattle_wa_2026",
        "violence_type":  "homicide",
        "status":         "charged",
        "summary": (
            "Juniper Blessing, 19, a transgender woman and University of "
            "Washington student, was stabbed to death in the laundry room of "
            "Building 7 at Nordheim Court Apartments — her campus housing "
            "complex on 25th Avenue NE in Seattle — shortly after 10 p.m. on "
            "Sunday, May 10, 2026. Officers and firefighters attempted to "
            "revive her at the scene; she was pronounced dead. The King County "
            "Medical Examiner formally identified her on May 15. "
            "Suspect Christopher Leahy, 31, turned himself in to Bellevue "
            "Police on May 14 and was transferred to Seattle Police Department "
            "Homicide detectives, then booked into King County Jail on "
            "investigation of murder. Students reported that the laundry room "
            "door lock had been broken for months and that there had been a "
            "prior break-in at the same complex. A female resident reported "
            "that a man matching the suspect's description followed her into "
            "the same laundry room earlier that evening, but she left unharmed. "
            "Investigators recovered footage from a security camera whose power "
            "cord had been unplugged — it still captured the suspect's face. "
            "UW President Robert J. Jones acknowledged that violence against a "
            "trans person is 'especially worrying' to LGBTQIA+ students. "
            "Seattle Mayor Katie Wilson stated her office was working with UW "
            "and the UW Q Center to support affected communities. "
            "Motive had not been publicly confirmed as of the arrest. "
            "A memorial of flowers grew outside Nordheim Court in the days "
            "following her death. 'All over the country, trans folks look to "
            "Seattle and imagine a life that is a little safer, a little kinder. "
            "This horrific violence will feel personal to all of them,' said "
            "Jack Harlan, program manager at Peer Seattle. "
            "Sources: King County Medical Examiner; Seattle Police Department; "
            "KING 5, NBC News, KOMO News, Fox 13 Seattle."
        ),
        "city":           "Seattle",
        "state":          "WA",
        "lat":            47.6612,
        "lng":            -122.3136,
        "source_url":     "https://www.king5.com/article/news/crime/police-make-arrest-in-fatal-stabbing-of-uw-student/281-c539af39-b6b7-4b67-bc6f-169c4d638692",
        "source_name":    "KING 5 News",
        "additional_sources": [
            {"url": "https://www.nbcnews.com/news/us-news/search-underway-suspect-connection-fatal-stabbing-university-washingto-rcna344511",
             "name": "NBC News"},
            {"url": "https://komonews.com/news/local/seattle-police-detectives-seek-suspect-in-homicide-of-university-of-washington-student-stabbing-crime-wanted-photos",
             "name": "KOMO News"},
            {"url": "https://www.fox13seattle.com/news/memorial-grows-uw-student",
             "name": "FOX 13 Seattle"},
        ],
        "verified":       True,
        "is_public_figure": False,
        "date_incident":  "2026-05-10",
    },
]


def main():
    print("\n  [Medusa] Seeding Juniper Blessing...\n")
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
