"""
sources/courtlistener.py — CourtListener REST API v4

Uses the /search/ endpoint with Token authentication.
Free account: 5,000 requests/day.

Token stored in ~/medusa/.env as COURTLISTENER_TOKEN=...
"""

import os
import re
from datetime import datetime
from medusa.fetch import safe_json
from medusa.record import district_to_city, normalize_violence_type, STATE_LARGEST_CITY

SEARCH_URL = "https://www.courtlistener.com/api/rest/v4/search/"
PAGE_SIZE   = 20


def _get_token() -> str:
    token = os.environ.get("COURTLISTENER_TOKEN", "")
    if not token:
        env_path = os.path.expanduser("~/medusa/.env")
        try:
            for line in open(env_path):
                line = line.strip()
                if line.startswith("COURTLISTENER_TOKEN="):
                    token = line.split("=", 1)[1].strip()
                    break
        except Exception:
            pass
    return token


def _auth_headers() -> dict:
    token = _get_token()
    if token:
        return {"Authorization": f"Token {token}"}
    return {}


QUERIES = [
    ("domestic violence assault intimate partner",     "domestic_violence"),
    ("sexual assault rape conviction sentence",         "sexual_assault"),
    ("stalking harassment restraining order violation", "stalking"),
    ("femicide murder intimate partner women",          "homicide"),
    ("sex trafficking women forced prostitution",       "trafficking"),
    ("attempted murder girlfriend wife assault",        "attempted_murder"),
    ("sexual abuse minor child molestation",            "child_abuse"),
    ("rape conviction sentence women",                  "rape"),
]


def fetch() -> list[dict]:
    records  = []
    seen_ids = set()
    headers  = _auth_headers()

    for search_term, vtype_hint in QUERIES:
        results = _search(search_term, vtype_hint, headers)
        for r in results:
            rid = r.get("_cl_id")
            if rid and rid in seen_ids:
                continue
            if rid:
                seen_ids.add(rid)
            records.append(r)

    print(f"[CourtListener] {len(records)} records fetched.")
    return records


def _search(search_term: str, vtype_hint: str, headers: dict) -> list[dict]:
    data = safe_json(
        SEARCH_URL,
        params={
            "q":         search_term,
            "type":      "r",
            "page_size": PAGE_SIZE,
            "order_by":  "score desc",
        },
        extra_headers=headers,
    )
    if not data:
        return []
    results = data.get("results", [])
    records = []
    for item in results:
        rec = _parse(item, vtype_hint)
        if rec:
            records.append(rec)
    return records


def _parse(item: dict, vtype_hint: str) -> dict | None:
    case_name = (
        item.get("caseName") or
        item.get("case_name_full") or
        item.get("case_name") or ""
    ).strip()
    if not case_name:
        return None

    court_str = (
        item.get("court_citation_string") or
        item.get("court") or ""
    ).strip()

    city, state = _resolve_location(court_str)
    if not city or not state:
        return None

    date_str = _clean_date(
        item.get("dateFiled") or
        item.get("date_filed") or ""
    )

    docket_number = item.get("docketNumber") or ""
    judge         = item.get("assignedTo") or ""

    summary = f"Court case: {case_name}."
    if court_str:
        summary += f" Filed in {court_str}."
    if docket_number:
        summary += f" Docket {docket_number}."
    if judge:
        summary += f" Judge: {judge}."

    vtype  = _infer_type(case_name, vtype_hint)
    status = "convicted" if item.get("dateTerminated") else "charged"

    cl_id      = item.get("id") or ""
    source_url = f"https://www.courtlistener.com/docket/{cl_id}/" if cl_id else ""

    return {
        "summary":       summary[:600],
        "city":          city,
        "state":         state,
        "date_incident": date_str,
        "violence_type": vtype,
        "status":        status,
        "source_url":    source_url,
        "source_name":   "CourtListener / PACER",
        "verified":      True,
        "_cl_id":        str(cl_id),
    }


def _resolve_location(court_str: str) -> tuple[str, str]:
    if not court_str:
        return "", ""
    loc = district_to_city(court_str)
    if loc:
        return loc
    return "", ""


def _infer_type(case_name: str, hint: str) -> str:
    text = case_name.lower()
    if any(x in text for x in ["murder", "homicide", "kill", "manslaughter"]):
        return "homicide"
    if any(x in text for x in ["rape", "sexual assault"]):
        return "sexual_assault"
    if "trafficking" in text:
        return "trafficking"
    if "stalking" in text:
        return "stalking"
    if "domestic" in text or "intimate partner" in text:
        return "domestic_violence"
    if "attempted murder" in text:
        return "attempted_murder"
    if any(x in text for x in ["child", "minor", "abuse"]):
        return "child_abuse"
    from medusa.record import normalize_violence_type
    return normalize_violence_type(hint)


def _clean_date(raw: str) -> str:
    if not raw:
        return ""
    if re.match(r"\d{4}-\d{2}-\d{2}", raw):
        return raw[:10]
    return raw[:10] if len(raw) >= 10 else raw
