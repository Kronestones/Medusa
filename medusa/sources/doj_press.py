"""
sources/doj_press.py — DOJ Press Release RSS (no API key required)

The single richest untapped source for Medusa.
Every federal prosecution announced here — named defendants,
charges, sentences, locations. No auth required.

Feed: https://www.justice.gov/rss/news.xml

MAINTENANCE NOTE:
  If feed returns 0: test with curl -s "https://www.justice.gov/rss/news.xml" | head -c 500
  If URL changed: check https://www.justice.gov/news for current RSS link
"""

import re
from medusa.fetch import safe_rss

DOJ_FEEDS = [
    "https://www.justice.gov/rss/news.xml",
    "https://www.justice.gov/usao/rss/press-releases.xml",
]

INCLUDE_KEYWORDS = [
    "domestic violence", "sexual assault", "rape", "stalking",
    "sex trafficking", "human trafficking", "femicide",
    "intimate partner", "trafficking", "harassment",
    "attempted murder", "strangled", "child abuse", "molestation",
    "sexual abuse", "sexual exploitation", "coercive",
    "violence against women", "assault", "murder", "homicide",
    "beaten", "battered", "restraining order",
]

EXCLUDE_KEYWORDS = [
    "drug trafficking", "drug conspiracy", "money laundering",
    "wire fraud", "tax fraud", "copyright", "antitrust",
    "securities fraud", "immigration fraud", "cyber",
    "ukraine", "russia", "china", "iran", "afghanistan",
]

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

_CITY_STATE_PATTERN = re.compile(
    r"([A-Z][a-zA-Z\s]{2,25}),\s*([A-Z]{2}|"
    r"Alabama|Alaska|Arizona|Arkansas|California|Colorado|Connecticut|"
    r"Delaware|Florida|Georgia|Hawaii|Idaho|Illinois|Indiana|Iowa|Kansas|"
    r"Kentucky|Louisiana|Maine|Maryland|Massachusetts|Michigan|Minnesota|"
    r"Mississippi|Missouri|Montana|Nebraska|Nevada|New Hampshire|New Jersey|"
    r"New Mexico|New York|North Carolina|North Dakota|Ohio|Oklahoma|Oregon|"
    r"Pennsylvania|Rhode Island|South Carolina|South Dakota|Tennessee|Texas|"
    r"Utah|Vermont|Virginia|Washington|West Virginia|Wisconsin|Wyoming)"
    r"[\s,\.]"
)

_SENTENCED   = re.compile(r"\bsentenced\b",                         re.IGNORECASE)
_CONVICTED   = re.compile(r"\bconvicted\b|\bguilty\b",              re.IGNORECASE)
_CHARGED     = re.compile(r"\bcharged\b|\bindicted\b|\barrested\b", re.IGNORECASE)
_ACQUITTED   = re.compile(r"\bacquitted\b|\bnot guilty\b",          re.IGNORECASE)

_PUBLIC_FIGURE = re.compile(
    r"\b(officer|deputy|sergeant|detective|agent|official|judge|"
    r"senator|congressman|mayor|governor|coach|teacher|professor|"
    r"pastor|priest|doctor|counselor|therapist|principal|warden|"
    r"guard|corrections|military|soldier)\b",
    re.IGNORECASE,
)


def fetch() -> list[dict]:
    records   = []
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

    print(f"[DOJ Press] {len(records)} records fetched.")
    return records


def _parse_entry(entry) -> dict | None:
    title   = entry.get("title")   or ""
    summary = entry.get("summary") or entry.get("description") or ""
    text    = f"{title} {summary}".lower()

    if not any(kw in text for kw in INCLUDE_KEYWORDS):
        return None
    if any(kw in text for kw in EXCLUDE_KEYWORDS):
        return None

    full_text   = f"{title} {summary}"
    city, state = _extract_location(full_text)
    if not state:
        return None

    return {
        "summary":          _clean_summary(title, summary),
        "city":             city or state,
        "state":            state,
        "date_incident":    _parse_date(entry.get("published") or entry.get("updated") or ""),
        "violence_type":    _infer_type(text),
        "status":           _infer_status(title),
        "is_public_figure": bool(_PUBLIC_FIGURE.search(full_text)),
        "source_url":       entry.get("link") or "",
        "source_name":      "DOJ Press Releases",
        "verified":         True,
    }


def _infer_type(text: str) -> str:
    if any(x in text for x in ["murder", "homicide", "killed", "femicide", "manslaughter"]):
        return "homicide"
    if any(x in text for x in ["rape", "raped"]):
        return "rape"
    if any(x in text for x in ["sex trafficking", "human trafficking"]):
        return "trafficking"
    if any(x in text for x in ["sexual assault", "sexual abuse", "sexual exploitation"]):
        return "sexual_assault"
    if "stalking" in text or "stalked" in text:
        return "stalking"
    if any(x in text for x in ["domestic violence", "intimate partner", "battered"]):
        return "domestic_violence"
    if any(x in text for x in ["attempted murder", "tried to kill"]):
        return "attempted_murder"
    if any(x in text for x in ["child abuse", "molestation", "child exploitation"]):
        return "child_abuse"
    if "coercive" in text:
        return "coercive_control"
    if "harassment" in text:
        return "harassment"
    return "assault"


def _infer_status(title: str) -> str:
    if _SENTENCED.search(title): return "convicted"
    if _CONVICTED.search(title): return "convicted"
    if _ACQUITTED.search(title): return "acquitted"
    if _CHARGED.search(title):   return "charged"
    return "reported"


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


def _clean_summary(title: str, body: str) -> str:
    clean = re.sub(r"<[^>]+>", "", body).strip()
    sentences = re.split(r"(?<=[.!?])\s+", clean)
    first = sentences[0] if sentences else ""
    if first and first != title:
        return f"{title} {first}"[:600]
    return title[:600]
