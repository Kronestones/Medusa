"""
watchdog.py — Medusa Source Health Monitor

Tracks which sources are returning records and which are silent.
Flags dead sources after 3 consecutive zero-return scans.
Inspired by River (Deep Roots watchdog) and Alice v4 MetaAnalyzer.

Built by Krone. 
"""

import json
import os
import time
from collections import defaultdict
from datetime import datetime, timezone

WATCHDOG_FILE     = "medusa_watchdog.json"
DEAD_THRESHOLD    = 3   # consecutive zeros = dead source
WARNING_THRESHOLD = 2   # consecutive zeros = warning


class SourceWatchdog:
    """
    Monitors source health across scans.
    Tracks consecutive zero returns per source.
    Flags dead sources and recommends action.
    """

    def __init__(self, filepath=WATCHDOG_FILE):
        self._filepath    = filepath
        self._consecutive = defaultdict(int)   # source -> consecutive zeros
        self._last_count  = defaultdict(int)   # source -> last record count
        self._total_scans = 0
        self._load()

    def record_scan(self, source_results: dict):
        """
        source_results: dict of source_name -> record count
        Call after every scan.
        """
        self._total_scans += 1
        for source, count in source_results.items():
            self._last_count[source] = count
            if count == 0:
                self._consecutive[source] += 1
            else:
                self._consecutive[source] = 0
        self._save()

    def health_report(self) -> str:
        lines = [f"[Watchdog] Source health after {self._total_scans} scans:"]
        dead    = []
        warning = []
        healthy = []

        for source, zeros in self._consecutive.items():
            last = self._last_count.get(source, 0)
            if zeros >= DEAD_THRESHOLD:
                dead.append(f"  ❌ DEAD   {source} — {zeros} consecutive zeros")
            elif zeros >= WARNING_THRESHOLD:
                warning.append(f"  ⚠️  WARN   {source} — {zeros} consecutive zeros")
            else:
                healthy.append(f"  ✓  OK     {source} — last returned {last}")

        for line in dead + warning + healthy:
            lines.append(line)

        if dead:
            lines.append(f"  → {len(dead)} dead sources — fix feeds or remove from scanner")
        if not dead and not warning:
            lines.append("  → All sources healthy")

        return "\n".join(lines)

    def dead_sources(self) -> list:
        return [s for s, z in self._consecutive.items() if z >= DEAD_THRESHOLD]

    def _save(self):
        try:
            with open(self._filepath, "w") as f:
                json.dump({
                    "total_scans":  self._total_scans,
                    "consecutive":  dict(self._consecutive),
                    "last_count":   dict(self._last_count),
                    "updated":      datetime.now(timezone.utc).isoformat(),
                }, f, indent=2)
        except Exception as e:
            print(f"[Watchdog] Save error: {e}")

    def _load(self):
        if not os.path.exists(self._filepath):
            return
        try:
            with open(self._filepath) as f:
                data = json.load(f)
            self._total_scans = data.get("total_scans", 0)
            self._consecutive = defaultdict(int, data.get("consecutive", {}))
            self._last_count  = defaultdict(int, data.get("last_count", {}))
            print(f"[Watchdog] Loaded. {self._total_scans} scans tracked.")
        except Exception as e:
            print(f"[Watchdog] Load error: {e}")
