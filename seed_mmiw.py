#!/usr/bin/env python3
"""
seed_mmiw.py — Missing and Murdered Indigenous Women & Girls (MMIW/MMIWG)

Documented cases, systemic failures, federal negligence, and statistical records.
Sources: BIA, FBI UCR, Urban Indian Health Institute, Sovereign Bodies Institute,
National Congress of American Indians, congressional testimony, court records.

Run: python3 seed_mmiw.py
"""

from medusa.database import init_db, save_case
from medusa.record import normalize_record

RECORDS = [

    # ── STATISTICAL FOUNDATION ────────────────────────────────────────────────
    {
        "summary": (
            "MMIW Crisis — National Scale. According to the Urban Indian Health "
            "Institute (2018), murder is the third leading cause of death for "
            "Indigenous women. Native American women are murdered at rates more than "
            "10 times the national average in some counties. The FBI estimates that "
            "over 5,700 Indigenous women and girls were reported missing in 2016 — "
            "yet the Justice Department logged only 116 cases. The gap between "
            "reported and investigated cases represents a systemic failure of federal "
            "law enforcement to protect Indigenous women. Approximately 84% of "
            "Indigenous women have experienced violence in their lifetime. 97% of "
            "violent crime against Indigenous women is committed by non-Native men, "
            "creating complex jurisdictional barriers to prosecution."
        ),
        "city": "Washington", "state": "DC",
        "lat": 38.9072, "lng": -77.0369,
        "date_incident": "2018-11-14",
        "violence_type": "coercive_control",
        "status": "documented",
        "source_url": "https://www.uihi.org/resources/missing-and-murdered-indigenous-women-girls/",
        "source_name": "Urban Indian Health Institute — MMIW Report 2018",
        "verified": True,
        "is_public_figure": False,
    },
    {
        "summary": (
            "Sovereign Bodies Institute — MMIW Database. The Sovereign Bodies "
            "Institute maintains the most comprehensive database of MMIW cases in "
            "North America. As of 2023, the database documents over 14,000 cases "
            "of missing and murdered Indigenous women and girls — the vast majority "
            "never investigated by federal or state authorities. The institute found "
            "that law enforcement agencies routinely misclassify Indigenous victims "
            "as runaways, fail to enter cases into national databases, and close "
            "cases without investigation. In many reservation communities, women "
            "have disappeared without a single law enforcement interview of potential "
            "witnesses. The database reveals that homicide clearance rates for "
            "Indigenous victims are significantly lower than for white victims."
        ),
        "city": "Arcata", "state": "CA",
        "lat": 40.8665, "lng": -124.0828,
        "date_incident": "2023-01-01",
        "violence_type": "homicide",
        "status": "documented",
        "source_url": "https://sovereign-bodies.org/sbi-database/",
        "source_name": "Sovereign Bodies Institute — MMIW Database",
        "verified": True,
        "is_public_figure": False,
    },

    # ── JURISDICTIONAL FAILURE ────────────────────────────────────────────────
    {
        "summary": (
            "Jurisdictional Gap — The Federal Hole That Lets Abusers Walk Free. "
            "Until 2013, tribal courts had no authority to prosecute non-Native men "
            "who committed violence against Native women on tribal land — even if the "
            "perpetrator lived on the reservation, was married to a tribal member, "
            "or had prior convictions. The Supreme Court ruling Oliphant v. Suquamish "
            "(1978) stripped tribes of this jurisdiction. This created a documented "
            "safe harbor: non-Native men could assault, rape, or kill Native women "
            "on reservations knowing tribal police could not arrest them and federal "
            "prosecutors rarely pursued cases. The 2013 VAWA reauthorization restored "
            "limited tribal jurisdiction — but only for domestic violence, not sexual "
            "assault by strangers. The 2022 VAWA reauthorization expanded this, but "
            "implementation remains incomplete. 97% of perpetrators of violence "
            "against Indigenous women are non-Native — this was not accidental."
        ),
        "city": "Washington", "state": "DC",
        "lat": 38.9072, "lng": -77.0369,
        "date_incident": "1978-03-06",
        "violence_type": "coercive_control",
        "status": "documented",
        "source_url": "https://www.ncai.org/policy-issues/tribal-governance/public-safety-and-justice/mmiw",
        "source_name": "NCAI — Oliphant v. Suquamish / VAWA Tribal Jurisdiction",
        "verified": True,
        "is_public_figure": False,
    },
    {
        "summary": (
            "FBI NCIC Failure — Indigenous Women Not Entered Into National Database. "
            "A 2021 GAO investigation found that law enforcement agencies — including "
            "federal agencies — routinely failed to enter missing Indigenous persons "
            "into the National Crime Information Center (NCIC) database. Without NCIC "
            "entry, cases are invisible to other agencies. The GAO found that BIA and "
            "FBI lacked formal agreements for sharing case information, had no "
            "standardized protocols for Indigenous missing persons cases, and could "
            "not account for thousands of open cases. The BIA's tribal justice "
            "programs were found to be chronically underfunded — some reservation "
            "communities of thousands had no law enforcement presence at night. "
            "The GAO recommended 15 corrective actions. As of 2023, fewer than "
            "half had been implemented."
        ),
        "city": "Washington", "state": "DC",
        "lat": 38.9072, "lng": -77.0369,
        "date_incident": "2021-07-20",
        "violence_type": "coercive_control",
        "status": "documented",
        "source_url": "https://www.gao.gov/products/gao-21-530",
        "source_name": "GAO-21-530 — Missing Indigenous Persons: Lack of Data",
        "verified": True,
        "is_public_figure": False,
    },

    # ── DOCUMENTED CASES ─────────────────────────────────────────────────────
    {
        "summary": (
            "Savanna's Act (2020) — Named for Savanna LaFontaine-Greywind. "
            "Savanna LaFontaine-Greywind, 22, was eight months pregnant when she "
            "was murdered by her neighbors in Fargo, North Dakota in August 2017. "
            "Her body was found in the Red River wrapped in plastic wrap. Her "
            "neighbors had cut her baby from her womb. Savanna's murder — and the "
            "inadequate initial law enforcement response — galvanized the MMIW "
            "movement and led directly to the passage of Savanna's Act (2020), "
            "which directed the DOJ to update protocols for responding to missing "
            "and murdered Indigenous people. Her killers were convicted. The baby "
            "survived. Savanna's Act was a landmark but advocates note it lacks "
            "mandatory enforcement mechanisms and dedicated funding."
        ),
        "city": "Fargo", "state": "ND",
        "lat": 46.8772, "lng": -96.7898,
        "date_incident": "2017-08-19",
        "violence_type": "homicide",
        "status": "convicted",
        "source_url": "https://www.congress.gov/bill/116th-congress/senate-bill/227",
        "source_name": "Savanna's Act — US Congress / DOJ",
        "verified": True,
        "is_public_figure": False,
    },
    {
        "summary": (
            "Hanna Harris, 21, Northern Cheyenne Nation, Montana. Disappeared July 4, "
            "2013 after a party on the Northern Cheyenne Reservation. Her body was "
            "found weeks later. Family members conducted their own search after "
            "reporting her missing — tribal and federal law enforcement were slow "
            "to respond. Her murder became a catalyst for Montana MMIW legislation "
            "and national advocacy. Her killer was convicted of deliberate homicide. "
            "Her case is one of thousands that illustrate the pattern: Indigenous "
            "women go missing, families search themselves, law enforcement responds "
            "inadequately, and if a perpetrator is caught it is often due to "
            "community pressure rather than systematic investigation."
        ),
        "city": "Lame Deer", "state": "MT",
        "lat": 45.6302, "lng": -106.6560,
        "date_incident": "2013-07-04",
        "violence_type": "homicide",
        "status": "convicted",
        "source_url": "https://www.theguardian.com/us-news/2019/jul/30/native-american-women-violence-mmiw-data",
        "source_name": "The Guardian — MMIW / Hanna Harris Case",
        "verified": True,
        "is_public_figure": False,
    },
    {
        "summary": (
            "Ashley HeavyRunner Loring, 20, Blackfeet Nation, Montana. Last seen "
            "June 2017 on the Blackfeet Reservation. Her sister Kimberly conducted "
            "a years-long search — walking the reservation, posting flyers, "
            "confronting indifferent law enforcement. The FBI did not open an "
            "investigation for over a year. Her case was featured in congressional "
            "testimony that directly led to passage of Savanna's Act and the "
            "Not Invisible Act. Her remains have never been found. Her sister "
            "testified before the Senate Committee on Indian Affairs: 'Ashley is "
            "not a cold case. She is my sister.' Her disappearance represents the "
            "rule, not the exception — most MMIW cases receive no federal attention "
            "until advocates force public awareness."
        ),
        "city": "Browning", "state": "MT",
        "lat": 48.5560, "lng": -113.0160,
        "date_incident": "2017-06-01",
        "violence_type": "homicide",
        "status": "unsolved",
        "source_url": "https://www.indian-affairs.senate.gov/hearings/examining-the-harms-to-native-americans-resulting-from-the-indian-child-welfare-act",
        "source_name": "Senate Committee on Indian Affairs — Ashley HeavyRunner Loring Testimony",
        "verified": True,
        "is_public_figure": False,
    },
    {
        "summary": (
            "Not Invisible Act (2020) — Federal Response to MMIW Crisis. Signed "
            "into law alongside Savanna's Act, the Not Invisible Act established a "
            "joint commission of tribal leaders, law enforcement, and survivors to "
            "make recommendations on reducing violent crime against Indigenous people. "
            "The commission's 2023 report found: chronic underfunding of tribal law "
            "enforcement, lack of victim services in rural reservation communities, "
            "failure of federal agencies to coordinate, and near-total absence of "
            "culturally appropriate trauma services for Indigenous survivors. "
            "The report made 43 recommendations. Advocates note that without "
            "mandatory appropriations, the act risks becoming another unfunded "
            "mandate — a pattern repeated throughout the history of federal "
            "promises to tribal nations."
        ),
        "city": "Washington", "state": "DC",
        "lat": 38.9072, "lng": -77.0369,
        "date_incident": "2023-11-01",
        "violence_type": "coercive_control",
        "status": "documented",
        "source_url": "https://www.doi.gov/sites/doi.gov/files/not-invisible-act-commission-report-2023.pdf",
        "source_name": "Not Invisible Act Commission Report 2023 — DOI",
        "verified": True,
        "is_public_figure": False,
    },
    {
        "summary": (
            "Highway of Tears — British Columbia / Northern US Border. A 724km "
            "stretch of Highway 16 in British Columbia has seen the disappearance "
            "or murder of at least 18 women — predominantly Indigenous — since 1969. "
            "Actual numbers are believed to be far higher. The remote highway, "
            "sparse policing, and hitchhiking as the only transport option for "
            "women in isolated communities created conditions exploited by predators. "
            "Canadian and US Indigenous advocates have linked the corridor to "
            "cross-border patterns of predation against Indigenous women. "
            "Despite years of advocacy, a formal joint US-Canada task force has "
            "never been established. The highway is emblematic of how geographic "
            "isolation, poverty, and law enforcement indifference converge to "
            "endanger Indigenous women."
        ),
        "city": "Havre", "state": "MT",
        "lat": 48.5500, "lng": -109.6800,
        "date_incident": "2000-01-01",
        "violence_type": "homicide",
        "status": "unsolved",
        "source_url": "https://www.highwayoftears.ca/",
        "source_name": "Highway of Tears Initiative",
        "verified": True,
        "is_public_figure": False,
    },
    {
        "summary": (
            "Urban Indigenous Women — Invisible in the MMIW Count. The MMIW crisis "
            "is most associated with reservations, but the Urban Indian Health "
            "Institute found that 56% of documented MMIW cases occurred in urban "
            "areas — yet urban Indigenous women receive virtually no targeted "
            "services or law enforcement attention. Urban Indigenous women are often "
            "not recognized as Native by police, are not connected to tribal "
            "resources, and fall through the cracks of both tribal and municipal "
            "systems. The UIHI documented cases in 71 cities — Seattle, Albuquerque, "
            "Phoenix, and Anchorage had the highest numbers. In most cases, urban "
            "police departments had no protocols for identifying or responding to "
            "Indigenous victims, and many cases were never connected to the broader "
            "MMIW data set."
        ),
        "city": "Seattle", "state": "WA",
        "lat": 47.6062, "lng": -122.3321,
        "date_incident": "2018-11-14",
        "violence_type": "coercive_control",
        "status": "documented",
        "source_url": "https://www.uihi.org/resources/missing-and-murdered-indigenous-women-girls/",
        "source_name": "Urban Indian Health Institute — Urban MMIW Report",
        "verified": True,
        "is_public_figure": False,
    },
    {
        "summary": (
            "Man Camps and Resource Extraction — Documented Surge in Violence. "
            "Research by the Sovereign Bodies Institute and tribal nations documents "
            "a consistent pattern: when oil, gas, or mining operations establish "
            "'man camps' — temporary worker housing — near Indigenous communities, "
            "rates of violence against Indigenous women surge. During the Bakken oil "
            "boom in North Dakota, the Standing Rock Sioux Tribe documented a "
            "dramatic increase in sex trafficking, assault, and murder of Indigenous "
            "women near man camp sites. Similar patterns were documented near the "
            "Dakota Access Pipeline construction. Perpetrators are predominantly "
            "non-Native workers. Tribal police lack jurisdiction. Federal authorities "
            "rarely intervene. The connection between resource extraction and "
            "Indigenous women's safety has been documented in congressional testimony "
            "but has not resulted in mandatory safety requirements for energy projects."
        ),
        "city": "Standing Rock", "state": "ND",
        "lat": 45.8736, "lng": -100.5382,
        "date_incident": "2016-04-01",
        "violence_type": "trafficking",
        "status": "documented",
        "source_url": "https://sovereign-bodies.org/man-camps/",
        "source_name": "Sovereign Bodies Institute — Man Camps Report",
        "verified": True,
        "is_public_figure": False,
    },
]


def main():
    print("[Seed MMIW] Seeding Missing and Murdered Indigenous Women records...")
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
            print(f"  Skipped (failed normalization): {rec.get('summary','')[:60]}")

    from medusa.database import get_case_count
    print(f"[Seed MMIW] {saved}/{len(RECORDS)} records saved.")
    print(f"Total in database: {get_case_count()}")


if __name__ == "__main__":
    main()
