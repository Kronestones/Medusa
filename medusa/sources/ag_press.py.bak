"""
sources/ag_press.py — State Attorney General press releases
"""

import re
from medusa.fetch import safe_rss
from medusa.record import STATE_LARGEST_CITY

AG_FEEDS = [
    ("Florida AG",    "https://myfloridalegal.com/rss.xml",    "FL"),
    ("Arizona AG",    "https://www.azag.gov/rss.xml",          "AZ"),
    ("Georgia AG",    "https://law.georgia.gov/rss.xml",       "GA"),
    ("California AG", "https://oag.ca.gov/rss.xml",            "CA"),
    ("Washington AG", "https://www.atg.wa.gov/rss.xml",        "WA"),
    ("Colorado AG",   "https://coag.gov/press-releases/feed/", "CO"),
    ("Texas AG",      "https://www.texasattorneygeneral.gov/news/rss.xml", "TX"),
    ("New York AG",   "https://ag.ny.gov/press-releases/rss.xml",         "NY"),
    ("Michigan AG",   "https://www.michigan.gov/ag/newsroom/rss",         "MI"),
    ("Ohio AG",       "https://www.ohioattorneygeneral.gov/News/rss.aspx","OH"),
]

INCLUDE_KEYWORDS = [
    "domestic violence", "sexual assault", "rape", "stalking",
    "trafficking", "child abuse", "child sexual abuse",
    "femicide", "murder", "homicide", "intimate partner",
    "sex offense", "molestation", "exploitation",
    "convicted", "sentenced", "arrested", "indicted",
    "assault", "strangulation", "attempted murder",
]

EXCLUDE_KEYWORDS = [
    "drug", "fraud", "tax", "price gouging", "scam",
    "antitrust", "environment", "consumer", "immigration",
    "firearm", "gun", "robbery", "burglary",
]

_CITY_STATE_RE = re.compile(r"([A-Z][a-zA-Z\s\-]{2,25}),\s*([A-Z]{2})\b")


def fetch() -> list[dict]:
    records = []
    for name, url, state in AG_FEEDS:
        entries = safe_rss(url)
        count_before = len(records)
        for entry in entries:
            # safe_rss returns dicts — use .get() not getattr
            title   = entry.get("title", "") or ""
            summary = entry.get("summary", "") or entry.get("description", "") or ""
            link    = entry.get("link", "") or ""
            text    = f"{title} {summary}".lower()

            if any(ex in text for ex in EXCLUDE_KEYWORDS):
                continue
            if not any(inc in text for inc in INCLUDE_KEYWORDS):
                continue

            vtype = _infer_type(text)
            status = "convicted" if any(x in text for x in [
                "convicted", "sentenced", "pleaded guilty", "guilty plea"
            ]) else "charged"

            # Try to extract city, fall back to state capital/largest city
            city = _extract_city(f"{title} {summary}", state) or \
                   STATE_LARGEST_CITY.get(state, "")

            date_str = _parse_date(entry.get("published") or entry.get("updated") or "")

            records.append({
                "summary":       f"{title}. {summary[:300]}".strip(),
                "city":          city,
                "state":         state,
                "date_incident": date_str,
                "violence_type": vtype,
                "status":        status,
                "source_url":    link,
                "source_name":   name,
                "verified":      True,
            })

        got = len(records) - count_before
        if got:
            print(f"[AG Press] {name}: {got} records")

    print(f"[AG Press] {len(records)} total records fetched.")
    return records


def _infer_type(text: str) -> str:
    if any(x in text for x in ["murder", "homicide", "femicide", "killed"]):
        return "homicide"
    if any(x in text for x in ["trafficking", "exploitation"]):
        return "trafficking"
    if any(x in text for x in ["child abuse", "child sexual", "molestation"]):
        return "child_abuse"
    if any(x in text for x in ["rape", "sexual assault", "sex offense"]):
        return "sexual_assault"
    if "stalking" in text:
        return "stalking"
    if "attempted murder" in text or "attempted to kill" in text:
        return "attempted_murder"
    return "domestic_violence"


def _extract_city(text: str, state: str) -> str:
    m = _CITY_STATE_RE.search(text)
    if m and m.group(2).upper() == state:
        return m.group(1).strip().title()
    return ""


def _parse_date(raw: str) -> str:
    if not raw:
        return ""
    import email.utils
    try:
        t = email.utils.parsedate(raw)
        if t:
            from datetime import date
            return date(*t[:3]).isoformat()
    except Exception:
        pass
    import re
    m = re.search(r"\d{4}-\d{2}-\d{2}", raw)
    return m.group(0) if m else ""
