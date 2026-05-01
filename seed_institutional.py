#!/usr/bin/env python3
"""
seed_institutional.py — Medusa institutional violence records

Seeds two categories:
1. Government actions that directly harm women's safety infrastructure
2. CDC/DOJ perpetrator relationship statistics — documents that most
   violence against women is committed by known men, not strangers

Run: python seed_institutional.py
"""

from medusa.database import init_db, save_case
from medusa.record import normalize_record

RECORDS = [

    # ── Women's Bureau Closure ────────────────────────────────────────────────
    {
        "summary": (
            "Trump administration proposed closure of the US Department of Labor "
            "Women's Bureau in May 2025 budget, eliminating the 105-year-old federal "
            "office created by Congress in 1920. The Bureau provided research on "
            "women's pay disparities, administered VAWA-related workplace grants, "
            "supported state paid leave programs covering ~50 million workers, and "
            "provided resources for victims of gender-based violence and harassment. "
            "DOGE simultaneously canceled congressionally mandated Women in "
            "Apprenticeship grants, dismissing them as 'wasteful DEI grants.' "
            "Source: National Partnership for Women & Families, June 4, 2025."
        ),
        "city":          "Washington",
        "state":         "DC",
        "date_incident": "2025-06-04",
        "violence_type": "coercive_control",
        "status":        "congressional_record",
        "source_url":    "https://nationalpartnership.org/news_post/npwf-condemns-proposed-closure-of-womens-bureau-in-trumps-budget/",
        "source_name":   "National Partnership for Women & Families / DOL",
        "verified":      True,
    },
    {
        "summary": (
            "DOGE eliminated the DOL Office of Federal Contract Compliance Programs "
            "(OFCCP) via executive order in January 2025, ending 40 years of "
            "enforcement requiring federal contractors to comply with "
            "anti-discrimination laws protecting women and minorities. The OFCCP "
            "had recovered $1B+ in back wages for workers including $1.8M for 600+ "
            "female LinkedIn employees subjected to discriminatory pay in 2022."
        ),
        "city":          "Washington",
        "state":         "DC",
        "date_incident": "2025-01-20",
        "violence_type": "coercive_control",
        "status":        "congressional_record",
        "source_url":    "https://tcf.org/content/report/what-cuts-to-the-department-of-labor-will-mean-for-you/",
        "source_name":   "The Century Foundation / DOL",
        "verified":      True,
    },

    # ── Who Assaults Women: CDC Perpetrator Statistics ─────────────────────────
    {
        "summary": (
            "CDC NISVS Data: Over half of female homicide victims in the US are "
            "killed by a current or former male intimate partner — not a stranger. "
            "1 in 5 homicide victims overall are killed by an intimate partner. "
            "The presence of a gun in a domestic violence situation increases the "
            "risk of homicide for women by 500%. More than half of women killed by "
            "gun violence are killed by family members or intimate partners. "
            "Source: CDC National Intimate Partner and Sexual Violence Survey."
        ),
        "city":          "Washington",
        "state":         "DC",
        "date_incident": "2022-01-01",
        "violence_type": "homicide",
        "status":        "reported",
        "source_url":    "https://www.cdc.gov/intimate-partner-violence/about/index.html",
        "source_name":   "CDC — National Intimate Partner and Sexual Violence Survey",
        "verified":      True,
    },
    {
        "summary": (
            "CDC NISVS Data: More than 1 in 3 women (43.5 million) in the US have "
            "experienced contact sexual violence, physical violence, and/or stalking "
            "by an intimate partner in their lifetime. About 1 in 4 women experience "
            "physical violence by an intimate partner. About 1 in 5 women have "
            "experienced completed or attempted rape. 48.7% of female rape victims "
            "were first raped before age 18. The vast majority of perpetrators are "
            "known to the victim — intimate partners, family members, or acquaintances. "
            "Source: CDC NISVS 2016/2017 Report."
        ),
        "city":          "Washington",
        "state":         "DC",
        "date_incident": "2022-01-01",
        "violence_type": "sexual_assault",
        "status":        "reported",
        "source_url":    "https://www.cdc.gov/nisvs/documentation/NISVSReportonIPV_2022.pdf",
        "source_name":   "CDC — National Intimate Partner and Sexual Violence Survey",
        "verified":      True,
    },
    {
        "summary": (
            "CDC NISVS Data: Women of color face disproportionate rates of intimate "
            "partner violence. Nearly 2 in 3 non-Hispanic multiracial women (63.8%), "
            "more than half of American Indian or Alaska Native women (57.7%), and "
            "more than half of non-Hispanic Black women have experienced contact "
            "sexual violence, physical violence, and/or stalking by an intimate "
            "partner in their lifetimes. Rates are 30-50% higher than those "
            "experienced by Hispanic and white non-Hispanic women. "
            "Source: CDC NISVS 2016/2017 Report."
        ),
        "city":          "Washington",
        "state":         "DC",
        "date_incident": "2022-01-01",
        "violence_type": "domestic_violence",
        "status":        "reported",
        "source_url":    "https://www.cdc.gov/nisvs/documentation/NISVSReportonIPV_2022.pdf",
        "source_name":   "CDC — National Intimate Partner and Sexual Violence Survey",
        "verified":      True,
    },
    {
        "summary": (
            "CDC / Bureau of Justice Statistics: Intimate partner violence accounts "
            "for 15% of all violent crime in the US. About 16 million women first "
            "experienced intimate partner violence before age 18. The lifetime "
            "economic cost of IPV — medical care, lost productivity, criminal justice "
            "— is $3.6 trillion. Cost per female victim over her lifetime: $103,767. "
            "96% of employed domestic violence victims experience problems at work "
            "due to abuse. Current or former intimate partners accounted for nearly "
            "33% of women killed in US workplaces between 2003 and 2008. "
            "Source: CDC NISVS / Bureau of Justice Statistics."
        ),
        "city":          "Washington",
        "state":         "DC",
        "date_incident": "2022-01-01",
        "violence_type": "domestic_violence",
        "status":        "reported",
        "source_url":    "https://www.thehotline.org/stakeholders/domestic-violence-statistics/",
        "source_name":   "CDC / Bureau of Justice Statistics via National DV Hotline",
        "verified":      True,
    },
    {
        "summary": (
            "WHO Global Data: Globally, 38% of all murders of women are committed "
            "by intimate partners. Nearly 1 in 3 women worldwide aged 15-49 who "
            "have been in a relationship report physical and/or sexual violence by "
            "an intimate partner. Intimate partner and sexual violence is "
            "predominantly perpetrated by men against women. Women who experience "
            "IPV are twice as likely to suffer depression, almost twice as likely "
            "to have an abortion, 16% more likely to suffer a miscarriage, and "
            "41% more likely to have a preterm birth. Source: WHO, 2024."
        ),
        "city":          "Washington",
        "state":         "DC",
        "date_incident": "2024-03-25",
        "violence_type": "domestic_violence",
        "status":        "reported",
        "source_url":    "https://www.who.int/news-room/fact-sheets/detail/violence-against-women",
        "source_name":   "World Health Organization",
        "verified":      True,
    },
]


def main():
    print("\n[Seed Institutional] Seeding institutional records and statistics...\n")
    init_db()
    saved = 0
    for raw in RECORDS:
        record = normalize_record(raw)
        if record and save_case(record):
            saved += 1
            print(f"  + [{record['violence_type'].upper()}] {record['summary'][:80]}...")
    print(f"\n[Seed Institutional] {saved}/{len(RECORDS)} records saved.\n")


if __name__ == "__main__":
    main()
