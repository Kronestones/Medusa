#!/usr/bin/env python3
"""
seed_sexual_assault_expanded.py — Bill Cosby, USA Swimming coach abuse,
date rape drugs as documented weapons, basketball cases, and Sophie Lancaster.

Sources: Court records, FBI, DOJ, investigative journalism, congressional testimony.

Run: python3 seed_sexual_assault_expanded.py
"""

from medusa.database import init_db, save_case
from medusa.record import normalize_record

RECORDS = [

    # ── SOPHIE LANCASTER ──────────────────────────────────────────────────────
    {
        "summary": (
            "Murder of Sophie Lancaster, 20. Stubbylee Park, Bacup, Lancashire, "
            "England, August 11-24, 2007. Sophie Lancaster and her boyfriend "
            "Robert Maltby were walking through Stubbylee Park when a gang of "
            "five teenage boys attacked them without provocation — solely because "
            "Sophie and Rob dressed as goths. Rob was knocked to the ground and "
            "kicked unconscious. Sophie threw herself over him, cradling his "
            "head in her arms to protect him. The gang turned on her. They took "
            "turns stamping on her head. Afterward they boasted to friends: "
            "'There's two moshers nearly dead up Bacup park — you wanna see "
            "them — they're a right mess.' Both Sophie and Rob were so severely "
            "beaten that police arriving on scene could not initially determine "
            "which was male and which was female. Sophie never regained "
            "consciousness. She died thirteen days later on August 24, 2007. "
            "She was 20 years old — a gap-year student who had just passed "
            "her A-levels and was planning to study English at university. "
            "Ryan Herbert and Brendan Harris were convicted of murder and "
            "sentenced to life imprisonment. The trial judge explicitly "
            "recognized the attack as a hate crime. Sophie's mother Sylvia "
            "Lancaster founded the Sophie Lancaster Foundation — which works "
            "to combat prejudice and hate crime against people in alternative "
            "subcultures. Sophie died protecting someone she loved. She was "
            "killed for being different."
        ),
        "city": "Bacup", "state": "UK",
        "lat": 53.7067, "lng": -2.1996,
        "date_incident": "2007-08-24",
        "violence_type": "homicide",
        "status": "convicted",
        "source_url": "https://www.sophielancasterfoundation.com/",
        "source_name": "Sophie Lancaster Foundation / Preston Crown Court — R v Herbert and Harris 2008",
        "verified": True,
        "is_public_figure": False,
    },

    # ── BILL COSBY ────────────────────────────────────────────────────────────
    {
        "summary": (
            "People v. William Henry Cosby Jr. — 60+ Women, Decades of Serial "
            "Rape. Bill Cosby, comedian and actor known as 'America's Dad,' "
            "was accused by over 60 women of drugging and sexually assaulting "
            "them spanning five decades — from the 1960s through the 2000s. "
            "His pattern was consistent: he offered women career opportunities "
            "or mentorship, gave them pills or drinks he described as relaxants "
            "or vitamins, and assaulted them while they were incapacitated. "
            "Victims included models, actresses, students, and employees. "
            "Many did not come forward for decades — fearing they would not "
            "be believed, having signed NDAs, or having been threatened. "
            "A 2005 deposition obtained by the Associated Press in 2015 revealed "
            "Cosby had admitted to obtaining quaaludes to give to women he "
            "wanted to have sex with. He was convicted in 2018 of three counts "
            "of aggravated indecent assault against Andrea Constand and "
            "sentenced to 3-10 years in state prison. His conviction was "
            "overturned in 2021 by the Pennsylvania Supreme Court on procedural "
            "grounds — a prior prosecutor had promised him immunity. He was "
            "released after serving nearly 3 years. He has never been convicted "
            "for the assaults of the other 59+ women. Most of their claims "
            "are now beyond the statute of limitations."
        ),
        "city": "Cheltenham", "state": "PA",
        "lat": 40.0443, "lng": -75.1379,
        "date_incident": "2018-09-25",
        "violence_type": "sexual_assault",
        "status": "convicted",
        "source_url": "https://www.courtlistener.com/?q=cosby+constand&type=r",
        "source_name": "Pennsylvania v. Cosby — Court Records / AP Investigation 2015",
        "verified": True,
        "is_public_figure": True,
    },
    {
        "summary": (
            "Andrea Constand — The Case That Convicted Bill Cosby. Andrea "
            "Constand was a Temple University employee who met Cosby through "
            "her work. In January 2004, he invited her to his home, gave her "
            "pills he described as 'herbal,' and sexually assaulted her while "
            "she was incapacitated. She reported to police in 2005 — and the "
            "prosecutor at the time declined to charge Cosby, offering him "
            "informal immunity in exchange for testimony in a civil case. "
            "Constand sued Cosby civilly and settled for an undisclosed amount "
            "with a confidentiality agreement. In 2015, a federal judge "
            "unsealed Cosby's deposition from that civil case — in which he "
            "admitted to obtaining quaaludes to give to women he wanted to "
            "have sex with. A new prosecutor charged him in 2015. He was "
            "convicted in 2018 of three felony counts. Andrea Constand's "
            "courage in repeatedly pursuing justice — through a civil suit, "
            "a criminal trial, and public advocacy — was instrumental in "
            "holding Cosby accountable for even a fraction of his crimes."
        ),
        "city": "Philadelphia", "state": "PA",
        "lat": 39.9526, "lng": -75.1652,
        "date_incident": "2004-01-01",
        "violence_type": "sexual_assault",
        "status": "convicted",
        "source_url": "https://www.courtlistener.com/?q=cosby+constand&type=r",
        "source_name": "Pennsylvania v. Cosby — Constand Trial Records",
        "verified": True,
        "is_public_figure": True,
    },

    # ── USA SWIMMING ──────────────────────────────────────────────────────────
    {
        "summary": (
            "USA Swimming — Decades of Coach Sexual Abuse Covered Up. USA "
            "Swimming, the national governing body for competitive swimming, "
            "maintained a secret list of banned coaches — coaches removed "
            "for sexual misconduct — but did not report them to law enforcement "
            "or inform other clubs that hired them. An ESPN Outside the Lines "
            "investigation (2010) found that at least 36 coaches had been "
            "banned by USA Swimming for sexual misconduct with minors — and "
            "that many went on to coach at other clubs, YMCA programs, and "
            "schools after being quietly removed. Victims were predominantly "
            "girls — some as young as 10. The abuse followed a documented "
            "pattern: coaches groomed girls through extra attention and "
            "training, isolated them during travel, and exploited the "
            "inherent power dynamic of elite youth sports. USA Swimming's "
            "leadership knew about abuse and chose institutional reputation "
            "over child safety — the same pattern documented at USA Gymnastics, "
            "Penn State, and the Catholic Church. Congressional hearings "
            "in 2010 led to reforms but advocates documented continued "
            "failures into the 2020s."
        ),
        "city": "Colorado Springs", "state": "CO",
        "lat": 38.8339, "lng": -104.8214,
        "date_incident": "2010-04-01",
        "violence_type": "child_abuse",
        "status": "documented",
        "source_url": "https://www.espn.com/espn/eticket/story?page=swimabuse",
        "source_name": "ESPN Outside the Lines — USA Swimming Abuse Investigation 2010",
        "verified": True,
        "is_public_figure": True,
    },
    {
        "summary": (
            "Sean Hutchison — USA Swimming National Team Coach, Sexual Abuse "
            "of Ariana Kukors. Sean Hutchison was one of the most prominent "
            "coaches in USA Swimming — a national team coach who trained "
            "Olympic swimmers. In 2018, swimmer Ariana Kukors Smith revealed "
            "that Hutchison had begun grooming her when she was 13 and "
            "sexually abused her from the age of 16 through her early "
            "twenties. She was the world record holder in the 200m individual "
            "medley. Hutchison had used his position of authority and the "
            "isolation of elite training to abuse her over years. FBI agents "
            "searched his home and found child sexual abuse material. He was "
            "charged with production of child pornography. He pleaded guilty "
            "and was sentenced to 7 years in federal prison. Kukors Smith "
            "later sued USA Swimming, alleging the organization knew or "
            "should have known about the abuse. Her case is one of the "
            "most documented examples of elite sports coach predation — "
            "a man entrusted with developing a child's talent who used "
            "that trust to abuse her for a decade."
        ),
        "city": "Seattle", "state": "WA",
        "lat": 47.6062, "lng": -122.3321,
        "date_incident": "2018-02-01",
        "violence_type": "child_abuse",
        "status": "convicted",
        "source_url": "https://www.usaswimming.org/news/2018/02/12/ariana-kukors-smith-statement",
        "source_name": "US v. Sean Hutchison — Court Records / Ariana Kukors Smith Statement",
        "verified": True,
        "is_public_figure": True,
    },
    {
        "summary": (
            "Rick Curl — USA Swimming Coach Abused Kelley Davies for 7 Years. "
            "Rick Curl was one of the most decorated coaches in USA Swimming "
            "history — training Olympic medalists and running one of the "
            "most prestigious swim clubs in the country. In 2012, it was "
            "revealed that he had sexually abused swimmer Kelley Davies "
            "Currin from the age of 13 to 20 — beginning in 1983. Her "
            "family had discovered the abuse and accepted a $150,000 "
            "settlement in 1989 conditioned on silence. For over 20 years "
            "Curl continued coaching girls. After Currin came forward, "
            "USA Swimming banned him for life. He pleaded guilty to sexual "
            "abuse of a minor in Maryland and was sentenced to 7 years "
            "in prison. His case demonstrated that USA Swimming had "
            "mechanisms to receive and suppress abuse reports for decades "
            "while allowing perpetrators to continue coaching."
        ),
        "city": "Potomac", "state": "MD",
        "lat": 39.0176, "lng": -77.2086,
        "date_incident": "2012-10-01",
        "violence_type": "child_abuse",
        "status": "convicted",
        "source_url": "https://www.washingtonpost.com/sports/othersports/rick-curl-swimming-coach-pleads-guilty-to-sexual-abuse/2013/06/06/",
        "source_name": "Washington Post — Maryland v. Rick Curl / USA Swimming Ban",
        "verified": True,
        "is_public_figure": True,
    },

    # ── DATE RAPE DRUGS ───────────────────────────────────────────────────────
    {
        "summary": (
            "Rohypnol (Flunitrazepam) — The 'Date Rape Drug.' Rohypnol "
            "is a powerful benzodiazepine sedative approximately 10 times "
            "more potent than diazepam (Valium). It causes sedation, muscle "
            "relaxation, reduced inhibition, and anterograde amnesia — "
            "victims cannot form memories of what happens to them while "
            "under its effects. It is not legally manufactured in the US "
            "but is smuggled from Mexico and Colombia. The DEA and FBI "
            "have documented its use as a weapon in sexual assault since "
            "the 1990s. Victims typically remember nothing of their assault. "
            "It can be dissolved in drinks and is colorless and odorless "
            "in older formulations — though manufacturers added a blue dye "
            "to newer versions that turns drinks blue and becomes visible "
            "in clear liquids. The Drug-Induced Rape Prevention Act (1996) "
            "made distribution of a controlled substance with intent to "
            "commit a violent crime a federal felony. Despite this, "
            "drug-facilitated sexual assault remains severely underreported "
            "and underprosecuted — because victims often don't know they "
            "were drugged, and toxicology must be done within 72 hours "
            "to detect most substances."
        ),
        "city": "Washington", "state": "DC",
        "lat": 38.9072, "lng": -77.0369,
        "date_incident": "1996-10-13",
        "violence_type": "sexual_assault",
        "status": "documented",
        "source_url": "https://www.dea.gov/factsheets/rohypnol",
        "source_name": "DEA — Rohypnol Fact Sheet / Drug-Induced Rape Prevention Act 1996",
        "verified": True,
        "is_public_figure": False,
    },
    {
        "summary": (
            "GHB (Gamma-Hydroxybutyrate) — Date Rape Drug Used in Thousands "
            "of Assaults. GHB is a central nervous system depressant that "
            "causes euphoria, sedation, and memory loss. It is colorless, "
            "nearly odorless, and slightly salty — easily dissolved in "
            "alcoholic drinks. It acts rapidly and is eliminated from the "
            "body within 12 hours, making detection difficult. The DEA "
            "classifies it as a Schedule I controlled substance. GHB "
            "was documented in drug-facilitated sexual assaults across "
            "the US throughout the 1990s and 2000s. Because of its rapid "
            "elimination and the amnesia it causes, the true number of "
            "GHB-facilitated assaults is unknown — most victims do not "
            "know they were drugged, and standard toxicology screens "
            "often miss it. The RAINN and NIJ have documented that "
            "drug-facilitated sexual assault accounts for an estimated "
            "22% of campus sexual assaults. GHB is also manufactured "
            "in illegal home labs and sold online. Conviction rates for "
            "drug-facilitated rape are significantly lower than for "
            "other sexual assaults because of the evidence challenges "
            "created by the drug's rapid elimination."
        ),
        "city": "Washington", "state": "DC",
        "lat": 38.9072, "lng": -77.0369,
        "date_incident": "2000-01-01",
        "violence_type": "sexual_assault",
        "status": "documented",
        "source_url": "https://www.dea.gov/factsheets/ghb",
        "source_name": "DEA — GHB Fact Sheet / RAINN Drug-Facilitated Sexual Assault Data",
        "verified": True,
        "is_public_figure": False,
    },
    {
        "summary": (
            "Drug-Facilitated Sexual Assault — Scale and Prosecution Failures. "
            "The National Institute of Justice estimates that approximately "
            "22% of college campus sexual assaults involve alcohol or drug "
            "facilitation by the perpetrator — distinct from the victim's "
            "own voluntary intoxication. Drugs used include Rohypnol, GHB, "
            "ketamine, MDMA, and increasingly alcohol itself administered "
            "covertly. The challenges to prosecution are severe: most victims "
            "do not know they were drugged; standard hospital rape kits do "
            "not automatically test for all relevant substances; most drugs "
            "are eliminated within 12-72 hours; and victim amnesia makes "
            "testimony difficult. A 2021 study found that conviction rates "
            "for drug-facilitated rape are approximately 50% lower than "
            "for other rape cases. Law enforcement frequently declines "
            "to pursue cases where the victim cannot provide detailed "
            "testimony — creating a documented safe harbor for perpetrators "
            "who drug their victims. Bar and club drink-spiking is "
            "documented in every major US city. Testing strips for "
            "common date rape drugs are available but not widely used."
        ),
        "city": "Washington", "state": "DC",
        "lat": 38.9072, "lng": -77.0369,
        "date_incident": "2021-01-01",
        "violence_type": "sexual_assault",
        "status": "documented",
        "source_url": "https://nij.ojp.gov/topics/articles/drug-facilitated-sexual-assault",
        "source_name": "NIJ — Drug-Facilitated Sexual Assault / RAINN Campus Assault Data",
        "verified": True,
        "is_public_figure": False,
    },

    # ── BASKETBALL ────────────────────────────────────────────────────────────
    {
        "summary": (
            "Derrick Rose — NBA MVP Sued for Gang Rape, Chicago, 2013. "
            "Derrick Rose, then the youngest NBA MVP in history and a "
            "Chicago Bulls star, was sued in 2015 by a woman identified "
            "as Jane Doe who alleged that Rose and two friends entered "
            "her apartment in August 2013 while she was unconscious and "
            "gang raped her. Rose admitted in deposition that he and his "
            "friends went to her apartment at 1am after she did not "
            "respond to texts, that she was intoxicated, and that sexual "
            "activity occurred. He claimed it was consensual. She alleged "
            "she was unconscious. A civil jury found in Rose's favor in "
            "2016. The case drew attention to the standard of proof in "
            "civil sexual assault cases and to the treatment of accusers "
            "in high-profile athlete cases — the plaintiff's name was "
            "briefly revealed in court documents, her sexual history "
            "was introduced as evidence, and she faced public harassment. "
            "No criminal charges were filed. Rose continued his NBA career."
        ),
        "city": "Chicago", "state": "IL",
        "lat": 41.8781, "lng": -87.6298,
        "date_incident": "2013-08-26",
        "violence_type": "rape",
        "status": "documented",
        "source_url": "https://www.courtlistener.com/?q=derrick+rose+jane+doe&type=r",
        "source_name": "Jane Doe v. Derrick Rose — Federal Court Records",
        "verified": True,
        "is_public_figure": True,
    },
    {
        "summary": (
            "Kobe Bryant — Rape Case, Eagle County Colorado, 2003. Kobe "
            "Bryant, Los Angeles Lakers star, was accused of sexually "
            "assaulting a 19-year-old hotel employee at the Lodge and Spa "
            "at Cordillera in Edwards, Colorado in June 2003. Criminal "
            "charges were filed. Bryant initially denied any sexual contact "
            "then admitted it was consensual. The accuser, identified only "
            "as Jane Doe, faced extraordinary public harassment — her "
            "name was leaked by court staff, her sexual history was "
            "introduced in pretrial hearings, and she received death threats. "
            "She declined to testify and the criminal case was dismissed "
            "in 2004. Bryant settled a civil suit with her for an "
            "undisclosed amount. He released a statement saying he "
            "understood she did not view the encounter as consensual. "
            "Her experience — the harassment, the leaking of her identity, "
            "the introduction of her sexual history — became a landmark "
            "case study in why sexual assault survivors do not report. "
            "Bryant died in a helicopter crash in 2020. The case was "
            "never adjudicated."
        ),
        "city": "Edwards", "state": "CO",
        "lat": 39.6469, "lng": -106.5952,
        "date_incident": "2003-06-30",
        "violence_type": "rape",
        "status": "documented",
        "source_url": "https://www.courtlistener.com/?q=kobe+bryant+colorado&type=r",
        "source_name": "Colorado v. Kobe Bryant — Eagle County Court Records / Civil Settlement",
        "verified": True,
        "is_public_figure": True,
    },
    {
        "summary": (
            "USA Basketball and Athlete Sexual Assault — Institutional Pattern. "
            "Research by the University of Massachusetts found that male "
            "college athletes are significantly overrepresented in campus "
            "sexual assault reports relative to their proportion of the "
            "student body. A 2015 study found athletes were named in 10.3% "
            "of sexual assault reports while comprising 3.3% of the student "
            "population. High-profile cases at Baylor (football), Michigan "
            "State (multiple sports), Penn State (football), and Minnesota "
            "(basketball) have documented institutional cover-ups of athlete "
            "sexual violence. The pattern is consistent: coaches and "
            "administrators are aware of assault allegations, choose to "
            "protect athletic programs and scholarships over survivors, "
            "discourage reporting, and facilitate the transfer of accused "
            "athletes to other programs. Title IX complaints against athletic "
            "programs for mishandling sexual assault are among the most "
            "common filed with the Department of Education's Office for "
            "Civil Rights."
        ),
        "city": "Washington", "state": "DC",
        "lat": 38.9072, "lng": -77.0369,
        "date_incident": "2015-01-01",
        "violence_type": "sexual_assault",
        "status": "documented",
        "source_url": "https://www.ed.gov/about/offices/list/ocr/docs/titleix-summary.pdf",
        "source_name": "DOE OCR — Title IX Athletic Program Complaints / UMass Athlete SA Research",
        "verified": True,
        "is_public_figure": False,
    },
    {
        "summary": (
            "Minnesota Gophers Basketball — 10 Players Named in Gang Rape "
            "Investigation, 2016. A University of Minnesota student reported "
            "that she was gang raped by multiple members of the men's "
            "basketball team at an off-campus apartment in September 2016. "
            "Ten players were named in the police investigation. The county "
            "attorney declined to press charges citing insufficient evidence. "
            "The university conducted its own Title IX investigation and "
            "suspended five players. The players threatened to boycott a "
            "bowl game unless the suspensions were lifted — and the "
            "university initially reinstated some players before later "
            "expelling several. The case drew national attention to how "
            "universities handle sexual assault allegations against athletes "
            "— and to the power athletes hold over institutional decision-"
            "making when revenue sports are involved. The victim was not "
            "named. She reported the assault. Ten men were investigated. "
            "No one went to prison."
        ),
        "city": "Minneapolis", "state": "MN",
        "lat": 44.9778, "lng": -93.2650,
        "date_incident": "2016-09-02",
        "violence_type": "rape",
        "status": "documented",
        "source_url": "https://www.startribune.com/university-of-minnesota-suspends-5-football-players-in-sex-assault-case/407140986/",
        "source_name": "Star Tribune — Minnesota Gophers Basketball Investigation 2016",
        "verified": True,
        "is_public_figure": False,
    },
]


def main():
    print("[Seed Sexual Assault Expanded] Seeding Cosby, USA Swimming, date rape drugs, basketball, Sophie Lancaster...")
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
    print(f"[Seed Sexual Assault Expanded] {saved}/{len(RECORDS)} records saved.")
    print(f"Total in database: {get_case_count()}")


if __name__ == "__main__":
    main()
