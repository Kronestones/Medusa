"""
seed_public_figures.py — Documented public figure cases

Court-documented, convicted, or credibly alleged in legal proceedings.
All cases sourced from public court records, DOJ announcements, or
major investigative journalism with named plaintiffs.

Run from ~/medusa:
    python3 seed_public_figures.py
"""

import sys, os
sys.path.insert(0, "/data/data/com.termux/files/home/medusa")
os.environ.setdefault("DATABASE_URL", input("Paste Medusa DATABASE_URL: ").strip())

from medusa.database import init_db, save_case, get_case_count

init_db()

CASES = [
    {
        "case_id":       "MEDUSA-WEINSTEIN-CONVICTION-2020",
        "violence_type": "rape",
        "summary":       "Harvey Weinstein convicted February 24, 2020 in New York on rape in the third degree and criminal sexual act in the first degree. Sentenced to 23 years. Over 80 women came forward with allegations. The case sparked the global #MeToo movement. A second conviction in Los Angeles added 16 years. New York conviction was overturned on appeal in 2024 — a new trial ordered. Los Angeles conviction stands.",
        "city":          "New York",
        "state":         "NY",
        "date_incident": "2006-01-01",
        "status":        "convicted",
        "source_url":    "https://www.justice.gov/usao-sdny",
        "source_name":   "People v. Weinstein NY 2020; LA County DA conviction 2023",
        "is_public_figure": True,
        "verified":      True,
    },
    {
        "case_id":       "MEDUSA-RKELLY-CONVICTION-2021",
        "violence_type": "trafficking",
        "summary":       "R. Kelly convicted September 27, 2021 in federal court on all counts including racketeering, sex trafficking, and bribery. Sentenced to 30 years. Kelly ran a decades-long criminal enterprise that recruited, groomed, and sexually abused women and underage girls. Additional convictions in Chicago added 20 years. Survivors documented abuse spanning from the 1990s through 2010s.",
        "city":          "New York",
        "state":         "NY",
        "date_incident": "1994-01-01",
        "status":        "convicted",
        "source_url":    "https://www.justice.gov/usao-edny/pr/r-kelly-sentenced-30-years-prison",
        "source_name":   "DOJ EDNY conviction; Northern District IL conviction 2022",
        "is_public_figure": True,
        "verified":      True,
    },
    {
        "case_id":       "MEDUSA-COSBY-CONVICTION-2018",
        "violence_type": "sexual_assault",
        "summary":       "Bill Cosby convicted April 26, 2018 on three counts of aggravated indecent assault against Andrea Constand. Sentenced to 3-10 years. Over 60 women accused Cosby of drugging and sexually assaulting them over five decades. Conviction overturned June 2021 by Pennsylvania Supreme Court on due process grounds related to a prior immunity agreement — not an acquittal. Cosby was released. Civil suits continue.",
        "city":          "Norristown",
        "state":         "PA",
        "date_incident": "2004-01-01",
        "status":        "reported",
        "source_url":    "https://www.courtlistener.com/docket/4314827/commonwealth-v-cosby/",
        "source_name":   "Commonwealth v. Cosby PA 2018",
        "is_public_figure": True,
        "verified":      True,
    },
    {
        "case_id":       "MEDUSA-NASSAR-CONVICTION-2018",
        "violence_type": "child_abuse",
        "summary":       "Larry Nassar, former USA Gymnastics team doctor, sentenced January 2018 to 40-175 years after pleading guilty to seven counts of criminal sexual conduct. Over 265 women and girls came forward, including Olympic gold medalists Simone Biles, Aly Raisman, and McKayla Maroney. Nassar abused victims under the guise of medical treatment for over two decades while USA Gymnastics and Michigan State University ignored complaints.",
        "city":          "Lansing",
        "state":         "MI",
        "date_incident": "1992-01-01",
        "status":        "convicted",
        "source_url":    "https://www.justice.gov/usao-wdmi/pr/larry-nassar-sentenced-federal-child-pornography-charges",
        "source_name":   "DOJ Western District Michigan 2017",
        "is_public_figure": True,
        "verified":      True,
    },
    {
        "case_id":       "MEDUSA-SANDUSKY-CONVICTION-2012",
        "violence_type": "child_abuse",
        "summary":       "Jerry Sandusky, Penn State defensive football coordinator, convicted June 22, 2012 on 45 counts of child sexual abuse. Sentenced to 30-60 years. Sandusky abused at least 10 boys over 15 years using his charity Second Mile as a hunting ground. Penn State officials including President Graham Spanier and coach Joe Paterno were found to have covered up abuse. FBI investigation found institutional failure at every level.",
        "city":          "Bellefonte",
        "state":         "PA",
        "date_incident": "1994-01-01",
        "status":        "convicted",
        "source_url":    "https://www.justice.gov/",
        "source_name":   "DOJ / Centre County Court conviction 2012",
        "is_public_figure": True,
        "verified":      True,
    },
    {
        "case_id":       "MEDUSA-TATE-TRAFFICKING-2023",
        "violence_type": "trafficking",
        "summary":       "Andrew Tate and his brother Tristan Tate were arrested in Romania in December 2022 and indicted in June 2023 on charges of human trafficking, rape, and forming a criminal gang to sexually exploit women. Romanian prosecutors allege the Tates lured women with false promises of romantic relationships then coerced them into producing pornographic content. Additionally accused of rape. Trial ongoing as of 2024. Tate also ran online 'Hustlers University' promoting misogynistic ideology to millions of young men.",
        "city":          "Bucharest",
        "state":         "NY",
        "date_incident": "2021-01-01",
        "status":        "charged",
        "source_url":    "https://www.bbc.com/news/world-europe-65926816",
        "source_name":   "BBC; Romanian DIICOT prosecution",
        "is_public_figure": True,
        "verified":      True,
    },
    {
        "case_id":       "MEDUSA-UBER-ASSAULTS-2022",
        "violence_type": "sexual_assault",
        "summary":       "Uber's 2022 US Safety Report documented 3,824 sexual assaults reported on the platform in 2019-2020, including 141 reports of rape. CNN investigation found Uber had fought to suppress safety reporting for years. Survivors filed class action lawsuits alleging Uber failed to conduct adequate background checks and ignored known predatory drivers. Uber settled multiple cases. The scale of assault on ride-share platforms has led to federal legislative proposals.",
        "city":          "San Francisco",
        "state":         "CA",
        "date_incident": "2019-01-01",
        "status":        "reported",
        "source_url":    "https://www.uber.com/us/en/safety/transparency-report/",
        "source_name":   "Uber US Safety Report 2022; CNN investigation",
        "is_public_figure": False,
        "verified":      True,
    },
    {
        "case_id":       "MEDUSA-ICE-DETENTION-ABUSE",
        "violence_type": "sexual_assault",
        "summary":       "The DHS Office of Inspector General documented widespread sexual abuse in ICE detention facilities. A 2020 whistleblower complaint alleged a doctor at Irwin County Detention Center performed unnecessary gynecological procedures on detained women without consent, including hysterectomies. Multiple women reported being pregnant after sexual assault in detention. Congress received over 30,000 complaints of abuse from ICE detention between 2010 and 2016. Detained women have no meaningful access to legal recourse.",
        "city":          "Ocilla",
        "state":         "GA",
        "date_incident": "2017-01-01",
        "status":        "reported",
        "source_url":    "https://www.oig.dhs.gov/reports/2021/oig-21-46-apr21",
        "source_name":   "DHS OIG Report; Congressional complaint records",
        "is_public_figure": False,
        "verified":      True,
    },
    {
        "case_id":       "MEDUSA-CATHOLIC-CHURCH-PA-2018",
        "violence_type": "child_abuse",
        "summary":       "Pennsylvania Attorney General Josh Shapiro released a grand jury report in August 2018 documenting over 1,000 child victims abused by 301 predator priests across six dioceses over 70 years. The report found the Catholic Church systematically covered up abuse, moved predatory priests between parishes, and intimidated victims. Similar AG investigations in other states found comparable patterns. The Church paid over $4 billion in settlements nationally.",
        "city":          "Harrisburg",
        "state":         "PA",
        "date_incident": "1940-01-01",
        "status":        "reported",
        "source_url":    "https://www.attorneygeneral.gov/reports/",
        "source_name":   "Pennsylvania AG Grand Jury Report 2018",
        "is_public_figure": True,
        "verified":      True,
    },
    {
        "case_id":       "MEDUSA-TATE-RAPE-CHATROOMS",
        "violence_type": "harassment",
        "summary":       "Online networks promoting rape culture, including channels associated with Andrew Tate's network and anonymous platforms, have been documented sharing rape footage, coordinating harassment of women, and recruiting vulnerable men into misogynistic ideology. Discord and Telegram channels with tens of thousands of members have shared non-consensual intimate images and instructional content on controlling women. Platform moderation has been inconsistent. Several individuals connected to these networks have faced criminal charges.",
        "city":          "Unknown",
        "state":         "US",
        "date_incident": "2020-01-01",
        "status":        "reported",
        "source_url":    "https://www.bbc.com/news/uk-63495573",
        "source_name":   "BBC investigation; platform moderation reports",
        "is_public_figure": False,
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

print(f"\nDone. {saved} public figure cases saved.")
print(f"Total in database: {get_case_count()}")
