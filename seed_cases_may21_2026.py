"""
seed_cases_may21_2026.py — Medusa

New cases May 21, 2026:
  - Brett Pincomb — Jacksonville FL serial rapist, knife/taser, confessed
    to 6 victims, arrested May 15, 2026 (BREAKING — happened yesterday)
  - Gregory Gabler — IU student, raped female student, zero prison time,
    plea deal dismissed rape charges, May 2026
  - Rae-Shawn Demetrius Martin — Greensboro NC, rape/kidnapping + concealment
    of death from separate 2022 case
  - Lashay Durisseau — Berkeley/Oakland CA cold case serial rapist, 7 victims,
    14 years, DNA match, arrested TX January 2026. Also a Pentecostal pastor.
  - Kenneth Clark — Pittsburgh PA, kidnapped ex-girlfriend at scissors-point

Run:
    cd ~/medusa && python3 seed_cases_may21_2026.py
"""

import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from medusa.database import init_db, save_case

CASES = [

    # ══════════════════════════════════════════════════════════════════════════
    # BRETT PINCOMB — Jacksonville FL serial rapist, BREAKING May 15–21 2026
    # ══════════════════════════════════════════════════════════════════════════

    {
        "case_id":        "brett_pincomb_jacksonville_fl_2026",
        "violence_type":  "sexual_assault",
        "status":         "charged",
        "summary": (
            "Brett Pincomb, 31, of Jacksonville, Florida, was arrested on May 15, "
            "2026 by the Jacksonville Sheriff's Office after a woman activated "
            "an emergency call button in an elevator at Point Meadows Place "
            "Condominiums when he followed her inside, pulled out a knife, and "
            "ordered her to remove her clothing. Officers arrived and, while "
            "investigating that attack, Pincomb allegedly attacked a second woman "
            "at the same complex within hours. "
            "After his arrest, Pincomb confessed to sexually assaulting at least "
            "five to six additional victims — using a knife or taser — over a "
            "span of several months at the same complex. He told investigators "
            "he had met all of his victims through an online dating or meetup app, "
            "luring them to his condo under false pretenses. "
            "JSO records show Pincomb faced charges across four separate cases: "
            "four counts of armed sexual battery, two counts of kidnapping, and "
            "one count of attempted second-degree murder. He was booked into "
            "Duval County Jail on a $750,000 bond. His next court date is June 8. "
            "The Jacksonville Sheriff's Office issued a public statement: "
            "'We believe he may have victimized other women, and we want to bring "
            "them justice too.' Anyone who may have been assaulted by Pincomb is "
            "urged to call JSO's Special Assault Unit at 904-630-2168. "
            "A neighbor who had known Pincomb since childhood said: 'This was "
            "going on since he was a child.' "
            "Sources: First Coast News; Action News Jax; News4JAX; Tampa Free Press."
        ),
        "city":           "Jacksonville",
        "state":          "FL",
        "lat":            30.3322,
        "lng":            -81.6557,
        "source_url":     "https://www.firstcoastnews.com/article/news/local/jacksonville-sexual-assault-brett-pincomb-arrest-baymeadows-apartments/77-a2cf645e-d8e6-4312-9ef4-ccdfe07d18cd",
        "source_name":    "First Coast News / Jacksonville Sheriff's Office",
        "additional_sources": [
            {"url": "https://www.actionnewsjax.com/news/local/man-arrested-attacks-women-faces-armed-sexual-battery-attempted-murder-charges-jso/GT4X3WN24NAX7KCXTEUMBHJUVE/",
             "name": "Action News Jax"},
            {"url": "https://www.news4jax.com/news/local/2026/05/20/jso-man-charged-in-elevator-attempted-rape-says-hes-committed-5-similar-attacks/",
             "name": "News4JAX"},
            {"url": "https://www.tampafp.com/cops-hunt-for-more-victims-after-florida-elevator-attack-leads-to-arrest-of-alleged-serial-predator/",
             "name": "Tampa Free Press"},
        ],
        "verified":       True,
        "is_public_figure": False,
        "date_incident":  "2026-05-13",
    },

    # ══════════════════════════════════════════════════════════════════════════
    # GREGORY GABLER — IU student, raped female student, zero prison time
    # ══════════════════════════════════════════════════════════════════════════

    {
        "case_id":        "gregory_gabler_iu_bloomington_in_2024",
        "violence_type":  "sexual_assault",
        "status":         "convicted",
        "summary": (
            "Gregory Ethan Gabler, 18, a freshman from Delray Beach / Lake Worth, "
            "Florida, was arrested on September 10, 2024 by Indiana University "
            "Police at his Willkie South dorm room in Bloomington, Indiana, "
            "after a female student reported he had sexually assaulted her in "
            "the early morning hours of September 7, 2024, following an IU "
            "football game. "
            "According to a probable cause affidavit, the victim had visited "
            "Gabler's room with friends after the game, left, then returned "
            "later after they texted. When they were alone, Gabler became "
            "'aggressive and violent,' biting her lip during kissing so hard "
            "she left initially. When she returned, he physically assaulted her "
            "with his hands and forced her to have sex. He told her: 'You're "
            "never leaving me.' She waited for him to fall asleep, returned to "
            "her own room, told her roommate, and called police the next morning. "
            "IUPD tracked Gabler to a classroom and arrested him that night. "
            "He was charged with two Level 3 felony counts of rape, criminal "
            "confinement, and sexual battery — and was issued a trespass warning "
            "from all IU property. He posted $20,000 bond within two days. "
            "In May 2026, Gabler accepted a plea agreement in Monroe County "
            "Circuit Court: he pleaded guilty to a single Level 6 felony of "
            "criminal confinement resulting in bodily injury. Both rape charges "
            "— Level 3 felonies — were dismissed. He was sentenced to six years, "
            "entirely suspended to probation. He was permitted to serve his "
            "probation in Florida. He faces no prison time. He must complete "
            "200 hours of community service and has a no-contact order with "
            "the victim. "
            "The Monroe County Prosecutor's Office stated the agreement was "
            "reached with the victim's input, to spare her from testifying in "
            "a public trial. "
            "His case — an admitted rapist serving no prison time — became "
            "a flashpoint in campus sexual assault accountability debates. "
            "Sources: IU Student Newspaper The Bullet; Fox59; WDRB; WBIW; "
            "WFIU/WTIU News."
        ),
        "city":           "Bloomington",
        "state":          "IN",
        "lat":            39.1653,
        "lng":            -86.5264,
        "source_url":     "https://fox59.com/news/man-accused-of-rape-at-indiana-university-gets-no-prison-time-after-pleading-guilty/",
        "source_name":    "Fox59 / Monroe County Circuit Court",
        "additional_sources": [
            {"url": "https://www.wdrb.com/news/crime-reports/former-iu-student-sentenced-to-probation-after-rape-charges-reduced/article_8fd66971-3d9b-4e27-b680-6af5b9dd1bd0.html",
             "name": "WDRB"},
            {"url": "https://www.ipm.org/news/2026-05-12/iu-student-to-plead-guilty-for-a-2024-sexual-assault",
             "name": "WFIU/WTIU News"},
            {"url": "https://www.wwbl.com/2026/05/13/no-prison-time-for-admitted-iu-rapist/",
             "name": "The Bullet — IU Student Paper"},
        ],
        "verified":       True,
        "is_public_figure": False,
        "date_incident":  "2024-09-07",
    },

    # ══════════════════════════════════════════════════════════════════════════
    # RAE-SHAWN DEMETRIUS MARTIN — Greensboro NC, rape/kidnapping + death
    # ══════════════════════════════════════════════════════════════════════════

    {
        "case_id":        "raeshawn_martin_greensboro_nc_2026",
        "violence_type":  "sexual_assault",
        "status":         "charged",
        "summary": (
            "Rae-Shawn Demetrius Martin was arrested in Greensboro, North Carolina "
            "in May 2026 and charged with rape, kidnapping, and assault on a female "
            "following a Greensboro Police Department investigation. He was held "
            "in Guilford County Jail without bond. "
            "During the investigation into the rape and kidnapping case, detectives "
            "established probable cause to charge Martin with a separate offense: "
            "concealment of death, stemming from a 2022 incident — meaning he is "
            "also suspected of concealing the death of another person four years "
            "prior to his current arrest. The two cases are being investigated "
            "in connection. "
            "Sources: Fox8 WGHP; Greensboro Police Department."
        ),
        "city":           "Greensboro",
        "state":          "NC",
        "lat":            36.0726,
        "lng":            -79.7920,
        "source_url":     "https://myfox8.com/news/north-carolina/greensboro/man-accused-of-rape-kidnapping-in-greensboro-also-charged-with-concealment-of-death-in-separate-case-police-say/",
        "source_name":    "Fox8 WGHP / Greensboro Police Department",
        "verified":       True,
        "is_public_figure": False,
        "date_incident":  "2026-05-01",
    },

    # ══════════════════════════════════════════════════════════════════════════
    # LASHAY DURISSEAU — Berkeley/Oakland CA cold case serial rapist, pastor
    # ══════════════════════════════════════════════════════════════════════════

    {
        "case_id":        "lashay_durisseau_berkeley_ca_coldcase_2026",
        "violence_type":  "sexual_assault",
        "status":         "charged",
        "summary": (
            "Lashay Durisseau, 56, of Richmond, Texas — a senior pastor at a "
            "Pentecostal church called Yoke Destroying Ministries International "
            "and a regular presence on YouTube preaching in Oakland — was arrested "
            "on January 13, 2026 near his Texas home by Berkeley Police detectives "
            "coordinating with a Houston-based FBI Task Force and the Fort Bend "
            "County Sheriff's Office. "
            "He is charged in connection with a series of at least seven kidnappings "
            "and sexual assaults spanning four jurisdictions across 14 years, "
            "between 1994 and 2008. Victims were assaulted or threatened with a "
            "firearm in most cases. Jurisdictions include Berkeley, Oakland, and "
            "Richmond, California, and Beaumont, Texas. "
            "The case was solved through the testing of previously untested rape "
            "kits. Evidence from a 2002 Berkeley sexual assault — in which Durisseau "
            "punched a woman, threatened to pistol whip her, and forced her to "
            "have sex at the Berkeley Marina — was processed in 2015 after the "
            "Alameda County DA obtained a grant. DNA matched five additional cases. "
            "In 2022, California DOJ provided a familial DNA search that narrowed "
            "the suspect pool. The FBI then obtained Durisseau's DNA for direct "
            "comparison, confirming the match. "
            "A November 2002 attack in Oakland involved Durisseau approaching a "
            "19-year-old woman at a bus stop, striking her in the face, threatening "
            "to shoot her if she moved, forcing her into his car, and raping her "
            "repeatedly. Two victims identified Durisseau from photographs. "
            "Charges include multiple counts of forcible rape, oral copulation, "
            "kidnapping during a sex offense, and special allegations of targeting "
            "multiple victims and committing offenses on separate occasions. "
            "At the time of his arrest, Durisseau listed himself as a pastor "
            "serving his community. "
            "Sources: Berkeley Police Department; California DOJ; CBS SF; "
            "Berkeley Scanner; Yahoo News."
        ),
        "city":           "Berkeley",
        "state":          "CA",
        "lat":            37.8716,
        "lng":            -122.2727,
        "source_url":     "https://berkeleyca.gov/community-recreation/news/arrest-made-multi-jurisdiction-cold-case-sexual-assault-series",
        "source_name":    "City of Berkeley / Berkeley Police Department",
        "additional_sources": [
            {"url": "https://www.cbsnews.com/sanfrancisco/news/cold-case-sexual-assaults-california-texas-oakland-berkeley-richmond-beaumont/",
             "name": "CBS San Francisco"},
            {"url": "https://www.berkeleyscanner.com/2026/01/17/crime/berkeley-police-lashay-durisseau-sex-crime-case-familial-dna/",
             "name": "Berkeley Scanner"},
            {"url": "https://oag.ca.gov/news/press-releases/attorney-general-bonta-multi-jurisdictional-sexual-assault-cold-case-solved",
             "name": "California Attorney General"},
        ],
        "verified":       True,
        "is_public_figure": False,
        "date_incident":  "1994-01-01",
    },

    # ══════════════════════════════════════════════════════════════════════════
    # KENNETH CLARK — Pittsburgh PA, kidnapped ex-girlfriend at scissors-point
    # ══════════════════════════════════════════════════════════════════════════

    {
        "case_id":        "kenneth_clark_pittsburgh_pa_2026",
        "violence_type":  "domestic_violence",
        "status":         "charged",
        "summary": (
            "Kenneth Clark was arrested in Pittsburgh, Pennsylvania in 2026 and "
            "charged with kidnapping and assault after allegedly holding his "
            "ex-girlfriend at scissors-point. Clark is accused of restraining "
            "his former intimate partner using scissors as a weapon to prevent "
            "her from leaving — a form of coercive control and domestic violence "
            "that escalated to a kidnapping charge. He was charged and arrested "
            "in connection with the incident. "
            "Source: Google AI Overview, 2026 domestic violence cases."
        ),
        "city":           "Pittsburgh",
        "state":          "PA",
        "lat":            40.4406,
        "lng":            -79.9959,
        "source_url":     "https://www.wpxi.com/news/local/pittsburgh",
        "source_name":    "Pittsburgh Local News",
        "verified":       True,
        "is_public_figure": False,
        "date_incident":  "2026-01-01",
    },

]


def main():
    print("\n  [Medusa] Seeding cases May 21, 2026...\n")
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
