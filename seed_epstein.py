"""
seed_epstein.py — Epstein network documented cases

Court-documented, publicly filed, legally verified records only.
Named associates with credible claims established in court filings,
depositions, settlements, or criminal convictions.

Run from ~/medusa:
    python3 seed_epstein.py
"""

import sys, os
sys.path.insert(0, "/data/data/com.termux/files/home/medusa")
os.environ.setdefault("DATABASE_URL", input("Paste Medusa DATABASE_URL: ").strip())

from medusa.database import init_db, save_case, get_case_count

init_db()

CASES = [
    {
        "case_id":       "MEDUSA-EPSTEIN-MAXWELL-2021",
        "violence_type": "trafficking",
        "summary":       "Ghislaine Maxwell convicted December 29, 2021 on five federal counts including sex trafficking of minors. Maxwell recruited and groomed underage girls for Jeffrey Epstein's sexual abuse network. Victims testified she was present during abuse and participated directly. Sentenced to 20 years federal prison June 2022.",
        "city":          "New York",
        "state":         "NY",
        "date_incident": "1994-01-01",
        "status":        "convicted",
        "source_url":    "https://www.justice.gov/usao-sdny/pr/ghislaine-maxwell-sentenced-20-years-prison-federal-sex-trafficking-crimes",
        "source_name":   "DOJ SDNY",
        "is_public_figure": True,
        "verified":      True,
    },
    {
        "case_id":       "MEDUSA-EPSTEIN-INDICTMENT-2019",
        "violence_type": "trafficking",
        "summary":       "Jeffrey Epstein indicted July 2019 on federal charges of sex trafficking dozens of minors between 2002 and 2005. Epstein ran a network that recruited vulnerable underage girls, paid them for 'massages,' and sexually abused them at his Manhattan mansion and Palm Beach estate. Epstein died in federal custody August 10, 2019. Previous 2008 plea deal allowed him to avoid federal charges — widely condemned as a miscarriage of justice.",
        "city":          "New York",
        "state":         "NY",
        "date_incident": "2002-01-01",
        "status":        "reported",
        "source_url":    "https://www.justice.gov/usao-sdny/pr/jeffrey-epstein-indicted-sex-trafficking-dozens-minors",
        "source_name":   "DOJ SDNY",
        "is_public_figure": True,
        "verified":      True,
    },
    {
        "case_id":       "MEDUSA-EPSTEIN-ANDREW-2022",
        "violence_type": "sexual_assault",
        "summary":       "Prince Andrew settled civil lawsuit brought by Virginia Giuffre in February 2022. Giuffre alleged Andrew sexually abused her when she was 17, after she was trafficked by Jeffrey Epstein and Ghislaine Maxwell. Settlement amount undisclosed. Andrew denied allegations but settled without admission. Previously stripped of royal duties and military titles.",
        "city":          "New York",
        "state":         "NY",
        "date_incident": "2001-01-01",
        "status":        "reported",
        "source_url":    "https://www.bbc.com/news/uk-60338997",
        "source_name":   "BBC / SDNY civil filing",
        "is_public_figure": True,
        "verified":      True,
    },
    {
        "case_id":       "MEDUSA-EPSTEIN-DERSHOWITZ-GIUFFRE",
        "violence_type": "sexual_assault",
        "summary":       "Virginia Giuffre alleged in sworn depositions that Alan Dershowitz sexually abused her when she was a minor, as part of Jeffrey Epstein's trafficking network. Dershowitz denied all allegations. Defamation suit and counter-suit filed. Giuffre later retracted claims against Dershowitz in a 2023 statement, stating she may have made a mistake. Case remains contested and publicly documented.",
        "city":          "Palm Beach",
        "state":         "FL",
        "date_incident": "2000-01-01",
        "status":        "reported",
        "source_url":    "https://www.courtlistener.com/docket/4355049/giuffre-v-dershowitz/",
        "source_name":   "CourtListener — Giuffre v. Dershowitz",
        "is_public_figure": True,
        "verified":      True,
    },
    {
        "case_id":       "MEDUSA-EPSTEIN-UNSEALED-2024",
        "violence_type": "trafficking",
        "summary":       "Court documents unsealed January 2024 in Giuffre v. Maxwell named numerous individuals alleged to have participated in or been aware of Epstein's trafficking network. Names included in sworn depositions and civil filings. Documents released by order of federal judge. Allegations are credible claims in court filings — not criminal convictions unless otherwise noted.",
        "city":          "New York",
        "state":         "NY",
        "date_incident": "2000-01-01",
        "status":        "reported",
        "source_url":    "https://www.courtlistener.com/docket/3384/"  ,
        "source_name":   "SDNY unsealed deposition transcripts 2024",
        "is_public_figure": True,
        "verified":      True,
    },
    {
        "case_id":       "MEDUSA-EPSTEIN-ACOSTA-2008",
        "violence_type": "trafficking",
        "summary":       "Alexander Acosta, as US Attorney for Southern Florida in 2008, negotiated a secret non-prosecution agreement with Jeffrey Epstein that shielded Epstein and unnamed co-conspirators from federal charges. Victims were not notified, in violation of the Crime Victims Rights Act. Federal judge ruled in 2019 the plea deal was illegally negotiated. Acosta resigned as Trump's Labor Secretary amid the scandal.",
        "city":          "Miami",
        "state":         "FL",
        "date_incident": "2008-01-01",
        "status":        "reported",
        "source_url":    "https://www.miamiherald.com/news/local/article220097825.html",
        "source_name":   "Miami Herald — Julie K. Brown investigation",
        "is_public_figure": True,
        "verified":      True,
    },
]

saved = 0
for case in CASES:
    if save_case(case):
        saved += 1
        print(f"  Saved: {case['case_id']}")
    else:
        print(f"  Already exists: {case['case_id']}")

print(f"\nDone. {saved} Epstein network cases saved.")
print(f"Total in database: {get_case_count()}")
