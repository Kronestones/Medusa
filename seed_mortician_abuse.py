"""
seed_mortician_abuse.py — Medusa

Sexual abuse of female corpses by morgue workers, funeral home
employees, and others. Documents the pattern, named cases, and
the critical legal gap: in many US states, necrophilia was not
a crime until the 2000s — and some states still have no law.

Cases:
  - Kenneth Douglas — Hamilton County OH morgue, up to 100 female
    corpses, 1976–1992
  - Domonique Smith — Columbus GA funeral home
  - Wisconsin necrophilia legal gap — charges dropped, no law existed
  - Stat: legal gap overview across US states

Run:
    cd ~/medusa && python3 seed_mortician_abuse.py
"""

import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from medusa.database import init_db, save_case

CASES = [

    # ══════════════════════════════════════════════════════════════════════════
    # KENNETH DOUGLAS — Hamilton County OH morgue, up to 100 female corpses
    # ══════════════════════════════════════════════════════════════════════════

    {
        "case_id":        "kenneth_douglas_hamilton_county_morgue_oh",
        "violence_type":  "sexual_assault",
        "status":         "convicted",
        "summary": (
            "Kenneth Douglas, a morgue attendant at the Hamilton County "
            "morgue in Cincinnati, Ohio from 1976 to 1992, admitted in a "
            "2014 deposition that he may have sexually abused up to 100 female "
            "corpses during his 16-year tenure — often while drunk or high "
            "on crack cocaine during overnight shifts. Supervisors were aware "
            "he had been drinking on the job and having sex with live women "
            "inside the morgue, but no action was taken. "
            "His crimes came to light only through advances in DNA technology. "
            "The first case was confirmed in 2007 when Douglas's DNA — obtained "
            "via a mandatory sample after a drug trafficking conviction — matched "
            "semen found on the body of Karen Range, 19, a murder victim whose "
            "body had been in the morgue in 1982. David Steffen had been on "
            "death row since 1983 for Range's murder including a rape conviction "
            "— but the DNA proved he had not raped her. Douglas had. Steffen's "
            "rape conviction was vacated. "
            "Douglas was convicted in 2008 of gross abuse of a corpse and "
            "sentenced to three years. In 2009, while serving that sentence, "
            "DNA linked him to two additional female corpses — both women "
            "whose bodies had passed through the Hamilton County morgue in 1991. "
            "He pleaded guilty to both additional counts and received consecutive "
            "three-year sentences. "
            "The families of his victims — women who had died violently and "
            "whose families trusted the state morgue to treat them with dignity "
            "— sued Hamilton County. The Sixth Circuit Court of Appeals ruled "
            "in 2014 that the lawsuits could proceed, finding that Douglas's "
            "supervisors had been aware of his behavior and failed to act. "
            "Douglas served a total of approximately nine years. "
            "The women he abused were murder victims, accident victims, and "
            "others who had died suddenly — brought to the morgue because "
            "they had no one left to protect them. "
            "Sources: Prison Legal News; NBC News; Newsweek."
        ),
        "city":           "Cincinnati",
        "state":          "OH",
        "lat":            39.1031,
        "lng":            -84.5120,
        "source_url":     "https://www.prisonlegalnews.org/news/2016/sep/2/death-penalty-case-reveals-morgue-worker-had-sex-100-female-corpses/",
        "source_name":    "Prison Legal News / NBC News",
        "additional_sources": [
            {"url": "https://www.newsweek.com/florida-funeral-home-worker-dead-corpse-abuse-allegations-1774637",
             "name": "Newsweek"},
            {"url": "https://www.nbcnews.com/news/amp/wbna29414767",
             "name": "NBC News — New charges in corpse abuse cases"},
        ],
        "verified":       True,
        "is_public_figure": False,
        "date_incident":  "1976-01-01",
    },

    # ══════════════════════════════════════════════════════════════════════════
    # DOMONIQUE SMITH — Columbus GA funeral home, broke in and assaulted body
    # ══════════════════════════════════════════════════════════════════════════

    {
        "case_id":        "domonique_smith_columbus_ga_funeral_home",
        "violence_type":  "sexual_assault",
        "status":         "convicted",
        "summary": (
            "Domonique Smith, 26, was charged with necrophilia in Columbus, "
            "Georgia after breaking into Hill Watson Peoples Funeral Service "
            "and sexually assaulting the body of a woman whose remains were "
            "in the funeral home's care. Police discovered the sexual assault "
            "while investigating Smith for stealing a bicycle from the funeral "
            "home. Smith pleaded guilty to burglary and remained in custody. "
            "The funeral director stated the business looks for the best "
            "protection and security for families — but the case illustrates "
            "that funeral homes, by their nature, house the bodies of vulnerable "
            "women with limited security and overnight exposure. "
            "Sources: Fox News; Columbus Ledger-Enquirer."
        ),
        "city":           "Columbus",
        "state":          "GA",
        "lat":            32.4610,
        "lng":            -84.9877,
        "source_url":     "https://www.foxnews.com/us/man-charged-with-having-sex-with-corpse-in-georgia-funeral-home.amp",
        "source_name":    "Fox News / Columbus Ledger-Enquirer",
        "verified":       True,
        "is_public_figure": False,
        "date_incident":  "2014-01-01",
    },

    # ══════════════════════════════════════════════════════════════════════════
    # WISCONSIN LEGAL GAP — charges dropped because no necrophilia law existed
    # ══════════════════════════════════════════════════════════════════════════

    {
        "case_id":        "wisconsin_necrophilia_legal_gap_2006",
        "violence_type":  "sexual_assault",
        "status":         "charges_declined",
        "summary": (
            "In September 2006, twins Nicholas and Alexander Grunke, 20, and "
            "their companion Dustin Radke, 20, were arrested in Wisconsin after "
            "attempting to dig up the body of a 20-year-old woman who had died "
            "in a motorcycle accident days earlier on August 27. They had seen "
            "her obituary photograph and decided to exhume her body for sexual "
            "purposes. A caller reported suspicious activity at the cemetery "
            "and deputies found someone had dug down to her burial vault. "
            "Prosecutors charged the three men with attempted sexual assault. "
            "Circuit Judge George Curry dismissed the sexual assault charges "
            "on the grounds that Wisconsin had no law against necrophilia — "
            "and therefore no law had been broken. The men faced only lesser "
            "charges of criminal damage to property and attempted break-in "
            "of a burial vault. "
            "The case exposed a critical legal gap: in 2006, the majority "
            "of US states had no specific statute criminalizing the sexual "
            "assault of a corpse. A dead woman's body had no legal protection "
            "from sexual violation in most of the country. "
            "Wisconsin subsequently passed a necrophilia law. "
            "The victim — a young woman killed in an accident — had her grave "
            "targeted by men who had seen her photo in her obituary. Her family "
            "had no legal recourse for the attempted violation of her body. "
            "Sources: Fox News; Whittier Law Review — Defiling the Dead: "
            "Necrophilia and the Law."
        ),
        "city":           "Madison",
        "state":          "WI",
        "lat":            43.0731,
        "lng":            -89.4012,
        "source_url":     "https://www.foxnews.com/story/sex-assault-charges-dropped-in-wis-necrophilia-case.amp",
        "source_name":    "Fox News / Wisconsin Circuit Court Records",
        "additional_sources": [
            {"url": "https://digitalcommons.law.scu.edu/cgi/viewcontent.cgi?article=1099&context=facpubs",
             "name": "Whittier Law Review — Defiling the Dead: Necrophilia and the Law"},
        ],
        "verified":       True,
        "is_public_figure": False,
        "date_incident":  "2006-09-02",
    },

    # ══════════════════════════════════════════════════════════════════════════
    # LEGAL GAP STAT — necrophilia laws across US states
    # ══════════════════════════════════════════════════════════════════════════

    {
        "case_id":        "stat_necrophilia_legal_gap_us_states",
        "violence_type":  "sexual_assault",
        "status":         "congressional_record",
        "summary": (
            "For most of American legal history, sexually assaulting a female "
            "corpse was not a crime in the majority of US states. A dead "
            "woman's body had no legal protection from sexual violation. "
            "The legal theory was that a corpse is not a person and therefore "
            "cannot be raped — and without a specific necrophilia statute, "
            "prosecutors had no charge to bring. "
            "As documented in the Whittier Law Review's analysis 'Defiling "
            "the Dead: Necrophilia and the Law,' courts across multiple "
            "jurisdictions held that a corpse cannot be raped because rape "
            "requires a living victim — meaning that if a victim died during "
            "or before the sexual assault, rape charges could not stand. "
            "The Alabama Court of Criminal Appeals ruled that if the intent "
            "to have sexual intercourse arose after the victim was already "
            "dead, 'there could be no forcible compulsion of the victim to "
            "engage in sexual intercourse' — and therefore no rape. "
            "Individual states have passed necrophilia statutes at different "
            "times, largely in response to specific cases: Wisconsin after "
            "the Grunke case (2006); states across the country through the "
            "1990s and 2000s. As of 2020, necrophilia remains legal or is "
            "covered only by general 'abuse of a corpse' statutes carrying "
            "minor penalties in several states. "
            "The women whose bodies are violated in morgues and funeral homes "
            "are overwhelmingly there because they died violently — murder "
            "victims, assault victims, accident victims. The legal system's "
            "failure to protect their bodies after death is an extension of "
            "its failure to protect them during life. "
            "Sources: Whittier Law Review; Prison Legal News; Newsweek."
        ),
        "city":           "Washington",
        "state":          "DC",
        "lat":            38.9072,
        "lng":            -77.0369,
        "source_url":     "https://digitalcommons.law.scu.edu/cgi/viewcontent.cgi?article=1099&context=facpubs",
        "source_name":    "Whittier Law Review — Defiling the Dead: Necrophilia and the Law",
        "verified":       True,
        "is_public_figure": False,
        "date_incident":  "2006-01-01",
    },

]


def main():
    print("\n  [Medusa] Seeding mortician/morgue abuse cases...\n")
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
