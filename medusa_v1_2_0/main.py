#!/usr/bin/env python3
"""
main.py — Medusa

Every act of male violence against women, documented.
All public records. All sources cited.

Usage:
    python main.py              # Run web server
    python main.py --scan       # Scan public records now
    python main.py --status     # Show counts
    python main.py --export FILE

Built on Project Themis architecture.
Founded by Krone the Architect · Powers Tracey Lynn · 2026
"""

import argparse, sys, os

parser = argparse.ArgumentParser(description="Medusa — Every act documented.")
parser.add_argument("--scan",    action="store_true")
parser.add_argument("--status",  action="store_true")
parser.add_argument("--export",  metavar="FILE")
parser.add_argument("--version", action="store_true")
args = parser.parse_args()

VERSION = "1.2.0"

if args.version:
    print(f"Medusa v{VERSION} — Built on Project Themis")
    sys.exit(0)

if args.scan:
    from medusa.scanner import MedusaScanner
    from medusa.database import init_db, save_case
    try: init_db()
    except Exception as e: print(f"  [Medusa] DB warning: {e}")
    scanner = MedusaScanner()
    print("  [Medusa] Scanning all public records…\n")
    cases = scanner.scan()
    saved = 0
    for c in cases:
        if save_case(c):
            saved += 1
            pf = " [OFFICIAL]" if c.get("is_public_figure") else ""
            print(f"  + [{c['violence_type'].upper()}{pf}] {c['city']}, {c['state']} — {c['case_id']}")
    print(f"\n  [Medusa] {len(cases)} found, {saved} new cases saved.\n")
    sys.exit(0)

if args.status:
    from medusa.database import get_stats
    try:
        s = get_stats()
        print()
        print("  ╔═══════════════════════════════════════════════╗")
        print("  ║   M E D U S A   —   Status                  ║")
        print("  ╚═══════════════════════════════════════════════╝")
        print(f"\n  Total cases:      {s['total']}")
        print(f"  Public figures:   {s['public_figures']}")
        print()
        for vt, n in s.get('by_type', {}).items():
            if n: print(f"  {vt:<24} {n}")
        print()
    except Exception as e:
        print(f"  Error: {e}")
    sys.exit(0)

if args.export:
    from medusa.database import get_cases
    import json
    cases = get_cases(limit=100000)
    with open(args.export, "w") as f:
        json.dump(cases, f, indent=2, default=str)
    print(f"\n  ✓ {len(cases)} cases exported to {args.export}\n")
    sys.exit(0)

# ── Web server ────────────────────────────────────────────────────────────────

from medusa.web import create_app

print()
print("  ╔═══════════════════════════════════════════════════════╗")
print("  ║   M E D U S A   —   Every Act Documented.           ║")
print(f"  ║   v{VERSION}  ·   Free public sources · No API cost          ║")
print("  ╚═══════════════════════════════════════════════════════╝")
print()

app  = create_app()
port = int(os.environ.get("PORT", 5050))
print(f"  Running on http://0.0.0.0:{port}\n")
app.run(host="0.0.0.0", port=port, debug=False)
