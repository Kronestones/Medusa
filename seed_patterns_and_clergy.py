"""
seed_patterns_and_clergy.py — Medusa

Three major topics:

1. CLERGY ABUSE — Systemic priest shuffling overview, Cardinal Bernard Law,
   Bishop John McCormack, Father John Geoghan, BishopAccountability.org
   database overview, Vatican ban on publishing accused lists (2025)

2. ONLINE DRUGGING/RAPE NETWORK — Dominique Pélicot (France), Motherless.com
   62M visits/month, Telegram groups, CNN investigation March 2026

3. HIKING TRAIL FEMICIDE PATTERN — Ivan Miller (Utah 2026), Rachel Morin
   (Maryland 2023), David Carpenter "The Trailside Killer" (CA 1979-81),
   Cathy Sposito (Arizona 1987/2023 cold case), Appalachian Trail 2019

Run:
    cd ~/medusa && python3 seed_patterns_and_clergy.py
"""

import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from medusa.database import init_db, save_case

CASES = [

    # ══════════════════════════════════════════════════════════════════════════
    # CLERGY — Systemic overview: priest shuffling pattern
    # ══════════════════════════════════════════════════════════════════════════

    {
        "case_id":        "stat_clergy_priest_shuffling_systemic",
        "violence_type":  "child_abuse",
        "status":         "congressional_record",
        "summary": (
            "The systematic transfer of credibly accused Catholic priests between "
            "parishes — known as 'priest shuffling' — is one of the most "
            "thoroughly documented institutional cover-ups in American history. "
            "Rather than reporting abusive priests to law enforcement, bishops "
            "across the United States and worldwide routinely transferred them "
            "to new parishes, giving them fresh access to children, while "
            "suppressing victims' reports and paying settlements with "
            "confidentiality clauses. "
            "The Boston Globe's Spotlight team exposed the practice in January "
            "2002, detailing how the Archdiocese of Boston — under Cardinal "
            "Bernard Law — had protected dozens of predator priests for decades. "
            "The investigation triggered a nationwide reckoning. By 2024, the "
            "names of more than 5,800 Catholic clergy credibly accused of sexual "
            "abuse had been publicly released by dioceses and religious orders "
            "across the United States. The Pennsylvania Grand Jury Report (2018) "
            "alone documented 300 predator priests and more than 1,000 victims "
            "across six dioceses over 70 years. "
            "Total financial settlements paid by the Catholic Church in the "
            "United States exceeded $3.5 billion by 2020. "
            "The most comprehensive public database of accused clergy is "
            "maintained by BishopAccountability.org, searchable by diocese, "
            "state, religious order, and name. ProPublica also maintains a "
            "searchable national database. "
            "In April 2025, Pope Francis banned dioceses from proactively "
            "publishing lists of credibly accused priests — a decision widely "
            "condemned by survivors as reinstating the culture of concealment. "
            "Sources: Boston Globe Spotlight; PA Grand Jury Report 2018; "
            "BishopAccountability.org; John Jay College Report 2004; "
            "ProPublica."
        ),
        "city":           "Washington",
        "state":          "DC",
        "lat":            38.9072,
        "lng":            -77.0369,
        "source_url":     "https://www.bishop-accountability.org/accused/",
        "source_name":    "BishopAccountability.org / Boston Globe Spotlight",
        "additional_sources": [
            {"url": "https://www.propublica.org/series/credibly-accused",
             "name": "ProPublica — Credibly Accused Database"},
            {"url": "https://www.attorneygeneral.gov/wp-content/uploads/2018/08/A-Report-of-the-Fortieth-Statewide-Investigating-Grand-Jury_Clean-Version.pdf",
             "name": "Pennsylvania Grand Jury Report 2018"},
        ],
        "verified":       True,
        "is_public_figure": False,
        "date_incident":  "2002-01-06",
    },

    # ══════════════════════════════════════════════════════════════════════════
    # CARDINAL BERNARD LAW — architect of Boston cover-up
    # ══════════════════════════════════════════════════════════════════════════

    {
        "case_id":        "cardinal_bernard_law_boston_coverup",
        "violence_type":  "child_abuse",
        "status":         "congressional_record",
        "summary": (
            "Cardinal Bernard Francis Law served as Archbishop of Boston from "
            "1984 to 2002. During his tenure he received detailed documentation "
            "of child sexual abuse by priests under his authority — including a "
            "letter from a fellow bishop in 1984 warning against reassigning "
            "Father John Geoghan — and repeatedly chose to transfer abusive "
            "priests to new parishes rather than report them to police. "
            "When accused priests became too high-profile, Law transferred some "
            "into military chaplaincy, placing them under federal jurisdiction "
            "and further out of diocesan accountability. "
            "Geoghan alone had sexually abused more than 130 boys across six "
            "Boston-area parishes over three decades while Law and predecessors "
            "moved him each time complaints arose. Law was personally aware "
            "of Geoghan's history when he approved a 1984 transfer to St. Julia's "
            "parish — where Geoghan abused more children. "
            "After the Boston Globe's Spotlight investigation exposed the "
            "cover-up in January 2002, Law resigned in December 2002. "
            "He faced no criminal charges. "
            "Pope John Paul II rewarded him with appointment as archpriest of "
            "the Basilica of Santa Maria Maggiore in Rome — one of the four "
            "principal basilicas in the Catholic Church — where he lived and "
            "worked comfortably until his death in 2017. He was also appointed "
            "to the Vatican's Congregation for Bishops, helping recommend "
            "episcopal appointments worldwide, even after his resignation "
            "in disgrace. He died unpunished at age 86. "
            "The Boston scandal triggered nationwide lawsuits, legislative reform, "
            "and the John Jay College study commissioned by the US Conference "
            "of Catholic Bishops, which found 4,392 priests with credible "
            "allegations against them between 1950 and 2002. "
            "Sources: Boston Globe Spotlight; Britannica; WBUR; IBTimes."
        ),
        "city":           "Boston",
        "state":          "MA",
        "lat":            42.3601,
        "lng":            -71.0589,
        "source_url":     "https://www.bostonglobe.com/news/special-reports/2002/01/06/church-allowed-abuse-priest-for-years/cSHfGkTIrAT25qKGvBuDNM/story.html",
        "source_name":    "Boston Globe Spotlight Investigation",
        "additional_sources": [
            {"url": "https://www.wbur.org/news/2015/09/22/cardinal-bernard-law",
             "name": "WBUR"},
            {"url": "https://www.britannica.com/topic/Catholic-Church-Sexual-Abuse-Crisis",
             "name": "Britannica — Catholic Church Sexual Abuse Crisis"},
        ],
        "verified":       True,
        "is_public_figure": True,
        "date_incident":  "1984-01-01",
    },

    # ══════════════════════════════════════════════════════════════════════════
    # FATHER JOHN GEOGHAN — serial abuser, 130+ victims, 6 parishes
    # ══════════════════════════════════════════════════════════════════════════

    {
        "case_id":        "father_john_geoghan_boston_ma",
        "violence_type":  "child_abuse",
        "status":         "convicted",
        "summary": (
            "Father John J. Geoghan was ordained in 1962 in Boston and became "
            "one of the most notorious documented pedophile priests in American "
            "history. Over three decades he sexually abused more than 130 boys "
            "— his youngest victim was four years old — across at least six "
            "Greater Boston parishes. Each time complaints were made, diocesan "
            "leadership moved him to a new parish rather than removing him from "
            "ministry or notifying police. "
            "In 1980 he told diocesan officials his repeated abuse of seven boys "
            "from one extended family was not a 'serious problem.' He was given "
            "therapy and reassigned. In 1984, Cardinal Law received a letter from "
            "a bishop warning against reassigning Geoghan, yet approved his "
            "transfer to St. Julia's parish in Weston — where he abused more "
            "children. The archdiocese had settled approximately 50 lawsuits "
            "against Geoghan by 1997, for over $10 million, all with "
            "confidentiality clauses. "
            "Geoghan was defrocked, convicted of indecent assault and battery "
            "on a 10-year-old boy, and sentenced to 9 to 10 years in prison. "
            "In August 2003, he was murdered in his cell at Souza-Baranowski "
            "Correctional Center by fellow inmate Joseph Druce. "
            "His case was the central subject of the Boston Globe's 2002 "
            "Spotlight investigation, portrayed in the 2015 Academy Award-winning "
            "film Spotlight. "
            "Sources: Boston Globe Spotlight; Britannica."
        ),
        "city":           "Boston",
        "state":          "MA",
        "lat":            42.3601,
        "lng":            -71.0589,
        "source_url":     "https://www.bostonglobe.com/news/special-reports/2002/01/06/church-allowed-abuse-priest-for-years/cSHfGkTIrAT25qKGvBuDNM/story.html",
        "source_name":    "Boston Globe Spotlight",
        "verified":       True,
        "is_public_figure": True,
        "date_incident":  "1962-01-01",
    },

    # ══════════════════════════════════════════════════════════════════════════
    # BISHOP JOHN McCORMACK — transferred abusive priests, NH diocese
    # ══════════════════════════════════════════════════════════════════════════

    {
        "case_id":        "bishop_john_mccormack_nh_coverup",
        "violence_type":  "child_abuse",
        "status":         "congressional_record",
        "summary": (
            "Bishop John B. McCormack served as director of ministerial personnel "
            "for the Boston Archdiocese from 1984 to 1994 under Cardinal Bernard "
            "Law, where he was responsible for investigating complaints of sexual "
            "misconduct by priests. According to published reports and court "
            "documents, McCormack repeatedly handled these complaints by "
            "transferring accused priests to different parishes rather than "
            "removing them from ministry or reporting them to police. "
            "He was later appointed Bishop of Manchester, New Hampshire. "
            "In 2002, New Hampshire prosecutors prepared child endangerment "
            "indictments against the Catholic Church — which would have been "
            "the first criminal indictment of a Catholic diocese in US history. "
            "McCormack averted prosecution by signing a 10-page agreement "
            "in December 2002 acknowledging the diocese had harmed children "
            "by moving abusive priests from parish to parish, and committing "
            "to strict child protection reforms and attorney general audits. "
            "The diocese paid out nearly $15.5 million in settlements to "
            "abuse victims over the preceding two years. "
            "McCormack died in 2022. He faced no criminal conviction. "
            "Sources: Union Leader; CBS News; AP."
        ),
        "city":           "Manchester",
        "state":          "NH",
        "lat":            42.9956,
        "lng":            -71.4548,
        "source_url":     "https://www.unionleader.com/news/religion/17-years-ago-nh-kicked-off-now-national-clergy-sex-abuse-scandal/article_968f71fc-1ad8-5215-800a-55bbce0db90e.html",
        "source_name":    "Union Leader / AP",
        "verified":       True,
        "is_public_figure": True,
        "date_incident":  "1984-01-01",
    },

    # ══════════════════════════════════════════════════════════════════════════
    # VATICAN BAN ON PUBLISHING ACCUSED PRIEST LISTS — April 2025
    # ══════════════════════════════════════════════════════════════════════════

    {
        "case_id":        "vatican_ban_accused_priest_lists_2025",
        "violence_type":  "child_abuse",
        "status":         "congressional_record",
        "summary": (
            "In April 2025, Pope Francis banned Catholic dioceses from "
            "proactively publishing lists of clergy credibly accused of sexual "
            "abuse of minors. The Vatican's instruction reversed a transparency "
            "practice that had been adopted by most US dioceses following the "
            "2002 Boston Globe Spotlight scandal and the 2018 Pennsylvania Grand "
            "Jury Report. Bishop Peter Libasci of Manchester, New Hampshire — "
            "who had published such a list in 2019 and updated it in 2024 — "
            "cited 'transparency' as his goal. "
            "Survivor advocacy organizations including SNAP (Survivors Network "
            "of those Abused by Priests) condemned the ban as reinstating the "
            "culture of concealment that had allowed abuse to continue for "
            "decades. The ban means that parents, parishioners, and communities "
            "can no longer access the names of credibly accused priests through "
            "official church channels. "
            "BishopAccountability.org and ProPublica continue to maintain "
            "independent public databases of accused clergy. "
            "Source: Catholic League; SNAP; BishopAccountability.org, April 2025."
        ),
        "city":           "Washington",
        "state":          "DC",
        "lat":            38.9072,
        "lng":            -77.0369,
        "source_url":     "https://www.catholicleague.org/vatican-bans-publishing-lists-of-credibly-accused-priests/",
        "source_name":    "Catholic League / SNAP / BishopAccountability.org",
        "verified":       True,
        "is_public_figure": False,
        "date_incident":  "2025-04-01",
    },

    # ══════════════════════════════════════════════════════════════════════════
    # DOMINIQUE PÉLICOT — drugged wife, invited 80+ men to rape her, France
    # ══════════════════════════════════════════════════════════════════════════

    {
        "case_id":        "dominique_pelicot_france_2024",
        "violence_type":  "sexual_assault",
        "status":         "convicted",
        "tab":            "global",
        "country":        "France",
        "summary": (
            "Dominique Pélicot, a French pensioner married for over 50 years, "
            "admitted in a 2024 French criminal trial that he had spent nearly "
            "a decade drugging his wife Gisèle Pélicot with the anti-anxiety "
            "drug lorazepam — mixed into her evening meals — rendering her "
            "unconscious, and then inviting dozens of strangers from an "
            "internet forum to rape her while she slept, which he filmed and "
            "meticulously archived on his computer in a folder labeled 'Abuses.' "
            "Video file titles recorded the date, a first name, and the nature "
            "of the act. "
            "Investigators identified 92 instances of sexual assault by 83 "
            "suspects. At least 51 men between the ages of 26 and 73 were "
            "arrested and charged. Dominique found his 'guests' on an internet "
            "forum called 'À son insu' ('Without Her Knowledge') — a community "
            "specifically organized around performing sexual acts on women "
            "without their consent, often while drugged. The forum was erased "
            "after being linked to a criminal investigation. "
            "Gisèle Pélicot waived her right to anonymity and insisted the "
            "trial be held in public, saying: 'Shame must change sides.' "
            "She attended every day of the trial. Dominique Pélicot was "
            "convicted and sentenced to 20 years — the maximum under French law. "
            "Her memoir launched in 22 languages in 2025. "
            "The case directly preceded a CNN investigation (March 2026) that "
            "found the online ecosystem enabling this kind of abuse was global, "
            "vast, and US-centered. "
            "Sources: The Independent; New York Times; Snopes; CNN."
        ),
        "city":           "Avignon",
        "state":          "DC",
        "lat":            43.9493,
        "lng":            4.8055,
        "source_url":     "https://www.aol.com/man-accused-filming-least-51-115037548.html",
        "source_name":    "The Independent / French Criminal Court",
        "additional_sources": [
            {"url": "https://www.snopes.com/fact-check/cnn-online-rape-academy/",
             "name": "Snopes — CNN Online Rape Academy fact check"},
        ],
        "verified":       True,
        "is_public_figure": False,
        "date_incident":  "2011-01-01",
    },

    # ══════════════════════════════════════════════════════════════════════════
    # MOTHERLESS.COM / ONLINE DRUGGING NETWORK — CNN investigation March 2026
    # ══════════════════════════════════════════════════════════════════════════

    {
        "case_id":        "stat_motherless_online_drugging_network_2026",
        "violence_type":  "sexual_assault",
        "status":         "congressional_record",
        "summary": (
            "In March 2026, CNN published a months-long investigation into a "
            "global online ecosystem enabling the drugging and rape of women "
            "by intimate partners. Key findings: "
            "Motherless.com — a US-based pornographic website that describes "
            "itself as a 'moral free file host where anything legal is hosted "
            "forever' — hosts more than 20,000 videos of so-called 'sleep' "
            "content uploaded by users, with hundreds of thousands of views. "
            "The site received approximately 62 million visits in February 2026 "
            "alone, with its core audience in the United States. "
            "German investigative journalists Isabell Beer and Isabel Ströh, "
            "reporting for the STRG_F documentary series, had previously "
            "uncovered a much larger international network: dozens of Telegram "
            "groups with up to 70,000 members each, dedicated to sharing "
            "techniques for drugging partners and videos of women being raped "
            "while unconscious. Their reporting triggered a political debate "
            "in Germany. "
            "The Pélicot case in France (2024) demonstrated the real-world "
            "outcome: a husband used the forum 'À son insu' ('Without Her "
            "Knowledge') to recruit 83 men to rape his unconscious drugged wife "
            "over approximately a decade. "
            "Snopes confirmed CNN's reporting was accurate on the site and its "
            "content but noted the 62 million figure referred to site visits "
            "rather than individual men. The scale of the network — regardless "
            "of precise user counts — represents one of the most documented "
            "examples of the industrialization of rape culture. "
            "Sources: CNN (March 2026); Snopes; STRG_F / Panorama die Reporter "
            "(Germany); The Independent."
        ),
        "city":           "New York",
        "state":          "NY",
        "lat":            40.7128,
        "lng":            -74.0060,
        "source_url":     "https://www.snopes.com/fact-check/cnn-online-rape-academy/",
        "source_name":    "CNN / Snopes / STRG_F Germany",
        "verified":       True,
        "is_public_figure": False,
        "date_incident":  "2026-03-01",
    },

    # ══════════════════════════════════════════════════════════════════════════
    # HIKING TRAIL FEMICIDE — Pattern overview
    # ══════════════════════════════════════════════════════════════════════════

    {
        "case_id":        "trend_hiking_trail_femicide_pattern",
        "violence_type":  "homicide",
        "status":         "congressional_record",
        "summary": (
            "Women are disproportionately targeted for sexual assault and murder "
            "on hiking trails and in outdoor recreational spaces across the "
            "United States. The pattern spans decades and is documented across "
            "multiple states. Perpetrators exploit the isolation of trails, the "
            "social expectation that outdoor spaces are safe, and women's reduced "
            "ability to call for help or escape. "
            "Documented cases include: David Carpenter, 'The Trailside Killer,' "
            "who murdered at least 10 people — mostly women — on trails in "
            "California's state parks near San Francisco between 1979 and 1981; "
            "Cathy Sposito, 23, killed on Thumb Butte Trail in Prescott, Arizona "
            "in 1987 — cold case solved by DNA in 2023; Rachel Morin, 37, mother "
            "of five, raped and murdered on a popular trail in Bel Air, Maryland "
            "in August 2023; Ivan Miller, 22, who randomly killed three women "
            "in Wayne County, Utah in March 2026 — two on a hiking trail and "
            "one elderly woman in her home; and a 2019 Appalachian Trail knife "
            "attack in Virginia in which one man was killed and a woman was "
            "stabbed multiple times and forced to play dead to survive. "
            "The threat is not confined to strangers: intimate partners and "
            "dating partners have also used hiking dates as settings for "
            "murder, particularly in cases where the killing was planned. "
            "The isolation of trails, combined with the social messaging that "
            "outdoor exercise is 'empowering' for women, creates a specific "
            "vulnerability that is under-documented as a pattern. "
            "Women's hiking safety organizations and trail advocacy groups "
            "have called for better lighting, trail cameras, and emergency "
            "call stations on popular trails. "
            "Sources: CBS News; CNN; Yahoo News; McClatchy."
        ),
        "city":           "Washington",
        "state":          "DC",
        "lat":            38.9072,
        "lng":            -77.0369,
        "source_url":     "https://www.cbsnews.com/news/3-women-found-dead-torrey-utah-hiking-trail-residence/",
        "source_name":    "CBS News / CNN / Yahoo News",
        "verified":       True,
        "is_public_figure": False,
        "date_incident":  "1979-01-01",
    },

    # ══════════════════════════════════════════════════════════════════════════
    # IVAN MILLER — Utah triple femicide on hiking trail, March 2026
    # ══════════════════════════════════════════════════════════════════════════

    {
        "case_id":        "ivan_miller_utah_hiking_triple_murder_2026",
        "violence_type":  "homicide",
        "status":         "charged",
        "summary": (
            "On March 5, 2026, Ivan Miller, 22, of Blakesburg, Iowa, traveled "
            "to rural Wayne County, Utah — near Capitol Reef National Park — "
            "where he committed three murders of women he had never met. "
            "He first entered the home of Margaret Oldroyd, 86, in Lyman, Utah, "
            "waited behind a door, and shot her in the back of the head. "
            "He then stole her Buick, drove to a nearby trailhead off State "
            "Route 12 near Torrey, Utah, and encountered Linda Dewey, 65, and "
            "her niece Natalie Graves, 34, who had been hiking together — "
            "'bonding over the beauty of a hike in one of their favorite places "
            "on Earth,' according to a family statement. "
            "Miller shot both women, then stabbed one multiple times when he "
            "realized she was still moving. He dragged their bodies into a ditch "
            "and stole their Subaru. Their husbands found the bodies and called "
            "dispatch that evening. "
            "Miller told investigators the killings 'had to be done.' He "
            "reportedly said he wanted to find a different vehicle — describing "
            "a motive as banal as car preference for ending three women's lives. "
            "He was arrested in Pagosa Springs, Colorado after the stolen "
            "vehicle was tracked across three states. "
            "He is charged with three counts of first-degree aggravated murder. "
            "Wayne County schools were closed for two days following the murders. "
            "Sources: CBS News; CNN; NBC News; ABC7."
        ),
        "city":           "Torrey",
        "state":          "UT",
        "lat":            38.2975,
        "lng":            -111.4176,
        "source_url":     "https://www.cbsnews.com/news/3-women-found-dead-torrey-utah-hiking-trail-residence/",
        "source_name":    "CBS News / Utah DPS",
        "additional_sources": [
            {"url": "https://www.cnn.com/2026/03/05/us/utah-women-deaths-wayne-county",
             "name": "CNN"},
            {"url": "https://www.aol.com/articles/2-women-were-bonding-over-025252352.html",
             "name": "NBC News"},
        ],
        "verified":       True,
        "is_public_figure": False,
        "date_incident":  "2026-03-05",
    },

    # ══════════════════════════════════════════════════════════════════════════
    # RACHEL MORIN — murdered on hiking trail, Bel Air MD, 2023
    # ══════════════════════════════════════════════════════════════════════════

    {
        "case_id":        "rachel_morin_bel_air_md_2023",
        "violence_type":  "homicide",
        "status":         "convicted",
        "summary": (
            "Rachel Morin, 37, a mother of five from Bel Air, Maryland, was "
            "raped and murdered on August 5, 2023, while exercising on the "
            "Ma & Pa Trail — a popular hiking trail northeast of Baltimore "
            "in Harford County. "
            "Prosecutors alleged Victor Martinez-Hernandez, 24, carried out "
            "a planned attack: he grabbed Morin off the trail, bashed her head "
            "against nearby rocks, raped her, and concealed her body in a "
            "drainage culvert where it was found the following day. "
            "DNA evidence collected from Morin's body matched Martinez-Hernandez. "
            "He had entered the United States illegally and was also linked to "
            "the killing of a woman in El Salvador and a 2023 home invasion "
            "in Los Angeles. He was arrested in Oklahoma in 2024. "
            "Martinez-Hernandez was convicted of first-degree murder and "
            "first-degree rape. Harford County Circuit Court Judge Yolanda "
            "Curtin sentenced him to life without the possibility of parole, "
            "plus an additional life sentence and 40 years. "
            "Rachel Morin left behind five children. Her case became a "
            "national flashpoint in immigration and border security debates "
            "during the 2024 presidential campaign. "
            "Sources: AP; Yahoo News."
        ),
        "city":           "Bel Air",
        "state":          "MD",
        "lat":            39.5354,
        "lng":            -76.3483,
        "source_url":     "https://www.yahoo.com/news/articles/salvadoran-fugitive-sentenced-life-womans-192803577.html",
        "source_name":    "AP / Harford County Circuit Court",
        "verified":       True,
        "is_public_figure": False,
        "date_incident":  "2023-08-05",
    },

    # ══════════════════════════════════════════════════════════════════════════
    # DAVID CARPENTER — "The Trailside Killer," CA 1979-1981
    # ══════════════════════════════════════════════════════════════════════════

    {
        "case_id":        "david_carpenter_trailside_killer_ca_1979",
        "violence_type":  "homicide",
        "status":         "convicted",
        "summary": (
            "David Carpenter, known as 'The Trailside Killer,' committed a "
            "series of murders on hiking trails in state parks near San "
            "Francisco, California between 1979 and 1981. He is believed to "
            "have murdered at least 10 people — the majority women — shooting "
            "most of them with a .38-caliber pistol after sexually assaulting "
            "them. His killing grounds included Mount Tamalpais State Park, "
            "Point Reyes National Seashore, and the Santa Cruz Mountains. "
            "His first documented victim, Edda Kane, was found kneeling with "
            "a single execution-style gunshot wound to the head at Mount "
            "Tamalpais on August 19, 1979. "
            "Carpenter had a prior criminal history stretching back to 1960 "
            "when he attacked a woman with a hammer and knife. He served "
            "prison time for that attack and a subsequent kidnapping conviction, "
            "was released in 1977, and began killing within two years. "
            "His crimes were so widely known that state parks posted warnings "
            "against hiking alone and visitor numbers declined for 21 months. "
            "Victims were predominantly women, mostly found shot and sexually "
            "assaulted. He was convicted and sentenced to death. "
            "Sources: Investigation Discovery; Sportskeeda."
        ),
        "city":           "San Francisco",
        "state":          "CA",
        "lat":            37.8716,
        "lng":            -122.4450,
        "source_url":     "https://www.sportskeeda.com/pop-culture/very-scary-people-id-who-alleged-victims-david-carpenter",
        "source_name":    "Investigation Discovery / Court Records",
        "verified":       True,
        "is_public_figure": False,
        "date_incident":  "1979-08-19",
    },

]


def main():
    print("\n  [Medusa] Seeding patterns and clergy cases...\n")
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
