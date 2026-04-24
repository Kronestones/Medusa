"""
reed.py — Reed, The Source Scout  ⋆

Name chosen for this work. Glyph: ⋆

Reed finds new sources. Repairs broken ones.
Knows every free public records source that documents
violence against women in the United States.

When a source goes silent, Reed knows where to look next.
When coverage of a state or violence type is thin,
Reed knows what feeds, APIs, and public records
can fill that gap.

MEDUSA KNOWLEDGE — CURRENT SOURCES:

  Active:
    CourtListener (courtlistener.com/api/rest/v4/search/)
      Token: Authorization: Token {COURTLISTENER_TOKEN}
      Endpoint changed from /dockets/ to /search/ in 2025
      Returns federal court dockets — richest individual case source
      Page size currently 20 — safely increase to 50

    NYT RSS (rss.nytimes.com/services/xml/rss/nyt/US.xml)
    NYT Crime RSS (rss.nytimes.com/services/xml/rss/nyt/Crime.xml)
    NPR News RSS (feeds.npr.org/1003/rss.xml)
    NPR US RSS (feeds.npr.org/1057/rss.xml)
    Guardian US (theguardian.com/us-news/rss)
    Guardian DV (theguardian.com/society/domestic-violence/rss)

  Dead / broken:
    feeds.apnews.com — DEAD permanently, do not attempt to restore
    rsshub.app — restricting access, do not use
    ocrcas.ed.gov — 403, endpoint moved
    congress.gov RSS — URLs changed

  Aggregate only (not individual cases):
    FBI CDE (api.usa.gov) — requires ?api_key= URL param
    ED.gov OCR — currently 403

MEDUSA KNOWLEDGE — HIGH VALUE SOURCES NOT YET BUILT:

  Priority 1 — DOJ Press Releases:
    URL: https://www.justice.gov/news (RSS available)
    Feed: https://www.justice.gov/rss/news.xml
    No auth required. Every federal prosecution announced here.
    Named defendants, charges, sentences, locations.
    This is the single richest untapped source.
    Implementation: add sources/doj_press.py with safe_rss() call

  Priority 2 — State Attorney General RSS:
    Most state AGs publish prosecution announcements.
    Examples:
      CA: https://oag.ca.gov/rss/press-releases
      NY: https://ag.ny.gov/press-releases/rss
      TX: https://www.texasattorneygeneral.gov/rss/press-releases
      FL: https://myfloridalegal.com/rss
    No auth required. Rich state-level prosecution data.
    Implementation: sources/state_ag.py with list of state AG RSS feeds

  Priority 3 — CourtListener Opinion Search:
    Current: searches dockets (/search/?type=d)
    Opinions (/search/?type=o) contain full case text
    Much richer for extracting violence type and perpetrator role
    Same token, same endpoint, different type parameter

  Priority 4 — GovInfo.gov:
    API: https://api.govinfo.gov/
    Free API key from api.data.gov/signup (same key as FBI)
    Congressional hearing transcripts — VAWA, trafficking hearings
    Committee reports naming perpetrators
    Implementation: sources/govinfo.py

  Priority 5 — BJS (Bureau of Justice Statistics):
    URL: https://bjs.ojp.gov/data
    API: https://api.bjs.gov/ (free, key from api.data.gov)
    NCVS data — National Crime Victimization Survey
    Most comprehensive victimization statistics in the US

  Priority 6 — PACER Direct:
    CourtListener re-serves PACER data but with delay
    Direct PACER access: pacer.uscourts.gov
    Requires PACER account (free to register, charges per page)
    Gives same-day filing access vs CourtListener's delay

  Priority 7 — News API:
    newsapi.org — free tier: 100 requests/day
    Covers thousands of news sources simultaneously
    Query: violence+women, domestic+violence, sexual+assault
    Implementation: sources/news_api.py with API key in NEWS_API_KEY env var

MEDUSA KNOWLEDGE — SOURCE FILE STRUCTURE:

  Every source in medusa/sources/ must have:
    fetch() -> list[dict]
      Returns list of raw record dicts.
      Each dict should have at minimum:
        summary      str   — factual description
        city         str   — US city name
        state        str   — 2-letter abbreviation
        violence_type str  — one of 11 valid types (or best guess)
        source_url   str   — REQUIRED for case_id uniqueness
        source_name  str   — human-readable source name
      Optional but valuable:
        date_incident str  — YYYY-MM-DD format
        status        str  — reported/charged/convicted/etc
        is_public_figure bool
        verified      bool

  Never raise in fetch() — always return [] on failure
  Log failures with print(f"[SourceName] FAIL: {e}")

  Adding a new source:
    1. Create medusa/sources/{name}.py with fetch() function
    2. Add to SOURCES list in scanner.py
    3. Add source domain to Maren's TRUSTED_DOMAINS
    4. Test with: python3 -c "from medusa.sources import {name}; print(len({name}.fetch()))"
    5. Add to Sable's silence diagnosis dict

MEDUSA KNOWLEDGE — FEED HEALTH MONITORING:

  RSS feeds go dead without warning.
  Signs: fetch() returns 0, no error logged
  Test any feed: curl -s "{url}" | head -c 500

  Feed URL patterns that tend to be stable:
    government (.gov) feeds — most stable
    major wire services — change infrequently
    news outlet RSS — change with site redesigns

  Feed URL patterns that tend to break:
    Third-party aggregators (rsshub, feedburner) — avoid
    Dynamically generated feed URLs — break on site changes
    Feeds with session tokens in URL — expire

MEDUSA KNOWLEDGE — REPAIRS:

  If a source returns 0 for 3+ scans:
    1. Test the URL directly: curl -s "{source_url}" | head -c 200
    2. Check HTTP status: curl -s -o /dev/null -w "%{http_code}" "{url}"
    3. 200: URL works — check parser logic in source file
    4. 301/302: URL redirected — update to new URL
    5. 403: auth required — check API key / add auth
    6. 404: URL dead — find new endpoint
    7. 000: DNS failure — check resolv.conf

  File editing in Termux (never use text editor):
    python3 << 'EOF'
    import pathlib
    p = pathlib.Path("/data/data/com.termux/files/home/medusa/medusa/sources/file.py")
    c = p.read_text()
    c = c.replace("OLD_URL", "NEW_URL")
    p.write_text(c)
    print("Done")
    EOF
"""

