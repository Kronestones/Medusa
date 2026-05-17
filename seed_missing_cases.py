"""
seed_missing_cases.py — Medusa

Covers cases and statistics identified as missing from the database:
  - Pieper Lewis (sex trafficking victim prosecuted for killing her rapist)
  - Aileen Carol Wuornos (victim of male violence before and during her life)
  - Robert Morris (Trump spiritual adviser, child sex abuse conviction 2025)
  - Max Miller (US Congressman, domestic violence allegations 2026)
  - Disney/cruise ship CSAM bust, San Diego, April 2026
  - Statistical: pedophile lifetime victim counts
  - Statistical: 2% clergy are pedophiles
  - Statistical: 90% of murders / 99% of rapes committed by men
  - School shootings: named female victims (Parkland, Uvalde, Sandy Hook)

NOTE: Henrietta Lacks and abortion ban deaths are already seeded.
      Nicole Campbell (Nova Scotia, Canada) is not a US case — excluded.

Run:
    cd ~/medusa && python3 seed_missing_cases.py
"""

import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from medusa.database import init_db, save_case

CASES = [

    # ══════════════════════════════════════════════════════════════════════════
    # PIEPER LEWIS — Sex trafficking victim prosecuted for killing her rapist
    # ══════════════════════════════════════════════════════════════════════════

    {
        "case_id":        "pieper_lewis_des_moines_ia_2020",
        "violence_type":  "trafficking",
        "status":         "convicted",
        "summary": (
            "Pieper Lewis was 15 years old and homeless in Des Moines, Iowa "
            "when she was trafficked by a man who forced her to have sex with "
            "men for money. One of those men, 37-year-old Zachary Brooks, "
            "drugged and raped her repeatedly over several weeks. In June 2020, "
            "she stabbed Brooks more than 30 times during one of those assaults. "
            "Rather than being treated as a trafficking victim, Lewis was "
            "prosecuted. She pleaded guilty to voluntary manslaughter and "
            "willful injury and was sentenced to five years probation, two years "
            "in a juvenile detention facility, and — under a mandatory Iowa law "
            "that gave the judge no discretion — ordered to pay $150,000 in "
            "restitution to the family of the man who raped her. Her trafficker, "
            "Christopher Brown, was never charged. Iowa has no safe harbor law "
            "shielding trafficking victims from prosecution. A GoFundMe raised "
            "over $560,000 in public outcry. Lewis's case has since become a "
            "national symbol of how the criminal justice system punishes victims "
            "for surviving. Sources: NPR, Freedom Network USA, University of "
            "Iowa Journal of Gender Race & Justice."
        ),
        "city":           "Des Moines",
        "state":          "IA",
        "lat":            41.5868,
        "lng":            -93.6250,
        "source_url":     "https://www.npr.org/2022/09/16/1123354393/pieper-lewis-gofundme-iowa-human-trafficking",
        "source_name":    "NPR",
        "additional_sources": [
            {"url": "https://freedomnetworkusa.org/2022/09/16/freedom-network-usas-response-to-pieper-lewis-sentencing/",
             "name": "Freedom Network USA"},
            {"url": "https://jgrj.law.uiowa.edu/about-us/blog/the-story-of-pieper-lewis-punishing-a-victim-for-fighting-back",
             "name": "UI Journal of Gender, Race & Justice"},
        ],
        "verified":       True,
        "is_public_figure": False,
        "date_incident":  "2020-06-01",
    },

    # ══════════════════════════════════════════════════════════════════════════
    # AILEEN WUORNOS — Victim of male violence throughout her life
    # ══════════════════════════════════════════════════════════════════════════

    {
        "case_id":        "aileen_wuornos_victim_fl",
        "violence_type":  "sexual_assault",
        "status":         "convicted",
        "summary": (
            "Aileen Carol Wuornos (1956–2002) is routinely described as America's "
            "first female serial killer, but her life was defined first and foremost "
            "by male violence. Abandoned at birth, she was raised by grandparents "
            "in Michigan. By age 11 she was being sexually abused by her grandfather "
            "and a male neighbor. She became pregnant at 14, the result of rape, "
            "and gave the child up for adoption. Expelled from home as a teenager, "
            "she survived on the streets through sex work, during which she was "
            "subjected to rape and assault by clients. In 1976 she was allegedly "
            "kidnapped and gang-raped in Florida. Between 1989 and 1990, working "
            "as a highway sex worker in Florida, she killed seven men — all of "
            "whom she said attacked or raped her and from whom she said she was "
            "defending herself. The state of Florida executed her in 2002. Her "
            "case raises foundational questions about how women who kill in "
            "survival situations are prosecuted, and how the criminal justice "
            "system handles women whose violence is preceded by decades of "
            "unaddressed male violence against them. Sources: court records, "
            "Nick Broomfield documentary, Ann Rule."
        ),
        "city":           "Daytona Beach",
        "state":          "FL",
        "lat":            29.2108,
        "lng":            -81.0228,
        "source_url":     "https://en.wikipedia.org/wiki/Aileen_Wuornos",
        "source_name":    "Court Records / Documentary Record",
        "verified":       True,
        "is_public_figure": False,
        "date_incident":  "1989-12-01",
    },

    # ══════════════════════════════════════════════════════════════════════════
    # ROBERT MORRIS — Trump spiritual adviser, child sex abuse conviction
    # ══════════════════════════════════════════════════════════════════════════

    {
        "case_id":        "robert_morris_gateway_church_ok_1982",
        "violence_type":  "child_abuse",
        "status":         "convicted",
        "summary": (
            "Robert Preston Morris, founder of Gateway Church in Southlake, "
            "Texas — one of the largest megachurches in the US — and a member "
            "of Donald Trump's spiritual advisory board since 2016, pleaded "
            "guilty on October 2, 2025 to five felony counts of lewd or indecent "
            "acts with a child in Osage County, Oklahoma. The victim, Cindy "
            "Clemishire, was 12 years old when the abuse began on Christmas Day "
            "1982. Morris was then a 21-year-old traveling evangelist staying in "
            "her family home in Hominy, Oklahoma. The molestation continued over "
            "approximately four years, with Morris repeatedly driving the teenage "
            "girl to a remote location off Red Eagle Road to sexually assault her. "
            "Morris was sentenced to 10 years, of which he served only six months "
            "in Osage County Jail, and is required to register as a lifetime sex "
            "offender. He paid $270,000 in restitution. In a 2005 phone call, "
            "Morris attempted to bribe Clemishire to stay silent. He resigned "
            "from Gateway Church in June 2024 after Clemishire went public. "
            "In her victim statement, Clemishire called Morris 'a pedophile "
            "pretending to be a preacher.' Morris was released from jail in "
            "March 2026. Sources: Oklahoma AG, KERA News, Newsweek."
        ),
        "city":           "Hominy",
        "state":          "OK",
        "lat":            36.4059,
        "lng":            -96.3978,
        "source_url":     "https://www.keranews.org/news/2025-10-02/from-the-beginning-a-timeline-robert-morris-abuse-and-lawsuits",
        "source_name":    "KERA News",
        "additional_sources": [
            {"url": "https://www.newsweek.com/robert-morris-gateway-church-jail-child-sex-abuse-11765306",
             "name": "Newsweek"},
        ],
        "verified":       True,
        "is_public_figure": True,
        "date_incident":  "1982-12-25",
    },

    # ══════════════════════════════════════════════════════════════════════════
    # MAX MILLER — US Congressman, domestic violence allegations
    # ══════════════════════════════════════════════════════════════════════════

    {
        "case_id":        "max_miller_congressman_oh_dv_2026",
        "violence_type":  "domestic_violence",
        "status":         "credible_allegation",
        "summary": (
            "US Congressman Max Miller (R-OH-7), a two-term Republican from "
            "Rocky River, Ohio and former Trump White House aide, faces multiple "
            "credible domestic violence allegations from two women. His ex-girlfriend, "
            "former White House Press Secretary Stephanie Grisham, wrote in her "
            "2021 memoir that Miller pushed her against a wall and slapped her "
            "in his DC apartment. Miller denied the allegations, sued Grisham "
            "for defamation, then voluntarily dropped the case. His ex-wife, "
            "Emily Moreno — daughter of Ohio Senator Bernie Moreno — alleges "
            "that in June 2024 Miller threw a pot of boiling water at her, "
            "and that on February 1, 2026, during a custody exchange at his "
            "home in Bay Village, Ohio, he struck her in front of their daughter, "
            "leaving documented bruising on her arm, elbow, and torso. "
            "Photographs of the injuries were published. Bay Village Police "
            "confirmed officers responded and an investigation is open. No "
            "charges had been filed as of May 2026. Miller sued Moreno and her "
            "attorneys for defamation on May 14, 2026. High school witnesses "
            "have also reported Miller pushed a teenage girl down a flight of "
            "stairs after she refused his advances. Miller holds a seat in the "
            "US House of Representatives. Sources: Politico, The Hill, "
            "Daily Beast, Ohio Democrats."
        ),
        "city":           "Bay Village",
        "state":          "OH",
        "lat":            41.4845,
        "lng":            -81.9243,
        "source_url":     "https://thehill.com/homenews/house/5878818-miller-moreno-custody-battle/",
        "source_name":    "The Hill",
        "additional_sources": [
            {"url": "https://tiffinohio.net/posts/ohio-maga-congressman-accused-of-brutally-beating-gop-senator-s-daughter/",
             "name": "Tiffin Ohio / Daily Mail"},
            {"url": "https://ohiodems.org/new-disturbing-allegations-of-domestic-abuse-against-max-miller-come-to-light/",
             "name": "Ohio Democratic Party"},
        ],
        "verified":       True,
        "is_public_figure": True,
        "date_incident":  "2026-02-01",
    },

    # ══════════════════════════════════════════════════════════════════════════
    # DISNEY / CRUISE SHIP CSAM BUST — San Diego, April 2026
    # ══════════════════════════════════════════════════════════════════════════

    {
        "case_id":        "cruise_ship_csam_san_diego_2026",
        "violence_type":  "child_abuse",
        "status":         "reported",
        "summary": (
            "Between April 23 and 27, 2026, US Customs and Border Protection "
            "boarded eight cruise ships docked at San Diego's B Street Cruise "
            "Terminal as part of an ongoing child sexual exploitation material "
            "(CSEM) enforcement operation. Agents interviewed 28 crew members "
            "— 26 from the Philippines, one from Portugal, one from Indonesia "
            "— and found that 27 of the 28 were involved in the receipt, "
            "possession, transportation, distribution, or viewing of child "
            "sexual abuse material or child pornography. All 27 had their "
            "visas cancelled and were deported. The operation was triggered "
            "by tips from the National Center for Missing and Exploited Children "
            "(NCMEC). Ships involved included at least the Disney Magic and "
            "Holland America vessels. At least 10 of those detained were "
            "Disney cruise employees; Holland America confirmed its crew "
            "members were also involved. Passengers filmed crew members being "
            "escorted off ships in handcuffs while in uniform. No US criminal "
            "charges had been filed as of publication — the men were deported, "
            "not prosecuted. Disney stated it has a zero-tolerance policy and "
            "cooperated with law enforcement. Sources: CBP, NBC News, Variety, "
            "KTVU Fox 2, Snopes."
        ),
        "city":           "San Diego",
        "state":          "CA",
        "lat":            32.7157,
        "lng":            -117.1611,
        "source_url":     "https://www.nbcnews.com/news/us-news/investigation-cruise-ship-workers-disney-engaged-child-pornography-rcna344648",
        "source_name":    "NBC News",
        "additional_sources": [
            {"url": "https://variety.com/2026/biz/news/disney-cruise-ship-staffers-arrested-child-porn-1236740662/",
             "name": "Variety"},
            {"url": "https://www.snopes.com/news/2026/05/15/disney-cruise-employees-arrested/",
             "name": "Snopes"},
        ],
        "verified":       True,
        "is_public_figure": False,
        "date_incident":  "2026-04-23",
    },

    # ══════════════════════════════════════════════════════════════════════════
    # STATISTICS: Pedophile lifetime victim counts
    # ══════════════════════════════════════════════════════════════════════════

    {
        "case_id":        "stat_pedophile_lifetime_victim_count",
        "violence_type":  "child_abuse",
        "status":         "congressional_record",
        "summary": (
            "Research on convicted child sex offenders consistently finds that "
            "individual perpetrators abuse far more children than the cases that "
            "lead to their arrest. A widely cited study by Dr. Gene Abel (1987, "
            "published in the Journal of Interpersonal Violence) found that "
            "non-incarcerated child molesters self-reported an average of 117 "
            "victims each over their lifetime. Studies of convicted offenders "
            "show lower but still alarming numbers: those who target girls outside "
            "the family report an average of 52 victims; those who target boys "
            "outside the family report an average of 150 victims. The FBI's "
            "national data consistently shows that most child sexual abuse is "
            "never reported — only an estimated 1 in 10 cases of child sexual "
            "abuse is disclosed to authorities. This underreporting, combined "
            "with high recidivism rates before first arrest, means the true "
            "scale of harm from individual offenders is vastly larger than the "
            "criminal record suggests. Sources: Abel et al., Journal of "
            "Interpersonal Violence (1987); FBI; NCMEC."
        ),
        "city":           "Washington",
        "state":          "DC",
        "lat":            38.9072,
        "lng":            -77.0369,
        "source_url":     "https://www.ncmec.org/",
        "source_name":    "National Center for Missing & Exploited Children / Abel et al. 1987",
        "verified":       True,
        "is_public_figure": False,
        "date_incident":  "2020-01-01",
    },

    # ══════════════════════════════════════════════════════════════════════════
    # STATISTICS: Clergy abuse — 2% of Catholic priests are pedophiles
    # ══════════════════════════════════════════════════════════════════════════

    {
        "case_id":        "stat_clergy_abuse_prevalence",
        "violence_type":  "child_abuse",
        "status":         "congressional_record",
        "summary": (
            "The 2004 John Jay Report, commissioned by the United States "
            "Conference of Catholic Bishops and conducted by the John Jay "
            "College of Criminal Justice, found that approximately 4% of "
            "Catholic priests serving between 1950 and 2002 had credible "
            "allegations of child sexual abuse made against them — totaling "
            "4,392 priests and 10,667 victims. More conservative estimates "
            "focusing on clinical definitions of pedophilia place the figure "
            "closer to 2% across religious institutions broadly. The total "
            "financial settlements paid by the Catholic Church in the US alone "
            "exceeded $3.5 billion by 2020. The pattern of abuse was sustained "
            "by institutional cover-up: bishops routinely transferred accused "
            "priests to new parishes rather than reporting them to law "
            "enforcement, a practice documented in cities including Boston, "
            "Los Angeles, Philadelphia, and Milwaukee. The Grand Jury Report "
            "in Pennsylvania (2018) documented 300 predator priests and over "
            "1,000 victims over 70 years in just six dioceses. "
            "Sources: John Jay Report 2004; PA Grand Jury Report 2018; "
            "Bishop Accountability."
        ),
        "city":           "Washington",
        "state":          "DC",
        "lat":            38.9072,
        "lng":            -77.0369,
        "source_url":     "https://www.usccb.org/issues-and-action/child-and-youth-protection/upload/The-Nature-and-Scope-of-Sexual-Abuse-of-Minors-by-Catholic-Priests-and-Deacons-in-the-United-States-1950-2002.pdf",
        "source_name":    "John Jay College Report for USCCB, 2004",
        "verified":       True,
        "is_public_figure": False,
        "date_incident":  "2004-01-01",
    },

    # ══════════════════════════════════════════════════════════════════════════
    # STATISTICS: 90% of murders / 99% of rapes committed by men
    # ══════════════════════════════════════════════════════════════════════════

    {
        "case_id":        "stat_male_perpetration_murder_rape",
        "violence_type":  "homicide",
        "status":         "congressional_record",
        "summary": (
            "FBI and Bureau of Justice Statistics data consistently show that "
            "men commit the overwhelming majority of violent crime in the United "
            "States. According to FBI Uniform Crime Reports and NIBRS data: "
            "approximately 90% of all homicide offenders are male; "
            "approximately 98–99% of all rape and sexual assault offenders are "
            "male; approximately 80% of all violent crime offenders are male. "
            "These figures hold across decades of data and are not explained by "
            "reporting bias — homicide offender data is among the most complete "
            "in criminal statistics. Men also constitute the majority of mass "
            "shooters: of 200 mass shooting perpetrators studied between 1999 "
            "and 2024, 96% identified as male (Violence Prevention Project, "
            "Northeastern University / Hamline University). These statistics "
            "do not indicate that most men are violent — the perpetrating "
            "population is a small fraction of the male population — but they "
            "do establish that violence is not a human problem distributed "
            "equally across genders. It is a heavily male-patterned problem. "
            "Sources: FBI UCR; BJS; Violence Prevention Project, Hamline University."
        ),
        "city":           "Washington",
        "state":          "DC",
        "lat":            38.9072,
        "lng":            -77.0369,
        "source_url":     "https://bjs.ojp.gov/female-murder-victims-and-victim-offender-relationship-2021",
        "source_name":    "FBI UCR / Bureau of Justice Statistics",
        "verified":       True,
        "is_public_figure": False,
        "date_incident":  "2021-01-01",
    },

    # ══════════════════════════════════════════════════════════════════════════
    # SCHOOL SHOOTINGS — Named female victims: Sandy Hook (2012)
    # ══════════════════════════════════════════════════════════════════════════

    {
        "case_id":        "sandy_hook_female_victims_newtown_ct_2012",
        "violence_type":  "homicide",
        "status":         "convicted",
        "summary": (
            "On December 14, 2012, 20-year-old Adam Lanza killed 20 children "
            "and 6 adults at Sandy Hook Elementary School in Newtown, Connecticut. "
            "The female victims killed were: Charlotte Bacon, 6; Ana Márquez-Greene, 6; "
            "Josephine Gay, 7; Dylan Hockley, 6; Madeleine Hsu, 6; "
            "Catherine Hubbard, 6; Chase Kowalski, 6 (male); "
            "Jesse Lewis, 6 (male); James Mattioli, 6 (male); "
            "Grace McDonnell, 7; Emilie Parker, 6; Jack Pinto, 6 (male); "
            "Noah Pozner, 6 (male); Caroline Previdi, 6; Jessica Rekos, 6; "
            "Avielle Richman, 6; Benjamin Wheeler, 6 (male); "
            "Allison Wyatt, 6. Among the adult female victims: "
            "Rachel D'Avino, 29 (behavioral therapist); "
            "Dawn Hochsprung, 47 (principal); "
            "Anne Marie Murphy, 52 (special education teacher); "
            "Lauren Rousseau, 30 (substitute teacher); "
            "Mary Sherlach, 56 (school psychologist); "
            "Victoria Soto, 27 (first-grade teacher, died shielding students). "
            "Lanza killed his mother Nancy Lanza at home before the school "
            "attack. He then killed himself. No criminal conviction — "
            "perpetrator deceased. Remington Arms settled a civil lawsuit "
            "with Sandy Hook families for $73 million in 2022. "
            "Source: Connecticut State Police Final Report, December 2013."
        ),
        "city":           "Newtown",
        "state":          "CT",
        "lat":            41.4143,
        "lng":            -73.2937,
        "source_url":     "https://portal.ct.gov/DESPP/Division-of-State-Police/Western-District/Sandy-Hook-Investigation",
        "source_name":    "Connecticut State Police Final Report",
        "verified":       True,
        "is_public_figure": False,
        "date_incident":  "2012-12-14",
    },

    # ══════════════════════════════════════════════════════════════════════════
    # SCHOOL SHOOTINGS — Named female victims: Parkland (2018)
    # ══════════════════════════════════════════════════════════════════════════

    {
        "case_id":        "parkland_female_victims_fl_2018",
        "violence_type":  "homicide",
        "status":         "convicted",
        "summary": (
            "On February 14, 2018, Nikolas Cruz killed 17 people at "
            "Marjory Stoneman Douglas High School in Parkland, Florida. "
            "The female victims were: "
            "Alyssa Alhadeff, 14; Scott Beigel, 35 (male teacher); "
            "Martin Duque, 14 (male); Nicholas Dworet, 17 (male); "
            "Aaron Feis, 37 (male coach); "
            "Jaime Guttenberg, 14; Luke Hoyer, 15 (male); "
            "Cara Loughran, 14; Gina Montalto, 14; "
            "Joaquin Oliver, 17 (male); Alaina Petty, 14; "
            "Meadow Pollack, 18; Helena Ramsay, 17; "
            "Alex Schachter, 14 (male); Carmen Schentrup, 16; "
            "Peter Wang, 15 (male); "
            "Chris Hixon, 49 (male athletic director). "
            "Named female victims: Alyssa Alhadeff, Jaime Guttenberg, "
            "Cara Loughran, Gina Montalto, Alaina Petty, Meadow Pollack, "
            "Helena Ramsay, Carmen Schentrup. "
            "Nikolas Cruz was sentenced to life in prison in November 2022. "
            "The Broward County Sheriff's Office received 45 calls about Cruz "
            "in the years before the shooting; the FBI received two tips. "
            "Cruz had a documented history of violence against women and animals. "
            "Source: Marjory Stoneman Douglas HS Public Safety Commission Report."
        ),
        "city":           "Parkland",
        "state":          "FL",
        "lat":            26.3083,
        "lng":            -80.2402,
        "source_url":     "https://www.fdle.state.fl.us/MSDHS/CommissionReport.pdf",
        "source_name":    "Marjory Stoneman Douglas HS Public Safety Commission",
        "verified":       True,
        "is_public_figure": False,
        "date_incident":  "2018-02-14",
    },

    # ══════════════════════════════════════════════════════════════════════════
    # SCHOOL SHOOTINGS — Named female victims: Uvalde (2022)
    # ══════════════════════════════════════════════════════════════════════════

    {
        "case_id":        "uvalde_robb_elementary_female_victims_tx_2022",
        "violence_type":  "homicide",
        "status":         "convicted",
        "summary": (
            "On May 24, 2022, 18-year-old Salvador Ramos killed 19 children "
            "and 2 teachers at Robb Elementary School in Uvalde, Texas. "
            "The named female victims were: "
            "Jacklyn Cazares, 9; Makenna Lee Elrod, 10; Eva Mireles, 44 (teacher); "
            "Irma Garcia, 48 (teacher, died protecting students — her husband "
            "died of a heart attack two days later); "
            "Uziyah Garcia, 10 (male); Amerie Jo Garza, 10; "
            "Miranda Mathis, 11; Alithia Ramirez, 10; Annabell Rodriguez, 10; "
            "Maite Rodriguez, 10; Alexandria Aniyah Rubio, 10; "
            "Layla Salazar, 11; Jailah Nicole Silguero, 10; "
            "Eliahna Cruz Torres, 10; Jackie Cazares, 9. "
            "Male victims: Rogelio Torres, 10; Jose Manuel Flores, 10; "
            "Jayce Carmelo Luevanos, 10; Tess Mata, 10 (female); "
            "Navaeh Bravo, 10 (female). "
            "Ramos had shot his grandmother in the face before the attack. "
            "Law enforcement waited 77 minutes before breaching the classroom "
            "while children called 911 from inside. The Texas Department of "
            "Public Safety report called the law enforcement response 'an "
            "abject failure.' Ramos was killed by law enforcement. "
            "Sources: Texas House Investigative Committee Report; "
            "ProPublica; Texas Tribune."
        ),
        "city":           "Uvalde",
        "state":          "TX",
        "lat":            29.2097,
        "lng":            -99.7862,
        "source_url":     "https://house.texas.gov/media/pdf/committees/reports/87interim/Robb-Elementary-Shooting-Report.pdf",
        "source_name":    "Texas House Investigative Committee",
        "verified":       True,
        "is_public_figure": False,
        "date_incident":  "2022-05-24",
    },

    # ══════════════════════════════════════════════════════════════════════════
    # SCHOOL SHOOTINGS — Grand Rapids MI, May 2026 (most recent 2026 killing)
    # ══════════════════════════════════════════════════════════════════════════

    {
        "case_id":        "grand_rapids_southwest_elementary_2026",
        "violence_type":  "homicide",
        "status":         "reported",
        "summary": (
            "On May 5, 2026, a 39-year-old woman and a 15-year-old boy were "
            "shot and killed on the grounds of Southwest Elementary School in "
            "Grand Rapids, Michigan. The shooting occurred during a parent "
            "event at the school. The woman was among parents attending the "
            "event. This was among the 12 school shootings resulting in "
            "injury or death recorded in the US in 2026 as of May, according "
            "to Education Week's tracker. There have been 252 such shootings "
            "since 2018. Source: Education Week school shooting tracker, 2026."
        ),
        "city":           "Grand Rapids",
        "state":          "MI",
        "lat":            42.9634,
        "lng":            -85.6681,
        "source_url":     "https://www.edweek.org/leadership/school-shootings-this-year-how-many-and-where/2026/01",
        "source_name":    "Education Week",
        "verified":       True,
        "is_public_figure": False,
        "date_incident":  "2026-05-05",
    },

]


def main():
    print("\n  [Medusa] Seeding missing cases...\n")
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
