"""
sources/doj.py - DOJ Press Releases + US Attorney Office announcements
"""
import re
from medusa.fetch import safe_rss
from medusa.record import district_to_city, STATE_LARGEST_CITY

DOJ_FEEDS = [  # USAO removed — was hanging scans
    "https://www.justice.gov/rss/news.xml",
    "https://www.justice.gov/ovw/rss/news.xml",
    "https://www.justice.gov/crt/rss/news.xml",
    "https://www.fbi.gov/feeds/fbi-in-the-news/rss.xml",
]

INCLUDE_KEYWORDS = [
    "domestic violence", "sexual assault", "rape", "stalking",
    "sex trafficking", "human trafficking", "intimate partner",
    "femicide", "child sexual", "child abuse", "molestation",
    "sexual exploitation", "sex abuse", "sexual contact",
    "enticement", "strangulation", "attempted murder",
    "sentenced", "convicted", "pleaded guilty", "indicted",
    "charged", "arrested", "guilty plea", "found guilty",
]

EXCLUDE_KEYWORDS = [
    "drug trafficking", "drug conspiracy", "narcotics", "fentanyl",
    "fraud", "embezzlement", "tax", "money laundering", "bribery",
    "firearms dealer", "export control", "sanction", "antitrust",
    "environmental", "immigration fraud", "visa fraud",
]

_DOJ_CITY_PATTERN = re.compile(
    r"^([A-Z][a-zA-Z\s\.]{2,30}),\s*([A-Z]{2})\s*[\u2013\u2014-]"
)
_IN_CITY_PATTERN = re.compile(
    r"\bin\s+([A-Z][a-zA-Z\s]{2,25}),\s*([A-Z]{2})\b"
)
_DISTRICT_PATTERN = re.compile(
    r"(Northern|Southern|Eastern|Western|Central|Middle)\s+District\s+of\s+([A-Za-z\s]+?)(?:\s+to|\s+for|\s+was|\s+has|\s*[,\.])",
    re.IGNORECASE,
)

_STATE_ABBR = {
    "alabama":"AL","alaska":"AK","arizona":"AZ","arkansas":"AR",
    "california":"CA","colorado":"CO","connecticut":"CT","delaware":"DE",
    "florida":"FL","georgia":"GA","hawaii":"HI","idaho":"ID","illinois":"IL",
    "indiana":"IN","iowa":"IA","kansas":"KS","kentucky":"KY","louisiana":"LA",
    "maine":"ME","maryland":"MD","massachusetts":"MA","michigan":"MI",
    "minnesota":"MN","mississippi":"MS","missouri":"MO","montana":"MT",
    "nebraska":"NE","nevada":"NV","new hampshire":"NH","new jersey":"NJ",
    "new mexico":"NM","new york":"NY","north carolina":"NC","north dakota":"ND",
    "ohio":"OH","oklahoma":"OK","oregon":"OR","pennsylvania":"PA",
    "rhode island":"RI","south carolina":"SC","south dakota":"SD",
    "tennessee":"TN","texas":"TX","utah":"UT","vermont":"VT","virginia":"VA",
    "washington":"WA","west virginia":"WV","wisconsin":"WI","wyoming":"WY",
    "district of columbia":"DC",
}

_STATE_SET = None
def _get_state_set():
    global _STATE_SET
    if _STATE_SET is None:
        _STATE_SET = set(_STATE_ABBR.values()) | {"DC"}
    return _STATE_SET


def fetch() -> list:
    records = []
    seen_urls = set()
    for feed_url in DOJ_FEEDS:
        entries = safe_rss(feed_url)
        for entry in entries:
            url = entry.get("link") or ""
            if url in seen_urls:
                continue
            rec = _parse_entry(entry)
            if rec:
                seen_urls.add(url)
                records.append(rec)
    print(f"[DOJ] {len(records)} records fetched.")
    return records


def _parse_entry(entry) -> dict | None:
    title   = entry.get("title") or ""
    summary = entry.get("summary") or entry.get("description") or ""
    text    = f"{title} {summary}".lower()
    if not any(kw in text for kw in INCLUDE_KEYWORDS):
        return None
    if _is_excluded(text):
        return None
    city, state = _extract_doj_location(title, summary)
    if not state:
        return None
    return {
        "summary":       _clean_summary(title, summary),
        "city":          city,
        "state":         state,
        "date_incident": _parse_date(entry.get("published") or entry.get("updated") or ""),
        "violence_type": _infer_type(text),
        "status":        _infer_status(text),
        "source_url":    entry.get("link") or "",
        "source_name":   _source_name(entry.get("link") or ""),
        "verified":      True,
    }


def _is_excluded(text: str) -> bool:
    if any(kw in text for kw in EXCLUDE_KEYWORDS):
        violence_present = any(kw in text for kw in [
            "domestic violence", "sexual assault", "rape", "stalking",
            "sex trafficking", "intimate partner", "child sexual",
        ])
        if not violence_present:
            return True
    return False


