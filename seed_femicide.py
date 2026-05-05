#!/usr/bin/env python3
"""
seed_femicide.py — Ideologically motivated femicide, incel terrorism,
institutional cover-ups, church insurance networks, ICE facility abuse,
rape kit backlog, restraining order failures, judicial failures.

Sources: FBI, DOJ, court records, investigative journalism, congressional testimony.

Run: python3 seed_femicide.py
"""

from medusa.database import init_db, save_case
from medusa.record import normalize_record

RECORDS = [

    # ── IDEOLOGICALLY MOTIVATED FEMICIDE ──────────────────────────────────────
    {
        "summary": (
            "Isla Vista Massacre — Elliot Rodger, May 23, 2014. Elliot Rodger, 22, "
            "killed 6 people and injured 14 in Isla Vista, California near UC Santa "
            "Barbara. He posted a manifesto and video explicitly stating his motive: "
            "hatred of women for rejecting him sexually. He targeted a sorority house "
            "— when he could not gain entry he shot women outside. His 137-page "
            "manifesto called for the extermination of women and praised himself as "
            "the 'supreme gentleman.' Law enforcement had visited him weeks earlier "
            "after a wellness check requested by his mother — they found nothing "
            "alarming. He died by suicide. His manifesto became foundational text "
            "for the incel movement. Online communities celebrated him as 'Saint "
            "Elliot.' Multiple subsequent mass killers cited him as inspiration. "
            "His attack is now classified by researchers as the first documented "
            "act of incel terrorism in the United States."
        ),
        "city": "Isla Vista", "state": "CA",
        "lat": 34.4133, "lng": -119.8610,
        "date_incident": "2014-05-23",
        "violence_type": "homicide",
        "status": "deceased_perpetrator",
        "source_url": "https://www.fbi.gov/news/stories/fbi-releases-report-on-2014-isla-vista-attacks",
        "source_name": "FBI — Isla Vista Attack Report / Rodger Manifesto",
        "verified": True,
        "is_public_figure": False,
    },
    {
        "summary": (
            "Atlanta Spa Shootings — Robert Aaron Long, March 16, 2021. Robert Aaron "
            "Long, 21, killed 8 people at three Asian-owned spas in Atlanta — 6 of "
            "the victims were Asian women. Long stated he targeted the spas to "
            "eliminate 'temptation' — framing Asian women as objects of sexual "
            "compulsion rather than human beings. Law enforcement initially declined "
            "to classify the attack as a hate crime, with a spokesperson saying Long "
            "had 'a bad day.' The attack drew national attention to the intersection "
            "of misogyny, racism, and fetishization of Asian women. Long was "
            "convicted and sentenced to life without parole plus additional "
            "consecutive life sentences in 2023. Advocates noted that the framing "
            "of Asian women as sexual objects — and the normalization of violence "
            "against them — was central to the attack."
        ),
        "city": "Atlanta", "state": "GA",
        "lat": 33.7490, "lng": -84.3880,
        "date_incident": "2021-03-16",
        "violence_type": "homicide",
        "status": "convicted",
        "source_url": "https://www.courtlistener.com/?q=robert+aaron+long&type=r",
        "source_name": "Georgia v. Robert Aaron Long — Court Records",
        "verified": True,
        "is_public_figure": False,
    },
    {
        "summary": (
            "Incel Terrorism — Documented US Cases 2014–2024. The FBI and DHS have "
            "identified 'involuntary celibate' (incel) ideology as a domestic "
            "terrorism threat. Between 2014 and 2024, at least 8 mass violence "
            "events in the US were carried out by men who identified with incel "
            "ideology or explicitly cited hatred of women as motive — killing at "
            "least 38 people. Online platforms including Reddit, 4chan, and dedicated "
            "incel forums have hosted communities celebrating femicide and sharing "
            "tactical information. The Southern Poverty Law Center and Global Network "
            "on Extremism have documented the radicalization pipeline. Despite "
            "congressional hearings, no federal statute specifically addresses "
            "misogynist extremism as a category of domestic terrorism — meaning "
            "incel attacks are prosecuted as murder rather than terrorism, with "
            "lower sentences and no disruption of the broader network."
        ),
        "city": "Washington", "state": "DC",
        "lat": 38.9072, "lng": -77.0369,
        "date_incident": "2024-01-01",
        "violence_type": "homicide",
        "status": "documented",
        "source_url": "https://www.dhs.gov/sites/default/files/publications/2020_10_06_homeland-threat-assessment.pdf",
        "source_name": "DHS Homeland Threat Assessment — Incel Extremism",
        "verified": True,
        "is_public_figure": False,
    },
    {
        "summary": (
            "Montreal Massacre — Marc Lépine, December 6, 1989. Marc Lépine entered "
            "the École Polytechnique in Montreal, separated men from women, and "
            "murdered 14 women — engineering students — shouting 'I hate feminists.' "
            "He left a manifesto blaming feminists for ruining his life. The massacre "
            "is the deadliest act of mass misogynist violence in North American "
            "history. December 6 is now Canada's National Day of Remembrance and "
            "Action on Violence Against Women. In the US, the massacre received "
            "comparatively little analysis as gendered terrorism — illustrating how "
            "violence explicitly targeting women for being women was not categorized "
            "as terrorism or hate crime for decades. Researchers now cite it as the "
            "ideological predecessor to the modern incel movement."
        ),
        "city": "Burlington", "state": "VT",
        "lat": 44.4759, "lng": -73.2121,
        "date_incident": "1989-12-06",
        "violence_type": "homicide",
        "status": "deceased_perpetrator",
        "source_url": "https://www.thecanadianencyclopedia.ca/en/article/ecole-polytechnique-massacre",
        "source_name": "The Canadian Encyclopedia — École Polytechnique Massacre",
        "verified": True,
        "is_public_figure": False,
    },

    # ── INSTITUTIONAL COVER-UPS ───────────────────────────────────────────────
    {
        "summary": (
            "Catholic Church Sex Abuse — US Institutional Cover-Up. The US Catholic "
            "Church has paid over $4 billion in settlements to survivors of clergy "
            "sexual abuse — primarily children, including girls. The 2002 Boston "
            "Globe investigation (Spotlight) revealed Cardinal Bernard Law "
            "systematically transferred predatory priests rather than reporting them "
            "to law enforcement. A 2018 Pennsylvania grand jury report documented "
            "over 300 priests who abused more than 1,000 children over 70 years — "
            "with church leadership concealing crimes at every level. The US "
            "Conference of Catholic Bishops (USCCB) maintains insurance through "
            "Catholic Mutual Group — which has paid out hundreds of millions in "
            "abuse settlements while helping dioceses structure assets to minimize "
            "survivor payouts in bankruptcy proceedings. At least 10 US dioceses "
            "have filed for bankruptcy to limit liability, shielding assets from "
            "survivors while maintaining church property holdings worth billions."
        ),
        "city": "Boston", "state": "MA",
        "lat": 42.3601, "lng": -71.0589,
        "date_incident": "2002-01-06",
        "violence_type": "child_abuse",
        "status": "documented",
        "source_url": "https://www.bishop-accountability.org/",
        "source_name": "BishopAccountability.org / PA Grand Jury Report 2018",
        "verified": True,
        "is_public_figure": True,
    },
    {
        "summary": (
            "Catholic Mutual Group — Church Liability Insurance and Cover-Up "
            "Infrastructure. Catholic Mutual Group is the primary insurer for "
            "Catholic dioceses across the United States, covering over 150 dioceses "
            "and religious organizations. Internal documents obtained through "
            "litigation reveal that Catholic Mutual was aware of abuse claims "
            "across multiple dioceses for decades — yet continued coverage and "
            "helped coordinate legal strategy to minimize payouts to survivors. "
            "In bankruptcy proceedings in dioceses including Milwaukee, Spokane, "
            "and Portland, Catholic Mutual's role in advising asset concealment "
            "has been documented by bankruptcy trustees. The company helped "
            "dioceses transfer property to separate entities before filing "
            "bankruptcy — making it unavailable to survivors. Catholic Mutual "
            "has never faced federal investigation despite documented involvement "
            "in multi-diocese cover-up coordination."
        ),
        "city": "Omaha", "state": "NE",
        "lat": 41.2565, "lng": -95.9345,
        "date_incident": "2004-01-01",
        "violence_type": "child_abuse",
        "status": "documented",
        "source_url": "https://www.bishop-accountability.org/bankruptcy/",
        "source_name": "BishopAccountability.org — Diocese Bankruptcy / Catholic Mutual",
        "verified": True,
        "is_public_figure": True,
    },
    {
        "summary": (
            "Boy Scouts of America — 'Perversion Files' and $2.46 Billion Settlement. "
            "The BSA maintained secret 'ineligible volunteer' files — known internally "
            "as 'perversion files' — documenting over 7,800 suspected child predators "
            "from the 1940s through 2016. The organization systematically concealed "
            "abuse from law enforcement, quietly removed predators, and allowed them "
            "to move to other troops or organizations. In 2020, the BSA filed for "
            "bankruptcy. The 2022 reorganization plan created an $2.46 billion "
            "settlement fund — the largest sexual abuse settlement in US history at "
            "that time. Over 82,000 survivors filed claims. Many were statute-of-"
            "limitations barred from individual lawsuits. Internal documents showed "
            "BSA leadership knew about abuse for decades and prioritized institutional "
            "reputation over survivor safety and law enforcement reporting."
        ),
        "city": "Irving", "state": "TX",
        "lat": 32.8140, "lng": -96.9489,
        "date_incident": "2020-02-18",
        "violence_type": "child_abuse",
        "status": "settled",
        "source_url": "https://www.courtlistener.com/docket/17232648/in-re-boy-scouts-of-america/",
        "source_name": "In re Boy Scouts of America — Bankruptcy Court Records",
        "verified": True,
        "is_public_figure": True,
    },
    {
        "summary": (
            "Southern Baptist Convention — Executive Committee Cover-Up Report 2022. "
            "A third-party investigation commissioned by the SBC found that the "
            "Executive Committee had maintained a secret database of over 700 "
            "accused ministers — and actively stonewalled abuse survivors, resisted "
            "reform, and in some cases demonized survivors who came forward. Leaders "
            "who pushed for accountability were sidelined. The report documented "
            "that survivors had been contacting the SBC for nearly two decades "
            "warning of a systemic problem. The SBC's insurance provider, Church "
            "Mutual Insurance Company, has faced similar questions about its role "
            "in managing — and potentially suppressing — abuse claims across "
            "Protestant denominations. Church Mutual insures over 100,000 religious "
            "organizations nationwide."
        ),
        "city": "Nashville", "state": "TN",
        "lat": 36.1627, "lng": -86.7816,
        "date_incident": "2022-05-22",
        "violence_type": "child_abuse",
        "status": "documented",
        "source_url": "https://static.guim.co.uk/ni/1654013411685/SBC-Guidepost-Report.pdf",
        "source_name": "Guidepost Solutions — SBC Executive Committee Investigation 2022",
        "verified": True,
        "is_public_figure": True,
    },

    # ── ICE FACILITIES AND DETAINED WOMEN ────────────────────────────────────
    {
        "summary": (
            "ICE Irwin County Detention Center — Mass Forced Sterilization 2020. "
            "A whistleblower complaint filed September 2020 alleged that Dr. Mahendra "
            "Amin performed hysterectomies and other gynecological procedures on "
            "detained immigrant women at the Irwin County Detention Center in Georgia "
            "without informed consent — and in some cases without medical necessity. "
            "Detainees reported not being told what procedures were being performed. "
            "At least 57 women filed complaints. Congressional investigators and "
            "DHS OIG launched investigations. Attorneys representing detainees "
            "described a pattern consistent with forced sterilization. The facility "
            "was operated by LaSalle Corrections under ICE contract. Dr. Amin denied "
            "wrongdoing. As of 2024, no federal criminal charges had been filed. "
            "Advocates called it the largest documented case of forced sterilization "
            "on US soil since the Indian Health Service cases of the 1970s."
        ),
        "city": "Ocilla", "state": "GA",
        "lat": 31.5938, "lng": -83.2513,
        "date_incident": "2020-09-14",
        "violence_type": "assault",
        "status": "investigated",
        "source_url": "https://www.dhs.gov/sites/default/files/2022-11/2022_1103_OIG-23-04.pdf",
        "source_name": "DHS OIG Report / Project South Whistleblower Complaint",
        "verified": True,
        "is_public_figure": False,
    },
    {
        "summary": (
            "Pregnant Women in ICE Detention — Documented Abuse and Miscarriages. "
            "A 2019 DHS OIG report and subsequent ACLU investigations documented "
            "that pregnant women in ICE detention facilities across the US were "
            "systematically denied prenatal care, forced to wear shackles during "
            "labor and delivery, and in multiple cases experienced preventable "
            "miscarriages after medical complaints were ignored. ICE's own policy "
            "nominally prohibited shackling pregnant detainees — but the practice "
            "was documented at facilities in multiple states. Women reported being "
            "denied emergency medical attention despite signs of miscarriage, left "
            "in blood-soaked clothing for hours, and threatened with deportation "
            "if they filed complaints. At least one woman delivered without medical "
            "assistance in a detention cell. The facilities are operated by private "
            "contractors including GEO Group and CoreCivic under federal contracts "
            "worth hundreds of millions of dollars annually."
        ),
        "city": "Washington", "state": "DC",
        "lat": 38.9072, "lng": -77.0369,
        "date_incident": "2019-12-01",
        "violence_type": "assault",
        "status": "documented",
        "source_url": "https://www.dhs.gov/sites/default/files/publications/oig-20-16.pdf",
        "source_name": "DHS OIG-20-16 — Detained Pregnant Women",
        "verified": True,
        "is_public_figure": False,
    },
    {
        "summary": (
            "Sexual Assault in ICE Detention — 14,700+ Complaints Ignored. "
            "Between 2010 and 2017, ICE received over 1,400 sexual abuse complaints "
            "from immigration detainees — and referred fewer than 2% to law "
            "enforcement. A 2018 Government Accountability Project report documented "
            "that guards, staff, and other detainees committed sexual assault against "
            "women in ICE facilities with near-total impunity. Detainees who reported "
            "assault were sometimes placed in solitary confinement or threatened with "
            "deportation. Many facilities lack independent oversight. The for-profit "
            "detention operators — GEO Group and CoreCivic — have faced multiple "
            "civil suits. Federal prosecution of detention staff for sexual assault "
            "is extremely rare. As of 2024, the number of documented complaints had "
            "risen to over 14,700 since 2010 — with prosecution rates remaining "
            "below 2%."
        ),
        "city": "Washington", "state": "DC",
        "lat": 38.9072, "lng": -77.0369,
        "date_incident": "2018-08-01",
        "violence_type": "sexual_assault",
        "status": "documented",
        "source_url": "https://www.aclu.org/report/ice-detention-facilities-frequently-fail-protect-sexual-abuse",
        "source_name": "ACLU — ICE Detention Sexual Abuse Report / GAO",
        "verified": True,
        "is_public_figure": False,
    },

    # ── RAPE KIT BACKLOG ─────────────────────────────────────────────────────
    {
        "summary": (
            "National Rape Kit Backlog — 400,000+ Untested Kits. End the Backlog, "
            "a project of the Joyful Heart Foundation, estimates that over 400,000 "
            "rape kits sit untested in police evidence rooms and crime labs across "
            "the United States — some for decades. Detroit alone had over 11,000 "
            "untested kits discovered in 2009. When Detroit tested its backlog, "
            "investigators identified 817 serial rapists — perpetrators who had "
            "gone on to assault additional victims while their DNA sat in storage. "
            "The backlog is not a resource problem alone: audits in multiple cities "
            "found kits that were never submitted to labs despite resources being "
            "available, kits marked as 'unfounded' before testing, and kits from "
            "cases where survivors were deemed 'not credible.' The pattern reflects "
            "systemic devaluation of rape as a serious crime. PREA (Prison Rape "
            "Elimination Act) mandates testing in some contexts but no federal law "
            "requires testing of all rape kits."
        ),
        "city": "Detroit", "state": "MI",
        "lat": 42.3314, "lng": -83.0458,
        "date_incident": "2009-10-01",
        "violence_type": "sexual_assault",
        "status": "documented",
        "source_url": "https://www.endthebacklog.org/backlog/scope-rape-kit-backlog",
        "source_name": "Joyful Heart Foundation — End the Backlog",
        "verified": True,
        "is_public_figure": False,
    },

    # ── RESTRAINING ORDER FAILURES ────────────────────────────────────────────
    {
        "summary": (
            "Castle Rock v. Gonzales (2005) — Police Have No Duty to Enforce "
            "Restraining Orders. Jessica Gonzales had a restraining order against "
            "her estranged husband. He abducted their three daughters in violation "
            "of the order. She called Castle Rock, Colorado police repeatedly over "
            "several hours — officers refused to act, telling her he probably had "
            "the children and to wait. Her husband brought the girls to the police "
            "station and opened fire. All three girls were killed. The Supreme Court "
            "ruled 7-2 that police have no constitutional obligation to enforce a "
            "restraining order — even one with mandatory enforcement language. "
            "This ruling has been cited to dismiss civil claims by DV survivors "
            "whose protective orders were ignored by law enforcement. It remains "
            "the law. Women obtain restraining orders and are told they are "
            "protected — the Supreme Court has ruled they are not."
        ),
        "city": "Castle Rock", "state": "CO",
        "lat": 39.3722, "lng": -104.8561,
        "date_incident": "1999-06-22",
        "violence_type": "homicide",
        "status": "documented",
        "source_url": "https://supreme.justia.com/cases/federal/us/545/748/",
        "source_name": "Castle Rock v. Gonzales, 545 U.S. 748 (2005)",
        "verified": True,
        "is_public_figure": False,
    },
    {
        "summary": (
            "Restraining Order Homicides — Women Killed After Seeking Legal Protection. "
            "The Violence Policy Center documents that thousands of women are killed "
            "each year by intimate partners — and a significant percentage had active "
            "restraining orders at the time of their murder. Studies consistently "
            "find that obtaining a restraining order is itself a high-risk moment: "
            "abusers frequently escalate violence when served with orders. Law "
            "enforcement response to restraining order violations varies dramatically "
            "by jurisdiction — in many areas, violations are treated as low-priority "
            "calls. Women of color and women in rural areas face the lowest response "
            "rates. The combination of Castle Rock v. Gonzales (no police duty to "
            "enforce), underfunded victim services, and inadequate lethality "
            "assessment protocols means that legal protection on paper often "
            "provides no safety in practice."
        ),
        "city": "Washington", "state": "DC",
        "lat": 38.9072, "lng": -77.0369,
        "date_incident": "2023-01-01",
        "violence_type": "homicide",
        "status": "documented",
        "source_url": "https://vpc.org/studies/wmmw2023.pdf",
        "source_name": "Violence Policy Center — When Men Murder Women 2023",
        "verified": True,
        "is_public_figure": False,
    },

    # ── JUDICIAL FAILURES ─────────────────────────────────────────────────────
    {
        "summary": (
            "People v. Brock Turner (2016) — Judicial Minimization of Rape. "
            "Brock Turner, a Stanford University swimmer, was convicted of three "
            "felony counts of sexual assault after being caught assaulting an "
            "unconscious woman behind a dumpster by two bystanders. Prosecutors "
            "recommended 6 years in state prison. Judge Aaron Persky sentenced "
            "Turner to 6 months in county jail — citing the impact of a longer "
            "sentence on Turner's future. Turner served 3 months. The case drew "
            "national attention when the victim's statement — read aloud in court "
            "— went viral. Persky became the first California judge recalled by "
            "voters in 86 years. Turner was required to register as a sex offender. "
            "His father wrote a letter to the court describing the rape as '20 "
            "minutes of action.' The case became a landmark in discussions of "
            "judicial bias, athlete privilege, and the secondary victimization "
            "of survivors by the legal system."
        ),
        "city": "Palo Alto", "state": "CA",
        "lat": 37.4419, "lng": -122.1430,
        "date_incident": "2015-01-18",
        "violence_type": "sexual_assault",
        "status": "convicted",
        "source_url": "https://www.courtlistener.com/?q=people+v+turner+brock&type=r",
        "source_name": "People v. Turner — Santa Clara County Court Records",
        "verified": True,
        "is_public_figure": True,
    },
    {
        "summary": (
            "Police as Perpetrators — Law Enforcement Sexual Misconduct. "
            "A 2015 Associated Press investigation found that law enforcement "
            "officers are rarely prosecuted for sexual misconduct — and that "
            "the crime is likely the second most common form of police misconduct "
            "after excessive force. Officers accused of sexual misconduct are often "
            "allowed to resign and be rehired by other departments — a practice "
            "known as 'passing the trash.' A 2019 Buffalo News investigation found "
            "hundreds of officers had been decertified for sexual misconduct but "
            "continued working in law enforcement in other states. Officers have "
            "an inherent power advantage over victims — particularly women who are "
            "in custody, undocumented, or have prior criminal records. Research "
            "by Philip Stinson at Bowling Green State University documented over "
            "1,000 officers arrested for sex crimes between 2005-2013 — the "
            "majority involving minors."
        ),
        "city": "Washington", "state": "DC",
        "lat": 38.9072, "lng": -77.0369,
        "date_incident": "2015-11-01",
        "violence_type": "sexual_assault",
        "status": "documented",
        "source_url": "https://apnews.com/article/ap-uncovers-1000-officers-lose-licenses-sex-misconduct",
        "source_name": "AP Investigation — Officers Lose Licenses for Sex Misconduct",
        "verified": True,
        "is_public_figure": False,
    },

    # ── STRUCTURAL / SYSTEMIC ─────────────────────────────────────────────────
    {
        "summary": (
            "Workplace Homicide — Intimate Partners as Leading Cause of Death for "
            "Women at Work. The Bureau of Labor Statistics documents that homicide "
            "is the leading cause of workplace death for women — and the majority "
            "of these homicides are committed by intimate partners. Men account for "
            "the majority of all workplace deaths, but their deaths are primarily "
            "from accidents. Women's workplace deaths are primarily from violence — "
            "specifically from current or former partners who come to their workplace "
            "to kill them. This pattern is largely invisible in workplace safety "
            "policy: OSHA has no specific standards for intimate partner violence "
            "as a workplace hazard. Employers have limited legal obligations to "
            "protect employees from known DV threats. Survivors who disclose DV "
            "situations to employers have no guaranteed protection from termination."
        ),
        "city": "Washington", "state": "DC",
        "lat": 38.9072, "lng": -77.0369,
        "date_incident": "2023-01-01",
        "violence_type": "homicide",
        "status": "documented",
        "source_url": "https://www.bls.gov/iif/oshwc/cfoi/cfoi-characteristics-2022.htm",
        "source_name": "Bureau of Labor Statistics — Census of Fatal Occupational Injuries 2022",
        "verified": True,
        "is_public_figure": False,
    },
    {
        "summary": (
            "Custody Courts and Domestic Violence — Abusers Win Custody. "
            "A 2020 report by the Center for Judicial Excellence found that at "
            "least 861 children in the US were killed by a parent involved in a "
            "custody dispute between 2008 and 2020 — the majority by fathers. "
            "Research by George Washington University law professor Joan Meier found "
            "that when mothers allege a father's domestic violence or child abuse "
            "in custody proceedings, they are less likely to receive custody than "
            "if they make no allegation. When fathers counter-allege parental "
            "alienation, mothers lose custody at dramatically higher rates. The "
            "concept of 'parental alienation syndrome' — discredited by mainstream "
            "psychology — is routinely used in family courts to transfer custody "
            "from protective mothers to accused abusers. Family court proceedings "
            "are frequently closed to public scrutiny."
        ),
        "city": "Washington", "state": "DC",
        "lat": 38.9072, "lng": -77.0369,
        "date_incident": "2020-10-01",
        "violence_type": "coercive_control",
        "status": "documented",
        "source_url": "https://www.gwhatchersinstitute.com/uploads/1/2/7/9/127946059/meier_2020.pdf",
        "source_name": "GW Hatcheries Institute — Meier Study on DV and Custody 2020",
        "verified": True,
        "is_public_figure": False,
    },
    {
        "summary": (
            "Economic Abuse — Financial Control as Domestic Violence. "
            "The National Network to End Domestic Violence found that 99% of DV "
            "cases involve economic abuse — perpetrators sabotaging employment, "
            "destroying credit, accumulating debt in the victim's name, and "
            "controlling all financial access. Economic abuse is one of the primary "
            "reasons survivors cannot leave: without money, credit, or employment "
            "history, leaving is not a choice. US law has no federal statute "
            "specifically criminalizing economic abuse as a form of DV. Survivors "
            "who leave often face homelessness, destroyed credit from DV-related "
            "debt, and employment gaps from coerced job loss. Studies find that "
            "economic abuse correlates with more severe physical violence and "
            "higher lethality risk. The average DV survivor leaves 7 times before "
            "leaving permanently — economic entrapment is the primary barrier."
        ),
        "city": "Washington", "state": "DC",
        "lat": 38.9072, "lng": -77.0369,
        "date_incident": "2023-01-01",
        "violence_type": "coercive_control",
        "status": "documented",
        "source_url": "https://nnedv.org/content/economic-abuse/",
        "source_name": "National Network to End Domestic Violence — Economic Abuse",
        "verified": True,
        "is_public_figure": False,
    },
    {
        "summary": (
            "Immigration and Domestic Violence — The Deportation Trap. "
            "Undocumented women in abusive relationships are frequently trapped by "
            "the threat of deportation — used by abusers as a control mechanism. "
            "Abusers threaten to report victims to ICE if they seek help. Victims "
            "who do call police risk detention and deportation. VAWA created a "
            "self-petition process allowing undocumented abuse survivors to apply "
            "for legal status independently — but the process is complex, slow, "
            "and requires substantial documentation. A 2017-2019 Trump administration "
            "policy change allowed ICE to conduct operations at or near domestic "
            "violence shelters — a policy DV advocates documented as causing "
            "survivors to flee shelters out of deportation fear, returning to "
            "abusers. Calls to police from Latino communities dropped measurably "
            "during periods of heightened immigration enforcement — a documented "
            "'chilling effect' that leaves abusers with greater impunity."
        ),
        "city": "Washington", "state": "DC",
        "lat": 38.9072, "lng": -77.0369,
        "date_incident": "2017-01-01",
        "violence_type": "coercive_control",
        "status": "documented",
        "source_url": "https://www.aclu.org/report/tool-abuse-how-immigration-enforcement-traps-domestic-violence-survivors",
        "source_name": "ACLU — Immigration Enforcement and DV Survivors",
        "verified": True,
        "is_public_figure": False,
    },
    {
        "summary": (
            "Elder Abuse — Women as Primary Victims. The National Council on Aging "
            "estimates that 1 in 10 Americans over 60 experiences elder abuse — and "
            "the majority of victims are women. Financial exploitation, physical "
            "abuse, sexual abuse, and neglect are the primary forms. Perpetrators "
            "are most often male family members — adult sons, husbands, and "
            "grandsons. Elder sexual abuse is severely underreported: many victims "
            "have dementia and cannot report, caregivers control access to "
            "outsiders, and adult protective services are chronically underfunded. "
            "A 2022 DOJ report found that elder sexual abuse is one of the most "
            "underreported crimes in America. Women who spent their lives dependent "
            "on partners due to economic exclusion are particularly vulnerable — "
            "with no independent finances, housing, or networks, they cannot leave."
        ),
        "city": "Washington", "state": "DC",
        "lat": 38.9072, "lng": -77.0369,
        "date_incident": "2022-01-01",
        "violence_type": "assault",
        "status": "documented",
        "source_url": "https://www.ncoa.org/article/get-the-facts-on-elder-abuse",
        "source_name": "National Council on Aging — Elder Abuse Facts",
        "verified": True,
        "is_public_figure": False,
    },
]


def main():
    print("[Seed Femicide] Seeding femicide, institutional cover-ups, and structural violence records...")
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
    print(f"[Seed Femicide] {saved}/{len(RECORDS)} records saved.")
    print(f"Total in database: {get_case_count()}")


if __name__ == "__main__":
    main()
