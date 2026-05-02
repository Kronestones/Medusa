"""
sources/ap_rss.py — Wire news RSS feeds (no API key required)

feeds.apnews.com    — PERMANENTLY DEAD. Do not restore.
feeds.reuters.com   — DEAD.
rsshub.app          — RESTRICTED. Do not use.

Active feeds as of 2026:
  NYT US News, NYT Crime, NPR News, NPR US, Guardian US, Guardian DV,
  ProPublica, Marshall Project (direct site feed)
"""

import re
from medusa.fetch import safe_rss
from medusa.record import normalize_violence_type, normalize_status

AP_FEEDS = [
    "https://rss.nytimes.com/services/xml/rss/nyt/US.xml",
    "https://rss.nytimes.com/services/xml/rss/nyt/Crime.xml",
    "https://feeds.npr.org/1001/rss.xml",
    "https://feeds.npr.org/1057/rss.xml",
    "https://www.theguardian.com/us-news/rss",
    "https://www.theguardian.com/society/domestic-violence/rss",
    "https://www.propublica.org/feeds/propublica/main",
    "https://feeds.themarshallproject.org/marshall-project-stories",
]

INCLUDE_KEYWORDS = [
    "domestic violence", "sexual assault", "rape", "stalking",
    "femicide", "intimate partner", "trafficking", "harassment",
    "restraining order", "murdered wife", "killed girlfriend",
    "assault women", "violence against women", "sex abuse",
    "attempted murder", "strangled", "stabbed wife", "beaten",
    "child abuse", "molestation", "sexual violence", "sexual abuse",
    "battered", "coercive control", "sex trafficking",
]

EXCLUDE_KEYWORDS = [
    "ukraine", "israel", "gaza", "russia", "china", "iran",
    "afghanistan", "syria", "iraq", "pakistan",
]

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
    records   = []
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

    print(f"[Wire RSS] {len(records)} records fetched.")
    return records


def _parse_entry(entry) -> dict | None:
    title   = entry.get("title")   or ""
    summary = entry.get("summary") or entry.get("description") or ""
    text    = f"{title} {summary}".lower()

    if not any(kw in text for kw in INCLUDE_KEYWORDS):
        return None
    if any(kw in text for kw in EXCLUDE_KEYWORDS):
        return None

    vtype      = _infer_type(text)
    full_text  = f"{title} {summary}"
    city, state = _extract_location(full_text)
    if not state:
        return None

    date_str = _parse_date(entry.get("published") or entry.get("updated") or "")
    status   = _infer_status(text)

    return {
        "summary":       _clean_summary(title, summary),
        "city":          city or state,
        "state":         state,
        "date_incident": date_str,
        "violence_type": vtype,
        "status":        status,
        "source_url":    entry.get("link") or "",
        "source_name":   "Wire RSS",
        "verified":      True,
    }


def _infer_type(text: str) -> str:
    if any(x in text for x in ["murder", "homicide", "killed", "femicide", "manslaughter", "strangled"]):
        return "homicide"
    if any(x in text for x in ["rape", "raped"]):
        return "rape"
    if any(x in text for x in ["sexual assault", "sex assault", "sexually assault", "sexual abuse", "sexual violence"]):
        return "sexual_assault"
    if "sex trafficking" in text or "human trafficking" in text or "trafficking" in text:
        return "trafficking"
    if "stalking" in text or "stalked" in text:
        return "stalking"
    if any(x in text for x in ["domestic violence", "intimate partner", "battered"]):
        return "domestic_violence"
    if any(x in text for x in ["attempted murder", "tried to kill", "attempted to kill"]):
        return "attempted_murder"
    if any(x in text for x in ["child abuse", "molestation", "molested"]):
        return "child_abuse"
    if "coercive control" in text:
        return "coercive_control"
    if "harassment" in text or "harassed" in text:
        return "harassment"
    return "assault"


def _extract_location(text: str) -> tuple[str, str]:
    match = _CITY_STATE_PATTERN.search(text)
    if match:
        raw_city  = match.group(1).strip().title()
        raw_state = match.group(2).strip()
        state = raw_state.upper() if len(raw_state) == 2 else _STATE_ABBR.get(raw_state.lower(), "")
        if state and raw_city:
            return raw_city, state
    match = _STATE_PATTERN.search(text)
    if match:
        state = _STATE_ABBR.get(match.group(0).lower(), "")
        return "", state
    return "", ""


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


def _infer_status(text: str) -> str:
    if any(x in text for x in ["convicted", "guilty plea", "pleaded guilty", "sentenced", "found guilty"]):
        return "convicted"
    if any(x in text for x in ["charged", "arrested", "indicted", "faces charges"]):
        return "charged"
    if any(x in text for x in ["acquitted", "not guilty", "charges dropped"]):
        return "acquitted"
    return "reported"


def _clean_summary(title: str, body: str) -> str:
    clean = re.sub(r"<[^>]+>", "", body).strip()
    sentences = re.split(r"(?<=[.!?])\s+", clean)
    first = sentences[0] if sentences else ""
    if first and first != title:
        return f"{title} {first}"[:600]
    return title[:600]
