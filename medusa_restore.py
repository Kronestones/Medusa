
"""
medusa_restore.py — Restore Medusa from full backup

Run from ~/medusa:
    python3 medusa_restore.py
"""

import sys, json
sys.path.insert(0, "/data/data/com.termux/files/home/medusa")

from medusa.database import init_db, save_case

def restore():
    path = "/data/data/com.termux/files/home/medusa/MEDUSA_BACKUP.json"
    with open(path) as f:
        data = json.load(f)
    
    cases = data.get("cases", [])
    print(f"Restoring {len(cases)} cases from {data.get('timestamp')}...")
    
    init_db()
    saved = 0
    for case in cases:
        if save_case(case):
            saved += 1
    
    print(f"Done. {saved} cases restored.")

if __name__ == "__main__":
    restore()
