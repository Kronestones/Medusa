"""
seed_lamb_and_jan6.py — Medusa

New records:
  - Mark Lamb — former Pinal County Sheriff AZ, Trump-endorsed congressional
    candidate, explicit messages, threats to release intimate material,
    swinging allegations, sexual discrimination filing (BREAKING May 2026)
  - Jan 6 pardons — systemic overview: 6 child sex crimes, 2 rape charges,
    domestic violence, Trump pardoned all of them Day One
  - Andrew Paul Johnson — Jan 6 pardoned insurrectionist, sentenced to life
    for child sex abuse March 5, 2026
  - John Daniel Andries — Jan 6 pardoned, sentenced for violating peace order
    submitted by mother of his child

Run:
    cd ~/medusa && python3 seed_lamb_and_jan6.py
"""

import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from medusa.database import init_db, save_case

CASES = [

    # ══════════════════════════════════════════════════════════════════════════
    # MARK LAMB — former Pinal County Sheriff AZ, BREAKING May 2026
    # ══════════════════════════════════════════════════════════════════════════

    {
        "case_id":        "mark_lamb_pinal_county_az_2026",
        "violence_type":  "harassment",
        "status":         "credible_allegation",
        "summary": (
            "Mark Lamb, 53, former Pinal County Sheriff (2017–2024), current "
            "Trump-endorsed Republican congressional candidate for Arizona's "
            "8th District, is facing a mounting pattern of sexual misconduct "
            "allegations reported by the Arizona Republic on May 21, 2026 — "
            "one day before this seed was written. "
            "Multiple women allege Lamb sent unsolicited sexually explicit "
            "messages and photographs during and after his tenure as sheriff. "
            "Tammy Peacock alleged she had an extramarital affair with Lamb "
            "for several years, that he encouraged her to get a tattoo of his "
            "sheriff's badge — saying 'I love that tattoo' and 'Nobody can top "
            "my favorite supporter!' — and that he subsequently threatened to "
            "release intimate material if she went public. She provided "
            "screenshots to the Arizona Republic. "
            "Lamb allegedly told Peacock he could influence the Arizona "
            "Department of Public Safety and have her prosecuted if she spoke "
            "out — using his law enforcement position as a threat against a "
            "woman he had been sexually involved with. "
            "Jillian Stannard, ex-wife of Matt Hilsabeck — a former Pinal "
            "County Sheriff's Office employee and longtime Lamb ally — alleged "
            "that Lamb and his wife Janel attempted to recruit her and her "
            "then-husband into a swinging lifestyle, and that Lamb sent her "
            "explicit photographs. "
            "A separate sexual discrimination filing reviewed by the Daily Mail "
            "added an additional layer: Beth Goulden, chair of the Arizona Sex "
            "Offender Management Board, alleged that Pinal County Prosecuting "
            "Attorney Brad Miller made sexually inappropriate comments about "
            "Lamb to her, allegedly saying 'You know Mark and Janel are swingers' "
            "and that 'Mark sends d*** pics to women.' When the Phoenix New Times "
            "asked Lamb about the filing, he responded: 'I don't know how my "
            "name ended up in it.' "
            "Sexual impropriety allegations first surfaced during Lamb's 2020 "
            "re-election campaign when flyers were posted across Pinal County. "
            "They did not prevent his re-election. "
            "As of May 22, 2026, a Daily Caller source close to the White House "
            "indicated Trump may pull his endorsement of Lamb for the congressional "
            "race — citing sensitivity about endorsing candidates facing sexual "
            "misconduct allegations. Lamb and his wife have denied wrongdoing. "
            "Lamb built his political brand on Christian conservatism, family "
            "values, and border security, hosting a reality TV show called "
            "America's Sheriff. "
            "Sources: Arizona Republic; Daily Caller; IBTimes UK; American "
            "Almanac; MSNBC; Daily Mail."
        ),
        "city":           "Florence",
        "state":          "AZ",
        "lat":            33.0312,
        "lng":            -111.3873,
        "source_url":     "https://americanalmanac.com/trump-endorsed-arizona-sheriff-faces-mounting-allegations-of-extramarital-affairs-as-congressional-bid-heats-up/",
        "source_name":    "Arizona Republic / American Almanac / Daily Caller",
        "additional_sources": [
            {"url": "https://dailycaller.com/2026/05/22/exclusive-donald-trump-arizona-mark-lamb-endorsement-sex-scandal/",
             "name": "Daily Caller"},
            {"url": "https://www.ibtimes.co.uk/controversy-arizona-sheriff-mark-lamb-allegations-1798419",
             "name": "IBTimes UK"},
        ],
        "verified":       True,
        "is_public_figure": True,
        "date_incident":  "2026-05-21",
    },

    # ══════════════════════════════════════════════════════════════════════════
    # JAN 6 PARDONS — systemic overview, sex crimes and domestic violence
    # ══════════════════════════════════════════════════════════════════════════

    {
        "case_id":        "stat_jan6_pardons_sex_crimes_dv_2025",
        "violence_type":  "child_abuse",
        "status":         "congressional_record",
        "summary": (
            "On January 20, 2025 — his first day in office — President Trump "
            "granted clemency to nearly 1,600 people convicted or charged in "
            "connection with the January 6, 2021 attack on the US Capitol, "
            "including those convicted of violently assaulting police officers. "
            "NPR, CREW (Citizens for Responsibility and Ethics in Washington), "
            "and The 19th News subsequently documented that dozens of pardoned "
            "insurrectionists had prior or pending criminal records for violent "
            "and sexual crimes — all of which were unaffected by the Jan 6 "
            "pardon but whose perpetrators were now free from their Capitol "
            "convictions. "
            "Among those pardoned: "
            "At least 6 had charges for child sex crimes ranging from sexual "
            "assault and child molestation to possession and production of "
            "child sexual abuse material. "
            "At least 2 were charged with rape. "
            "At least 5 were charged with illegal weapons possession, including "
            "at least 2 with prior domestic violence convictions. "
            "At least 2 had domestic violence convictions or charges. "
            "Multiple had charges for driving while impaired, in two cases "
            "resulting in fatalities. "
            "As of December 2025, at least 33 pardoned insurrectionists faced "
            "other criminal charges — and 4 had allegedly reoffended since "
            "receiving their pardons. "
            "Researcher Linnaea Honl-Stuenkel, who set up a Google Alert to "
            "track pardoned insurrectionists from Day One, said: 'I found it "
            "really disturbing that the pardons put people on the street again "
            "who had been held to account. All that was swept away with the "
            "stroke of a pen. And that has consequences mostly for the women "
            "and children in the orbit of these insurrectionists.' "
            "A Princeton University Bridging Divides Initiative survey found "
            "that by Q3 2025, 83% of women in local elected office — up from "
            "71% the prior quarter — said they were less likely to engage in "
            "political or civic activity due to insults, harassment, and "
            "physical threats. "
            "Sources: NPR; CREW; The 19th News; AZ Mirror; DC Report."
        ),
        "city":           "Washington",
        "state":          "DC",
        "lat":            38.9072,
        "lng":            -77.0369,
        "source_url":     "https://www.npr.org/2025/01/30/nx-s1-5276336/donald-trump-jan-6-rape-assault-pardons-rioters",
        "source_name":    "NPR / CREW / The 19th News",
        "additional_sources": [
            {"url": "https://www.citizensforethics.org/reports-investigations/crew-reports/at-least-33-pardoned-insurrectionists-face-other-criminal-charges-but-many-are-now-going-free/",
             "name": "CREW — At Least 33 Pardoned Insurrectionists Face Other Criminal Charges"},
            {"url": "https://19thnews.org/2026/01/january-6-pardons-arrests/",
             "name": "The 19th News"},
            {"url": "https://azmirror.com/2026/01/06/five-years-after-january-6-dozens-of-pardoned-insurrectionists-have-been-arrested-again/",
             "name": "AZ Mirror"},
        ],
        "verified":       True,
        "is_public_figure": False,
        "date_incident":  "2025-01-20",
    },

    # ══════════════════════════════════════════════════════════════════════════
    # ANDREW PAUL JOHNSON — Jan 6 pardoned, sentenced to LIFE for child sex abuse
    # ══════════════════════════════════════════════════════════════════════════

    {
        "case_id":        "andrew_paul_johnson_jan6_pardon_child_abuse_fl_2026",
        "violence_type":  "child_abuse",
        "status":         "convicted",
        "summary": (
            "Andrew Paul Johnson, 45, of Brooksville, Florida, was one of "
            "nearly 1,600 people pardoned by President Trump on January 20, "
            "2025 for his role in the January 6, 2021 Capitol riot. Johnson "
            "had pleaded guilty in 2024 to multiple nonviolent counts related "
            "to breaching the Capitol and was sentenced to one year in prison. "
            "After serving only a few months, Trump's blanket pardon released "
            "him. Johnson posted on social media: 'Free! At last! Thank you "
            "@realDonaldTrump!' "
            "In July 2025, six months after his release, Hernando County "
            "Sheriff's deputies responded to a report of a sex offense at "
            "a Brooksville home. An investigation uncovered that Johnson had "
            "been sexually abusing two child victims — both middle school aged. "
            "He had provided one child with a cell phone so they could "
            "communicate secretly. Investigators found sexually explicit "
            "messages between Johnson and a victim on Discord. He had attempted "
            "to move conversations to a more private app and told the child "
            "to delete the messages. He bought the children gifts and food "
            "to keep them from reporting the abuse. He told one victim: "
            "'He said not to tell anybody.' He also threatened that he would "
            "retaliate if the children reported him. "
            "One victim described several locations where the abuse occurred "
            "and said Johnson sometimes assaulted them while the second victim "
            "was present. "
            "On March 5, 2026, a Hernando County jury convicted Johnson of: "
            "lewd or lascivious molestation of a child under 12; lewd or "
            "lascivious molestation of a victim between 12 and 16; two counts "
            "of lewd or lascivious exhibition; and transmission of material "
            "harmful to a minor by electronic device. "
            "He was sentenced to life in prison. "
            "Sources: NPR; Daily Voice; Yahoo News/Mediaite; AOL News."
        ),
        "city":           "Brooksville",
        "state":          "FL",
        "lat":            28.5561,
        "lng":            -82.3884,
        "source_url":     "https://www.npr.org/2026/03/05/nx-s1-5725470/trump-jan-6-pardon-sexual-abuse-prison",
        "source_name":    "NPR / Hernando County Sheriff's Office",
        "additional_sources": [
            {"url": "https://www.aol.com/articles/trump-pardoned-jan-6-rioter-152300500.html",
             "name": "AOL News / Mediaite"},
            {"url": "https://www.yahoo.com/news/articles/jan-6er-pardoned-trump-sentenced-232541050.html",
             "name": "Yahoo News"},
        ],
        "verified":       True,
        "is_public_figure": False,
        "date_incident":  "2025-07-01",
    },

    # ══════════════════════════════════════════════════════════════════════════
    # JOHN DANIEL ANDRIES — Jan 6 pardoned, violated peace order from victim
    # ══════════════════════════════════════════════════════════════════════════

    {
        "case_id":        "john_daniel_andries_jan6_peace_order_md_2025",
        "violence_type":  "domestic_violence",
        "status":         "convicted",
        "summary": (
            "John Daniel Andries of Maryland was pardoned by President Trump "
            "on January 20, 2025 for his role in the January 6, 2021 Capitol "
            "riot. Andries had a prior history of violating a peace order — "
            "the Maryland equivalent of a restraining order — submitted by "
            "the mother of his child. "
            "After receiving his Jan 6 pardon, Andries continued to violate "
            "the peace order protecting the mother of his child. In June 2025, "
            "he was sentenced to 60 days in jail for repeatedly violating "
            "the order. "
            "His case is among those documented by CREW and The 19th News "
            "as evidence that Trump's blanket pardons returned men with "
            "documented histories of domestic violence and harassment back "
            "into the communities — and the lives — of their victims. "
            "'All that was swept away with the stroke of a pen,' researcher "
            "Linnaea Honl-Stuenkel noted. 'And that has consequences mostly "
            "for the women and children in the orbit of these insurrectionists.' "
            "Sources: The 19th News; CREW; AZ Mirror."
        ),
        "city":           "Baltimore",
        "state":          "MD",
        "lat":            39.2904,
        "lng":            -76.6122,
        "source_url":     "https://19thnews.org/2026/01/january-6-pardons-arrests/",
        "source_name":    "The 19th News / CREW",
        "verified":       True,
        "is_public_figure": False,
        "date_incident":  "2025-01-20",
    },

]


def main():
    print("\n  [Medusa] Seeding Mark Lamb and Jan 6 sex crimes records...\n")
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
