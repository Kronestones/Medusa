"""
web.py — Medusa Web Interface

Public map. No login. No account.
Every act documented. Every source cited.

Routes:
    /               → Leaflet map
    /api/cases      → All mapped cases (JSON)
    /api/stats      → Counts by type (JSON)
    /api/scan       → Trigger a scan (POST)
    /api/status     → System status (JSON)

Built on Project Themis architecture.
"""

import os
from flask import Flask, jsonify, render_template, request
from datetime import datetime, timezone

from .database import init_db, save_case, get_cases, get_case_count, get_stats

app      = Flask(__name__)
_scanner = None


def _get_scanner():
    global _scanner
    if _scanner is None:
        from .scanner import MedusaScanner
        _scanner = MedusaScanner()
    return _scanner


def create_app():
    try:
        init_db()
        print("[Medusa Web] DB initialized.")
    except Exception as e:
        print(f"[Medusa Web] DB init warning: {e}")
    start_scheduler()
    return app


@app.route("/")
def index():
    try:
        total = get_case_count()
    except Exception:
        total = 0
    return render_template("entry.html", total=total)

@app.route("/map")
def map_view():
    try:
        total = get_case_count()
    except Exception:
        total = 0
    return render_template("map.html", total=total)


@app.route("/api/cases")
def api_cases():
    limit         = min(int(request.args.get("limit", 2000)), 10000)
    violence_type = request.args.get("type")
    state         = request.args.get("state")
    pub_fig       = request.args.get("public_figure")
    if pub_fig is not None:
        pub_fig = pub_fig.lower() == "true"

    all_cases = get_cases(limit=limit, violence_type=violence_type,
                          state=state, public_figure=pub_fig)
    mapped = [c for c in all_cases if c.get("lat") and c.get("lng")]

    return jsonify({
        "ok":      True,
        "cases":   mapped,
        "total":   get_case_count(),
        "updated": datetime.now(timezone.utc).isoformat(),
    })


@app.route("/api/stats")
def api_stats():
    return jsonify({"ok": True, **get_stats()})


@app.route("/api/scan", methods=["POST"])
def api_scan():
    import threading
    def _do_scan():
        try:
            s = _get_scanner()
            cases = s.scan()
            saved = sum(1 for c in cases if save_case(c))
            print(f"[Medusa] Scan complete. {saved} new cases saved.")
        except Exception as e:
            print(f"[Medusa] Scan error: {e}")
    threading.Thread(target=_do_scan, daemon=True).start()
    return jsonify({"ok": True, "message": "Scan started."})

@app.route("/api/press")
def api_press():
    import requests, xml.etree.ElementTree as ET
    feeds = [
        ("The 19th",     "https://19thnews.org/feed/"),
        ("Ms. Magazine", "https://msmagazine.com/feed/"),
        ("Rewire News",  "https://rewirenewsgroup.com/feed/"),
        ("Guardian DV",  "https://www.theguardian.com/society/domestic-violence/rss"),
        ("Guardian SA",  "https://www.theguardian.com/society/rape-and-sexual-assault/rss"),
    ]
    keywords = [
        "domestic violence","sexual assault","rape","stalking","trafficking",
        "femicide","intimate partner","violence against women","gender violence",
        "abuse","epstein","rape chat","uber assault","ice detention","pregnant",
        "andrew tate","exploitation","grooming","predator","harvey weinstein",
        "maxwell","sex trafficking","child abuse","missing women",
    ]
    articles = []
    for name, url in feeds:
        try:
            r = requests.get(url, headers={"User-Agent": "Medusa/1.2"}, timeout=8)
            root = ET.fromstring(r.content)
            for item in root.findall(".//item"):
                title = item.findtext("title") or ""
                desc  = item.findtext("description") or ""
                link  = item.findtext("link") or ""
                pub   = item.findtext("pubDate") or ""
                text  = (title + " " + desc).lower()
                if any(k in text for k in keywords):
                    articles.append({
                        "source": name,
                        "title":  title,
                        "desc":   desc[:200],
                        "link":   link,
                        "date":   pub[:16],
                    })
        except Exception as e:
            print(f"[Press] {name} error: {e}")
    return jsonify({"ok": True, "articles": articles})


