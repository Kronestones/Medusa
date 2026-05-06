#!/usr/bin/env python3
"""
seed_trafficking_ice.py — Truck stop sex trafficking corridors and
pregnant/minor girls in ICE and ORR custody.

Sources: DOJ, DHS OIG, Polaris Project, Senate investigations,
investigative journalism, court records.

Run: python3 seed_trafficking_ice.py
"""

from medusa.database import init_db, save_case
from medusa.record import normalize_record

RECORDS = [

    # ── TRUCK STOP TRAFFICKING ────────────────────────────────────────────────
    {
        "summary": (
            "Truck Stop Sex Trafficking — National Scale. The Polaris Project "
            "and FBI have documented that truck stops along major US interstate "
            "corridors are among the most common venues for sex trafficking in "
            "America. Long-haul truckers are both primary consumers and, in some "
            "cases, transporters of trafficking victims. The Truckers Against "
            "Trafficking organization estimates that tens of thousands of "
            "trafficking victims pass through truck stops annually. Girls as "
            "young as 11 and 12 have been recovered from truck stop trafficking "
            "operations. The I-10, I-20, I-40, I-75, and I-95 corridors are "
            "particularly documented. Truck stops operated by Flying J, Pilot, "
            "and Love's have been sites of documented trafficking arrests. "
            "Victims are often runaways, aged-out foster youth, and girls from "
            "low-income families who are recruited by traffickers with promises "
            "of food, shelter, and belonging — then controlled through debt "
            "bondage, violence, and addiction."
        ),
        "city": "Washington", "state": "DC",
        "lat": 38.9072, "lng": -77.0369,
        "date_incident": "2023-01-01",
        "violence_type": "trafficking",
        "status": "documented",
        "source_url": "https://polarisproject.org/wp-content/uploads/2019/09/Polaris-Typology-of-Modern-Slavery.pdf",
        "source_name": "Polaris Project — Typology of Modern Slavery / Truckers Against Trafficking",
        "verified": True,
        "is_public_figure": False,
    },
    {
        "summary": (
            "I-20 Corridor — Atlanta to Texas Trafficking Pipeline. The I-20 "
            "interstate corridor from Atlanta, Georgia through Alabama, Mississippi, "
            "Louisiana, and into Texas is one of the most heavily documented "
            "sex trafficking routes in the United States. Atlanta is a major "
            "trafficking hub — the FBI has ranked it among the top cities for "
            "child sex trafficking. Girls are recruited in Atlanta and moved "
            "west along I-20 through truck stops, motels, and rest areas. "
            "The Super Bowl effect — documented spikes in trafficking around "
            "major sporting events — has been observed repeatedly along this "
            "corridor. Operation Cross Country, the FBI's annual anti-trafficking "
            "operation, has recovered hundreds of children along I-20 corridor "
            "states. Traffickers use apps including Instagram, Snapchat, and "
            "Facebook to recruit girls, then move them along the corridor "
            "to avoid detection by local law enforcement."
        ),
        "city": "Atlanta", "state": "GA",
        "lat": 33.7490, "lng": -84.3880,
        "date_incident": "2023-01-01",
        "violence_type": "trafficking",
        "status": "documented",
        "source_url": "https://www.fbi.gov/investigate/violent-crime/human-trafficking",
        "source_name": "FBI — Operation Cross Country / Polaris Project I-20 Corridor",
        "verified": True,
        "is_public_figure": False,
    },
    {
        "summary": (
            "Truck Stop Trafficking — Girls Recovered in FBI Operations. "
            "FBI Operation Cross Country — an annual national anti-trafficking "
            "operation — has recovered over 6,000 child sex trafficking victims "
            "since 2008, many from truck stops, motels, and rest areas along "
            "interstate highways. In a single 2019 operation, 103 children "
            "were recovered across 38 states in one week. The youngest victims "
            "recovered have been as young as 11. Traffickers target girls at "
            "truck stops because the constant turnover of customers provides "
            "anonymity, cash transactions leave no record, and truckers travel "
            "between jurisdictions making prosecution difficult. Girls are "
            "sometimes kept in the trucks themselves — moving constantly across "
            "state lines. Many victims are not identified as trafficking victims "
            "by law enforcement and are instead arrested for prostitution — "
            "criminalizing the trafficked child rather than the trafficker."
        ),
        "city": "Washington", "state": "DC",
        "lat": 38.9072, "lng": -77.0369,
        "date_incident": "2019-10-01",
        "violence_type": "trafficking",
        "status": "documented",
        "source_url": "https://www.fbi.gov/news/stories/operation-cross-country-2019-results",
        "source_name": "FBI — Operation Cross Country 2019 Results",
        "verified": True,
        "is_public_figure": False,
    },
    {
        "summary": (
            "Criminalization of Trafficked Girls — Arrested Instead of Protected. "
            "A 2014 report by the Shared Hope International found that in most "
            "US states, children who are trafficked for sex are still arrested "
            "and prosecuted for prostitution — despite being victims of a federal "
            "crime. Girls as young as 12 have been arrested for prostitution "
            "at truck stops while their traffickers received lesser charges or "
            "walked free. The Safe Harbor movement has pushed for laws protecting "
            "trafficked minors from prosecution — but as of 2023, fewer than "
            "half of US states have comprehensive safe harbor protections. "
            "Black girls are disproportionately arrested rather than identified "
            "as victims — a pattern documented by the Georgetown Law Center "
            "on Poverty and Inequality as the 'adultification' of Black girls, "
            "in which Black children are perceived as older, less innocent, "
            "and less deserving of protection than white children of the same age."
        ),
        "city": "Washington", "state": "DC",
        "lat": 38.9072, "lng": -77.0369,
        "date_incident": "2023-01-01",
        "violence_type": "trafficking",
        "status": "documented",
        "source_url": "https://sharedhope.org/what-we-do/bring-justice/reportcards/",
        "source_name": "Shared Hope International — Protected Innocence Challenge / Georgetown Adultification Report",
        "verified": True,
        "is_public_figure": False,
    },
    {
        "summary": (
            "Love's Travel Stop — Documented Trafficking Arrests. Love's Travel "
            "Stops, one of the largest truck stop chains in the United States "
            "with over 600 locations, has been the site of multiple documented "
            "sex trafficking arrests. In 2021, a Love's location in Oklahoma "
            "was the site of a trafficking operation involving minors. In Texas, "
            "multiple Love's locations along I-10 and I-20 have been documented "
            "in FBI and Texas DPS trafficking investigations. Love's has "
            "partnered with Truckers Against Trafficking to train employees "
            "to recognize trafficking — but advocates note that training alone "
            "is insufficient without structural changes to how trafficking "
            "victims are identified and reported. The truck stop industry "
            "generates billions in annual revenue from long-haul truckers "
            "while the exploitation of trafficking victims at these locations "
            "has gone largely unaddressed as a corporate responsibility issue."
        ),
        "city": "Oklahoma City", "state": "OK",
        "lat": 35.4676, "lng": -97.5164,
        "date_incident": "2021-01-01",
        "violence_type": "trafficking",
        "status": "documented",
        "source_url": "https://truckersagainsttrafficking.org/",
        "source_name": "Truckers Against Trafficking / Texas DPS Human Trafficking Reports",
        "verified": True,
        "is_public_figure": False,
    },

    # ── PREGNANT GIRLS IN ICE / ORR CUSTODY ──────────────────────────────────
    {
        "summary": (
            "Pregnant Unaccompanied Minors in ORR Custody — Systematic Failures. "
            "The Office of Refugee Resettlement (ORR), which houses unaccompanied "
            "migrant children, has documented hundreds of pregnant girls in its "
            "custody annually — some as young as 12 and 13. Many are pregnant "
            "as a result of rape during their journey to the US or rape in "
            "their home countries. A 2018 Senate investigation found that ORR "
            "shelters were systematically denying pregnant minors access to "
            "abortion — even in cases of rape — under a policy implemented by "
            "the Trump administration. The ACLU filed suit in Garza v. Hargan "
            "(2017) on behalf of a 17-year-old identified as 'Jane Doe' who "
            "was detained in a Texas ORR facility and denied abortion access "
            "despite being a rape victim. The DC Circuit ruled in her favor. "
            "The policy of blocking abortion access for detained pregnant minors "
            "continued in various forms through multiple administrations."
        ),
        "city": "Washington", "state": "DC",
        "lat": 38.9072, "lng": -77.0369,
        "date_incident": "2018-01-01",
        "violence_type": "coercive_control",
        "status": "documented",
        "source_url": "https://www.aclu.org/cases/garza-v-hargan",
        "source_name": "ACLU — Garza v. Hargan / Senate ORR Investigation 2018",
        "verified": True,
        "is_public_figure": False,
    },
    {
        "summary": (
            "Jane Doe — 17-Year-Old Rape Victim Denied Abortion in ORR Custody, "
            "Texas, 2017. A 17-year-old unaccompanied minor from Central America, "
            "identified only as Jane Doe, was detained in a federally funded "
            "shelter in Texas after crossing the border. She was pregnant as "
            "a result of rape. She obtained a judicial bypass in Texas court — "
            "meeting every legal requirement for an abortion. The Trump "
            "administration's ORR director Scott Lloyd personally intervened "
            "to block her from leaving the facility to obtain the procedure, "
            "took her to an anti-abortion pregnancy center against her will, "
            "and notified her parents in her home country — people she had "
            "fled — without her consent. She was held for weeks while the "
            "ACLU fought in federal court. She eventually obtained the abortion "
            "after a DC Circuit ruling. Scott Lloyd was found to have "
            "personally intervened in at least 18 similar cases."
        ),
        "city": "San Antonio", "state": "TX",
        "lat": 29.4241, "lng": -98.4936,
        "date_incident": "2017-09-01",
        "violence_type": "coercive_control",
        "status": "documented",
        "source_url": "https://www.aclu.org/cases/garza-v-hargan",
        "source_name": "ACLU — Garza v. Hargan / Jane Doe ORR Case",
        "verified": True,
        "is_public_figure": False,
    },
    {
        "summary": (
            "Scott Lloyd — ORR Director Who Personally Blocked Abortions for "
            "Detained Migrant Girls. Scott Lloyd served as director of the "
            "Office of Refugee Resettlement under the Trump administration "
            "from 2017-2018. Internal documents obtained through FOIA requests "
            "revealed that Lloyd personally tracked the pregnancies of detained "
            "unaccompanied minors in ORR custody and intervened to block "
            "abortion access — including in cases of rape. He required staff "
            "to report any pregnant minor to him directly. He directed staff "
            "to take girls to anti-abortion pregnancy centers. He contacted "
            "parents in home countries without the girls' consent — in some "
            "cases notifying families the girls had fled from. Documents "
            "showed he intervened in at least 18 cases. A federal court "
            "found his actions unconstitutional. He faced no criminal charges. "
            "The girls he targeted were rape victims, some as young as 12, "
            "held in federal custody with no family and no legal representation."
        ),
        "city": "Washington", "state": "DC",
        "lat": 38.9072, "lng": -77.0369,
        "date_incident": "2017-10-01",
        "violence_type": "coercive_control",
        "status": "documented",
        "source_url": "https://www.aclu.org/news/immigrants-rights/internal-documents-show-trump-officials-blocked-abortions-undocumented-minors",
        "source_name": "ACLU — FOIA Documents: Scott Lloyd ORR Abortion Interference",
        "verified": True,
        "is_public_figure": True,
    },
    {
        "summary": (
            "Pregnant Girls in HHS Shelters — Raped in US Custody. A 2018 "
            "Senate Permanent Subcommittee on Investigations report found that "
            "the Department of Health and Human Services had placed unaccompanied "
            "migrant children — including girls — with sponsors who then "
            "trafficked them. Some girls placed with sponsors were found to "
            "have become pregnant in the US after placement — indicating sexual "
            "abuse by their sponsors. HHS had conducted inadequate background "
            "checks on sponsors and had lost contact with thousands of children "
            "after placement. A 2019 follow-up found HHS still could not "
            "account for the whereabouts of 1,488 migrant children. Girls who "
            "entered the US fleeing sexual violence were placed in situations "
            "where they were sexually violated again — this time by adults "
            "the US government had vetted and approved as safe."
        ),
        "city": "Washington", "state": "DC",
        "lat": 38.9072, "lng": -77.0369,
        "date_incident": "2018-04-26",
        "violence_type": "trafficking",
        "status": "documented",
        "source_url": "https://www.hsgac.senate.gov/imo/media/doc/2018-01-28%20Majority%20Staff%20Report%20-%20Protecting%20Unaccompanied%20Alien%20Children%20from%20Trafficking%20and%20Other%20Abuses.pdf",
        "source_name": "Senate PSI — Protecting Unaccompanied Children from Trafficking 2018",
        "verified": True,
        "is_public_figure": False,
    },
    {
        "summary": (
            "Sexual Abuse of Migrant Children in US Custody — 4,500 Complaints. "
            "Between 2014 and 2018, the Department of Justice received over "
            "4,500 complaints of sexual abuse of unaccompanied migrant children "
            "in US government custody — in ORR shelters and HHS-contracted "
            "facilities. The complaints included abuse by staff, guards, older "
            "residents, and sponsors. A 2019 New York Times investigation found "
            "that federal contractors running the shelters were not required to "
            "report all abuse allegations to law enforcement — only to HHS. "
            "Dozens of complaints were never investigated. Girls reported being "
            "touched by male staff during searches, being watched while "
            "showering, and being coerced into sexual contact. The youngest "
            "victims documented were under 10 years old. The contractors "
            "running these facilities — including Southwest Key Programs and "
            "Comprehensive Health Services — received billions in federal "
            "contracts while abuse complaints mounted."
        ),
        "city": "Washington", "state": "DC",
        "lat": 38.9072, "lng": -77.0369,
        "date_incident": "2019-02-27",
        "violence_type": "child_abuse",
        "status": "documented",
        "source_url": "https://www.nytimes.com/2019/02/27/us/immigrant-children-sexual-abuse.html",
        "source_name": "NYT — Sexual Abuse of Migrant Children in US Custody 2019",
        "verified": True,
        "is_public_figure": False,
    },
    {
        "summary": (
            "Clint, Texas Border Patrol Station — Children in Squalor, 2019. "
            "In June 2019, attorneys and doctors who visited the Border Patrol "
            "station in Clint, Texas found hundreds of migrant children — "
            "including infants and toddlers — being held in conditions of "
            "extreme neglect. Children were sleeping on concrete floors, "
            "going without showers for weeks, and caring for younger children "
            "without adult supervision. A 2-year-old girl was found caring "
            "for a 1-year-old infant. Girls reported being held in cells so "
            "crowded they could not lie down. There was inadequate food, "
            "water, and medical care. A teenage girl who had given birth "
            "was held with her newborn in these conditions. The conditions "
            "were described by medical professionals as dangerous and "
            "potentially life-threatening. Border Patrol initially disputed "
            "the reports — then internal documents confirmed them. No "
            "officials were held accountable."
        ),
        "city": "Clint", "state": "TX",
        "lat": 31.5918, "lng": -106.2238,
        "date_incident": "2019-06-17",
        "violence_type": "child_abuse",
        "status": "documented",
        "source_url": "https://www.aclu.org/news/immigrants-rights/inside-clint-texas-child-detention-center",
        "source_name": "ACLU — Inside Clint Texas Detention Center / Associated Press",
        "verified": True,
        "is_public_figure": False,
    },
    {
        "summary": (
            "Migrant Girls Raped on the Journey — Contraception as Standard "
            "Practice. The rape of migrant women and girls during the journey "
            "to the US is so prevalent and expected that humanitarian "
            "organizations along migration routes distribute contraception "
            "as standard practice. Doctors Without Borders has documented "
            "that in some years, up to 31% of migrant women and girls "
            "traveling through Mexico report being sexually assaulted during "
            "the journey — primarily by gang members, cartel members, "
            "and corrupt officials. Girls traveling alone face the highest "
            "risk. Some are kidnapped and held in sexual slavery for extended "
            "periods before being released or escaping. Those who arrive "
            "at the US border are often already survivors of sexual violence "
            "— and then enter a detention system that has documented its "
            "own sexual abuse problem. The contraception distribution is "
            "known colloquially as 'the depo shot' — a grim acknowledgment "
            "that rape is not a possibility but a near-certainty."
        ),
        "city": "El Paso", "state": "TX",
        "lat": 31.7619, "lng": -106.4850,
        "date_incident": "2023-01-01",
        "violence_type": "rape",
        "status": "documented",
        "source_url": "https://www.msf.org/forced-to-flee-central-america-broken-journey",
        "source_name": "Doctors Without Borders — Forced to Flee: Central America's Broken Journey",
        "verified": True,
        "is_public_figure": False,
    },
    {
        "summary": (
            "Southwest Key Programs — Billion-Dollar Contractor, Documented "
            "Abuse. Southwest Key Programs is one of the largest operators "
            "of federally contracted shelters for unaccompanied migrant "
            "children — receiving over $1 billion in federal contracts. "
            "Between 2014 and 2019, Southwest Key facilities were the site "
            "of multiple documented sexual abuse incidents involving staff "
            "and children. In 2018, a Southwest Key employee in Arizona was "
            "arrested for sexually abusing a 14-year-old girl in his care. "
            "In 2019, a former Southwest Key employee in Texas was charged "
            "with sexually abusing multiple minors in a shelter. A Senate "
            "investigation found Southwest Key had inadequate background "
            "check procedures and had hired employees with prior criminal "
            "records. Despite documented abuse, Southwest Key continued "
            "to receive federal contracts. Its CEO Juan Sanchez earned "
            "$3.6 million in 2016 — while children in his facilities "
            "were being sexually abused."
        ),
        "city": "Austin", "state": "TX",
        "lat": 30.2672, "lng": -97.7431,
        "date_incident": "2019-01-01",
        "violence_type": "child_abuse",
        "status": "documented",
        "source_url": "https://www.nytimes.com/2018/12/05/us/southwest-key-arizona-sex-abuse.html",
        "source_name": "NYT — Southwest Key Programs Sexual Abuse / Senate Investigation",
        "verified": True,
        "is_public_figure": True,
    },
]


def main():
    print("[Seed Trafficking ICE] Seeding truck stop trafficking and ICE/ORR pregnant girls records...")
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
    print(f"[Seed Trafficking ICE] {saved}/{len(RECORDS)} records saved.")
    print(f"Total in database: {get_case_count()}")


if __name__ == "__main__":
    main()
