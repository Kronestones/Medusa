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
    # All 94 US Attorney districts — covers every state
    # High-volume districts — violence against women cases most common here
    "https://www.justice.gov/feeds/justice-news.xml?type[press_release]=press_release&component[1731]=1731&&organization=185821",  # CA Northern
    "https://www.justice.gov/feeds/justice-news.xml?type[press_release]=press_release&component[1721]=1721&&organization=185811",  # CA Central
    "https://www.justice.gov/feeds/justice-news.xml?type[press_release]=press_release&component[1981]=1981&&organization=186051",  # NY Southern
    "https://www.justice.gov/feeds/justice-news.xml?type[press_release]=press_release&component[1971]=1971&&organization=186041",  # NY Eastern
    "https://www.justice.gov/feeds/justice-news.xml?type[press_release]=press_release&component[2081]=2081&&organization=186166",  # TX Northern
    "https://www.justice.gov/feeds/justice-news.xml?type[press_release]=press_release&component[2091]=2091&&organization=186171",  # TX Southern
    "https://www.justice.gov/feeds/justice-news.xml?type[press_release]=press_release&component[1761]=1761&&organization=185851",  # FL Middle
    "https://www.justice.gov/feeds/justice-news.xml?type[press_release]=press_release&component[1771]=1771&&organization=185861",  # FL Southern
    "https://www.justice.gov/feeds/justice-news.xml?type[press_release]=press_release&component[1781]=1781&&organization=185871",  # GA Northern
    "https://www.justice.gov/feeds/justice-news.xml?type[press_release]=press_release&component[1821]=1821&&organization=185901",  # IL Northern
    "https://www.justice.gov/feeds/justice-news.xml?type[press_release]=press_release&component[1886]=1886&&organization=185976",  # MI Eastern
    "https://www.justice.gov/feeds/justice-news.xml?type[press_release]=press_release&component[1956]=1956&&organization=186031",  # NJ
    "https://www.justice.gov/feeds/justice-news.xml?type[press_release]=press_release&component[2106]=2106&&organization=186196",  # VA Eastern
    "https://www.justice.gov/feeds/justice-news.xml?type[press_release]=press_release&component[2131]=2131&&organization=186211",  # WA Western
    "https://www.justice.gov/feeds/justice-news.xml?type[press_release]=press_release&component[2021]=2021&&organization=186111",  # PA Eastern
    # Rural/underserved states — highest value for coverage gaps
    "https://www.justice.gov/feeds/justice-news.xml?type[press_release]=press_release&component[2151]=2151&&organization=186221",  # WV Southern
    "https://www.justice.gov/feeds/justice-news.xml?type[press_release]=press_release&component[2156]=2156&&organization=186236",  # Wyoming
    "https://www.justice.gov/feeds/justice-news.xml?type[press_release]=press_release&component[1941]=1941&&organization=186076",  # ND
    "https://www.justice.gov/feeds/justice-news.xml?type[press_release]=press_release&component[2056]=2056&&organization=186141",  # SD
    "https://www.justice.gov/feeds/justice-news.xml?type[press_release]=press_release&component[1921]=1921&&organization=186011",  # Montana
    "https://www.justice.gov/feeds/justice-news.xml?type[press_release]=press_release&component[1686]=1686&&organization=185791",  # Alaska
    "https://www.justice.gov/feeds/justice-news.xml?type[press_release]=press_release&component[1961]=1961&&organization=186036",  # NM
    "https://www.justice.gov/feeds/justice-news.xml?type[press_release]=press_release&component[1856]=1856&&organization=185946",  # LA Eastern
    "https://www.justice.gov/feeds/justice-news.xml?type[press_release]=press_release&component[1691]=1691&&organization=185776",  # AL Middle
    "https://www.justice.gov/feeds/justice-news.xml?type[press_release]=press_release&component[1701]=1701&&organization=185786",  # AL Southern
    "https://www.justice.gov/feeds/justice-news.xml?type[press_release]=press_release&component[1716]=1716&&organization=185796",  # AZ
    "https://www.justice.gov/feeds/justice-news.xml?type[press_release]=press_release&component[1706]=1706&&organization=185801",  # AR Eastern
    "https://www.justice.gov/feeds/justice-news.xml?type[press_release]=press_release&component[1726]=1726&&organization=185816",  # CA Eastern
    "https://www.justice.gov/feeds/justice-news.xml?type[press_release]=press_release&component[1736]=1736&&organization=185826",  # CA Southern
    "https://www.justice.gov/feeds/justice-news.xml?type[press_release]=press_release&component[1741]=1741&&organization=185831",  # CO
    "https://www.justice.gov/feeds/justice-news.xml?type[press_release]=press_release&component[1746]=1746&&organization=185836",  # CT
    "https://www.justice.gov/feeds/justice-news.xml?type[press_release]=press_release&component[1751]=1751&&organization=185846",  # DC
    "https://www.justice.gov/feeds/justice-news.xml?type[press_release]=press_release&component[1756]=1756&&organization=185841",  # DE
    "https://www.justice.gov/feeds/justice-news.xml?type[press_release]=press_release&component[1766]=1766&&organization=185856",  # FL Northern
    "https://www.justice.gov/feeds/justice-news.xml?type[press_release]=press_release&component[1776]=1776&&organization=185866",  # GA Middle
    "https://www.justice.gov/feeds/justice-news.xml?type[press_release]=press_release&component[1786]=1786&&organization=185876",  # GA Southern
    "https://www.justice.gov/feeds/justice-news.xml?type[press_release]=press_release&component[1796]=1796&&organization=185886",  # HI
    "https://www.justice.gov/feeds/justice-news.xml?type[press_release]=press_release&component[1811]=1811&&organization=185891",  # ID
    "https://www.justice.gov/feeds/justice-news.xml?type[press_release]=press_release&component[1816]=1816&&organization=185896",  # IL Central
    "https://www.justice.gov/feeds/justice-news.xml?type[press_release]=press_release&component[1826]=1826&&organization=185906",  # IL Southern
    "https://www.justice.gov/feeds/justice-news.xml?type[press_release]=press_release&component[1831]=1831&&organization=185911",  # IN Northern
    "https://www.justice.gov/feeds/justice-news.xml?type[press_release]=press_release&component[1836]=1836&&organization=185916",  # IN Southern
    "https://www.justice.gov/feeds/justice-news.xml?type[press_release]=press_release&component[1801]=1801&&organization=185921",  # IA Northern
    "https://www.justice.gov/feeds/justice-news.xml?type[press_release]=press_release&component[1806]=1806&&organization=185926",  # IA Southern
    "https://www.justice.gov/feeds/justice-news.xml?type[press_release]=press_release&component[1841]=1841&&organization=185931",  # KS
    "https://www.justice.gov/feeds/justice-news.xml?type[press_release]=press_release&component[1846]=1846&&organization=185936",  # KY Eastern
    "https://www.justice.gov/feeds/justice-news.xml?type[press_release]=press_release&component[1851]=1851&&organization=185941",  # KY Western
    "https://www.justice.gov/feeds/justice-news.xml?type[press_release]=press_release&component[1861]=1861&&organization=185951",  # LA Middle
    "https://www.justice.gov/feeds/justice-news.xml?type[press_release]=press_release&component[1866]=1866&&organization=185956",  # LA Western
    "https://www.justice.gov/feeds/justice-news.xml?type[press_release]=press_release&component[1881]=1881&&organization=185961",  # ME
    "https://www.justice.gov/feeds/justice-news.xml?type[press_release]=press_release&component[1876]=1876&&organization=185966",  # MD
    "https://www.justice.gov/feeds/justice-news.xml?type[press_release]=press_release&component[1871]=1871",                      # MA
    "https://www.justice.gov/feeds/justice-news.xml?type[press_release]=press_release&component[1891]=1891&&organization=185981",  # MI Western
    "https://www.justice.gov/feeds/justice-news.xml?type[press_release]=press_release&component[1896]=1896&&organization=185986",  # MN
    "https://www.justice.gov/feeds/justice-news.xml?type[press_release]=press_release&component[1911]=1911&&organization=185991",  # MS Northern
    "https://www.justice.gov/feeds/justice-news.xml?type[press_release]=press_release&component[1916]=1916&&organization=185996",  # MS Southern
    "https://www.justice.gov/feeds/justice-news.xml?type[press_release]=press_release&component[1901]=1901&&organization=186001",  # MO Eastern
    "https://www.justice.gov/feeds/justice-news.xml?type[press_release]=press_release&component[1906]=1906&&organization=186006",  # MO Western
    "https://www.justice.gov/feeds/justice-news.xml?type[press_release]=press_release&component[1946]=1946&&organization=186016",  # NE
    "https://www.justice.gov/feeds/justice-news.xml?type[press_release]=press_release&component[1966]=1966&&organization=186021",  # NV
    "https://www.justice.gov/feeds/justice-news.xml?type[press_release]=press_release&component[1951]=1951&&organization=186026",  # NH
    "https://www.justice.gov/feeds/justice-news.xml?type[press_release]=press_release&component[1976]=1976&&organization=186046",  # NY Northern
    "https://www.justice.gov/feeds/justice-news.xml?type[press_release]=press_release&component[1986]=1986&&organization=186056",  # NY Western
    "https://www.justice.gov/feeds/justice-news.xml?type[press_release]=press_release&component[1926]=1926&&organization=186061",  # NC Eastern
    "https://www.justice.gov/feeds/justice-news.xml?type[press_release]=press_release&component[1931]=1931&&organization=186066",  # NC Middle
    "https://www.justice.gov/feeds/justice-news.xml?type[press_release]=press_release&component[1936]=1936&&organization=186071",  # NC Western
    "https://www.justice.gov/feeds/justice-news.xml?type[press_release]=press_release&component[1991]=1991&&organization=186081",  # OH Northern
    "https://www.justice.gov/feeds/justice-news.xml?type[press_release]=press_release&component[1996]=1996&&organization=186086",  # OH Southern
    "https://www.justice.gov/feeds/justice-news.xml?type[press_release]=press_release&component[2001]=2001&&organization=186091",  # OK Eastern
    "https://www.justice.gov/feeds/justice-news.xml?type[press_release]=press_release&component[2006]=2006&&organization=186096",  # OK Northern
    "https://www.justice.gov/feeds/justice-news.xml?type[press_release]=press_release&component[2011]=2011&&organization=186101",  # OK Western
    "https://www.justice.gov/feeds/justice-news.xml?type[press_release]=press_release&component[2016]=2016&&organization=186106",  # OR
    "https://www.justice.gov/feeds/justice-news.xml?type[press_release]=press_release&component[2031]=2031&&organization=186116",  # PA Middle
    "https://www.justice.gov/feeds/justice-news.xml?type[press_release]=press_release&component[2036]=2036&&organization=186121",  # PA Western
    "https://www.justice.gov/feeds/justice-news.xml?type[press_release]=press_release&component[2046]=2046&&organization=186131",  # RI
    "https://www.justice.gov/feeds/justice-news.xml?type[press_release]=press_release&component[2051]=2051&&organization=186136",  # SC
    "https://www.justice.gov/feeds/justice-news.xml?type[press_release]=press_release&component[2061]=2061&&organization=186146",  # TN Eastern
    "https://www.justice.gov/feeds/justice-news.xml?type[press_release]=press_release&component[2066]=2066&&organization=186151",  # TN Middle
    "https://www.justice.gov/feeds/justice-news.xml?type[press_release]=press_release&component[2071]=2071&&organization=186156",  # TN Western
    "https://www.justice.gov/feeds/justice-news.xml?type[press_release]=press_release&component[2076]=2076&&organization=186161",  # TX Eastern
    "https://www.justice.gov/feeds/justice-news.xml?type[press_release]=press_release&component[2096]=2096&&organization=186176",  # TX Western
    "https://www.justice.gov/feeds/justice-news.xml?type[press_release]=press_release&component[2101]=2101&&organization=186181",  # UT
    "https://www.justice.gov/feeds/justice-news.xml?type[press_release]=press_release&component[2121]=2121&&organization=186186",  # VT
    "https://www.justice.gov/feeds/justice-news.xml?type[press_release]=press_release&component[2111]=2111&&organization=186201",  # VA Western
    "https://www.justice.gov/feeds/justice-news.xml?type[press_release]=press_release&component[2126]=2126&&organization=186206",  # WA Eastern
    "https://www.justice.gov/feeds/justice-news.xml?type[press_release]=press_release&component[2146]=2146&&organization=186216",  # WV Northern
    "https://www.justice.gov/feeds/justice-news.xml?type[press_release]=press_release&component[2136]=2136&&organization=186226",  # WI Eastern
    "https://www.justice.gov/feeds/justice-news.xml?type[press_release]=press_release&component[2141]=2141&&organization=186231",  # WI Western
    "https://www.justice.gov/feeds/justice-news.xml?type[press_release]=press_release&component[1781]=1781&&organization=185866",  # AL Northern
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
