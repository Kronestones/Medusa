"""
seed_stuart_adams_utah.py — Medusa

Utah Senate President J. Stuart Adams — used his position to quietly
rewrite child rape sentencing law (SB213) after his granddaughter was
charged with two counts of child rape and two counts of child sodomy
against a 13-year-old victim. The law change meant she avoided prison
and the sex offender registry entirely. August 2025.

Run:
    cd ~/medusa && python3 seed_stuart_adams_utah.py
"""

import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from medusa.database import init_db, save_case

CASES = [
    {
        "case_id":        "stuart_adams_utah_sb213_child_rape_law_2025",
        "violence_type":  "child_abuse",
        "status":         "congressional_record",
        "summary": (
            "In 2023, an 18-year-old Utah high school student — the granddaughter "
            "of Utah Senate President J. Stuart Adams, the most powerful Republican "
            "in the Utah Legislature — was arrested and charged with two counts of "
            "child rape and two counts of child sodomy after having sex with a "
            "13-year-old victim. She faced four first-degree felonies, a prison "
            "sentence potentially ranging from six years to life, and mandatory "
            "lifetime registration as a sex offender. "
            "The victim's mother had learned of the assault when her daughter "
            "mentioned it in a 'random conversation,' saying she understood what "
            "had happened. Plea negotiations were at an impasse — prosecutors "
            "insisted on sex offender registration, which the defense refused. "
            "Adams then confidentially told fellow Republican Senate Majority "
            "Leader Kirk Cullimore that the law governing high school offenders "
            "should be reviewed. Cullimore sponsored Senate Bill 213, a 49-page "
            "omnibus criminal justice bill. The bill was drafted in part by "
            "Cara Tangaro — the defense attorney representing Adams's granddaughter "
            "in the active rape case. SB213 passed almost entirely on party lines "
            "— all Utah Senate Republicans voted for it — and was signed into law "
            "by Republican Governor Spencer Cox on March 19, 2024. "
            "Under SB213, 18-year-olds enrolled in high school at the time of "
            "a sexual offense are no longer prosecuted as adults — they are "
            "charged as minors. The law was not technically retroactive. However, "
            "according to the judge, prosecutor, and defense attorney in the case, "
            "the granddaughter's situation was 'pivotal' in the decision to amend "
            "the law. Two months after the law passed, prosecutors offered a new "
            "plea deal. At sentencing, defense attorney Tangaro told Judge Rita "
            "Cornish: 'You saw the legislative change. We all agree that's not "
            "retroactive, but the government did change their offer based on that.' "
            "The granddaughter pleaded guilty to reduced charges, served no "
            "additional jail time beyond one week already served, was placed on "
            "four years of probation, ordered to pay a $1,500 fine, complete "
            "120 hours of community service, and complete sex offender treatment — "
            "but was NOT required to register as a sex offender. "
            "Adams denied wrongdoing and refused to resign, saying the process "
            "was 'done ethically and morally perfect.' He said he was 'surprised "
            "by the severity of the charges' against his granddaughter and was "
            "'not aware' the legislative change could factor into the plea deal. "
            "Democrats called for his resignation. The story broke publicly in "
            "August 2025 via the Salt Lake Tribune. "
            "Adams is the same legislator who led Utah's campaign against "
            "transgender athletes in women's sports, arguing that trans athletes "
            "put cisgender girls at risk — while simultaneously working to reduce "
            "consequences for his granddaughter who raped a 13-year-old girl. "
            "The 13-year-old victim and her family have not been publicly identified. "
            "Sources: Salt Lake Tribune; Newsweek; Deseret News; Utah News Dispatch; "
            "New Republic; Snopes."
        ),
        "city":           "Salt Lake City",
        "state":          "UT",
        "lat":            40.7608,
        "lng":            -111.8910,
        "source_url":     "https://www.sltrib.com/news/politics/2025/08/02/utah-senate-pres-stuart-adams/",
        "source_name":    "Salt Lake Tribune",
        "additional_sources": [
            {"url": "https://www.newsweek.com/gop-senator-child-rape-law-utah-j-stuart-adams-2109138",
             "name": "Newsweek"},
            {"url": "https://www.deseret.com/politics/2025/08/13/stuart-adams-wont-resign-over-claims-he-influenced-grandaughters-plea-deal/",
             "name": "Deseret News"},
            {"url": "https://utahnewsdispatch.com/2025/08/21/gov-spencer-cox-new-law-impact-on-senate-president-stuart-adams-relative/",
             "name": "Utah News Dispatch"},
            {"url": "https://newrepublic.com/post/198855/republican-lawmaker-consent-child-rape-law-relative-charges",
             "name": "New Republic"},
        ],
        "verified":       True,
        "is_public_figure": True,
        "date_incident":  "2023-01-01",
    },
]


def main():
    print("\n  [Medusa] Seeding J. Stuart Adams / SB213 case...\n")
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