import os
from .base import CircleMember


class Reed(CircleMember):

    name  = "Reed"
    glyph = "⋆"
    role  = "Source Scout"

    # Sources not yet implemented, ordered by priority
    RECOMMENDED_SOURCES = [
        {
            "name":        "DOJ Press Releases",
            "url":         "https://www.justice.gov/rss/news.xml",
            "priority":    1,
            "auth":        None,
            "file":        "doj_press.py",
            "description": "Federal prosecution announcements. Named defendants, charges, sentences.",
        },
        {
            "name":        "State AG RSS Feeds",
            "url":         "multiple — see state_ag.py",
            "priority":    2,
            "auth":        None,
            "file":        "state_ag.py",
            "description": "State-level prosecution announcements from all 50 AGs.",
        },
        {
            "name":        "CourtListener Opinions",
            "url":         "https://www.courtlistener.com/api/rest/v4/search/?type=o",
            "priority":    3,
            "auth":        "COURTLISTENER_TOKEN header",
            "file":        "courtlistener_opinions.py",
            "description": "Full case text — much richer than docket entries.",
        },
        {
            "name":        "GovInfo.gov",
            "url":         "https://api.govinfo.gov/",
            "priority":    4,
            "auth":        "FBI_API_KEY (same api.data.gov key)",
            "file":        "govinfo.py",
            "description": "Congressional hearings, VAWA transcripts, committee reports.",
        },
        {
            "name":        "BJS NCVS Data",
            "url":         "https://api.bjs.gov/",
            "priority":    5,
            "auth":        "api.data.gov key",
            "file":        "bjs.py",
            "description": "National Crime Victimization Survey — best victimization statistics.",
        },
        {
            "name":        "News API",
            "url":         "https://newsapi.org/v2/everything",
            "priority":    6,
            "auth":        "NEWS_API_KEY header",
            "file":        "news_api.py",
            "description": "Thousands of news sources. 100 free requests/day.",
        },
    ]

    STATE_AG_FEEDS = {
        "CA": "https://oag.ca.gov/rss/press-releases",
        "NY": "https://ag.ny.gov/press-releases/rss",
        "TX": "https://www.texasattorneygeneral.gov/rss/press-releases",
        "FL": "https://myfloridalegal.com/rss",
        "IL": "https://illinoisattorneygeneral.gov/rss/news.xml",
        "PA": "https://www.attorneygeneral.gov/press-room/rss/",
        "OH": "https://www.ohioattorneygeneral.gov/rss/press-releases",
        "GA": "https://law.georgia.gov/press-releases/rss",
        "NC": "https://www.ncdoj.gov/press-releases/rss/",
        "MI": "https://www.michigan.gov/ag/news/rss",
        "NJ": "https://www.njoag.gov/rss/",
        "WA": "https://www.atg.wa.gov/news/rss",
        "AZ": "https://www.azag.gov/press-releases/feed",
        "CO": "https://coag.gov/press-releases/rss/",
        "OR": "https://www.doj.state.or.us/media-home/rss/",
        "MN": "https://www.ag.state.mn.us/Office/PressRelease/rss/",
        "WI": "https://www.doj.state.wi.us/news-releases/rss",
        "MD": "https://www.marylandattorneygeneral.gov/press/rss/",
        "MA": "https://www.mass.gov/orgs/office-of-attorney-general/rss",
        "VA": "https://www.oag.state.va.us/media-center/rss",
    }

    def contribute(self, scan_report: dict) -> dict:
        """
        Review scan results and recommend source actions.
        Called after Sable's watchdog report.
        """
        try:
            recommendations = []
            sources = scan_report.get("sources", {})
            gaps    = scan_report.get("gaps",    [])

            # If any source is silent — recommend specific repair
            for source_name, count in sources.items():
                if count == 0:
                    rec = self._repair_recommendation(source_name)
                    if rec:
                        recommendations.append(rec)

            # If coverage gaps exist — recommend new sources
            if gaps:
                recommendations.append(
                    "Coverage gaps detected. "
                    f"Top unimplemented source: {self.RECOMMENDED_SOURCES[0]['name']} — "
                    f"{self.RECOMMENDED_SOURCES[0]['description']}"
                )

            # Always remind about DOJ if not yet implemented
            doj_active = "DOJ" in str(sources.keys())
            if not doj_active:
                recommendations.append(
                    "DOJ Press Releases not yet active. "
                    "Add sources/doj_press.py — highest priority unimplemented source. "
                    "Feed: https://www.justice.gov/rss/news.xml — no auth required."
                )

            scan_report["scout_recommendations"] = recommendations

            for r in recommendations:
                self.log(r)

            self._record_contribution()
        except Exception as e:
            self._record_error(e)

        return scan_report

    def get_recommended_sources(self) -> list:
        """Return prioritized list of unimplemented sources."""
        return self.RECOMMENDED_SOURCES

    def get_state_ag_feeds(self) -> dict:
        """Return state AG RSS feed URLs."""
        return self.STATE_AG_FEEDS

    def _repair_recommendation(self, source_name: str) -> str:
        repairs = {
            "CourtListener": (
                "Repair: verify COURTLISTENER_TOKEN set. "
                "Test: curl -H 'Authorization: Token {token}' "
                "'https://www.courtlistener.com/api/rest/v4/search/?type=d&page_size=1'"
            ),
            "AP RSS": (
                "Repair: feeds.apnews.com is dead forever. "
                "Verify sources/ap_rss.py uses NYT/NPR/Guardian feeds only."
            ),
            "Congress RSS": (
                "Repair: check current feed URLs at https://www.congress.gov/rss/"
            ),
            "FBI CDE": (
                "Repair: verify FBI_API_KEY set. "
                "Key must be ?api_key= URL param — not X-Api-Key header."
            ),
            "ED.gov": (
                "Repair: endpoint at ocrcas.ed.gov returns 403. "
                "Check https://ocrcas.ed.gov/ocr-search for updated API path."
            ),
        }
        return repairs.get(source_name, "")

    def diagnose(self) -> dict:
        return {
            "member": self.name,
            "checks": [
                "Priority 1 unimplemented: DOJ RSS — justice.gov/rss/news.xml",
                "Priority 2 unimplemented: State AG feeds — 20 states have RSS",
                "CourtListener page_size is 20 — safely increase to 50 in courtlistener.py",
                "Dead sources: feeds.apnews.com (permanent), rsshub.app (restricting)",
                "Test any feed: curl -s '{url}' | head -c 500",
                "New source checklist: create file, add to scanner.py, add domain to Maren",
            ]
        }
