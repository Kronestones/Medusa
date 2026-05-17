"""
seed_nicole_campbell_global.py — Medusa

Agnes Nicole Campbell — stabbed to death by her new boyfriend
Robert Jason MacKenzie, New Glasgow, Nova Scotia, Canada. Dec. 30, 2015.
MacKenzie convicted of manslaughter, sentenced to 15 years (2019).

This is a Canadian case — belongs in the Global/International tab.
Set extra["tab"] = "global" so the frontend can filter it correctly.

Run:
    cd ~/medusa && python3 seed_nicole_campbell_global.py
"""

import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from medusa.database import init_db, save_case

CASES = [
    {
        "case_id":        "nicole_campbell_new_glasgow_ns_canada_2015",
        "violence_type":  "homicide",
        "status":         "convicted",
        "summary": (
            "Agnes Nicole Campbell, 33, a mother of three from Pictou County, "
            "Nova Scotia, Canada, was stabbed to death on December 30, 2015, "
            "in a Temperance Street apartment in New Glasgow, Nova Scotia. "
            "Police found her body after a 911 call from a downstairs neighbour "
            "reporting a noise complaint; she was discovered at the top of the "
            "stairs leading to her boyfriend's apartment. An autopsy found five "
            "stab wounds to the back and side of her neck, superficial sharp-force "
            "injuries to her hands, and abrasions on her face — consistent with "
            "defensive wounds. "
            "The perpetrator, Robert Jason MacKenzie, 36, was her boyfriend of "
            "only a few weeks. He was arrested the following day after police "
            "observed him leaving an adjacent vacant apartment carrying wet "
            "clothing and a fixed-blade knife. Campbell's blood and DNA were "
            "found on the clothing. MacKenzie admitted to a high level of "
            "intoxication — alcohol and methamphetamine — at the time of the "
            "killing. He was initially charged with second-degree murder. "
            "In December 2018, he pleaded guilty to the reduced charge of "
            "manslaughter. In February 2019, Nova Scotia Supreme Court Justice "
            "Nick Scaravelli sentenced him to 15 years, with credit for 1,148 "
            "days already served, leaving approximately 10 years remaining. "
            "'The manner of brutality of the acts committed by Mr. MacKenzie "
            "carries a high degree of moral blameworthiness requiring a lengthy "
            "sentence,' the judge stated. Campbell's family attended court "
            "wearing t-shirts bearing her photo and black-and-red victim "
            "memorial ribbons. Her aunt stated: 'I do not want revenge — "
            "but I want justice.' "
            "This case is a Canadian intimate partner femicide. "
            "Sources: CBC News, Global News, CTV Atlantic."
        ),
        # Canadian case — approximate coordinates for New Glasgow, NS
        "city":           "New Glasgow",
        "state":          "NS",   # Nova Scotia — will not match US state validator;
                                   # store in extra and use a placeholder US state below
                                   # if the DB rejects NS. See note.
        "lat":            45.5854,
        "lng":            -62.6481,
        "source_url":     "https://www.cbc.ca/news/canada/nova-scotia/new-glasgow-manslaughter-sentence-15-years-1.5028384",
        "source_name":    "CBC News",
        "additional_sources": [
            {"url": "https://globalnews.ca/news/4985700/n-s-man-gets-15-years-for-manslaughter/",
             "name": "Global News"},
            {"url": "https://atlantic.ctvnews.ca/n-s-man-gets-15-years-for-stabbing-new-girlfriend-to-death-1.4307278",
             "name": "CTV Atlantic"},
        ],
        "verified":       True,
        "is_public_figure": False,
        "date_incident":  "2015-12-30",
        # Flag this record for the Global/International tab
        "tab":            "global",
        "country":        "Canada",
    },
]


def main():
    print("\n  [Medusa] Seeding Nicole Campbell (Global tab)...\n")
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
    print("  NOTE: 'state' is set to 'NS' (Nova Scotia). If the DB validator")
    print("  rejects non-US states, change state to 'DC' and rely on")
    print("  extra['country'] = 'Canada' and extra['tab'] = 'global'")
    print("  to place this record correctly in the frontend.\n")


if __name__ == "__main__":
    main()
