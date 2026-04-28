
"""
sources/ag_press.py — State Attorney General press releases

Live AG RSS feeds covering convictions and arrests for:
domestic violence, sexual assault, trafficking, child abuse.
"""

import re
from medusa.fetch import safe_rss
from medusa.record import normalize_violence_type

AG_FEEDS = [
    ("Florida AG",    "https://myfloridalegal.com/rss.xml",   "FL"),
    ("Arizona AG",    "https://www.azag.gov/rss.xml",         "AZ"),
    ("Georgia AG",    "https://law.georgia.gov/rss.xml",      "GA"),
    ("California AG", "https://oag.ca.gov/rss.xml",           "CA"),
    ("Washington AG", "https://www.atg.wa.gov/rss.xml",       "WA"),
]

INCLUDE_KEYWORDS = [
    "domestic violence", "sexual assault", "rape", "stalking",
    "trafficking", "child abuse", "child sexual abuse",
    "femicide", "murder", "homicide", "intimate partner",
    "sex offense", "molestation", "exploitation",
    "missing", "convicted", "sentenced", "arrested", "indicted",
    "victim", "assault", "strangulation",
]

EXCLUDE_KEYWORDS = [
    "drug", "fraud", "tax", "price gouging", "scam",
    "antitrust", "environment", "consumer", "immigration",
    "firearm", "gun", "robbery", "burglary",
]

def fetch() -> list[dict]:
    records = []
    for name, url, state in AG_FEEDS:
        entries = safe_rss(url)
        for entry in entries:
            title   = getattr(entry, "title", "") or ""
            summary = getattr(entry, "summary", "") or ""
            link    = getattr(entry, "link", "") or ""
            text    = f"{title} {summary}".lower()

            if any(ex in text for ex in EXCLUDE_KEYWORDS):
                continue
            if not any(inc in text for inc in INCLUDE_KEYWORDS):
                continue

            vtype = "domestic_violence"
            if any(x in text for x in ["trafficking", "exploitation"]):
                vtype = "trafficking"
            elif any(x in text for x in ["child abuse", "child sexual", "molestation"]):
                vtype = "child_abuse"
            elif any(x in text for x in ["rape", "sexual assault", "sex offense"]):
                vtype = "sexual_assault"
            elif any(x in text for x in ["murder", "homicide", "femicide", "killed"]):
                vtype = "homicide"
            elif "stalking" in text:
                vtype = "stalking"

            records.append({
                "summary":       f"{title}. {summary[:300]}".strip(),
                "city":          "Unknown",
                "state":         state,
                "date_incident": "",
                "violence_type": vtype,
                "status":        "convicted" if any(x in text for x in ["convicted", "sentenced", "pleaded guilty"]) else "charged",
                "source_url":    link,
                "source_name":   name,
                "verified":      True,
            })

    print(f"[AG Press] {len(records)} records fetched.")
    return records
