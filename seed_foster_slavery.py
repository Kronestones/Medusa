#!/usr/bin/env python3
"""
seed_foster_slavery.py — Foster care to trafficking pipeline, aged-out
girls, and the history of sexual slavery targeting women and girls.

Sources: FBI, HHS, congressional testimony, court records, investigative
journalism, National Center for Missing and Exploited Children.

Run: python3 seed_foster_slavery.py
"""

from medusa.database import init_db, save_case
from medusa.record import normalize_record

RECORDS = [

    # ── FOSTER CARE TO TRAFFICKING PIPELINE ──────────────────────────────────
    {
        "summary": (
            "Foster Care to Sex Trafficking Pipeline — Federal Data. The FBI and "
            "HHS have documented a direct pipeline from foster care to sex "
            "trafficking. In 2013, the FBI reported that 60% of child sex "
            "trafficking victims recovered in a national operation had come from "
            "the foster care or group home system. A 2019 HHS report found that "
            "approximately 40% of confirmed trafficking victims had prior child "
            "welfare involvement. Girls who age out of foster care at 18 without "
            "stable housing, income, or family support are among the most vulnerable "
            "trafficking targets. Traffickers specifically recruit at group homes, "
            "shelters, and in communities near child welfare offices — offering "
            "housing, affection, and belonging to girls who have none. The Preventing "
            "Sex Trafficking and Strengthening Families Act (2014) required states "
            "to document trafficking among youth in foster care — but implementation "
            "has been inconsistent and underfunded. Girls of color are "
            "disproportionately represented in both the foster care system and "
            "among trafficking victims."
        ),
        "city": "Washington", "state": "DC",
        "lat": 38.9072, "lng": -77.0369,
        "date_incident": "2019-01-01",
        "violence_type": "trafficking",
        "status": "documented",
        "source_url": "https://www.acf.hhs.gov/sites/default/files/documents/cb/sex_trafficking_data.pdf",
        "source_name": "HHS — Sex Trafficking of Minors in Foster Care / FBI 2013 Operation Cross Country",
        "verified": True,
        "is_public_figure": False,
    },
    {
        "summary": (
            "Aging Out of Foster Care — The Cliff at 18. Each year, approximately "
            "20,000 young people age out of the US foster care system at 18 — "
            "often with no housing, no financial support, no family, and no "
            "preparation for independent living. Studies consistently show that "
            "within 4 years of aging out: 50% will experience homelessness, "
            "25% will experience post-traumatic stress disorder, 30% will have "
            "no high school diploma, and fewer than 3% will earn a college degree. "
            "Girls who age out face acute trafficking risk — traffickers specifically "
            "target girls leaving group homes and transitional housing. The Family "
            "First Prevention Services Act (2018) and subsequent legislation have "
            "extended some support to age 21 in participating states — but "
            "implementation is incomplete. Many states still cut off support at "
            "18. The foster care cliff is a documented federal policy failure "
            "that funnels vulnerable girls directly into the conditions traffickers exploit."
        ),
        "city": "Washington", "state": "DC",
        "lat": 38.9072, "lng": -77.0369,
        "date_incident": "2023-01-01",
        "violence_type": "trafficking",
        "status": "documented",
        "source_url": "https://www.childwelfare.gov/topics/systemwide/youth/independentliving/",
        "source_name": "Child Welfare Information Gateway — Aging Out of Foster Care",
        "verified": True,
        "is_public_figure": False,
    },
    {
        "summary": (
            "DCFS and Group Home Failures — Children Trafficked While in State "
            "Custody. Multiple investigations have documented that children have "
            "been trafficked while in the legal custody of state child welfare "
            "agencies — from group homes, residential facilities, and foster "
            "placements. A 2018 Senate Permanent Subcommittee on Investigations "
            "report found that children in HHS-funded shelters were trafficked "
            "by staff and other residents. In Georgia, a 2019 investigation found "
            "girls in DFCS custody were being trafficked from group homes in "
            "Atlanta. In Los Angeles, the DCFS has faced repeated findings of "
            "children going missing from placements and being found in trafficking "
            "situations. The systemic issue: group homes and residential facilities "
            "are under-supervised, understaffed, and in some cases run by operators "
            "who are themselves connected to trafficking networks. Children who "
            "go missing from these placements are often not reported promptly "
            "to law enforcement."
        ),
        "city": "Atlanta", "state": "GA",
        "lat": 33.7490, "lng": -84.3880,
        "date_incident": "2019-01-01",
        "violence_type": "trafficking",
        "status": "documented",
        "source_url": "https://www.hsgac.senate.gov/subcommittees/investigations/media/federal-failures-put-thousands-of-unaccompanied-alien-children-at-risk",
        "source_name": "Senate PSI — HHS Shelter Failures / Georgia DFCS Investigation",
        "verified": True,
        "is_public_figure": False,
    },

    # ── SLAVERY AND SEXUAL VIOLENCE ───────────────────────────────────────────
    {
        "summary": (
            "Slavery and Sexual Violence — Systematic Rape as a Tool of Control. "
            "The sexual violation of enslaved Black women was a foundational feature "
            "of American slavery — not incidental to it. Enslaved women had no "
            "legal protection from rape. Owners, overseers, and other white men "
            "raped enslaved women with complete impunity — the law explicitly "
            "excluded enslaved people from rape protections. Rape was used as a "
            "tool of terror, control, and forced reproduction — enslaved women "
            "were bred to produce more enslaved people as property. The children "
            "of rape were themselves enslaved. This sexual violence was never "
            "prosecuted. No reparations were ever made. The psychological, "
            "familial, and economic consequences — including the destruction of "
            "family structures, the theft of bodily autonomy across generations, "
            "and the establishment of racial hierarchies of whose bodies matter — "
            "are documented in scholarship as foundational to contemporary racial "
            "disparities in violence against Black women. Buck v. Bell (1927), "
            "which permitted forced sterilization and was never overturned, "
            "extended the logic of bodily ownership into the 20th century."
        ),
        "city": "Washington", "state": "DC",
        "lat": 38.9072, "lng": -77.0369,
        "date_incident": "1865-12-06",
        "violence_type": "rape",
        "status": "documented",
        "source_url": "https://www.nps.gov/subjects/undergroundrailroad/sexual-violence.htm",
        "source_name": "NPS — Sexual Violence Under Slavery / Legal Scholarship on Slavery and Rape Law",
        "verified": True,
        "is_public_figure": False,
    },
    {
        "summary": (
            "Buck v. Bell (1927) — Forced Sterilization Still Legal. In Buck v. Bell, "
            "the Supreme Court ruled 8-1 that states could forcibly sterilize "
            "people deemed 'unfit' — including people with disabilities, the poor, "
            "immigrants, and people of color. Justice Oliver Wendell Holmes wrote: "
            "'Three generations of imbeciles are enough.' The ruling led to the "
            "forced sterilization of approximately 60,000 Americans — the majority "
            "women — in 32 states. The eugenics programs targeted poor white women, "
            "Black women, Indigenous women, and women with disabilities. California "
            "sterilized more people than any other state — its program was studied "
            "and praised by Nazi Germany before World War II. Buck v. Bell has "
            "never been overturned by the Supreme Court. It remains valid precedent. "
            "Subsequent forced sterilization cases — including the Indian Health "
            "Service and California prison programs — have occurred in its shadow. "
            "Women in the US have no constitutional protection against forced "
            "sterilization based on this ruling."
        ),
        "city": "Washington", "state": "DC",
        "lat": 38.9072, "lng": -77.0369,
        "date_incident": "1927-05-02",
        "violence_type": "assault",
        "status": "documented",
        "source_url": "https://supreme.justia.com/cases/federal/us/274/200/",
        "source_name": "Buck v. Bell, 274 U.S. 200 (1927) — Never Overturned",
        "verified": True,
        "is_public_figure": False,
    },
    {
        "summary": (
            "California Prison Forced Sterilization — 2006–2010. A 2013 "
            "investigation by the Center for Investigative Reporting found that "
            "approximately 150 women were sterilized in California state prisons "
            "between 2006 and 2010 without required state approvals — and in some "
            "cases without informed consent. Prison doctors pressured women who "
            "had multiple children or who were deemed likely to return to prison "
            "to agree to tubal ligations. One doctor told the reporter the "
            "procedures were cost-effective compared to 'welfare babies.' The "
            "women were often approached while in labor or immediately postpartum — "
            "a time when informed consent is legally and ethically compromised. "
            "A subsequent audit found the numbers may have been higher — up to "
            "250 procedures. California enacted a law in 2014 prohibiting "
            "sterilization of inmates without specific review. No doctor was "
            "criminally prosecuted. The case directly echoed the Indian Health "
            "Service sterilizations of the 1970s."
        ),
        "city": "Sacramento", "state": "CA",
        "lat": 38.5816, "lng": -121.4944,
        "date_incident": "2013-07-07",
        "violence_type": "assault",
        "status": "documented",
        "source_url": "https://revealnews.org/article/california-prisons-illegally-sterilized-female-inmates/",
        "source_name": "Reveal / Center for Investigative Reporting — California Prison Sterilization 2013",
        "verified": True,
        "is_public_figure": False,
    },
    {
        "summary": (
            "Comfort Women — WWII Sexual Slavery and US Geopolitical Cover-Up. "
            "An estimated 200,000 women and girls — predominantly Korean, Chinese, "
            "Filipino, and Indonesian — were forced into sexual slavery by the "
            "Imperial Japanese military during World War II. Known as 'comfort "
            "women,' they were held in military brothels, raped repeatedly by "
            "soldiers, and in many cases killed or abandoned at the end of the war. "
            "Survivors spent decades seeking acknowledgment and reparations from "
            "Japan. The US government, in the interest of maintaining the US-Japan "
            "alliance during the Cold War, actively suppressed documentation of "
            "the comfort women system — including concealing evidence discovered "
            "during the occupation of Japan. The 2007 US House Resolution 121 "
            "called on Japan to formally acknowledge and apologize — it was "
            "non-binding and Japan has never issued a full apology. Survivors "
            "have died waiting for justice. The last known survivors are elderly. "
            "Their testimony represents one of the most documented cases of "
            "state-organized mass sexual slavery in modern history."
        ),
        "city": "Washington", "state": "DC",
        "lat": 38.9072, "lng": -77.0369,
        "date_incident": "1945-09-02",
        "violence_type": "trafficking",
        "status": "documented",
        "source_url": "https://www.congress.gov/bill/110th-congress/house-concurrent-resolution/121",
        "source_name": "US House Resolution 121 (2007) / Korean Council for Justice and Remembrance",
        "verified": True,
        "is_public_figure": False,
    },
    {
        "summary": (
            "Modern Slavery in the United States — Domestic Servitude and "
            "Agricultural Trafficking. The US State Department estimates that "
            "between 14,500 and 17,500 people are trafficked into the United "
            "States annually — the majority women and girls. Domestic servitude "
            "— in which women are brought to the US on false promises and forced "
            "to work as household staff without pay, unable to leave — is one "
            "of the most common forms. Agricultural trafficking — documented in "
            "Florida, California, North Carolina, and other agricultural states "
            "— holds women and girls in forced labor on farms. The H-2A and "
            "other guest worker visa programs have been documented as vectors "
            "for labor trafficking — workers tied to a specific employer cannot "
            "leave abusive situations without losing their visa status. Polaris "
            "Project's National Human Trafficking Hotline received over 51,000 "
            "contacts in 2022 — with domestic work, agriculture, and commercial "
            "sex as the leading industries. Women of color and immigrant women "
            "are disproportionately victimized."
        ),
        "city": "Washington", "state": "DC",
        "lat": 38.9072, "lng": -77.0369,
        "date_incident": "2022-01-01",
        "violence_type": "trafficking",
        "status": "documented",
        "source_url": "https://polarisproject.org/2022-us-national-human-trafficking-hotline-statistics/",
        "source_name": "Polaris Project — 2022 National Human Trafficking Hotline Statistics",
        "verified": True,
        "is_public_figure": False,
    },
]


def main():
    print("[Seed Foster/Slavery] Seeding foster care trafficking pipeline and slavery records...")
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
    print(f"[Seed Foster/Slavery] {saved}/{len(RECORDS)} records saved.")
    print(f"Total in database: {get_case_count()}")


if __name__ == "__main__":
    main()
