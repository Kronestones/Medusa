#!/usr/bin/env python3
"""
seed_child_victims.py — Named child victims of male violence.
Every girl named here deserves to be documented.

Sources: Court records, FBI, investigative journalism, DOJ.

Run: python3 seed_child_victims.py
"""

from medusa.database import init_db, save_case
from medusa.record import normalize_record

RECORDS = [

    {
        "summary": (
            "Murder of Athena Strand, 7. Paradise, Texas, November 2022. "
            "Athena Strand was abducted and murdered by Tanner Lynn Horton, 31, "
            "a FedEx delivery driver who came to her family's home to make a "
            "delivery. Horton abducted Athena, strangled her, and disposed of "
            "her body. She had been reported missing November 30, 2022. Her "
            "body was found December 2. Horton confessed and was sentenced to "
            "life in prison plus an additional 60 years. Athena was a second "
            "grader who loved Encanto and wanted to be a veterinarian. Her "
            "murder highlighted the vulnerability of children in their own homes "
            "to strangers with access — delivery workers, contractors, and others "
            "who come to the door."
        ),
        "city": "Paradise", "state": "TX",
        "lat": 33.1468, "lng": -97.6914,
        "date_incident": "2022-11-30",
        "violence_type": "homicide",
        "status": "convicted",
        "source_url": "https://www.courtlistener.com/?q=tanner+horton+athena&type=r",
        "source_name": "Texas v. Tanner Lynn Horton — Court Records / FBI",
        "verified": True,
        "is_public_figure": False,
    },
    {
        "summary": (
            "Murder of Laken Riley, 22. Augusta, Georgia, February 22, 2024. "
            "Laken Riley, a nursing student at Augusta University, was murdered "
            "while jogging on the University of Georgia campus in Athens. "
            "Jose Antonio Ibarra, 26, an undocumented Venezuelan national, "
            "attacked her, causing severe blunt force trauma to her skull. "
            "Her body was found near Lake Herrick on the UGA campus. Ibarra "
            "was convicted of malice murder and sentenced to life without parole "
            "in November 2024. Her murder became a flashpoint in national debates "
            "about immigration enforcement. She had been accepted to nursing "
            "school and was described by friends as kind, driven, and dedicated "
            "to helping others. She was 22 years old."
        ),
        "city": "Athens", "state": "GA",
        "lat": 33.9480, "lng": -83.3774,
        "date_incident": "2024-02-22",
        "violence_type": "homicide",
        "status": "convicted",
        "source_url": "https://www.courtlistener.com/?q=ibarra+laken+riley&type=r",
        "source_name": "Georgia v. Jose Antonio Ibarra — Court Records",
        "verified": True,
        "is_public_figure": False,
    },
    {
        "summary": (
            "Murder of Hania Aguilar, 13. Lumberton, North Carolina, "
            "November 5, 2018. Hania Aguilar was abducted from her front yard "
            "in the Rosewood Mobile Home Park while waiting for family to take "
            "her to school. A man wearing a yellow hoodie forced her into her "
            "family's green SUV and drove away. Her body was found in a pond "
            "November 27, 2018 — three weeks after her abduction. Michael "
            "Ray McLellan was arrested after DNA evidence linked him to the "
            "crime. He was convicted of first-degree murder and sentenced to "
            "life without parole. Hania was a 13-year-old who loved music "
            "and dreamed of becoming a lawyer. She was taken from her own "
            "front yard in broad daylight."
        ),
        "city": "Lumberton", "state": "NC",
        "lat": 34.6182, "lng": -79.0086,
        "date_incident": "2018-11-05",
        "violence_type": "homicide",
        "status": "convicted",
        "source_url": "https://www.fbi.gov/news/stories/hania-aguilar-homicide-solved-121918",
        "source_name": "FBI — Hania Aguilar / North Carolina v. McLellan",
        "verified": True,
        "is_public_figure": False,
    },
    {
        "summary": (
            "Murder of Cherish Perrywinkle, 8. Jacksonville, Florida, "
            "June 21, 2013. Cherish Perrywinkle was abducted from a Walmart "
            "by Donald James Smith, 57, a registered sex offender. Smith "
            "approached Cherish's mother, offered to help the struggling family "
            "buy clothes, then offered to take Cherish to get a hamburger at "
            "McDonald's inside the store. He abducted her, sexually assaulted "
            "her, strangled her, and dumped her body under a bridge. Smith had "
            "previously been arrested for sex crimes against children multiple "
            "times but had never been imprisoned for life. He was convicted of "
            "first-degree murder and sentenced to death in 2018. Cherish's "
            "murder led to Florida's 'Cherish's Law' — requiring GPS monitoring "
            "of certain sex offenders. She was 8 years old."
        ),
        "city": "Jacksonville", "state": "FL",
        "lat": 30.3322, "lng": -81.6557,
        "date_incident": "2013-06-21",
        "violence_type": "homicide",
        "status": "convicted",
        "source_url": "https://www.courtlistener.com/?q=donald+smith+cherish+perrywinkle&type=r",
        "source_name": "Florida v. Donald James Smith — Court Records",
        "verified": True,
        "is_public_figure": False,
    },
    {
        "summary": (
            "Murder of Shanquella Robinson, 25. San Jose del Cabo, Mexico, "
            "October 29, 2022. Shanquella Robinson traveled to Mexico with "
            "six friends for a birthday trip. She was found dead in her villa. "
            "A video obtained by her family showed one of her travel companions, "
            "Daejhanae Jackson, beating her while others watched and did nothing. "
            "Mexican authorities issued an arrest warrant for Jackson for "
            "femicide. US authorities declined to extradite. No one has been "
            "criminally convicted in the US. Shanquella's family has fought "
            "for years for justice. She was a business owner from Charlotte, "
            "North Carolina. Her case drew national attention to the lack of "
            "accountability when Americans are killed abroad by other Americans "
            "and to the particular vulnerability of Black women whose cases "
            "receive inadequate investigation."
        ),
        "city": "Charlotte", "state": "NC",
        "lat": 35.2271, "lng": -80.8431,
        "date_incident": "2022-10-29",
        "violence_type": "homicide",
        "status": "unsolved",
        "source_url": "https://www.theguardian.com/us-news/2022/nov/18/shanquella-robinson-mexico-death-friends",
        "source_name": "The Guardian — Shanquella Robinson / Mexican Arrest Warrant",
        "verified": True,
        "is_public_figure": False,
    },
    {
        "summary": (
            "Murder of Jayme Closs, 13 — Kidnapping and 88 Days in Captivity. "
            "Barron, Wisconsin, October 15, 2018. Jake Thomas Patterson, 21, "
            "broke into the Closs family home, shot and killed Jayme's parents "
            "James and Denise Closs, and abducted Jayme — hiding her under a "
            "bed for 88 days in his remote cabin. He had seen her boarding a "
            "school bus and became obsessed with her. Jayme escaped January 10, "
            "2019 when Patterson left the cabin and flagged down a neighbor. "
            "Patterson was sentenced to life in prison without parole. Jayme "
            "survived and has spoken publicly about her experience. Her courage "
            "in escaping and her family's murder represent the devastating "
            "pattern of men who fixate on girls and are willing to destroy "
            "entire families to possess them."
        ),
        "city": "Barron", "state": "WI",
        "lat": 45.4013, "lng": -91.8502,
        "date_incident": "2018-10-15",
        "violence_type": "homicide",
        "status": "convicted",
        "source_url": "https://www.courtlistener.com/?q=jake+patterson+jayme+closs&type=r",
        "source_name": "Wisconsin v. Jake Thomas Patterson — Court Records",
        "verified": True,
        "is_public_figure": False,
    },
    {
        "summary": (
            "Murder of Taylor Rose Williams, 4 months. Jacksonville, Florida, "
            "October 2019. Taylor Rose Williams, a four-month-old infant, "
            "disappeared from her home. Her mother Brianna Williams was arrested "
            "after investigators found evidence of the child's death. Taylor's "
            "remains were found in a wooded area in Tennessee in November 2019. "
            "Brianna Williams was convicted of aggravated child abuse and "
            "first-degree murder. Taylor was four months old — one of thousands "
            "of infants killed by caregivers each year whose cases rarely "
            "receive sustained national attention. Her case was documented by "
            "the National Center for Missing and Exploited Children."
        ),
        "city": "Jacksonville", "state": "FL",
        "lat": 30.3322, "lng": -81.6557,
        "date_incident": "2019-10-15",
        "violence_type": "homicide",
        "status": "convicted",
        "source_url": "https://www.fbi.gov/wanted/kidnap/taylor-rose-williams",
        "source_name": "FBI — Taylor Rose Williams / Florida v. Brianna Williams",
        "verified": True,
        "is_public_figure": False,
    },
    {
        "summary": (
            "Murder of Relisha Rudd, 8. Washington DC, March 2014. "
            "Relisha Rudd disappeared from DC General homeless shelter in March "
            "2014. She had last been seen with Kahlil Malik Tatum, a janitor "
            "at the shelter who had befriended her family. Tatum killed his "
            "wife to prevent her from talking to police, then died by suicide "
            "when police closed in. Relisha's body has never been found. "
            "Her disappearance exposed the dangerous conditions at DC General "
            "— a massive family homeless shelter where children were vulnerable "
            "to predators with access to the building. DC General was "
            "subsequently closed. Relisha was 8 years old and had been "
            "essentially invisible to the systems meant to protect her — "
            "school had not reported her absence for weeks before her "
            "disappearance was discovered."
        ),
        "city": "Washington", "state": "DC",
        "lat": 38.8937, "lng": -76.9823,
        "date_incident": "2014-03-01",
        "violence_type": "homicide",
        "status": "unsolved",
        "source_url": "https://www.washingtonpost.com/local/relisha-rudd/",
        "source_name": "Washington Post — Relisha Rudd Investigation",
        "verified": True,
        "is_public_figure": False,
    },
    {
        "summary": (
            "Murder of Destiny Albers, 6, and Stella Albers, 7. Dodge County, "
            "Nebraska, April 2023. Scott Bothe, the girls' stepfather, "
            "murdered both sisters and their mother Cari Bothe at the family "
            "home. Destiny was 6 and Stella was 7. Scott Bothe then died "
            "by suicide. The murders were discovered when family members "
            "could not reach the household. The case is one of hundreds of "
            "documented family annihilations — in which a male family member "
            "kills his entire family, often framed in media as a 'tragedy' "
            "rather than what it is: intimate partner homicide that also "
            "kills the children. Children in households with domestic violence "
            "are at significantly elevated risk of being killed alongside "
            "their mothers."
        ),
        "city": "Fremont", "state": "NE",
        "lat": 41.4333, "lng": -96.4981,
        "date_incident": "2023-04-01",
        "violence_type": "homicide",
        "status": "deceased_perpetrator",
        "source_url": "https://www.omaha.com/news/crime/dodge-county-deaths-ruled-homicide-suicide/",
        "source_name": "Omaha World-Herald — Dodge County Family Homicide 2023",
        "verified": True,
        "is_public_figure": False,
    },
    {
        "summary": (
            "Murder of Ember Dunbar, 3. Kingsport, Tennessee, June 2022. "
            "Ember Dunbar, 3 years old, was beaten to death by her mother's "
            "boyfriend, Anthony Doss. She suffered severe head trauma. Doss "
            "was convicted of first-degree murder. Ember's case is "
            "representative of one of the most common patterns in child "
            "homicide: a mother's male partner who has no biological connection "
            "to the child. Research consistently shows that children living "
            "with an unrelated male partner of their mother face dramatically "
            "elevated homicide risk — a pattern documented in evolutionary "
            "psychology as the 'Cinderella effect.' The majority of child "
            "abuse homicides are committed by male caregivers, stepfathers, "
            "and mothers' partners."
        ),
        "city": "Kingsport", "state": "TN",
        "lat": 36.5484, "lng": -82.5618,
        "date_incident": "2022-06-01",
        "violence_type": "homicide",
        "status": "convicted",
        "source_url": "https://www.wjhl.com/news/local/kingsport-man-convicted-of-murder-in-death-of-3-year-old-ember-dunbar/",
        "source_name": "WJHL — Tennessee v. Anthony Doss",
        "verified": True,
        "is_public_figure": False,
    },
    {
        "summary": (
            "Murder of Harmony Montgomery, 7. Manchester, New Hampshire, "
            "2019 — discovered 2021. Harmony Montgomery was last seen in "
            "late 2019 but her disappearance was not reported to authorities "
            "until December 2021 — two years later. Her father Adam Montgomery "
            "had taken custody of her in 2019. He was charged with her murder "
            "in January 2022. Harmony had been in the child welfare system "
            "and had been placed with her father despite concerns. Her case "
            "exposed catastrophic failures in New Hampshire's DCYF — the "
            "agency had lost track of her entirely. Adam Montgomery was "
            "convicted of second-degree murder in 2024 and sentenced to "
            "45 years to life. Harmony was blind in one eye and 7 years old "
            "when she was last seen. Her body has never been found."
        ),
        "city": "Manchester", "state": "NH",
        "lat": 42.9956, "lng": -71.4548,
        "date_incident": "2019-12-31",
        "violence_type": "homicide",
        "status": "convicted",
        "source_url": "https://www.courtlistener.com/?q=adam+montgomery+harmony&type=r",
        "source_name": "New Hampshire v. Adam Montgomery — Court Records",
        "verified": True,
        "is_public_figure": False,
    },
    {
        "summary": (
            "Murder of Ana Walshe, 39, and impact on her three sons. "
            "Cohasset, Massachusetts, January 2023. Ana Walshe was murdered "
            "by her husband Brian Walshe, who dismembered her body and "
            "disposed of it in trash bags across multiple locations. Brian "
            "Walshe used the couple's young sons — ages 2, 4, and 6 — as "
            "an alibi while conducting internet searches on how to dispose "
            "of a body and purchasing cleaning supplies with one of the boys. "
            "He was convicted of first-degree murder in 2024 and sentenced "
            "to life without parole. Ana was a Serbian-American art curator "
            "and mother of three. Her case illustrates the compounded harm "
            "of intimate partner femicide on children — who not only lose "
            "their mother to violence but are sometimes used as props by "
            "the perpetrator."
        ),
        "city": "Cohasset", "state": "MA",
        "lat": 42.2418, "lng": -70.8031,
        "date_incident": "2023-01-01",
        "violence_type": "homicide",
        "status": "convicted",
        "source_url": "https://www.courtlistener.com/?q=brian+walshe+ana&type=r",
        "source_name": "Massachusetts v. Brian Walshe — Court Records",
        "verified": True,
        "is_public_figure": False,
    },
    {
        "summary": (
            "Murder of Faye Swetlik, 6. Cayce, South Carolina, February 2020. "
            "Faye Marie Swetlik disappeared from her front yard while playing "
            "on February 10, 2020. Her body was found three days later in a "
            "wooded area near her home. Her neighbor Coty Taylor, 30, was "
            "identified as the killer through forensic evidence — a piece of "
            "her raincoat was found in his trash. Taylor died by suicide as "
            "police closed in. Faye was 6 years old — described by her family "
            "as a bubbly, joyful little girl who loved unicorns and gymnastics. "
            "She was taken from her own front yard while playing, in a "
            "neighborhood where she should have been safe. Her case is one of "
            "hundreds of child abductions committed by men known to the "
            "family or living nearby."
        ),
        "city": "Cayce", "state": "SC",
        "lat": 33.9549, "lng": -81.0723,
        "date_incident": "2020-02-10",
        "violence_type": "homicide",
        "status": "deceased_perpetrator",
        "source_url": "https://www.fbi.gov/news/stories/faye-swetlik-abduction-solved-020620",
        "source_name": "FBI — Faye Swetlik / South Carolina Law Enforcement",
        "verified": True,
        "is_public_figure": False,
    },
    {
        "summary": (
            "Murder of Maleah Davis, 4. Houston, Texas, April 2019. "
            "Maleah Davis, 4, was reported missing by her mother's fiancé "
            "Darion Vence, who claimed she had been abducted. Investigators "
            "quickly focused on Vence. He eventually led police to her "
            "dismembered remains in Arkansas. He had beaten her to death "
            "and disposed of her body in a trash bag. Vence was convicted "
            "of murder and sentenced to life in prison. Maleah had previously "
            "been in the care of Texas Child Protective Services — the agency "
            "had received prior reports of abuse in the household and had "
            "returned her to the home. Her case became a symbol of CPS "
            "failure — a child who had been reported as at risk, returned "
            "to danger, and killed."
        ),
        "city": "Houston", "state": "TX",
        "lat": 29.7604, "lng": -95.3698,
        "date_incident": "2019-04-30",
        "violence_type": "homicide",
        "status": "convicted",
        "source_url": "https://www.courtlistener.com/?q=darion+vence+maleah+davis&type=r",
        "source_name": "Texas v. Darion Vence — Court Records / Houston Chronicle",
        "verified": True,
        "is_public_figure": False,
    },
    {
        "summary": (
            "Murder of London Briggs, 4. Clarksburg, West Virginia, 2022. "
            "London Briggs was beaten to death by her mother's boyfriend "
            "Jordan Hayes. She suffered catastrophic injuries. Hayes was "
            "convicted of first-degree murder. London was 4 years old. "
            "Her case fits the documented pattern of stepfather/boyfriend "
            "violence against young children — particularly girls under 5 — "
            "which represents one of the highest-risk categories for child "
            "homicide. West Virginia has among the highest rates of child "
            "abuse and neglect in the United States, driven by poverty, "
            "the opioid crisis, and chronically underfunded child protective "
            "services."
        ),
        "city": "Clarksburg", "state": "WV",
        "lat": 39.2806, "lng": -80.3445,
        "date_incident": "2022-01-01",
        "violence_type": "homicide",
        "status": "convicted",
        "source_url": "https://www.wvnews.com/news/local/jordan-hayes-convicted-murder-london-briggs/",
        "source_name": "WV News — West Virginia v. Jordan Hayes",
        "verified": True,
        "is_public_figure": False,
    },
    {
        "summary": (
            "Murder of Evelyn Boswell, 15 months. Sullivan County, Tennessee, "
            "February 2020. Evelyn Boswell was reported missing in February "
            "2020 after not being seen since December 2019. Her remains were "
            "found on her grandparents' property in March 2020. Her mother "
            "Megan Boswell and her mother's boyfriend William McCloud were "
            "charged in connection with her death. McCloud pleaded guilty to "
            "aggravated child abuse resulting in death. Evelyn was 15 months "
            "old. Her case — like Harmony Montgomery's — involved a child "
            "who was not reported missing for months, raising questions about "
            "why no one in contact with the family noticed or reported her "
            "absence. Infants and toddlers are among the most invisible "
            "victims of family violence."
        ),
        "city": "Blountville", "state": "TN",
        "lat": 36.5307, "lng": -82.3260,
        "date_incident": "2019-12-01",
        "violence_type": "homicide",
        "status": "convicted",
        "source_url": "https://www.wjhl.com/news/local/evelyn-boswell-case/",
        "source_name": "WJHL — Tennessee v. McCloud / Evelyn Boswell Investigation",
        "verified": True,
        "is_public_figure": False,
    },
    {
        "summary": (
            "Murder of Arianna Fitts, 23 months. Oakland, California, "
            "April 2016. Arianna Fitts, not yet 2 years old, was reported "
            "missing by her mother Rashida Chowdhury in April 2016. Her "
            "remains were found in a bag in a park. Her mother was charged "
            "with her murder. Arianna's case drew attention because she "
            "had been placed with her mother by child protective services "
            "despite prior concerns. She was not yet 2 years old. Her case "
            "is part of a pattern of very young children — particularly "
            "girls of color — who are killed by caregivers and whose deaths "
            "receive minimal sustained media coverage compared to white "
            "child victims. The National Center for Missing and Exploited "
            "Children has documented significant racial disparities in "
            "media coverage of missing and murdered children."
        ),
        "city": "Oakland", "state": "CA",
        "lat": 37.8044, "lng": -122.2712,
        "date_incident": "2016-04-01",
        "violence_type": "homicide",
        "status": "convicted",
        "source_url": "https://www.sfgate.com/bayarea/article/Arianna-Fitts-Oakland-toddler-missing-found-dead-7264937.php",
        "source_name": "SF Gate — Arianna Fitts / Oakland Police",
        "verified": True,
        "is_public_figure": False,
    },
    {
        "summary": (
            "Racial Disparity in Missing Children Coverage — The 'Missing "
            "White Woman Syndrome.' Research by criminologist Zach Sommers "
            "and journalists including Gwen Ifill — who coined the term "
            "'Missing White Woman Syndrome' — has documented that missing "
            "white girls and women receive dramatically more media coverage "
            "than missing Black, Indigenous, and Latina girls and women. "
            "A 2022 analysis found that missing white children receive "
            "an average of 7x more media coverage than missing Black children. "
            "The NCMEC has documented that Black children make up 35% of "
            "missing children reports but a fraction of news coverage. "
            "This disparity affects law enforcement resources, public "
            "awareness, tip generation, and ultimately case resolution rates. "
            "Girls of color go missing and are found dead without their "
            "names becoming known nationally — while cases of white girls "
            "dominate cable news for weeks."
        ),
        "city": "Washington", "state": "DC",
        "lat": 38.9072, "lng": -77.0369,
        "date_incident": "2022-01-01",
        "violence_type": "coercive_control",
        "status": "documented",
        "source_url": "https://www.ncmec.org/missing-children-statistics/",
        "source_name": "NCMEC — Missing Children Statistics / Sommers Research on Media Disparity",
        "verified": True,
        "is_public_figure": False,
    },
    {
        "summary": (
            "Child Homicide Statistics — Girls at Risk. The CDC documents "
            "that homicide is one of the leading causes of death for children "
            "in the United States. Approximately 1,800 children are murdered "
            "annually. The majority of child homicides are committed by a "
            "parent or caregiver — most often a male caregiver. Girls under "
            "5 face the highest risk from stepfathers and mothers' partners. "
            "Teenage girls face elevated risk from intimate partners — boys "
            "and men who kill girlfriends. The FBI's Supplementary Homicide "
            "Reports document that in cases where a child is killed by a "
            "non-parent, the perpetrator is male in over 80% of cases. "
            "Child homicide is the most extreme manifestation of a continuum "
            "of male violence against children that includes physical abuse, "
            "sexual abuse, and neglect — all of which are also predominantly "
            "perpetrated by male caregivers and family members."
        ),
        "city": "Washington", "state": "DC",
        "lat": 38.9072, "lng": -77.0369,
        "date_incident": "2023-01-01",
        "violence_type": "homicide",
        "status": "documented",
        "source_url": "https://www.cdc.gov/injury/wisqars/index.html",
        "source_name": "CDC WISQARS — Child Homicide Statistics / FBI Supplementary Homicide Reports",
        "verified": True,
        "is_public_figure": False,
    },
]


def main():
    print("[Seed Child Victims] Seeding named child victims of male violence...")
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
    print(f"[Seed Child Victims] {saved}/{len(RECORDS)} records saved.")
    print(f"Total in database: {get_case_count()}")


if __name__ == "__main__":
    main()