def _extract_doj_location(title: str, body: str) -> tuple:
    body_clean = re.sub(r"<[^>]+>", " ", body).strip()
    m = _DOJ_CITY_PATTERN.match(body_clean)
    if m:
        city = m.group(1).strip().title()
        state = m.group(2).upper()
        if state in _get_state_set():
            if city.upper() != "WASHINGTON" or state == "DC":
                return city, state
    m = _IN_CITY_PATTERN.search(title + " " + body_clean[:500])
    if m:
        city = m.group(1).strip().title()
        state = m.group(2).upper()
        if state in _get_state_set():
            return city, state
    m = _DISTRICT_PATTERN.search(title + " " + body_clean[:500])
    if m:
        direction = m.group(1).lower()
        state_name = m.group(2).strip().lower()
        loc = district_to_city(f"{direction} district of {state_name}")
        if loc:
            return loc
    m = re.search(r'\b([A-Z][a-zA-Z\s]{2,20}),\s+([A-Z]{2})\b', title)
    if m:
        city = m.group(1).strip().title()
        state = m.group(2).upper()
        if state in _get_state_set():
            return city, state
    state_pat = re.compile(
        r'\b(Alabama|Alaska|Arizona|Arkansas|California|Colorado|Connecticut|'
        r'Delaware|Florida|Georgia|Hawaii|Idaho|Illinois|Indiana|Iowa|Kansas|'
        r'Kentucky|Louisiana|Maine|Maryland|Massachusetts|Michigan|Minnesota|'
        r'Mississippi|Missouri|Montana|Nebraska|Nevada|New Hampshire|New Jersey|'
        r'New Mexico|New York|North Carolina|North Dakota|Ohio|Oklahoma|Oregon|'
        r'Pennsylvania|Rhode Island|South Carolina|South Dakota|Tennessee|Texas|'
        r'Utah|Vermont|Virginia|Washington|West Virginia|Wisconsin|Wyoming)\b',
        re.IGNORECASE,
    )
    m = state_pat.search(title)
    if m:
        abbr = _STATE_ABBR.get(m.group(0).lower(), "")
        if abbr:
            return STATE_LARGEST_CITY.get(abbr, ""), abbr
    return "", ""


def _infer_type(text: str) -> str:
    if any(x in text for x in ["murder", "homicide", "killed", "killing", "femicide", "manslaughter"]):
        return "homicide"
    if any(x in text for x in ["attempted murder", "attempted homicide"]):
        return "attempted_murder"
    if any(x in text for x in ["rape", "raped", "aggravated sexual abuse"]):
        return "rape"
    if any(x in text for x in ["sexual assault", "sex assault", "sexually assaulted", "sexual abuse", "sexual contact"]):
        return "sexual_assault"
    if any(x in text for x in ["sex trafficking", "human trafficking", "forced prostitution", "enticement"]):
        return "trafficking"
    if any(x in text for x in ["stalking", "cyberstalking"]):
        return "stalking"
    if any(x in text for x in ["domestic violence", "intimate partner", "assault resulting", "strangulation"]):
        return "domestic_violence"
    if any(x in text for x in ["child sexual", "child abuse", "molestation", "child pornography"]):
        return "child_abuse"
    if "harassment" in text:
        return "harassment"
    return "assault"


def _infer_status(text: str) -> str:
    if any(x in text for x in ["sentenced", "years in prison", "months in prison", "life in prison"]):
        return "convicted"
    if any(x in text for x in ["convicted", "found guilty", "guilty verdict", "pleaded guilty", "guilty plea"]):
        return "convicted"
    if any(x in text for x in ["indicted", "charged", "faces charges", "arrested"]):
        return "charged"
    return "charged"


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
    m = re.match(r"(\d{4}-\d{2}-\d{2})", raw)
    return m.group(1) if m else ""


def _clean_summary(title: str, body: str) -> str:
    clean = re.sub(r"<[^>]+>", " ", body).strip()
    sentences = re.split(r"(?<=[.!?])\s+", clean)
    excerpt = " ".join(sentences[:2]) if len(sentences) >= 2 else clean
    if excerpt and excerpt.lower()[:30] != title.lower()[:30]:
        return f"{title} {excerpt}"[:600]
    return title[:600]


def _source_name(url: str) -> str:
    if "justice.gov/ovw" in url:  return "DOJ Office on Violence Against Women"
    if "justice.gov/crt" in url:  return "DOJ Civil Rights Division"
    if "justice.gov/usao" in url: return "US Attorney's Office"
    if "justice.gov" in url:      return "DOJ Press Release"
    if "fbi.gov" in url:          return "FBI"
    return "DOJ"
