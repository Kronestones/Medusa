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
    except Exception as e:
        print(f"[Medusa] Scheduled scan error: {e}")


def start_scheduler():
    import threading, time
    from apscheduler.schedulers.background import BackgroundScheduler
    scheduler = BackgroundScheduler()
    scheduler.add_job(
        _run_scheduled_scan,
        trigger="interval",
        hours=6,
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
