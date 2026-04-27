
"""
medusa_backup.py — Full case data backup for Medusa

Run from ~/medusa:
    python3 medusa_backup.py

Saves all cases to MEDUSA_BACKUP.json so they can be restored
if the database is ever wiped.
"""

import sys, json
sys.path.insert(0, "/data/data/com.termux/files/home/medusa")

from medusa.database import get_cases, get_case_count
from datetime import datetime, timezone

def backup():
    print("Backing up Medusa cases...")
    cases = get_cases(limit=50000)
    
    data = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "total": len(cases),
        "cases": cases,
    }
    
    path = "/data/data/com.termux/files/home/medusa/MEDUSA_BACKUP.json"
    with open(path, "w") as f:
        json.dump(data, f, indent=2, default=str)
    
    print(f"Done. {len(cases)} cases saved to MEDUSA_BACKUP.json")

if __name__ == "__main__":
    backup()
