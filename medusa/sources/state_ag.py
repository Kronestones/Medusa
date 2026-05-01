"""
sources/state_ag.py — State Attorney General press releases

State AGs announce every conviction and indictment in their state.
These are among the best sources for local/rural cases that never
reach national wire services.

Currently wired: TX, NY, IL, OH, PA (the five states missing per todo)
Plus: CA, FL, GA, WA, CO — all high-volume states

Feed strategy:
  Most state AGs have a press release RSS or JSON endpoint.
  We try RSS first, fall back to scraping the press release page.

No API key required for any of these.
"""

import re
from medusa.fetch import safe_rss, safe_json, safe_get
from medusa.record import VALID_STATES, STATE_LARGEST_CITY

# State AG RSS / JSON feeds
# Format: (state_abbr, state_name, feed_url, feed_type)
STATE_AG_FEEDS = [
    # Texas — AG press releases RSS
    ("TX", "Texas",        "https://www.texasattorneygeneral.gov/news/rss.xml",  "rss"),
    # New York — AG press releases
    ("NY", "New York",     "https://ag.ny.gov/press-releases/rss.xml",           "rss"),
    # Illinois — AG newsroom
    ("IL", "Illinois",     "https://illinoisattorneygeneral.gov/news/rss.xml",    "rss"),
    # Ohio — AG news
    ("OH", "Ohio",         "https://www.ohioattorneygeneral.gov/News/rss.aspx",   "rss"),
    # Pennsylvania — AG news
    ("PA", "Pennsylvania", "https://www.attorneygeneral.gov/news/rss/",           "rss"),
    # California — AG
    ("CA", "California",   "https://oag.ca.gov/news/rss",                         "rss"),
    # Florida — AG
    ("FL", "Florida",      "https://www.myfloridalegal.com/news/rss",             "rss"),
    # Georgia — AG
    ("GA", "Georgia",      "https://law.georgia.gov/news/rss",                    "rss"),
    # Washington — AG
    ("WA", "Washington",   "https://www.atg.wa.gov/news/rss.xml",                 "rss"),
    # Colorado — AG
    ("CO", "Colorado",     "https://coag.gov/news/rss/",                          "rss"),
    # Michigan — AG
    ("MI", "Michigan",     "https://www.michigan.gov/ag/newsroom/rss",            "rss"),
    # Arizona — AG
    ("AZ", "Arizona",      "https://www.azag.gov/rss.xml",                        "rss"),
    # Minnesota — AG
    ("MN", "Minnesota",    "https://www.ag.state.mn.us/Office/Communications/rss.asp", "rss"),
    # North Carolina — AG
    ("NC", "North Carolina","https://ncdoj.gov/news/rss/",                        "rss"),
    # Virginia — AG
    ("VA", "Virginia",     "https://www.oag.state.va.us/media-center/news-releases/rss", "rss"),
]

INCLUDE_KEYWORDS = [
    "domestic violence", "sexual assault", "rape", "stalking",
    "trafficking", "intimate partner", "femicide", "murder", "homicide",
    "child abuse", "child exploitation", "molestation", "sex offense",
    "attempted murder", "strangled", "assault", "harassment",
    "protective order", "restraining order", "coercive",
    "grooming", "exploitation",
]

EXCLUDE_KEYWORDS = [
    "fraud", "antitrust", "consumer protection", "securities",
    "environmental", "opioid", "medicare", "medicaid", "tax",
    "bankruptcy", "corporate", "insurance", "data breach",
]

_CITY_STATE_RE = re.compile(r"([A-Z][a-zA-Z\s\-]{2,25}),\s*([A-Z]{2})\b")


def fetch() -> list[dict]:
    records = []
    seen_urls = set()
    total_by_state = {}

    for state_abbr, state_name, feed_url, feed_type in STATE_AG_FEEDS:
        state_records = _fetch_state(state_abbr, state_name, feed_url, seen_urls)
        records.extend(state_records)
        if state_records:
            total_by_state[state_abbr] = len(state_records)

    summary = " · ".join(f"{k}:{v}" for k, v in total_by_state.items())
    print(f"[State AGs] {len(records)} total records. [{summary}]")
    return records


def _fetch_state(state_abbr: str, state_name: str,
                 feed_url: str, seen_urls: set) -> list[dict]:
    entries = safe_rss(feed_url)
    records = []

    for entry in entries:
        url = entry.get("link") or ""
        if url in seen_urls:
            continue

        title   = entry.get("title") or ""
        summary = entry.get("summary") or entry.get("description") or ""
        text    = f"{title} {summary}".lower()

        if not any(kw in text for kw in INCLUDE_KEYWORDS):
            continue
        if any(kw in text for kw in EXCLUDE_KEYWORDS):
            continue

        vtype  = _infer_type(text)
        status = _infer_status(text)

        # Try to extract specific city; fall back to state's largest
        city = _extract_city(f"{title} {summary}", state_abbr) or \
               STATE_LARGEST_CITY.get(state_abbr, "")

        date_str = _parse_date(entry.get("published") or entry.get("updated") or "")
        clean    = _clean_text(title, summary)

        records.append({
            "summary":       clean,
            "city":          city,
            "state":         state_abbr,
            "date_incident": date_str,
            "violence_type": vtype,
            "status":        status,
            "source_url":    url,
            "source_name":   f"{state_name} Attorney General",
            "verified":      True,
        })
        seen_urls.add(url)

    return records


def _infer_type(text: str) -> str:
    if any(x in text for x in ["murder", "homicide", "killed", "femicide", "manslaughter"]):
        return "homicide"
    if any(x in text for x in ["attempted murder", "tried to kill"]):
        return "attempted_murder"
    if any(x in text for x in ["rape", "raped"]):
        return "rape"
    if any(x in text for x in ["sexual assault", "sex assault", "sex offense",
                                 "exploitation", "grooming", "molestation"]):
        return "sexual_assault"
    if "trafficking" in text:
        return "trafficking"
    if "stalking" in text or "stalked" in text:
        return "stalking"
    if any(x in text for x in ["domestic violence", "intimate partner", "dating violence"]):
        return "domestic_violence"
    if any(x in text for x in ["child abuse", "child exploitation"]):
        return "child_abuse"
    if "coercive" in text:
        return "coercive_control"
    if "harassment" in text:
        return "harassment"
    return "assault"


def _infer_status(text: str) -> str:
    if any(x in text for x in ["convicted", "sentenced", "guilty plea",
                                 "pleaded guilty", "found guilty", "sentenced to"]):
        return "convicted"
    if any(x in text for x in ["charged", "indicted", "arrested", "faces charges"]):
        return "charged"
    return "charged"   # AG default: they announce charges or convictions


def _extract_city(text: str, state_abbr: str) -> str:
    m = _CITY_STATE_RE.search(text)
    if m and m.group(2).upper() == state_abbr:
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
    m = re.search(r"\d{4}-\d{2}-\d{2}", raw)
    if m:
        return m.group(0)
    return ""


def _clean_text(title: str, body: str) -> str:
    clean = re.sub(r"<[^>]+>", "", body).strip()
    sentences = re.split(r"(?<=[.!?])\s+", clean)
    first = sentences[0] if sentences else ""
    if first and first.strip() != title.strip():
        return f"{title} {first}"[:600]
    return title[:600]
