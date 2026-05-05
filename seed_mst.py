#!/usr/bin/env python3
"""
seed_mst.py — Military Sexual Trauma (MST), reporting suppression,
VA failures, and the systemic protection of perpetrators in the US military.

Sources: DoD Annual Reports on Sexual Assault, VA, GAO, congressional
testimony, court records, investigative journalism.

Run: python3 seed_mst.py
"""

from medusa.database import init_db, save_case
from medusa.record import normalize_record

RECORDS = [

    # ── SCALE OF THE PROBLEM ──────────────────────────────────────────────────
    {
        "summary": (
            "Military Sexual Trauma — Scale and Systemic Suppression. The Department "
            "of Defense 2023 Annual Report on Sexual Assault documented 7,794 reports "
            "of sexual assault involving service members — but estimates that only "
            "20% of assaults are reported. This means an estimated 35,000–40,000 "
            "sexual assaults occur in the US military every year. Women in the "
            "military are sexually assaulted at rates dramatically higher than "
            "their civilian peers. 1 in 3 women veterans reports being sexually "
            "assaulted during their service. The military's own data shows that "
            "retaliation against survivors who report is common — 62% of women "
            "who reported assault in a 2021 RAND survey said they experienced "
            "social or professional retaliation. Perpetrators face low prosecution "
            "rates: of substantiated cases, fewer than 30% result in court-martial. "
            "The military justice system — which historically kept prosecution "
            "decisions with commanding officers who often protected perpetrators — "
            "was partially reformed by the Military Justice Improvement Act (2022), "
            "which removed some cases from commander discretion. Advocates call "
            "the reform incomplete."
        ),
        "city": "Washington", "state": "DC",
        "lat": 38.9072, "lng": -77.0369,
        "date_incident": "2023-05-01",
        "violence_type": "sexual_assault",
        "status": "documented",
        "source_url": "https://www.sapr.mil/reports",
        "source_name": "DoD Annual Report on Sexual Assault in the Military 2023",
        "verified": True,
        "is_public_figure": False,
    },
    {
        "summary": (
            "Vanessa Guillen — Murdered at Fort Hood After Reporting Sexual "
            "Harassment, April 22, 2020. Specialist Vanessa Guillen, 20, was "
            "bludgeoned to death at Fort Hood, Texas by fellow soldier Aaron "
            "Robinson, who then dismembered her body and disposed of it near a "
            "river. She had told her family she was being sexually harassed by "
            "a superior but feared retaliation if she reported it. She went "
            "missing in April 2020. Her remains were found in June. Robinson "
            "died by suicide when confronted by police. Her murder exposed "
            "Fort Hood as one of the most dangerous installations in the US "
            "military for sexual assault and murder — an independent review "
            "found Fort Hood leadership had failed to address a toxic culture "
            "of sexual harassment and assault. Congress passed the 'I Am Vanessa "
            "Guillen Act' in 2021, allowing soldiers to report sexual harassment "
            "to an independent body rather than their chain of command. Her "
            "family became prominent advocates for military sexual assault reform."
        ),
        "city": "Killeen", "state": "TX",
        "lat": 31.1171, "lng": -97.7278,
        "date_incident": "2020-04-22",
        "violence_type": "homicide",
        "status": "documented",
        "source_url": "https://www.congress.gov/bill/116th-congress/house-bill/8270",
        "source_name": "I Am Vanessa Guillen Act / Fort Hood Independent Review Report",
        "verified": True,
        "is_public_figure": False,
    },
    {
        "summary": (
            "Fort Hood — Systemic Failure Documented. An independent review of "
            "Fort Hood ordered after Vanessa Guillen's murder found the installation "
            "had the highest rates of sexual assault, sexual harassment, and murder "
            "in the US Army. The review found that Fort Hood leadership had "
            "consistently underreported sexual assault, failed to investigate "
            "complaints, and created a command climate in which victims feared "
            "coming forward. Between 2016 and 2020, 28 soldiers died at Fort Hood "
            "in circumstances that raised concerns. The installation was renamed "
            "Fort Cavazos in 2023 as part of a broader renaming of bases honoring "
            "Confederate officers — but advocates noted the name change did not "
            "address the underlying culture. Multiple commanders were relieved of "
            "duty following the review. The Fort Hood findings were held up in "
            "Congress as evidence that the military justice system — placing "
            "prosecution decisions with commanding officers — was structurally "
            "incapable of addressing sexual violence."
        ),
        "city": "Killeen", "state": "TX",
        "lat": 31.1171, "lng": -97.7278,
        "date_incident": "2020-12-08",
        "violence_type": "sexual_assault",
        "status": "documented",
        "source_url": "https://www.armed-services.senate.gov/imo/media/doc/FHISC_Report_20201203.pdf",
        "source_name": "Fort Hood Independent Review Committee Report 2020",
        "verified": True,
        "is_public_figure": False,
    },
    {
        "summary": (
            "VA Failure to Treat Military Sexual Trauma Survivors. The Department "
            "of Veterans Affairs is required by law to provide free mental health "
            "treatment to veterans who experienced Military Sexual Trauma — "
            "regardless of discharge status or service length. Despite this, "
            "a 2021 GAO report found the VA was failing to screen, identify, "
            "and connect MST survivors to care. Many survivors — particularly "
            "women veterans who were discharged for unrelated misconduct after "
            "reporting assault — are unaware of their MST care entitlement. "
            "Veterans with 'other than honorable' discharges — sometimes given "
            "to survivors whose behavior changed after trauma — are often denied "
            "VA benefits entirely. Women veterans with MST histories have "
            "dramatically higher rates of PTSD, depression, homelessness, and "
            "suicide than male veterans. The VA's suicide prevention programs "
            "have historically focused on male veterans — leaving women survivors "
            "underserved in crisis intervention as well as treatment."
        ),
        "city": "Washington", "state": "DC",
        "lat": 38.9072, "lng": -77.0369,
        "date_incident": "2021-06-01",
        "violence_type": "sexual_assault",
        "status": "documented",
        "source_url": "https://www.gao.gov/products/gao-21-569",
        "source_name": "GAO-21-569 — VA Military Sexual Trauma Services",
        "verified": True,
        "is_public_figure": False,
    },
    {
        "summary": (
            "Military Sexual Assault at the Academies — West Point, Annapolis, "
            "Air Force Academy. The US service academies have documented persistent "
            "sexual assault problems. The DoD 2023 survey of academy students found "
            "that 15.7% of female cadets and midshipmen at the service academies "
            "experienced sexual assault in the prior year — significantly higher "
            "than rates at civilian universities. The Air Force Academy scandal "
            "of 2003 — in which over 50 female cadets reported being raped by "
            "fellow cadets and found their complaints dismissed or punished — "
            "led to congressional hearings and the first major military sexual "
            "assault reform push. Two decades later, academy assault rates "
            "remain high. Female cadets report being told by peers and superiors "
            "that reporting will end their careers. The pipeline of future officers "
            "is being trained in institutions where sexual violence is endemic "
            "and underreported."
        ),
        "city": "Colorado Springs", "state": "CO",
        "lat": 38.9983, "lng": -104.8613,
        "date_incident": "2023-01-01",
        "violence_type": "sexual_assault",
        "status": "documented",
        "source_url": "https://www.sapr.mil/reports",
        "source_name": "DoD Service Academy Report on Sexual Assault 2023",
        "verified": True,
        "is_public_figure": False,
    },
    {
        "summary": (
            "Retaliation Against Military Sexual Assault Reporters — Documented "
            "Pattern. Multiple congressional investigations and DoD surveys have "
            "documented that retaliation against military members who report sexual "
            "assault is common, severe, and career-ending. Forms of retaliation "
            "include: being labeled a troublemaker, receiving poor performance "
            "evaluations, being passed over for promotion, being reassigned away "
            "from their unit while the perpetrator remains, being subjected to "
            "investigations of their own conduct, and in some cases being "
            "court-martialed. The film 'The Invisible War' (2012) documented "
            "retaliation against survivors and prompted congressional hearings "
            "that led to partial reforms. A 2021 RAND survey found 62% of women "
            "who reported assault experienced retaliation. The Military Justice "
            "Improvement and Increasing Prevention Act (2022) removed prosecution "
            "decisions from commanders for serious offenses — a reform survivors "
            "had advocated for decades. Implementation is ongoing."
        ),
        "city": "Washington", "state": "DC",
        "lat": 38.9072, "lng": -77.0369,
        "date_incident": "2022-12-23",
        "violence_type": "coercive_control",
        "status": "documented",
        "source_url": "https://www.congress.gov/bill/117th-congress/senate-bill/1520",
        "source_name": "MJIA 2022 / RAND MST Survey 2021 / The Invisible War Documentary",
        "verified": True,
        "is_public_figure": False,
    },
]


def main():
    print("[Seed MST] Seeding Military Sexual Trauma records...")
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
    print(f"[Seed MST] {saved}/{len(RECORDS)} records saved.")
    print(f"Total in database: {get_case_count()}")


if __name__ == "__main__":
    main()
