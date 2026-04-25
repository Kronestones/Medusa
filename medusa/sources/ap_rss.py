"""
sources/ap_rss.py — AP News RSS feeds (no API key required)

AP News publishes topic RSS feeds publicly.
We pull the crime/justice/courts feed and filter for violence against women.

Feed URL: https://feeds.apnews.com/rss/apf-topnews
Topic feeds: https://apnews.com/hub/crime  (RSS available)

feedparser handles encoding, date parsing, and malformed XML gracefully.
"""

import re
from medusa.fetch import safe_rss
from medusa.record import normalize_violence_type, normalize_status

# AP RSS feeds — public, no key
AP_FEEDS = [
    "https://feeds.apnews.com/rss/apf-topnews",
    "https://feeds.apnews.com/rss/apf-usnews",
    # Topic-specific (may vary by availability)
    "https://apnews.com/rss/tag/crime",
    "https://apnews.com/rss/tag/courts",
    "https://apnews.com/rss/tag/domestic-violence",
    "https://apnews.com/rss/tag/sexual-assault",
]

# Keywords that indicate violence against women coverage
INCLUDE_KEYWORDS = [
    "domestic violence", "sexual assault", "rape", "stalking",
    "femicide", "intimate partner", "trafficking", "harassment",
    "restraining order", "murdered wife", "killed girlfriend",
    "assault women", "violence against women", "sex abuse",
    "attempted murder", "strangled", "stabbed wife", "beaten",
    "child abuse", "molestation",
]

# Keywords that disqualify (not US, not relevant)
EXCLUDE_KEYWORDS = [
    "ukraine", "israel", "gaza", "russia", "china", "iran",
    "afghanistan", "syria", "iraq", "pakistan",
]

# US state names and abbreviations for location extraction
_STATE_PATTERN = re.compile(
    r"\b(Alabama|Alaska|Arizona|Arkansas|California|Colorado|Connecticut|"
    r"Delaware|Florida|Georgia|Hawaii|Idaho|Illinois|Indiana|Iowa|Kansas|"
    r"Kentucky|Louisiana|Maine|Maryland|Massachusetts|Michigan|Minnesota|"
    r"Mississippi|Missouri|Montana|Nebraska|Nevada|New Hampshire|New Jersey|"
    r"New Mexico|New York|North Carolina|North Dakota|Ohio|Oklahoma|Oregon|"
    r"Pennsylvania|Rhode Island|South Carolina|South Dakota|Tennessee|Texas|"
    r"Utah|Vermont|Virginia|Washington|West Virginia|Wisconsin|Wyoming|"
    r"D\.C\.|District of Columbia)\b",
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
    "d.c.":"DC","district of columbia":"DC",
}

# Pattern: "City, State" or "City, ST"
_CITY_STATE_PATTERN = re.compile(
    r"([A-Z][a-zA-Z\s]{2,25}),\s*([A-Z]{2}|" +
    r"Alabama|Alaska|Arizona|Arkansas|California|Colorado|Connecticut|"
    r"Delaware|Florida|Georgia|Hawaii|Idaho|Illinois|Indiana|Iowa|Kansas|"
    r"Kentucky|Louisiana|Maine|Maryland|Massachusetts|Michigan|Minnesota|"
    r"Mississippi|Missouri|Montana|Nebraska|Nevada|New Hampshire|New Jersey|"
    r"New Mexico|New York|North Carolina|North Dakota|Ohio|Oklahoma|Oregon|"
    r"Pennsylvania|Rhode Island|South Carolina|South Dakota|Tennessee|Texas|"
    r"Utah|Vermont|Virginia|Washington|West Virginia|Wisconsin|Wyoming)"
    r"[\s,\.]"
)


def fetch() -> list[dict]:
    """Pull AP News RSS feeds, filter for violence against women, return records."""
    records = []
    seen_urls = set()

    for feed_url in AP_FEEDS:
        entries = safe_rss(feed_url)
        for entry in entries:
            url = entry.get("link") or ""
            if url in seen_urls:
                continue

            rec = _parse_entry(entry)
            if rec:
                seen_urls.add(url)
                records.append(rec)

    print(f"[AP RSS] {len(records)} records fetched.")
    return records


