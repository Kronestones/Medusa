#!/usr/bin/env python3
"""
seed_statistics.py — Current verified violence statistics

Sources:
  CDC NISVS 2023/2024 Data Brief (released 2025) — most current available
  CDC NISVS 2016/2017 IPV Report
  HRC Epidemic of Violence 2024 Report
  WHO Violence Against Women Fact Sheet 2024
  Bureau of Justice Statistics
  National DV Hotline 2025

Run: python seed_statistics.py
"""

from medusa.database import init_db, save_case
from medusa.record import normalize_record

RECORDS = [

    # ── Sexual Violence — CDC NISVS 2023/2024 ─────────────────────────────────
    {
        "summary": (
            "CDC NISVS 2023/2024: Nearly half of women in the United States (45.1%) "
            "have experienced some form of contact sexual violence in their lifetimes. "
            "21.0% reported completed or attempted rape. 20.3% reported sexual "
            "coercion. 39.0% reported unwanted sexual contact. Data collected from "
            "8,842 women September 2023 through September 2024. These are likely "
            "underestimates — the survey excludes institutionalized and unhoused adults."
        ),
        "city": "Washington", "state": "DC",
        "date_incident": "2025-01-01",
        "violence_type": "sexual_assault",
        "status": "reported",
        "source_url": "https://www.cdc.gov/nisvs/media/pdfs/sexualviolence-brief.pdf",
        "source_name": "CDC NISVS 2023/2024 Sexual Violence Data Brief",
        "verified": True,
    },
    {
        "summary": (
            "CDC NISVS 2023/2024: Approximately 1 in 3 women in the US experienced "
            "verbal sexual harassment in the workplace (30.4%) or a public place "
            "(29.5%) in their lifetimes. More than 1 in 4 women (28.2%) experienced "
            "technology-facilitated sexual violence — including non-consensual sharing "
            "of intimate images, online sexual harassment, and sexual extortion."
        ),
        "city": "Washington", "state": "DC",
        "date_incident": "2025-01-01",
        "violence_type": "harassment",
        "status": "reported",
        "source_url": "https://www.cdc.gov/nisvs/media/pdfs/sexualviolence-brief.pdf",
        "source_name": "CDC NISVS 2023/2024 Sexual Violence Data Brief",
        "verified": True,
    },

    # ── Stalking — CDC NISVS 2023/2024 ───────────────────────────────────────
    {
        "summary": (
            "CDC NISVS 2023/2024: More than 1 in 5 women (22.5% — approximately "
            "28.8 million women) in the United States have experienced stalking during "
            "their lifetimes. Nearly all female stalking victims (98.7%) felt afraid, "
            "threatened, or concerned for their safety or the safety of others. "
            "The majority of stalking perpetrators are known to the victim."
        ),
        "city": "Washington", "state": "DC",
        "date_incident": "2025-01-01",
        "violence_type": "stalking",
        "status": "reported",
        "source_url": "https://vawnet.org/material/national-intimate-partner-and-sexual-violence-survey-20232024-stalking-data-brief",
        "source_name": "CDC NISVS 2023/2024 Stalking Data Brief",
        "verified": True,
    },

    # ── Intimate Partner Violence — CDC NISVS 2016/2017 ──────────────────────
    {
        "summary": (
            "CDC NISVS: 47.3% of women in the United States have experienced intimate "
            "partner violence in the form of contact sexual violence, physical violence, "
            "or stalking. 49.4% have experienced psychological aggression by an intimate "
            "partner. Nearly 1 in 4 women experience severe physical violence from a "
            "partner. 85% of domestic violence victims are female. "
            "Source: CDC NISVS 2016/2017 Report on Intimate Partner Violence."
        ),
        "city": "Washington", "state": "DC",
        "date_incident": "2022-01-01",
        "violence_type": "domestic_violence",
        "status": "reported",
        "source_url": "https://www.cdc.gov/nisvs/documentation/NISVSReportonIPV_2022.pdf",
        "source_name": "CDC NISVS 2016/2017 Report on Intimate Partner Violence",
        "verified": True,
    },
    {
        "summary": (
            "CDC NISVS: Race and ethnicity disparities in intimate partner violence. "
            "Lifetime IPV prevalence by group: Multiracial women 63.8%, American Indian "
            "or Alaska Native women 57.7%, Black women 53.6%, Hispanic women 37.1%, "
            "white women 34.7%. Police-reported IPV rates are 2-3 times higher among "
            "Black and Hispanic women than white women. "
            "Source: CDC NISVS 2016/2017 / NCBI 2024."
        ),
        "city": "Washington", "state": "DC",
        "date_incident": "2022-01-01",
        "violence_type": "domestic_violence",
        "status": "reported",
        "source_url": "https://www.ncbi.nlm.nih.gov/books/NBK605464/",
        "source_name": "CDC NISVS / NCBI — IPV by Race and Ethnicity",
        "verified": True,
    },
    {
        "summary": (
            "CDC / National DV Hotline 2025: Every minute, 24 people are victims of "
            "intimate partner violence — over 16 million victims annually. "
            "Approximately 75% of domestic violence-related deaths are women. "
            "An estimated 4 women are murdered by intimate partners daily in the US. "
            "Women in the US are 11 times more likely to be killed with guns compared "
            "to women in other high-income countries. "
            "The presence of a firearm raises DV homicide risk by 500%."
        ),
        "city": "Washington", "state": "DC",
        "date_incident": "2025-01-01",
        "violence_type": "homicide",
        "status": "reported",
        "source_url": "https://www.thehotline.org/stakeholders/domestic-violence-statistics/",
        "source_name": "National DV Hotline / CDC 2025",
        "verified": True,
    },
    {
        "summary": (
            "Bureau of Justice Statistics / CDC: Intimate partner violence accounts for "
            "15% of all violent crime in the US. 96% of employed domestic violence "
            "victims experience problems at work due to abuse — including being "
            "harassed at work by their abuser, arriving late, missing work, or losing "
            "their job. 44% of full-time workers have experienced the effects of DV "
            "in the workplace. Current or former intimate partners accounted for nearly "
            "33% of women killed in US workplaces between 2003 and 2008."
        ),
        "city": "Washington", "state": "DC",
        "date_incident": "2025-01-01",
        "violence_type": "domestic_violence",
        "status": "reported",
        "source_url": "https://www.thehotline.org/stakeholders/domestic-violence-statistics/",
        "source_name": "Bureau of Justice Statistics / National DV Hotline",
        "verified": True,
    },
    {
        "summary": (
            "CDC: Lifetime economic cost of intimate partner violence against women in "
            "the US is $3.6 trillion. Cost per female victim over her lifetime: "
            "$103,767 — including medical care, lost productivity, criminal justice "
            "costs, and other expenses. IPV costs the US economy more than $8.3 billion "
            "per year in healthcare and lost productivity alone."
        ),
        "city": "Washington", "state": "DC",
        "date_incident": "2022-01-01",
        "violence_type": "domestic_violence",
        "status": "reported",
        "source_url": "https://www.cdc.gov/intimate-partner-violence/about/index.html",
        "source_name": "CDC — Economic Cost of Intimate Partner Violence",
        "verified": True,
    },

    # ── Teen / Youth Dating Violence ──────────────────────────────────────────
    {
        "summary": (
            "CDC Youth Risk Behavior Survey 2024: 1 in 10 high school students have "
            "experienced physical teen dating violence. 1 in 3 college women report "
            "experiencing abuse in relationships, ranging from physical to digital forms "
            "of control. Female respondents reported significantly higher prevalence of "
            "physical or sexual dating violence than male respondents (20.9% vs 10.4%). "
            "Youth who experience marginalization have higher reported prevalence. "
            "Source: CDC YRBSS 2024 / National DV Hotline 2025."
        ),
        "city": "Washington", "state": "DC",
        "date_incident": "2024-01-01",
        "violence_type": "domestic_violence",
        "status": "reported",
        "source_url": "https://www.cdc.gov/yrbss/index.htm",
        "source_name": "CDC Youth Risk Behavior Surveillance System 2024",
        "verified": True,
    },

    # ── Homicide ──────────────────────────────────────────────────────────────
    {
        "summary": (
            "CDC NISVS: Over half of female homicide victims in the US are killed by a "
            "current or former intimate male partner — not a stranger. 1 in 5 homicide "
            "victims overall are killed by an intimate partner. More than half of women "
            "killed by gun violence are killed by family members or intimate partners. "
            "4 women are murdered by intimate partners daily in the United States. "
            "Source: CDC / Violence Policy Center."
        ),
        "city": "Washington", "state": "DC",
        "date_incident": "2025-01-01",
        "violence_type": "homicide",
        "status": "reported",
        "source_url": "https://www.cdc.gov/intimate-partner-violence/about/index.html",
        "source_name": "CDC — Intimate Partner Homicide Statistics",
        "verified": True,
    },

    # ── Rape ──────────────────────────────────────────────────────────────────
    {
        "summary": (
            "CDC NISVS 2023/2024: 21% of women in the US have experienced completed or "
            "attempted rape in their lifetimes. 48.7% of female rape victims were first "
            "raped before age 18. 79.6% knew their perpetrator — including intimate "
            "partners, family members, friends, and acquaintances. Rape is profoundly "
            "underreported: only an estimated 20-30% of rapes are reported to police. "
            "Source: CDC NISVS 2023/2024."
        ),
        "city": "Washington", "state": "DC",
        "date_incident": "2025-01-01",
        "violence_type": "rape",
        "status": "reported",
        "source_url": "https://www.cdc.gov/nisvs/media/pdfs/sexualviolence-brief.pdf",
        "source_name": "CDC NISVS 2023/2024 Sexual Violence Data Brief",
        "verified": True,
    },

    # ── WHO Global ────────────────────────────────────────────────────────────
    {
        "summary": (
            "WHO 2024: Globally, 38% of all murders of women are committed by intimate "
            "partners. Nearly 1 in 3 women worldwide aged 15-49 have experienced "
            "physical and/or sexual violence by an intimate partner. Violence against "
            "women is predominantly perpetrated by men. Women who experience IPV are: "
            "2× more likely to suffer depression, 1.5× more likely to acquire HIV, "
            "41% more likely to have a preterm birth, and nearly twice as likely to "
            "have an abortion. Source: WHO Violence Against Women Fact Sheet, 2024."
        ),
        "city": "Washington", "state": "DC",
        "date_incident": "2024-03-25",
        "violence_type": "domestic_violence",
        "status": "reported",
        "source_url": "https://www.who.int/news-room/fact-sheets/detail/violence-against-women",
        "source_name": "World Health Organization — Violence Against Women 2024",
        "verified": True,
    },
# ── Trans Violence — HRC 2024 ─────────────────────────────────────────────
    {
        "summary": (
            "HRC Epidemic of Violence 2024: At least 36 transgender and gender-expansive "
            "people were killed in the US in the 12-month period ending November 2024. "
            "Since 2013, HRC has recorded 372 deaths — with the actual number likely "
            "much higher due to misgendering and underreporting. 84.4% of all victims "
            "identified since 2013 were Black, Indigenous, or people of color. "
            "73.7% of all victims have been Black trans women — 274 lives. "
            "Guns were involved in the majority of cases. In 38.2% of cases, "
            "no arrest has been made. Source: HRC Foundation 2024."
        ),
        "city": "Washington", "state": "DC",
        "date_incident": "2024-11-20",
        "violence_type": "trans_violence",
        "status": "reported",
        "source_url": "https://reports.hrc.org/an-epidemic-of-violence-2024",
        "source_name": "HRC Foundation — Epidemic of Violence 2024",
        "verified": True,
    },
    {
        "summary": (
            "HRC 2025 Annual Report: 27 transgender and gender-nonconforming people were "
            "killed in the US in the 12-month period ending November 20, 2025. Since "
            "2013, a total of 399 trans and gender nonconforming people have been killed. "
            "43.9% of trans adults reported experiencing discrimination based on gender "
            "identity in 2025. 57.6% said they were less open about their LGBTQ+ "
            "identities compared to a year ago amid escalating anti-trans legislation. "
            "Over 500 anti-LGBTQ+ bills were introduced in 2024, over 40 passed into law."
            " Source: HRC Foundation Annual Report 2025."
        ),
        "city": "Washington", "state": "DC",
        "date_incident": "2025-11-20",
        "violence_type": "trans_violence",
        "status": "reported",
        "source_url": "https://www.hrc.org/press-releases/remembrance-is-not-enough-hrcs-annual-report-outlines-ongoing-onslaught-of-violence-against-trans-people-amid-relentless-political-attacks",
        "source_name": "HRC Foundation Annual Report 2025",
        "verified": True,
    },

    # ── Child Abuse ───────────────────────────────────────────────────────────
    {
        "summary": (
            "CDC / Childhelp National Child Abuse Hotline: Approximately 700,000 children "
            "are abused annually in the US. 1 in 4 girls and 1 in 13 boys experience "
            "sexual abuse at some point in childhood. 91% of child sexual abuse is "
            "perpetrated by someone the child or family knows. Children who experience "
            "abuse are 25% more likely to experience teen pregnancy, 30% more likely to "
            "commit a violent crime, and are at significantly higher risk for adult IPV "
            "victimization. Child abuse costs the US $124 billion annually."
        ),
        "city": "Washington", "state": "DC",
        "date_incident": "2024-01-01",
        "violence_type": "child_abuse",
        "status": "reported",
        "source_url": "https://www.childhelp.org/child-abuse-statistics/",
        "source_name": "CDC / Childhelp National Child Abuse Statistics",
        "verified": True,
    },

    # ── Human Trafficking ─────────────────────────────────────────────────────
    {
        "summary": (
            "US Dept of State / Polaris Project: An estimated 24.9 million people are "
            "victims of human trafficking globally at any given time. In the US, the "
            "National Human Trafficking Hotline receives 40,000+ contacts per year. "
            "Women and girls account for 71% of all trafficking victims globally and "
            "99% of victims in the commercial sex industry. The average age of entry "
            "into sex trafficking in the US is 12-14 years old. Traffickers are most "
            "commonly intimate partners or family members of victims."
        ),
        "city": "Washington", "state": "DC",
        "date_incident": "2024-01-01",
        "violence_type": "trafficking",
        "status": "reported",
        "source_url": "https://polarisproject.org/human-trafficking/",
        "source_name": "US Dept of State / Polaris Project",
        "verified": True,
    },

    # ── Coercive Control ──────────────────────────────────────────────────────
    {
        "summary": (
            "CDC / National DV Hotline: Coercive control — a pattern of behavior used "
            "to dominate and isolate — affects an estimated 60-80% of domestic violence "
            "victims. It includes financial abuse, reproductive coercion, isolation from "
            "family and friends, monitoring of communications, and threats. Coercive "
            "control is the most reliable predictor of lethal domestic violence, more "
            "so than physical violence alone. Only a handful of US states have enacted "
            "laws specifically criminalizing coercive control — it remains legal in the "
            "majority of states."
        ),
        "city": "Washington", "state": "DC",
        "date_incident": "2024-01-01",
        "violence_type": "coercive_control",
        "status": "reported",
        "source_url": "https://www.thehotline.org/resources/what-is-coercive-control/",
        "source_name": "National DV Hotline / CDC",
        "verified": True,
    },

    # ── Underreporting ────────────────────────────────────────────────────────
    {
        "summary": (
            "Bureau of Justice Statistics: Intimate partner violence is severely "
            "underreported. Only 53% of IPV incidents are reported to police. Rape is "
            "reported to police at an estimated 20-30% rate. Sexual assault by an "
            "acquaintance is reported at even lower rates. Reasons for non-reporting "
            "include fear of retaliation, distrust of police, shame, financial "
            "dependence on abuser, immigration status concerns, and prior negative "
            "experiences with the criminal justice system. Medusa documents only "
            "publicly recorded cases — the vast majority of violence never appears "
            "in any official record."
        ),
        "city": "Washington", "state": "DC",
        "date_incident": "2024-01-01",
        "violence_type": "assault",
        "status": "reported",
        "source_url": "https://bjs.ojp.gov/content/pub/pdf/ipvus.pdf",
        "source_name": "Bureau of Justice Statistics — Underreporting of IPV",
        "verified": True,
    },

]


def main():
    print("\n[Seed Statistics] Seeding verified violence statistics...\n")
    init_db()
    saved = 0
    for raw in RECORDS:
        record = normalize_record(raw)
        if record and save_case(record):
            saved += 1
            print(f"  + [{record['violence_type'].upper()}] {record['summary'][:75]}...")
    print(f"\n[Seed Statistics] {saved}/{len(RECORDS)} records saved.\n")


if __name__ == "__main__":
    main()
