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
    return app


@app.route("/")
def index():
    return render_template("map.html")


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
    try:
        scanner   = _get_scanner()
        new_cases = scanner.scan()
        saved = sum(1 for c in new_cases if save_case(c))
        return jsonify({
            "ok":      True,
            "found":   len(new_cases),
            "saved":   saved,
            "message": f"Scan complete. {saved} new cases documented.",
        })
    except Exception as e:
        return jsonify({"ok": False, "error": str(e)}), 500


@app.route("/api/status")
def api_status():
    s = _get_scanner()
    return jsonify({
        "ok":        True,
        "version":   "1.1.0",
        "cases":     get_case_count(),
        "last_scan": s.last_scan,
        "time":      datetime.now(timezone.utc).isoformat(),
    })


if __name__ == "__main__":
    app = create_app()
    port = int(os.environ.get("PORT", 5050))
    app.run(host="0.0.0.0", port=port, debug=False)
