
"""
sources/wiki_homicides.py — Wikipedia state homicide lists filtered for
male violence against women and domestic/intimate partner cases.
"""

import re
import hashlib
import requests

WIKI_PAGES = [
    ("List of homicides in California",    "CA"),
    ("List of homicides in Illinois",      "IL"),
    ("List of homicides in Michigan",      "MI"),
    ("List of homicides in Massachusetts", "MA"),
    ("List of homicides in Wisconsin",     "WI"),
    ("List of homicides in Oregon",        "OR"),
    ("List of homicides in Nevada",        "NV"),
]

RELEVANT_TERMS = [
    "wife", "girlfriend", "domestic", "intimate partner",
    "woman killed", "women killed", "mother killed",
    "sexual assault", "rape", "femicide",
    "daughter killed", "female victim", "estranged wife",
    "ex-wife", "ex-girlfriend", "dating partner",
    "strangulation", "strangled", "stabbed wife",
    "murdered wife", "killed girlfriend",
]

EXCLUDE_TERMS = [
    "mass shooting", "terrorism", "gang", "robbery",
    "drug", "shooting spree", "school shooting",
]

def clean(text):
    if not text:
        return ""
    text = re.sub(r"<ref[^>]*>.*?</ref>", "", text, flags=re.DOTALL)
    text = re.sub(r"<ref[^/]*/?>", "", text)
    text = re.sub(r"{{[^}]*}}", "", text)
    text = re.sub(r"\[\[([^|\]]+)\|([^\]]+)\]\]", r"\2", text)
    text = re.sub(r"\[\[([^\]]+)\]\]", r"\1", text)
    return text.strip(" |\n")

def parse_date(text):
    text = clean(text)
    m = re.search(r"(\d{4})-(\d{2})-(\d{2})", text)
    if m:
        return m.group(0)
    m = re.search(r"\b(1[89]\d{2}|20[0-2]\d)\b", text)
    return m.group(1) if m else None

def make_id(name, state):
    h = hashlib.sha1(f"{name}:{state}".encode()).hexdigest()[:8].upper()
    return f"MEDUSA-WIKI-{h}"

def fetch_page(page_title, state):
    r = requests.get(
        "https://en.wikipedia.org/w/api.php",
        params={
            "action": "parse",
            "page":   page_title,
            "prop":   "wikitext",
            "format": "json",
        },
        headers={"User-Agent": "Medusa/1.2 (sentinel.commons@gmail.com)"},
        timeout=15,
    )
    if not r.ok:
        return []

    text = r.json().get("parse", {}).get("wikitext", {}).get("*", "")
    blocks = text.split("\n|-\n")
    records = []

    for block in blocks:
        block_lower = block.lower()
        if not any(term in block_lower for term in RELEVANT_TERMS):
            continue
        if any(term in block_lower for term in EXCLUDE_TERMS):
            continue

        # Row may be single line with || separators or multiline
        full_line = " ".join(l.strip() for l in block.split("\n") if l.strip().startswith("|"))
        cols = [c.strip() for c in full_line.lstrip("|").split("||")]
        if len(cols) < 4:
            continue

        # Columns: No | Incident | Location | Date | Deaths | Description
        incident    = clean(cols[1]) if len(cols) > 1 else ""
        location    = clean(cols[2]) if len(cols) > 2 else ""
        date        = parse_date(cols[3]) if len(cols) > 3 else None
        description = clean(cols[5]) if len(cols) > 5 else ""

        if not incident:
            continue

        summary = f"{incident}."
        if location: summary += f" Location: {location}."
        if description: summary += f" {description[:300]}"

        # Determine violence type
        vtype = "homicide"
        text_lower = f"{incident} {description}".lower()
        if any(x in text_lower for x in ["sexual assault", "rape", "sexually assaulted"]):
            vtype = "sexual_assault"
        elif "domestic" in text_lower or "intimate partner" in text_lower:
            vtype = "domestic_violence"
        elif "stalking" in text_lower:
            vtype = "stalking"

        wiki_slug = incident.replace(" ", "_")
        source_url = f"https://en.wikipedia.org/wiki/{wiki_slug}"

        records.append({
            "summary":       summary[:600],
            "city":          location or "Unknown",
            "state":         state,
            "date_incident": date or "",
            "violence_type": vtype,
            "status":        "reported",
            "source_url":    source_url,
            "source_name":   f"Wikipedia — {page_title}",
            "verified":      True,
        })

    return records

def fetch() -> list[dict]:
    all_records = []
    for page_title, state in WIKI_PAGES:
        try:
            records = fetch_page(page_title, state)
            print(f"[Wiki Homicides] {state}: {len(records)} relevant cases")
            all_records.extend(records)
        except Exception as e:
            print(f"[Wiki Homicides] {state} error: {e}")

    print(f"[Wiki Homicides] {len(all_records)} total records fetched.")
    return all_records
