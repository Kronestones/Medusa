"""
seed_sentencing_and_personhood.py — Medusa

New records:
  - Brock Turner / Chanel Miller — Stanford rape, 6 months served, 2015/2016
  - UK Fordingbridge — three boys convicted of raping two girls aged 14 & 15,
    given youth rehabilitation orders, no prison, May 2026 (BREAKING)
  - NC HB 1232 — Life at Fertilization constitutional amendment, filed May 2026
  - Personhood / abortion-as-homicide bills across 10+ states, 2025–2026
    (GA, ID, IN, IA, KY, MO, ND, OK, SC, TX, IL, SD, TN, MT)

Run:
    cd ~/medusa && python3 seed_sentencing_and_personhood.py
"""

import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from medusa.database import init_db, save_case

CASES = [

    # ══════════════════════════════════════════════════════════════════════════
    # CHANEL MILLER / BROCK TURNER — Stanford rape, 6 months served
    # ══════════════════════════════════════════════════════════════════════════

    {
        "case_id":        "chanel_miller_brock_turner_stanford_ca_2015",
        "violence_type":  "sexual_assault",
        "status":         "convicted",
        "summary": (
            "On January 18, 2015, Chanel Miller — then 22, referred to in "
            "court documents as Emily Doe — was sexually assaulted behind a "
            "dumpster near a fraternity house at Stanford University in Palo "
            "Alto, California. She was unconscious. Two Swedish graduate "
            "students cycling past saw Brock Turner, 19, a Stanford swimmer "
            "and Olympic hopeful, on top of her and intervened. Turner fled "
            "on foot and was tackled and held until police arrived. "
            "Miller was found partially clothed, completely unresponsive, "
            "with pine needles in her hair and dirt on her body. She did not "
            "know she had been assaulted until she read about it in the news. "
            "Turner was charged with five felony counts. Two rape counts were "
            "dropped at the preliminary hearing. He was convicted in March 2016 "
            "on three felony counts: assault with intent to commit rape of an "
            "intoxicated person, penetration of an intoxicated person, and "
            "penetration of an unconscious person. "
            "Prosecutors asked for six years in prison. "
            "Santa Clara County Superior Court Judge Aaron Persky sentenced "
            "Turner to six months in county jail and three years probation, "
            "saying that a longer sentence would have 'a severe impact' on "
            "Turner. Turner was released after serving three months. "
            "Turner's father Dan Turner submitted a letter to the court "
            "describing his son's crime as '20 minutes of action out of his "
            "20 plus years of life.' "
            "In court, Chanel Miller read a 12-page victim impact statement "
            "directly to Turner — one of the most widely read documents to "
            "emerge from a sexual assault case in American history. It included: "
            "'You don't know me, but you've been inside me, and that's why we're "
            "here today.' And: 'You took away my worth, my privacy, my energy, "
            "my time, my safety, my intimacy, my confidence, my own voice, "
            "until today.' "
            "She anticipated the leniency: 'If I had been sexually assaulted "
            "by an un-athletic guy from a community college, what would his "
            "sentence be?' "
            "Judge Aaron Persky was recalled by California voters in June 2018 "
            "— the first California judge recalled in 86 years — in a campaign "
            "led by Stanford law professor Michele Landis Dauber. "
            "In 2019 Chanel Miller published her memoir Know My Name, revealing "
            "her identity publicly for the first time. California subsequently "
            "passed legislation removing judicial discretion in sentencing for "
            "sexual assault of an unconscious or intoxicated person. "
            "Brock Turner is a registered sex offender. He served 90 days. "
            "Sources: CNN; NPR; EBSCO Law; Palo Alto Weekly; ABC News."
        ),
        "city":           "Palo Alto",
        "state":          "CA",
        "lat":            37.4419,
        "lng":            -122.1430,
        "source_url":     "https://www.cnn.com/2016/06/06/us/sexual-assault-brock-turner-stanford",
        "source_name":    "CNN / Santa Clara County Superior Court",
        "additional_sources": [
            {"url": "https://www.npr.org/sections/thetwo-way/2016/06/06/481010919/california-rape-case-sentence-sparks-outrage",
             "name": "NPR"},
            {"url": "https://www.ebsco.com/research-starters/law/people-v-turner",
             "name": "EBSCO Law — People v. Turner"},
            {"url": "https://abcnews.com/US/victim-brock-turner-stanford-sexual-assault-case-public/story?id=65385613",
             "name": "ABC News — Chanel Miller goes public"},
        ],
        "verified":       True,
        "is_public_figure": False,
        "date_incident":  "2015-01-18",
    },

    # ══════════════════════════════════════════════════════════════════════════
    # UK FORDINGBRIDGE — three boys convicted of raping two girls, no prison
    # ══════════════════════════════════════════════════════════════════════════

    {
        "case_id":        "fordingbridge_uk_rape_boys_no_prison_2026",
        "violence_type":  "sexual_assault",
        "status":         "convicted",
        "summary": (
            "Three teenage boys — two aged 15 and one aged 14 at sentencing — "
            "were convicted on March 5, 2026 at Southampton Crown Court of "
            "raping two girls aged 14 and 15 in separate attacks in "
            "Fordingbridge, Hampshire, England, in November 2024 and "
            "January 2025. The boys were aged 13 and 14 at the time of "
            "the offences. They cannot be named under UK law. "
            "In the first attack (November 26, 2024), a 15-year-old girl "
            "had met one of the defendants online and travelled to meet him. "
            "She was taken to an underpass by the River Avon where she was "
            "raped by two of the defendants. "
            "In the second attack (January 17, 2025), a 14-year-old girl "
            "became separated from friends. She was threatened with a knife "
            "and forced to leave her mobile phone and AirTag in a shop so "
            "her location could not be tracked, before being taken to a "
            "secluded area. Two defendants took turns raping her while the "
            "others encouraged the assault and filmed it. The girls did not "
            "know each other. "
            "At sentencing, the judge told the defendants: 'I have to remember "
            "that you are not small adults. I should avoid criminalising these "
            "children unnecessarily.' "
            "All three boys were given Youth Rehabilitation Orders. The two "
            "older boys also received Intensive Supervision and Surveillance "
            "requirements. No boy received a custodial sentence. "
            "One 15-year-old was convicted of raping both girls and four counts "
            "of taking indecent images — filming the attacks. His sentence: "
            "a three-year Youth Rehabilitation Order. "
            "The UK government announced a review of the sentences within days "
            "of the ruling. Former Home Office minister Jess Phillips said "
            "the sentences were 'unduly lenient' and sent a 'bad message.' "
            "Conservative leader Kemi Badenoch said the defendants received "
            "'no punishment at all.' Hampshire Police and Crime Commissioner "
            "Donna Jones said: 'I'm deeply concerned these boys felt they could "
            "carry out such terrifying acts and share them online and not go "
            "to prison.' "
            "The victim of the first attack attended the sentencing, screened "
            "from the boys' view, and read her victim impact statement. "
            "Sources: Crown Prosecution Service; GB News; Inkl/British Brief; "
            "BBC News."
        ),
        "city":           "Southampton",
        "state":          "DC",
        "lat":            50.9097,
        "lng":            -1.4044,
        "source_url":     "https://www.cps.gov.uk/wessex/news/three-teenage-boys-sentenced-after-two-girls-raped-separate-attacks",
        "source_name":    "Crown Prosecution Service UK",
        "additional_sources": [
            {"url": "https://www.gbnews.com/news/three-teenagers-dodge-jail-sentenced",
             "name": "GB News"},
            {"url": "https://britbrief.co.uk/politics/scandals/government-reviews-lenient-rape-sentences-for-three-boys.html",
             "name": "British Brief"},
            {"url": "https://www.inkl.com/news/government-to-review-non-custodial-sentence-for-three-boys-convicted-of-rape",
             "name": "Inkl / The Independent"},
        ],
        "verified":       True,
        "is_public_figure": False,
        "date_incident":  "2024-11-26",
        "tab":            "global",
        "country":        "United Kingdom",
    },

    # ══════════════════════════════════════════════════════════════════════════
    # NC HB 1232 — Life at Fertilization constitutional amendment, May 2026
    # ══════════════════════════════════════════════════════════════════════════

    {
        "case_id":        "law_nc_hb1232_life_at_fertilization_2026",
        "violence_type":  "coercive_control",
        "status":         "congressional_record",
        "summary": (
            "North Carolina House Bill 1232, filed May 13, 2026 and sponsored "
            "by Republicans Keith Kidwell and Ben T. Moss Jr., proposes a "
            "constitutional amendment to Article I of the North Carolina "
            "Constitution declaring that human life begins at the moment of "
            "fertilization and that all such life shall be recognized as an "
            "individual person entitled to full legal protection from "
            "fertilization until natural death. "
            "The bill would hold any person 'willfully seeking to destroy "
            "the life of another, at any stage of life' accountable for "
            "first-degree murder or attempted murder — with no exception "
            "specified for rape, incest, or medical emergency in the bill "
            "text as filed. "
            "Subject to approval by a majority of voters in the 2026 general "
            "election, the amendment would place the question directly on the "
            "North Carolina ballot. The bill passed first reading on May 14, "
            "2026 and was referred to the Committee on Rules, Calendar, and "
            "Operations of the House. "
            "The practical implications: a woman who miscarries could "
            "potentially face investigation. A woman who takes emergency "
            "contraception could potentially face murder charges. IVF — "
            "which involves the creation and sometimes the disposal of "
            "fertilized embryos — would become legally precarious or "
            "impossible. A rape survivor seeking an abortion would be "
            "committing first-degree murder under this bill's language. "
            "This is one of more than 10 similar 'personhood' or "
            "'abortion as homicide' bills introduced across US states "
            "in 2025–2026. "
            "Sources: NC General Assembly; FastDemocracy; UNC Legislative "
            "Reporting Service."
        ),
        "city":           "Raleigh",
        "state":          "NC",
        "lat":            35.7796,
        "lng":            -78.6382,
        "source_url":     "https://www.ncleg.gov/BillLookUp/2025/H1232",
        "source_name":    "NC General Assembly — HB 1232",
        "additional_sources": [
            {"url": "https://lrs.sog.unc.edu/billsum/h-1232-2025-2026",
             "name": "UNC Legislative Reporting Service"},
            {"url": "https://fastdemocracy.com/bill-search/nc/2025-2026/bills/NCB00014772/",
             "name": "FastDemocracy"},
        ],
        "verified":       True,
        "is_public_figure": False,
        "date_incident":  "2026-05-13",
    },

    # ══════════════════════════════════════════════════════════════════════════
    # PERSONHOOD / ABORTION AS HOMICIDE BILLS — 10+ states, 2025–2026
    # ══════════════════════════════════════════════════════════════════════════

    {
        "case_id":        "stat_personhood_abortion_homicide_bills_2025_2026",
        "violence_type":  "coercive_control",
        "status":         "congressional_record",
        "summary": (
            "In 2025 and 2026, Republican lawmakers introduced bills in at "
            "least 14 US states that would classify abortion as homicide by "
            "granting full legal personhood to fertilized eggs from the moment "
            "of conception. States include: Georgia, Idaho, Indiana, Iowa, "
            "Kentucky, Missouri, North Dakota, Oklahoma, South Carolina, Texas, "
            "Illinois, South Dakota, Tennessee, and Montana. North Carolina "
            "filed HB 1232 on May 13, 2026. "
            "Under these bills: "
            "— A woman who has an abortion could be charged with first-degree "
            "murder and, in eight of the states, face the death penalty. "
            "— A woman who miscarries could face investigation for suspected "
            "murder. "
            "— A woman who takes emergency contraception could face murder "
            "charges. "
            "— IVF — which involves fertilizing multiple eggs and sometimes "
            "disposing of unused embryos — would be effectively banned or "
            "made criminally dangerous for providers and patients. "
            "— A rape survivor seeking an abortion would be committing murder "
            "under these bills, with no rape exception specified in most "
            "of the legislation as drafted. "
            "A 2025 survey by Pregnancy Justice and the National Women's Law "
            "Center found 59% of likely voters opposed granting legal rights "
            "to embryos once they understood the criminal implications. "
            "Most individual bills have failed or stalled in committee. "
            "Reproductive rights legal organizations warn the pattern signals "
            "a long-term campaign to establish fetal personhood in law — "
            "which, if adopted by a state and upheld by the Supreme Court, "
            "would constitute the most sweeping restriction on women's bodily "
            "autonomy in US history. "
            "The Georgetown O'Neill Institute documented at least nine states "
            "with active personhood legislation as of March 2025. "
            "Sources: Time Magazine; The Hill; The 19th News; Georgetown "
            "O'Neill Institute; Stateline; North Dakota Monitor; "
            "Center for Reproductive Rights."
        ),
        "city":           "Washington",
        "state":          "DC",
        "lat":            38.9072,
        "lng":            -77.0369,
        "source_url":     "https://time.com/7269263/bills-punishing-people-seeking-abortions/",
        "source_name":    "Time Magazine / Center for Reproductive Rights / Georgetown O'Neill Institute",
        "additional_sources": [
            {"url": "https://thehill.com/policy/healthcare/5217297-republican-state-lawmakers-abortion-homicide-bills/",
             "name": "The Hill"},
            {"url": "https://19thnews.org/2025/04/state-bills-abortion-homicide-pregnant-people/",
             "name": "The 19th News"},
            {"url": "https://oneill.law.georgetown.edu/publications/laws-that-would-make-abortion-homicide-in-nine-us-states-2/",
             "name": "Georgetown O'Neill Institute"},
            {"url": "https://www.newsfromthestates.com/article/unpopular-abortion-homicide-bills-wont-fade-concerning-reproductive-rights-advocates",
             "name": "News From The States"},
        ],
        "verified":       True,
        "is_public_figure": False,
        "date_incident":  "2025-01-01",
    },

]


def main():
    print("\n  [Medusa] Seeding sentencing and personhood records...\n")
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
