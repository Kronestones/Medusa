"""
seed_history2.py — Additional documented history of legal oppression of women in the US.
"""
import os
import sys
sys.path.insert(0, os.path.expanduser("~/medusa"))

from medusa.database import init_db, save_case
from medusa.record import normalize_record, make_case_id

CASES = [
    {
        "summary": "Women Excluded from Jury Service — Not Fully Remedied Until 1973. Women were systematically excluded from jury duty across the United States for most of American history. The Supreme Court upheld all-male juries in Hoyt v. Florida (1961), ruling that women were the 'center of home and family life' and could be automatically exempted. It was not until Taylor v. Louisiana (1975) that the Supreme Court ruled automatic exemptions for women unconstitutional. Several states excluded women from juries entirely until forced by federal law. This meant that for generations, women who were victims of rape, domestic violence, and murder were judged entirely by panels of men.",
        "city": "Washington", "state": "DC",
        "date_incident": "1975-01-21",
        "violence_type": "coercive_control",
        "status": "reported",
        "source_url": "https://supreme.justia.com/cases/federal/us/419/522/",
        "source_name": "US Supreme Court — Taylor v. Louisiana 1975 / Hoyt v. Florida 1961",
        "verified": True,
    },
    {
        "summary": "Homestead Act (1862) — Women Largely Excluded from Land Ownership. The Homestead Act of 1862 granted 160 acres of public land to citizens who settled and improved it. However, only widows and women who were heads of household could claim land — married women were excluded entirely because their legal identity was subsumed by their husbands under coverture law. A married woman's property, wages, and legal existence belonged to her husband. The coverture system meant women could not own property, sign contracts, or sue in court independently until state-by-state reforms in the late 19th and early 20th centuries.",
        "city": "Washington", "state": "DC",
        "date_incident": "1862-05-20",
        "violence_type": "coercive_control",
        "status": "reported",
        "source_url": "https://www.archives.gov/education/lessons/homestead-act",
        "source_name": "National Archives — Homestead Act 1862 / Coverture Law History",
        "verified": True,
    },
    {
        "summary": "Birth Control Pill Trials on Puerto Rican Women — 1955-1956. The first large-scale human trials of the birth control pill were conducted on poor Puerto Rican women in 1955-1956 by researchers Gregory Pincus and John Rock. Women were not fully informed they were participating in experimental drug trials or told about potential side effects. Three women died during the trials — their deaths were not investigated. Puerto Rico was chosen because researchers believed they would face less opposition there than on the US mainland. The trials paved the way for FDA approval in 1960 but the ethical violations were never formally addressed.",
        "city": "San Juan", "state": "DC",
        "date_incident": "1956-01-01",
        "violence_type": "coercive_control",
        "status": "reported",
        "source_url": "https://www.pbs.org/wgbh/americanexperience/features/pill-significant-events-development-birth-control-pill/",
        "source_name": "PBS American Experience — Birth Control Pill Puerto Rico Trials 1955-56",
        "verified": True,
    },
    {
        "summary": "Night Work Bans — Women Legally Barred from Working Nights. Many US states maintained laws prohibiting women from working night shifts well into the 1960s, ostensibly for their 'protection.' These laws effectively barred women from higher-paying manufacturing, transportation, and service jobs that required night work. The laws were used to justify paying women less and denying them promotions. Federal courts began striking down these laws after Title VII of the Civil Rights Act (1964) prohibited sex discrimination in employment. The last state night work restrictions for women were not eliminated until the early 1970s.",
        "city": "Washington", "state": "DC",
        "date_incident": "1964-07-02",
        "violence_type": "coercive_control",
        "status": "reported",
        "source_url": "https://www.eeoc.gov/statutes/title-vii-civil-rights-act-1964",
        "source_name": "EEOC — Title VII Civil Rights Act 1964 / Night Work Restrictions History",
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
    print(f"\nHistory seed 2 complete. {saved} saved, {skipped} skipped.")

if __name__ == "__main__":
    seed()
