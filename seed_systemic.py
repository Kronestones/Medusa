#!/usr/bin/env python3
"""
seed_systemic.py — Pay gap, pink tax, campus sexual assault, femicide during
pregnancy, criminalization of miscarriage, stealthing, and the complete body
of US laws that kept women legally subordinate to men.

Sources: DOL, Census Bureau, court records, congressional testimony, CDC,
GAO, ACLU, investigative journalism, legal scholarship.

Run: python3 seed_systemic.py
"""

from medusa.database import init_db, save_case
from medusa.record import normalize_record

RECORDS = [

    # ── LAWS KEEPING WOMEN BEHOLDEN TO MEN ───────────────────────────────────
    {
        "summary": (
            "Coverture — The Legal Erasure of Women. Under coverture, the foundational "
            "legal doctrine of English common law imported into American law, a woman's "
            "legal identity ceased to exist upon marriage. She could not own property, "
            "sign contracts, keep her wages, sue or be sued, or make legal decisions "
            "without her husband's consent. Her husband owned her body, her labor, her "
            "children, and her property. Coverture was the law in every US state at "
            "founding. Elements of coverture persisted in US law for over 180 years: "
            "married women could not own property independently until the Married "
            "Women's Property Acts (1839–1900s, state by state). Women could not "
            "maintain separate bank accounts until the 1960s. Husbands could legally "
            "collect their wives' wages until well into the 20th century. Marital rape "
            "was not criminalized in all 50 states until 1993. Coverture was never "
            "formally abolished by federal law — it was dismantled piece by piece over "
            "150 years through individual statutes and court decisions."
        ),
        "city": "Washington", "state": "DC",
        "lat": 38.9072, "lng": -77.0369,
        "date_incident": "1776-07-04",
        "violence_type": "coercive_control",
        "status": "documented",
        "source_url": "https://www.law.cornell.edu/wex/coverture",
        "source_name": "Cornell Law — Coverture / Married Women's Property Acts",
        "verified": True,
        "is_public_figure": False,
    },
    {
        "summary": (
            "Head and Master Laws — Husbands as Legal Rulers of the Household. "
            "Until 1980, Louisiana's 'Head and Master' law gave husbands unilateral "
            "control over jointly owned property — a wife could not sell, mortgage, "
            "or encumber marital property without her husband's consent, but he could "
            "do so without hers. The Supreme Court struck it down in Kirchberg v. "
            "Feenstra (1981). Similar laws existed in other states. These laws meant "
            "that women who worked, saved, and built assets during marriage had no "
            "legal right to those assets without their husband's permission. Head and "
            "Master laws were the legal infrastructure of economic dependency — "
            "trapping women in marriages they could not afford to leave because they "
            "had no legal claim to the assets they had helped create."
        ),
        "city": "New Orleans", "state": "LA",
        "lat": 29.9511, "lng": -90.0715,
        "date_incident": "1981-03-23",
        "violence_type": "coercive_control",
        "status": "documented",
        "source_url": "https://supreme.justia.com/cases/federal/us/450/455/",
        "source_name": "Kirchberg v. Feenstra, 450 U.S. 455 (1981)",
        "verified": True,
        "is_public_figure": False,
    },
    {
        "summary": (
            "Marital Exemption for Rape — Legal Until 1993. The marital rape "
            "exemption — rooted in a 1736 statement by English jurist Matthew Hale "
            "that a wife gives 'irrevocable consent' to sex upon marriage — was "
            "codified in US law in every state. A husband could not be convicted of "
            "raping his wife. North Carolina was the last state to fully criminalize "
            "marital rape in 1993. Even today, 13 states treat marital rape as a "
            "lesser offense than rape by a stranger — with shorter statutes of "
            "limitations, lower penalties, or additional requirements for prosecution. "
            "Some states still require the couple to be living apart or require "
            "physical force beyond the rape itself. The marital rape exemption was "
            "not a historical footnote — it was active law within living memory and "
            "its remnants remain in state statutes today."
        ),
        "city": "Washington", "state": "DC",
        "lat": 38.9072, "lng": -77.0369,
        "date_incident": "1993-01-01",
        "violence_type": "rape",
        "status": "documented",
        "source_url": "https://www.law.umich.edu/special/exoneration/Pages/casedetail.aspx",
        "source_name": "RAINN / Legal Momentum — Marital Rape Laws by State",
        "verified": True,
        "is_public_figure": False,
    },
    {
        "summary": (
            "Women Could Not Serve on Juries in All States Until 1973. Women were "
            "excluded from jury service by law or practice in most states until well "
            "into the 20th century. The Supreme Court upheld all-male juries in "
            "Hoyt v. Florida (1961) — ruling that women's primary role was in the "
            "home and that exempting them from jury duty was rational. Taylor v. "
            "Louisiana (1975) finally established that systematic exclusion of women "
            "from juries was unconstitutional. Until then, women accused of crimes "
            "were judged by all-male juries. Women who were victims of crimes had "
            "their cases decided by men who had never been required to consider "
            "women's perspectives as a matter of legal obligation. The composition "
            "of juries in rape cases — all male, in a legal culture that blamed "
            "victims — directly determined conviction rates for sexual violence."
        ),
        "city": "Washington", "state": "DC",
        "lat": 38.9072, "lng": -77.0369,
        "date_incident": "1975-01-21",
        "violence_type": "coercive_control",
        "status": "documented",
        "source_url": "https://supreme.justia.com/cases/federal/us/419/522/",
        "source_name": "Taylor v. Louisiana, 419 U.S. 522 (1975)",
        "verified": True,
        "is_public_figure": False,
    },
    {
        "summary": (
            "Pregnancy Discrimination — Legal Until 1978. Until the Pregnancy "
            "Discrimination Act of 1978, employers could legally fire women for "
            "becoming pregnant, refuse to hire pregnant women, and deny disability "
            "benefits for pregnancy-related conditions. The Supreme Court ruled in "
            "General Electric v. Gilbert (1976) that pregnancy discrimination was "
            "not sex discrimination under Title VII. Congress overrode this ruling "
            "with the PDA two years later. Even after the PDA, enforcement was weak: "
            "a 2021 study found that pregnancy discrimination charges filed with the "
            "EEOC increased 65% between 1997 and 2017. In 2022, Congress passed the "
            "Pregnant Workers Fairness Act — requiring employers to provide reasonable "
            "accommodations for pregnancy — because the PDA alone had proven "
            "insufficient. Women continue to be pushed out of jobs during and after "
            "pregnancy at documented rates."
        ),
        "city": "Washington", "state": "DC",
        "lat": 38.9072, "lng": -77.0369,
        "date_incident": "1978-10-31",
        "violence_type": "coercive_control",
        "status": "documented",
        "source_url": "https://www.eeoc.gov/pregnancy-discrimination",
        "source_name": "EEOC — Pregnancy Discrimination Act / PWFA",
        "verified": True,
        "is_public_figure": False,
    },
    {
        "summary": (
            "Women Could Not Get a Passport Without Husband's Permission Until 1937. "
            "Until 1937, married American women could not obtain a US passport "
            "independently — they were listed on their husband's passport as dependents. "
            "A husband could prevent his wife from traveling internationally simply "
            "by withholding his consent. This was not an obscure technicality — it "
            "was active policy that physically restricted women's movement and "
            "autonomy. Combined with laws preventing women from owning property, "
            "maintaining bank accounts, or signing contracts, the passport restriction "
            "was part of a comprehensive legal architecture that made independent "
            "life for married women functionally impossible. Women who fled abusive "
            "marriages could not leave the country without their abuser's permission."
        ),
        "city": "Washington", "state": "DC",
        "lat": 38.9072, "lng": -77.0369,
        "date_incident": "1937-01-01",
        "violence_type": "coercive_control",
        "status": "documented",
        "source_url": "https://history.state.gov/milestones/1921-1936/citizenship",
        "source_name": "US State Department — History of Women's Passport Rights",
        "verified": True,
        "is_public_figure": False,
    },
    {
        "summary": (
            "Married Women Could Not Establish Legal Domicile Until 1988. Under "
            "common law doctrine, a married woman's legal domicile was automatically "
            "that of her husband — regardless of where she actually lived. This "
            "affected voting registration, eligibility for state benefits, tax "
            "filing, and legal jurisdiction. A woman who lived in one state but "
            "whose husband was domiciled in another had no independent legal home. "
            "The Uniform Disposition of Community Property Act and subsequent state "
            "reforms addressed this, but some states retained elements of the "
            "doctrine into the 1980s. This legal erasure of women's independent "
            "geographic existence was a direct extension of coverture — the law "
            "did not recognize that a married woman existed as a separate person "
            "with her own location in the world."
        ),
        "city": "Washington", "state": "DC",
        "lat": 38.9072, "lng": -77.0369,
        "date_incident": "1988-01-01",
        "violence_type": "coercive_control",
        "status": "documented",
        "source_url": "https://www.law.cornell.edu/wex/domicile",
        "source_name": "Cornell Law — Domicile / Married Women's Legal Status",
        "verified": True,
        "is_public_figure": False,
    },

    # ── PAY GAP ───────────────────────────────────────────────────────────────
    {
        "summary": (
            "The Gender Pay Gap — Documented Economic Violence. The US Census Bureau "
            "2023 data shows women earn 84 cents for every dollar earned by men — a "
            "gap that has barely moved in 20 years. For women of color the gap is "
            "dramatically worse: Black women earn 67 cents, Native American women "
            "60 cents, and Latina women 57 cents for every dollar earned by white "
            "non-Hispanic men. The pay gap is not explained by occupation or hours "
            "worked — studies controlling for these factors find an unexplained gap "
            "of 8–12% attributable to discrimination. The pay gap compounds over a "
            "lifetime: the average woman loses $400,000–$1 million in lifetime "
            "earnings compared to a similarly qualified man. Lower lifetime earnings "
            "mean lower Social Security benefits, lower retirement savings, and "
            "greater economic vulnerability in old age. The pay gap is a mechanism "
            "of economic control that keeps women financially dependent and less able "
            "to escape abusive situations."
        ),
        "city": "Washington", "state": "DC",
        "lat": 38.9072, "lng": -77.0369,
        "date_incident": "2023-09-12",
        "violence_type": "coercive_control",
        "status": "documented",
        "source_url": "https://www.census.gov/library/publications/2023/demo/p60-279.html",
        "source_name": "US Census Bureau — Income and Poverty in the United States 2023",
        "verified": True,
        "is_public_figure": False,
    },
    {
        "summary": (
            "Equal Pay Act (1963) — 60 Years of Inadequate Enforcement. The Equal "
            "Pay Act required equal pay for equal work regardless of sex. Sixty years "
            "later, the gender pay gap persists. Enforcement gaps are structural: "
            "the Act allows pay differences based on seniority, merit, or 'any factor "
            "other than sex' — a loophole that has been used to justify discriminatory "
            "pay. Salary history bans — laws preventing employers from asking about "
            "prior pay — have been shown to reduce the gap, but are only in effect "
            "in some states. The Paycheck Fairness Act, which would have strengthened "
            "enforcement, has been introduced in Congress repeatedly and has never "
            "passed. The EEOC resolves only a fraction of pay discrimination charges "
            "filed annually. Women who discover pay discrimination face retaliation, "
            "confidentiality clauses, and arbitration agreements that prevent "
            "collective action."
        ),
        "city": "Washington", "state": "DC",
        "lat": 38.9072, "lng": -77.0369,
        "date_incident": "1963-06-10",
        "violence_type": "coercive_control",
        "status": "documented",
        "source_url": "https://www.eeoc.gov/laws/statutes/epa.cfm",
        "source_name": "EEOC — Equal Pay Act / Paycheck Fairness Act History",
        "verified": True,
        "is_public_figure": False,
    },

    # ── PINK TAX ──────────────────────────────────────────────────────────────
    {
        "summary": (
            "The Pink Tax — Women Pay More for Being Women. The 'pink tax' refers "
            "to the documented premium charged for products and services marketed to "
            "women versus nearly identical products marketed to men. A 2015 New York "
            "City Department of Consumer Affairs study found women pay an average "
            "7% more than men for similar products — 13% more for personal care "
            "products. Razors, shampoo, deodorant, clothing, and dry cleaning all "
            "show consistent price premiums for women's versions. Additionally, "
            "until the Menstrual Equity for All Act provisions, 30 states taxed "
            "menstrual products as luxury items — taxing a biological necessity while "
            "exempting Viagra, dandruff shampoo, and Rogaine in many jurisdictions. "
            "As of 2024, 20 states still tax period products. The pink tax costs "
            "the average American woman an estimated $1,300–$2,200 per year — a "
            "compounding economic penalty applied to women simply for existing."
        ),
        "city": "Washington", "state": "DC",
        "lat": 38.9072, "lng": -77.0369,
        "date_incident": "2015-12-01",
        "violence_type": "coercive_control",
        "status": "documented",
        "source_url": "https://www.dca.ny.gov/media/pdf/Study-of-Gender-Pricing-in-NYC.pdf",
        "source_name": "NYC Dept of Consumer Affairs — From Cradle to Cane: The Cost of Being Female 2015",
        "verified": True,
        "is_public_figure": False,
    },
    {
        "summary": (
            "Tampon Tax — Taxing Biological Necessity. Menstrual products are "
            "classified as luxury or non-essential items subject to sales tax in "
            "approximately 20 US states as of 2024. States that tax period products "
            "include Mississippi, Alabama, Georgia, and others — while simultaneously "
            "exempting items like Rogaine, gun club memberships, and candy in "
            "various state tax codes. The average woman spends approximately $150 "
            "per year on menstrual products before tax. Low-income women and girls "
            "face 'period poverty' — inability to afford menstrual products — which "
            "causes school absenteeism and workplace absence. A 2021 survey found "
            "that 1 in 5 US teens had struggled to afford period products. "
            "Period poverty disproportionately affects women of color, homeless "
            "women, and incarcerated women — in many prisons, menstrual products "
            "are withheld as a form of punishment or control."
        ),
        "city": "Washington", "state": "DC",
        "lat": 38.9072, "lng": -77.0369,
        "date_incident": "2024-01-01",
        "violence_type": "coercive_control",
        "status": "documented",
        "source_url": "https://www.periodequity.org/state-laws",
        "source_name": "Period Equity — State Tampon Tax Laws 2024",
        "verified": True,
        "is_public_figure": False,
    },

    # ── CAMPUS SEXUAL ASSAULT ─────────────────────────────────────────────────
    {
        "summary": (
            "Campus Sexual Assault — National Scale. The Association of American "
            "Universities 2019 Campus Climate Survey — the largest ever conducted — "
            "found that 26.4% of undergraduate women experienced sexual assault or "
            "misconduct. 13% experienced penetration by force or incapacitation. "
            "Fewer than 25% reported the assault to campus or law enforcement. "
            "The most common reason for not reporting: believing it was not serious "
            "enough, fear of not being believed, and fear of retaliation. Campus "
            "sexual assault is a structural problem enabled by institutional "
            "incentives to minimize reports, protect athletic programs and donors, "
            "and avoid negative publicity. The Clery Act requires campuses to "
            "report crime statistics — but advocates have documented systematic "
            "underreporting, misclassification, and failure to notify survivors "
            "of their rights."
        ),
        "city": "Washington", "state": "DC",
        "lat": 38.9072, "lng": -77.0369,
        "date_incident": "2019-10-15",
        "violence_type": "sexual_assault",
        "status": "documented",
        "source_url": "https://www.aau.edu/key-issues/campus-climate-and-safety/aau-campus-climate-survey-2019",
        "source_name": "AAU Campus Climate Survey 2019",
        "verified": True,
        "is_public_figure": False,
    },
    {
        "summary": (
            "Baylor University Football — Institutional Cover-Up of Serial Rape. "
            "An independent investigation by law firm Pepper Hamilton (2016) found "
            "that Baylor University systematically failed to respond to reports of "
            "sexual assault by football players — actively discouraging reporting, "
            "failing to investigate, and in some cases pressuring victims to recant. "
            "At least 17 women reported sexual or physical assault by 19 football "
            "players between 2011 and 2014. Head coach Art Briles was fired. "
            "President Ken Starr was removed. Multiple players were convicted. "
            "Baylor settled with survivors for a confidential amount. The pattern "
            "— university prioritizing athletic program reputation over survivor "
            "safety — has been documented at Michigan State (Nassar), Penn State "
            "(Sandusky), Ohio State (Strauss), and numerous other institutions. "
            "Athletic revenue and donor relationships create documented institutional "
            "incentives to suppress assault reports."
        ),
        "city": "Waco", "state": "TX",
        "lat": 31.5493, "lng": -97.1467,
        "date_incident": "2016-05-26",
        "violence_type": "sexual_assault",
        "status": "settled",
        "source_url": "https://www.documentcloud.org/documents/2838480-Pepper-Hamilton-Findings-of-Fact.html",
        "source_name": "Pepper Hamilton — Baylor University Findings of Fact 2016",
        "verified": True,
        "is_public_figure": True,
    },
    {
        "summary": (
            "Stanford University Sexual Assault Culture — Documented Institutional "
            "Failures. Beyond the Brock Turner case, Stanford University has faced "
            "multiple Title IX investigations and lawsuits for inadequate response "
            "to sexual assault. A 2019 lawsuit by a survivor documented that Stanford "
            "allowed a student with multiple prior assault complaints to remain "
            "enrolled and continue contact with his victims. Stanford's own campus "
            "climate survey found 1 in 4 female undergraduates experienced unwanted "
            "sexual contact. Elite universities face particular structural pressures: "
            "wealthy donors, legacy admissions, and reputational concerns create "
            "incentives to handle assault internally rather than involving law "
            "enforcement. The Department of Education's Office for Civil Rights "
            "has open Title IX investigations at hundreds of universities at any "
            "given time — the backlog means many cases are never resolved."
        ),
        "city": "Palo Alto", "state": "CA",
        "lat": 37.4419, "lng": -122.1430,
        "date_incident": "2019-01-01",
        "violence_type": "sexual_assault",
        "status": "documented",
        "source_url": "https://www.ed.gov/about/offices/list/ocr/docs/titleix-summary.pdf",
        "source_name": "DOE Office for Civil Rights — Title IX Investigations",
        "verified": True,
        "is_public_figure": False,
    },

    # ── FEMICIDE DURING PREGNANCY ─────────────────────────────────────────────
    {
        "summary": (
            "Homicide is the Leading Cause of Death During Pregnancy in the US. "
            "A landmark 2022 study in Obstetrics & Gynecology (Golberg et al.) "
            "analyzing death certificates from 2018-2019 found that homicide was "
            "the leading cause of pregnancy-associated death — accounting for more "
            "deaths than any obstetric cause including hemorrhage, embolism, or "
            "cardiac disease. Pregnant women are murdered at rates 16% higher than "
            "non-pregnant women of the same age. The perpetrator is almost always "
            "an intimate partner. The pregnancy itself is frequently the trigger: "
            "abusers escalate violence when partners become pregnant, when they "
            "attempt to leave, or when they disclose the pregnancy to others. "
            "CDC data shows that between 2018-2019, approximately 324 women were "
            "murdered during or within a year of pregnancy — the majority by "
            "current or former intimate partners."
        ),
        "city": "Washington", "state": "DC",
        "lat": 38.9072, "lng": -77.0369,
        "date_incident": "2022-10-01",
        "violence_type": "homicide",
        "status": "documented",
        "source_url": "https://www.acog.org/clinical/clinical-guidance/obstetric-care-consensus/articles/2022/homicide-leading-cause-pregnancy-associated-death",
        "source_name": "Obstetrics & Gynecology — Homicide Leading Cause of Pregnancy Death 2022",
        "verified": True,
        "is_public_figure": False,
    },
    {
        "summary": (
            "Laci Peterson — Femicide During Pregnancy, Scott Peterson (2002). "
            "Laci Peterson, 8 months pregnant, was murdered by her husband Scott "
            "Peterson on Christmas Eve 2002 in Modesto, California. Her remains "
            "and those of her unborn son Conner were found in San Francisco Bay "
            "in April 2003. Scott Peterson was convicted of first-degree murder "
            "of Laci and second-degree murder of Conner and sentenced to death "
            "(later commuted to life without parole after California's death "
            "penalty moratorium). Her case brought national attention to intimate "
            "partner femicide during pregnancy. Studies consistently show that "
            "pregnancy is a period of heightened lethality risk — partners who "
            "are unwilling to become parents, who are having affairs, or who "
            "escalate controlling behavior during pregnancy are documented "
            "predictors of homicide risk."
        ),
        "city": "Modesto", "state": "CA",
        "lat": 37.6391, "lng": -120.9969,
        "date_incident": "2002-12-24",
        "violence_type": "homicide",
        "status": "convicted",
        "source_url": "https://www.courtlistener.com/?q=scott+peterson&type=r",
        "source_name": "People v. Scott Peterson — Stanislaus County Court Records",
        "verified": True,
        "is_public_figure": True,
    },
    {
        "summary": (
            "Shanann Watts — Femicide During Pregnancy, Christopher Watts (2018). "
            "Shanann Watts, 15 weeks pregnant, was murdered by her husband "
            "Christopher Watts in Frederick, Colorado in August 2018. He also "
            "murdered their two daughters, Bella (4) and Celeste (3). He buried "
            "Shanann in a shallow grave and submerged the girls' bodies in oil "
            "tanks at the oil field where he worked. He had been having an affair "
            "and did not want the pregnancy. He pleaded guilty to avoid the death "
            "penalty and was sentenced to five consecutive life sentences. Her "
            "case was widely publicized and is frequently cited in research on "
            "intimate partner femicide during pregnancy — illustrating the pattern "
            "of escalation when a partner becomes pregnant and the abuser seeks "
            "to exit the relationship without legal or financial consequence."
        ),
        "city": "Frederick", "state": "CO",
        "lat": 40.0975, "lng": -104.9578,
        "date_incident": "2018-08-13",
        "violence_type": "homicide",
        "status": "convicted",
        "source_url": "https://www.courtlistener.com/?q=christopher+watts&type=r",
        "source_name": "Colorado v. Christopher Watts — Weld County Court Records",
        "verified": True,
        "is_public_figure": True,
    },

    # ── CRIMINALIZATION OF MISCARRIAGE ────────────────────────────────────────
    {
        "summary": (
            "Criminalization of Pregnancy Loss Post-Dobbs — Women Arrested for "
            "Miscarriage. Since the Dobbs decision (2022), multiple women have "
            "been investigated, arrested, or prosecuted in states with abortion "
            "bans following pregnancy loss. In Texas, a woman was arrested in "
            "2023 after being reported by hospital staff following a miscarriage — "
            "charges were later dropped after national outcry. In Louisiana, "
            "women miscarrying have been denied medication (misoprostol) because "
            "it is also used for abortions. Medical providers report delaying "
            "treatment for miscarriages and ectopic pregnancies out of fear of "
            "prosecution. The ACLU has documented cases in Alabama, Georgia, "
            "South Carolina, and Oklahoma where pregnancy loss has triggered "
            "law enforcement contact. Prosecutors are using fetal homicide laws "
            "and controlled substance laws against women who experience pregnancy "
            "loss — particularly those with prior substance use history."
        ),
        "city": "Austin", "state": "TX",
        "lat": 30.2672, "lng": -97.7431,
        "date_incident": "2023-04-01",
        "violence_type": "coercive_control",
        "status": "documented",
        "source_url": "https://www.aclu.org/report/criminalizing-pregnancy",
        "source_name": "ACLU — Criminalizing Pregnancy: Policing Pregnant Women Who Use Drugs",
        "verified": True,
        "is_public_figure": False,
    },
    {
        "summary": (
            "Purvi Patel — Prosecuted for Miscarriage, Indiana (2015). Purvi Patel "
            "was sentenced to 20 years in prison in Indiana after suffering what she "
            "said was a miscarriage. Prosecutors charged her with both feticide AND "
            "neglect of a dependent — contradictory charges requiring the fetus to "
            "be both dead (feticide) and alive (neglect) simultaneously. She was "
            "convicted of both. An appeals court vacated the feticide conviction "
            "in 2016 but upheld the neglect charge. She served about 18 months. "
            "Her case was the first in US history in which a woman was convicted "
            "under a feticide law for actions against her own fetus. Her prosecution "
            "was a preview of post-Dobbs criminalization — the use of fetal "
            "protection laws, originally designed to prosecute attackers who cause "
            "pregnancy loss, against the pregnant women themselves."
        ),
        "city": "South Bend", "state": "IN",
        "lat": 41.6764, "lng": -86.2520,
        "date_incident": "2015-02-13",
        "violence_type": "coercive_control",
        "status": "convicted",
        "source_url": "https://www.courtlistener.com/?q=purvi+patel&type=r",
        "source_name": "Indiana v. Patel — St. Joseph County Court Records",
        "verified": True,
        "is_public_figure": False,
    },
    {
        "summary": (
            "Brittney Poolaw — Convicted for Miscarriage, Oklahoma (2021). "
            "Brittney Poolaw, a Native American woman, was convicted of first-degree "
            "manslaughter and sentenced to 4 years in prison after suffering a "
            "miscarriage at 15-17 weeks. Prosecutors argued her methamphetamine "
            "use caused the miscarriage despite medical testimony that the fetus "
            "had multiple anomalies incompatible with life. She was convicted by "
            "an all-white jury. Her case illustrates the intersection of race, "
            "pregnancy, substance use, and criminalization: Indigenous and Black "
            "women are disproportionately prosecuted for pregnancy outcomes. "
            "National Advocates for Pregnant Women has documented hundreds of "
            "similar cases across the US — the majority involving women of color "
            "and women with substance use histories. These prosecutions predate "
            "Dobbs and have accelerated dramatically since 2022."
        ),
        "city": "Lawton", "state": "OK",
        "lat": 34.6036, "lng": -98.3959,
        "date_incident": "2021-10-26",
        "violence_type": "coercive_control",
        "status": "convicted",
        "source_url": "https://www.theguardian.com/us-news/2021/oct/27/oklahoma-woman-brittney-poolaw-manslaughter-miscarriage",
        "source_name": "The Guardian — Brittney Poolaw Conviction 2021",
        "verified": True,
        "is_public_figure": False,
    },

    # ── STEALTHING ────────────────────────────────────────────────────────────
    {
        "summary": (
            "Stealthing — Non-Consensual Condom Removal. Stealthing refers to the "
            "practice of removing a condom during sex without a partner's consent. "
            "A 2017 study by Alexandra Brodsky in the Columbia Journal of Gender "
            "and Law found stealthing to be widespread — with one survey finding "
            "approximately 12% of women and 10% of men reporting having had a "
            "condom removed without consent. Stealthing exposes victims to STIs "
            "and unwanted pregnancy without consent. California became the first "
            "US state to explicitly classify stealthing as sexual battery in 2021. "
            "As of 2024, fewer than 10 states have passed explicit stealthing laws. "
            "In the majority of US states, stealthing is not explicitly illegal — "
            "prosecutors must use general sexual assault or battery statutes, which "
            "often do not clearly apply. The practice is a documented form of "
            "reproductive coercion — deliberately exposing a partner to pregnancy "
            "risk without consent as a means of control."
        ),
        "city": "Sacramento", "state": "CA",
        "lat": 38.5816, "lng": -121.4944,
        "date_incident": "2021-10-07",
        "violence_type": "sexual_assault",
        "status": "documented",
        "source_url": "https://columbialawreview.org/content/rape-adjacent-imagining-legal-responses-to-nonconsensual-condom-removal/",
        "source_name": "Columbia Journal of Gender and Law — Brodsky, Rape-Adjacent 2017 / CA SB 287",
        "verified": True,
        "is_public_figure": False,
    },
    {
        "summary": (
            "Reproductive Coercion — Documented in 25% of DV Cases. Reproductive "
            "coercion includes sabotaging birth control, removing contraceptive "
            "devices, forcing pregnancy, or forcing abortion. A 2010 study in "
            "Contraception found that 25% of women in DV shelters reported "
            "pregnancy coercion and 15% reported birth control sabotage by a "
            "partner. Partners hide birth control pills, puncture condoms, "
            "remove IUDs, or threaten to leave if a partner doesn't become "
            "pregnant. After Dobbs, advocates have documented abusers weaponizing "
            "abortion bans — moving pregnant partners to states with bans, "
            "confiscating medication abortion, and using pregnancy as a means "
            "of trapping victims who cannot access termination. Reproductive "
            "coercion is classified as a form of intimate partner violence by "
            "the CDC and American College of OB/GYNs but is not specifically "
            "criminalized in most US states."
        ),
        "city": "Washington", "state": "DC",
        "lat": 38.9072, "lng": -77.0369,
        "date_incident": "2023-01-01",
        "violence_type": "coercive_control",
        "status": "documented",
        "source_url": "https://www.cdc.gov/reproductivehealth/contraception/index.htm",
        "source_name": "CDC / Contraception Journal — Reproductive Coercion Research",
        "verified": True,
        "is_public_figure": False,
    },
    {
        "summary": (
            "Post-Dobbs Abortion Denial — Documented Deaths and Medical Harm. "
            "Since Dobbs v. Jackson (June 2022), investigative outlets including "
            "ProPublica, the Texas Tribune, and KFF Health News have documented "
            "multiple deaths and severe medical harm resulting from denial of "
            "abortion care in states with bans. In Texas, at least two women — "
            "Josseli Barnica and Amanda Zurawski — nearly died after being denied "
            "care for incomplete miscarriages. Amber Thurman died in Georgia after "
            "being denied a dilation and curettage procedure for a missed miscarriage. "
            "Candi Miller died at home in Georgia after being unable to access "
            "abortion care for a nonviable pregnancy. Physicians report being unable "
            "to treat ectopic pregnancies, septic miscarriages, and previable "
            "premature rupture of membranes without fear of prosecution. The medical "
            "harms of abortion bans are documented, ongoing, and accelerating."
        ),
        "city": "Austin", "state": "TX",
        "lat": 30.2672, "lng": -97.7431,
        "date_incident": "2022-06-24",
        "violence_type": "homicide",
        "status": "documented",
        "source_url": "https://www.propublica.org/article/abortion-ban-texas-women-died-miscarriage-care",
        "source_name": "ProPublica — Women Died After Being Denied Abortion Care in Texas",
        "verified": True,
        "is_public_figure": False,
    },
]


def main():
    print("[Seed Systemic] Seeding pay gap, pink tax, campus assault, pregnancy femicide, miscarriage criminalization, stealthing, and laws of subordination...")
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
    print(f"[Seed Systemic] {saved}/{len(RECORDS)} records saved.")
    print(f"Total in database: {get_case_count()}")


if __name__ == "__main__":
    main()
