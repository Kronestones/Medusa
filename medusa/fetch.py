"""
fetch.py — Medusa safe HTTP wrapper

Every outbound request goes through here.
Never raises. Returns None on any failure.
Handles: timeouts, retries, rate-limit backoff, user-agent.
"""

import time
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

HEADERS = {
    "User-Agent": (
        "Medusa/1.2 (public violence documentation project; "
        "contact: sentinel.commons@gmail.com)"
    ),
    "Accept": "application/json, application/xml, text/html, */*",
}

# Retry on 429, 500, 502, 503, 504
_RETRY = Retry(
    total=3,
    backoff_factor=2,          # 2s, 4s, 8s
    status_forcelist=[429, 500, 502, 503, 504],
    allowed_methods=["GET"],
    raise_on_status=False,
)

_SESSION = requests.Session()
_SESSION.mount("https://", HTTPAdapter(max_retries=_RETRY))
_SESSION.mount("http://",  HTTPAdapter(max_retries=_RETRY))


def safe_get(url: str, params: dict = None, timeout: int = 15,
             extra_headers: dict = None, accept_xml: bool = False) -> requests.Response | None:
    """
    GET url with retry/backoff. Returns Response or None.
    Caller checks .ok and parses .json() / .text / .content themselves.
    """
    headers = dict(HEADERS)
    if accept_xml:
        headers["Accept"] = "application/xml, text/xml, */*"
    if extra_headers:
        headers.update(extra_headers)
    try:
        resp = _SESSION.get(url, params=params, headers=headers, timeout=timeout)
        if resp.status_code == 429:
            retry_after = int(resp.headers.get("Retry-After", 10))
            print(f"[fetch] 429 from {url[:60]} — waiting {retry_after}s")
            time.sleep(retry_after)
            resp = _SESSION.get(url, params=params, headers=headers, timeout=timeout)
        return resp
    except Exception as e:
        print(f"[fetch] FAIL {url[:80]}: {e}")
        return None


def safe_json(url: str, params: dict = None, timeout: int = 15,
              extra_headers: dict = None) -> dict | list | None:
    """GET and parse JSON. Returns parsed object or None."""
    resp = safe_get(url, params=params, timeout=timeout, extra_headers=extra_headers)
    if resp is None or not resp.ok:
        return None
    try:
        return resp.json()
    except Exception as e:
        print(f"[fetch] JSON parse error {url[:80]}: {e}")
        return None


def safe_rss(url: str, timeout: int = 15) -> list:
    """
    Fetch and parse an RSS/Atom feed.
    Returns list of feedparser entries, or [].
    """
    try:
        import feedparser
        resp = safe_get(url, timeout=timeout, accept_xml=True)
        if resp is None or not resp.ok:
            return []
        feed = feedparser.parse(resp.content)
        return feed.entries if hasattr(feed, "entries") else []
    except Exception as e:
        print(f"[fetch] RSS error {url[:80]}: {e}")
        return []