def _parse_entry(entry) -> dict | None:
    title   = entry.get("title") or ""
    summary = entry.get("summary") or entry.get("description") or ""
    text    = f"{title} {summary}".lower()

    # Must match at least one include keyword
    if not any(kw in text for kw in INCLUDE_KEYWORDS):
        return None

    # Must not be foreign news
    if any(kw in text for kw in EXCLUDE_KEYWORDS):
        return None

    # Infer violence type
    vtype = _infer_type(text)

    # Extract location
    full_text = f"{title} {summary}"
    city, state = _extract_location(full_text)
    if not state:
        return None    # Can't place it in the US — skip

    # Date
    published = entry.get("published") or entry.get("updated") or ""
    date_str  = _parse_date(published)

    # Status
    status = _infer_status(text)

    # Summary — use title + first sentence of AP summary, cleaned
    clean_summary = _clean_summary(title, summary)

    return {
        "summary":       clean_summary,
        "city":          city or state,   # city may be empty; state city used as fallback
        "state":         state,
        "date_incident": date_str,
        "violence_type": vtype,
        "status":        status,
        "source_url":    entry.get("link") or "",
        "source_name":   "AP News",
        "verified":      True,
    }


def _infer_type(text: str) -> str:
    if any(x in text for x in ["murder", "homicide", "killed", "femicide", "manslaughter"]):
        return "homicide"
    if any(x in text for x in ["rape", "raped"]):
        return "rape"
    if any(x in text for x in ["sexual assault", "sex assault", "sexually assault"]):
        return "sexual_assault"
    if "trafficking" in text:
        return "trafficking"
    if "stalking" in text or "stalked" in text:
        return "stalking"
    if any(x in text for x in ["domestic violence", "intimate partner"]):
        return "domestic_violence"
    if any(x in text for x in ["attempted murder", "tried to kill", "attempted to kill"]):
        return "attempted_murder"
    if any(x in text for x in ["child abuse", "molestation", "molested"]):
        return "child_abuse"
    if "harassment" in text or "harassed" in text:
        return "harassment"
    return "assault"


def _extract_location(text: str) -> tuple[str, str]:
    """Extract (city, state) from AP article text. Returns ("","") if not found."""
    # Try "City, State" pattern first
    match = _CITY_STATE_PATTERN.search(text)
    if match:
        raw_city  = match.group(1).strip().title()
        raw_state = match.group(2).strip()
        # Normalize state
        if len(raw_state) == 2:
            state = raw_state.upper()
        else:
            state = _STATE_ABBR.get(raw_state.lower(), "")
        if state and raw_city:
            return raw_city, state

    # Fall back to just state name
    match = _STATE_PATTERN.search(text)
    if match:
        state = _STATE_ABBR.get(match.group(0).lower(), "")
        return "", state

    return "", ""


def _parse_date(raw: str) -> str:
    if not raw:
        return ""
    # RSS dates: "Mon, 21 Apr 2026 14:00:00 +0000" or ISO
    import email.utils
    try:
        import time as _time
        t = email.utils.parsedate(raw)
        if t:
            from datetime import date
            return date(*t[:3]).isoformat()
    except Exception:
        pass
    # Try ISO
    m = re.match(r"(\d{4}-\d{2}-\d{2})", raw)
    if m:
        return m.group(1)
    return ""


def _infer_status(text: str) -> str:
    if any(x in text for x in ["convicted", "guilty plea", "pleaded guilty",
                                 "sentenced", "found guilty"]):
        return "convicted"
    if any(x in text for x in ["charged", "arrested", "indicted", "faces charges"]):
        return "charged"
    if any(x in text for x in ["acquitted", "not guilty", "charges dropped"]):
        return "acquitted"
    return "reported"


def _clean_summary(title: str, body: str) -> str:
    # Strip HTML tags
    clean_body = re.sub(r"<[^>]+>", "", body).strip()
    # First sentence of body
    sentences = re.split(r"(?<=[.!?])\s+", clean_body)
    first_sentence = sentences[0] if sentences else ""
    if first_sentence and first_sentence != title:
        return f"{title} {first_sentence}"[:600]
    return title[:600]