@app.route("/api/research")
def api_research():
    import requests, xml.etree.ElementTree as ET
    feeds = [
        ("CDC Newsroom",       "https://tools.cdc.gov/api/v2/resources/media/277590.rss"),
        ("WHO News",           "https://www.who.int/rss-feeds/news-english.xml"),
        ("JAMA Network",       "https://jamanetwork.com/rss/site_3/67.xml"),
        ("NIJ Research",       "https://nij.ojp.gov/rss.xml"),
        ("Lancet",             "https://www.thelancet.com/rssfeed/lancet_online.xml"),
    ]
    keywords = [
        "domestic violence","sexual assault","rape","intimate partner",
        "gender violence","femicide","trafficking","stalking","coercive control",
        "sexual abuse","child abuse","violence against women","gender based",
        "reproductive coercion","strangulation","harassment",
    ]
    articles = []
    for name, url in feeds:
        try:
            r = requests.get(url, headers={"User-Agent": "Medusa/1.2"}, timeout=8)
            root = ET.fromstring(r.content)
            for item in root.findall(".//item"):
                title = item.findtext("title") or ""
                desc  = item.findtext("description") or ""
                link  = item.findtext("link") or ""
                pub   = item.findtext("pubDate") or ""
                text  = (title + " " + desc).lower()
                if any(k in text for k in keywords):
                    articles.append({
                        "source": name,
                        "title":  title,
                        "desc":   desc[:200],
                        "link":   link,
                        "date":   pub[:16],
                    })
        except Exception as e:
            print(f"[Research] {name} error: {e}")
    return jsonify({"ok": True, "articles": articles})


@app.route("/api/international")
def api_international():
    import requests, xml.etree.ElementTree as ET
    feeds = [
        ("UN Women",           "https://www.unwomen.org/en/rss-feeds/news"),
        ("Amnesty Intl",       "https://www.amnesty.org/en/feed/"),
        ("Guardian Global",    "https://www.theguardian.com/society/gender/rss"),
        ("Reuters World",      "https://feeds.reuters.com/reuters/worldNews"),
        ("Human Rights Watch", "https://www.hrw.org/rss/world-report-chapters.xml"),
        ("BBC Gender",         "https://feeds.bbci.co.uk/news/world/rss.xml"),
    ]
    keywords = [
        "domestic violence","sexual assault","rape","femicide","trafficking",
        "violence against women","gender violence","child marriage","forced marriage",
        "honour killing","fgm","female genital","reproductive rights","abortion",
        "stalking","intimate partner","women rights","girls rights",
        "maternal","gender based violence","missing women",
    ]
    articles = []
    for name, url in feeds:
        try:
            r = requests.get(url, headers={"User-Agent": "Medusa/1.2"}, timeout=8)
            root = ET.fromstring(r.content)
            for item in root.findall(".//item"):
                title = item.findtext("title") or ""
                desc  = item.findtext("description") or ""
                link  = item.findtext("link") or ""
                pub   = item.findtext("pubDate") or ""
                text  = (title + " " + desc).lower()
                if any(k in text for k in keywords):
                    articles.append({
                        "source": name,
                        "title":  title,
                        "desc":   desc[:200],
                        "link":   link,
                        "date":   pub[:16],
                    })
        except Exception as e:
            print(f"[International] {name} error: {e}")
    return jsonify({"ok": True, "articles": articles})

@app.route("/api/status")
def api_status():
    s = _get_scanner()
    return jsonify({
        "ok":        True,
        "version":   "1.0.0",
        "cases":     get_case_count(),
        "last_scan": s.last_scan,
        "time":      datetime.now(timezone.utc).isoformat(),
    })


if __name__ == "__main__":
    app = create_app()
    port = int(os.environ.get("PORT", 5050))
    app.run(host="0.0.0.0", port=port, debug=False)


# ── 24-hour auto-scan scheduler ───────────────────────────────────────────────
def _run_scheduled_scan():
    """Run silently in background every 24 hours."""
    try:
        print(f"[Medusa] Scheduled scan starting...")
        scanner = _get_scanner()
        cases   = scanner.scan()
        saved   = 0
        for c in cases:
            from .database import save_case
            if save_case(c):
                saved += 1
        print(f"[Medusa] Scheduled scan complete. {saved} new cases saved.")

        # Auto-backup after every scan
        try:
            import json
            from datetime import datetime, timezone
            cases = get_cases(limit=50000)
            backup = {
                "timestamp": datetime.now(timezone.utc).isoformat(),
                "total": len(cases),
                "cases": cases,
            }
            with open("MEDUSA_BACKUP.json", "w") as f:
                json.dump(backup, f, default=str)
            print(f"[Medusa] Auto-backup complete. {len(cases)} cases saved.")
        except Exception as be:
            print(f"[Medusa] Backup error: {be}")

    except Exception as e:
        print(f"[Medusa] Scheduled scan error: {e}")


def start_scheduler():
    import threading, time
    from apscheduler.schedulers.background import BackgroundScheduler
    scheduler = BackgroundScheduler()
    scheduler.add_job(
        _run_scheduled_scan,
        trigger="interval",
        hours=2,
        id="medusa_scan",
        replace_existing=True,
    )
    scheduler.start()
    print("[Medusa] 6-hour scan scheduler started.")

    # Startup scan after 30 seconds
    def _startup():
        time.sleep(30)
        _run_scheduled_scan()
    threading.Thread(target=_startup, daemon=True).start()

    return scheduler
