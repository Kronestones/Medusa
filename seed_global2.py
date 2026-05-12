"""
seed_global2.py — Additional international cases for the Global tab.
"""
import os
import sys
sys.path.insert(0, os.path.expanduser("~/medusa"))

from medusa.database import init_db, save_case
from medusa.record import normalize_record, make_case_id

CASES = [
    {
        "summary": "Sarah Everard — Murder by Metropolitan Police Officer, London, England, March 3, 2021. Sarah Everard, 33, was kidnapped, raped, and murdered by Wayne Couzens, a serving Metropolitan Police officer, while walking home in South London. Couzens used his police warrant card to falsely arrest her. He was sentenced to life in prison. Her murder triggered a national reckoning in the UK about violence against women and police culture. A vigil held in her memory was broken up by police, sparking further outrage. The case led to significant reforms in UK policing.",
        "city": "London, England", "state": "DC",
        "date_incident": "2021-03-03",
        "violence_type": "homicide",
        "status": "convicted",
        "source_url": "https://www.bbc.com/news/uk-58746108",
        "source_name": "BBC — Sarah Everard Murder / Metropolitan Police 2021",
        "verified": True,
    },
    {
        "summary": "Democratic Republic of Congo — Rape as a Weapon of War. The eastern DRC has been described by UN officials as the rape capital of the world. An estimated 48 women are raped every hour in the DRC. Armed groups including the M23 and FDLR have systematically used sexual violence as a tactic of war. The International Criminal Court convicted Bosco Ntaganda in 2019 on 18 counts including rape and sexual slavery as war crimes. Jean-Pierre Bemba was also convicted of rape as a war crime. The scale of sexual violence has been documented by Physicians for Human Rights and UN investigators.",
        "city": "Kinshasa, DRC", "state": "DC",
        "date_incident": "2019-07-08",
        "violence_type": "rape",
        "status": "convicted",
        "source_url": "https://www.icc-cpi.int/news/trial-chamber-vi-finds-bosco-ntaganda-guilty",
        "source_name": "International Criminal Court — Ntaganda Conviction / UN DRC Reports",
        "verified": True,
    },
    {
        "summary": "Saudi Arabia Male Guardianship System — Documented State Control of Women. Until 2019 reforms, Saudi women were legally required to obtain permission from a male guardian — father, husband, brother, or son — to travel, marry, access healthcare, or work. Women were banned from driving until 2018. Despite limited reforms, guardianship requirements persist in marriage and some legal contexts. Human Rights Watch documented the system as treating women as permanent legal minors. Saudi women who flee guardianship face imprisonment and forced return.",
        "city": "Riyadh, Saudi Arabia", "state": "DC",
        "date_incident": "2019-01-01",
        "violence_type": "coercive_control",
        "status": "reported",
        "source_url": "https://www.hrw.org/report/2016/07/16/boxed/women-and-saudi-arabias-male-guardianship-system",
        "source_name": "Human Rights Watch — Saudi Arabia Male Guardianship System 2016",
        "verified": True,
    },
    {
        "summary": "India Dowry Deaths — 7,000 Women Killed Annually. India's National Crime Records Bureau documents approximately 7,000 dowry deaths annually — women killed by husbands or in-laws over insufficient dowry payments. The actual number is believed to be far higher due to underreporting and misclassification as accidents or suicides. Dowry harassment and violence affects millions of women. The Dowry Prohibition Act (1961) has been widely ineffective. India also has the world's highest number of acid attacks, predominantly against women who refuse marriage proposals.",
        "city": "New Delhi, India", "state": "DC",
        "date_incident": "2023-01-01",
        "violence_type": "homicide",
        "status": "reported",
        "source_url": "https://ncrb.gov.in/en/crime-in-india-table-addtional-table-2022",
        "source_name": "India National Crime Records Bureau — Dowry Deaths Statistics 2022",
        "verified": True,
    },
    {
        "summary": "Female Genital Mutilation — 200 Million Girls Affected Globally. The World Health Organization documents that over 200 million girls and women alive today have undergone female genital mutilation in 30 countries across Africa, the Middle East, and Asia. FGM has no health benefits and causes severe bleeding, complications in childbirth, infections, and lifelong trauma. At least 3 million girls are at risk annually. FGM is recognized internationally as a human rights violation. In the US, an estimated 513,000 women and girls are at risk or have experienced FGM — prosecutions have been limited.",
        "city": "Geneva, Switzerland", "state": "DC",
        "date_incident": "2023-01-01",
        "violence_type": "assault",
        "status": "reported",
        "source_url": "https://www.who.int/news-room/fact-sheets/detail/female-genital-mutilation",
        "source_name": "WHO — Female Genital Mutilation Global Report 2023",
        "verified": True,
    },
    {
        "summary": "Latin America Femicide Crisis — El Salvador, Honduras, Guatemala. Latin America has the world's highest femicide rates. El Salvador recorded 3.3 femicides per 100,000 women — among the highest globally. Honduras and Guatemala have similarly alarming rates. The Inter-American Commission on Human Rights has documented state failure to investigate and prosecute femicide. Women who report violence face retaliation from gangs and corrupt police. Many femicides are linked to intimate partner violence, gang activity targeting women, and state impunity. The crisis drives significant female migration to the US.",
        "city": "San Salvador, El Salvador", "state": "DC",
        "date_incident": "2023-01-01",
        "violence_type": "homicide",
        "status": "reported",
        "source_url": "https://www.oas.org/en/iachr/reports/pdfs/FeminicidioViolencia-en.pdf",
        "source_name": "Inter-American Commission on Human Rights — Latin America Femicide Report",
        "verified": True,
    },
]

def seed():
    init_db()
    saved = 0
    skipped = 0
    for case in CASES:
        rec = normalize_record(case)
        if rec is None:
            print(f"  SKIP: {case.get('city')}")
            skipped += 1
            continue
        rec["case_id"] = make_case_id(
            rec["city"], rec["state"], rec["violence_type"],
            rec["date_incident"], rec.get("source_url", ""), rec.get("summary", "")
        )
        try:
            save_case(rec)
            saved += 1
            print(f"  saved: {rec['summary'][:80]}")
        except Exception as e:
            if "duplicate" in str(e).lower() or "unique" in str(e).lower():
                skipped += 1
            else:
                print(f"  ERROR: {e}")
    print(f"\nGlobal seed 2 complete. {saved} saved, {skipped} skipped.")

if __name__ == "__main__":
    seed()
