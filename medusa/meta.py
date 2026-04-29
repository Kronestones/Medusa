"""
meta.py — Medusa Self-Awareness Engine
Adapted from Alice v4 MetaAnalyzer and FamilyBias architecture.

Alice detects when her geometry is settling or repeating.
Medusa detects when her scanning is settling or missing coverage.

Alice concepts → Medusa concepts:
  family       → violence_type
  attractor    → over-represented type (child_abuse dominating)
  novelty      → new cases saved / total found
  settling     → yield declining, same cases returned
  FamilyBias   → QueryBias — nudge toward underrepresented types

Built by Krone. Adapted from Alice v4.
"""

import json, time, hashlib
from collections import Counter
from dataclasses import dataclass
from datetime import datetime, timezone

META_WINDOW         = 10
ATTRACTOR_THRESHOLD = 0.35
SETTLING_THRESHOLD  = 0.05
SOURCE_DOMINANCE    = 0.70

ALL_TYPES = [
    "homicide", "attempted_murder", "sexual_assault", "rape",
    "domestic_violence", "stalking", "harassment", "trafficking",
    "child_abuse", "assault", "coercive_control",
]

@dataclass
class ScanRecord:
    timestamp  : float
    found      : int
    saved      : int
    by_type    : dict
    by_source  : dict
    scan_id    : str

    @property
    def save_rate(self):
        return self.saved / self.found if self.found > 0 else 0.0

    def to_dict(self):
        return self.__dict__.copy()

    @classmethod
    def from_dict(cls, d):
        return cls(**d)

    @classmethod
    def build(cls, found, saved, cases):
        by_type   = dict(Counter(c.get("violence_type","unknown") for c in cases))
        by_source = dict(Counter(c.get("source_name","unknown") for c in cases))
        ts        = time.time()
        scan_id   = hashlib.sha1(f"{ts}:{saved}".encode()).hexdigest()[:12]
        return cls(timestamp=ts, found=found, saved=saved,
                   by_type=by_type, by_source=by_source, scan_id=scan_id)


@dataclass
class QueryBias:
    deprioritize : list
    prioritize   : list
    strength     : float
    reason       : str

    @classmethod
    def neutral(cls):
        return cls([], [], 0.0, "balanced")


@dataclass
class MetaReport:
    window_size      : int
    mean_save_rate   : float
    save_trend       : str
    attractors       : list
    source_dominated : bool
    settling         : bool
    recommendations  : list
    query_bias       : QueryBias
    timestamp        : float

    def summary(self):
        lines = [
            f"[Medusa Meta] {datetime.fromtimestamp(self.timestamp, tz=timezone.utc).isoformat()}",
            f"  Window: {self.window_size} scans | Yield: {self.mean_save_rate:.1%} | Trend: {self.save_trend}",
            f"  Settling: {self.settling} | Attractors: {[f"{t}({f:.0%})" for t,f in self.attractors] or None}",
        ]
        for r in self.recommendations:
            lines.append(f"  → {r}")
        return "\n".join(lines)


class MedusaMetaAnalyzer:

    def analyze(self, history):
        window = history[-META_WINDOW:] if len(history) > META_WINDOW else history
        n      = len(window)

        if n == 0:
            return MetaReport(0, 0.0, "unknown", [], False, False,
                              ["Not enough history yet"], QueryBias.neutral(), time.time())

        rates     = [r.save_rate for r in window]
        mean_rate = sum(rates) / n
        settling  = mean_rate < SETTLING_THRESHOLD

        if n >= 6:
            mid      = n // 2
            first_h  = sum(rates[:mid]) / mid
            second_h = sum(rates[mid:]) / (n - mid)
            delta    = second_h - first_h
            trend    = "rising" if delta > 0.03 else "falling" if delta < -0.03 else "stable"
        else:
            trend = "stable"

        type_totals   = Counter()
        source_totals = Counter()
        total_cases   = 0

        for rec in window:
            for vtype, count in rec.by_type.items():
                type_totals[vtype] += count
                total_cases        += count
            for src, count in rec.by_source.items():
                source_totals[src] += count

        attractors = [
            (vtype, count / total_cases)
            for vtype, count in type_totals.most_common()
            if total_cases > 0 and count / total_cases > ATTRACTOR_THRESHOLD
        ]

        source_dominated = bool(source_totals and
            source_totals.most_common(1)[0][1] / max(sum(source_totals.values()), 1) > SOURCE_DOMINANCE)

        missing   = [t for t in ALL_TYPES if t not in type_totals]
        low_types = [t for t in ALL_TYPES
                     if t in type_totals and type_totals[t] / max(total_cases,1) < 0.03]
        over_types = [vtype for vtype, freq in attractors]
        prioritize = (missing + low_types)[:4]

        bias_strength = 0.7 if settling else (0.4 if attractors else 0.0)
        bias_reason   = (f"Under-represented: {prioritize}" if prioritize
                         else f"Attractor: {over_types[0]}" if over_types else "balanced")

        query_bias = QueryBias(over_types, prioritize, bias_strength, bias_reason)

        recs = []
        if settling:
            recs.append("Save rate low — rotate queries or add sources")
        if attractors:
            recs.append(f"Attractor {attractors[0][0]} at {attractors[0][1]:.0%} — deprioritize")
        if source_dominated:
            recs.append("Source concentration — add new sources")
        if missing:
            recs.append(f"Missing types entirely: {missing[:3]}")
        if trend == "falling" and not settling:
            recs.append("Yield declining — add AG feeds or Wikipedia sources")
        if not recs:
            recs.append("Scan health good")

        return MetaReport(n, mean_rate, trend, attractors,
                          source_dominated, settling, recs, query_bias, time.time())


class ScanHistory:
    def __init__(self, filepath="medusa_scan_history.jsonl"):
        self._filepath = filepath
        self._history  = []
        self._analyzer = MedusaMetaAnalyzer()
        self._load()

    def record(self, scan):
        self._history.append(scan)
        self._append(scan)

    def latest_bias(self):
        if not self._history:
            return QueryBias.neutral()
        return self._analyzer.analyze(self._history).query_bias

    def analyze(self):
        return self._analyzer.analyze(self._history)

    def report(self):
        return self.analyze().summary()

    def _append(self, scan):
        try:
            with open(self._filepath, "a") as f:
                f.write(json.dumps(scan.to_dict()) + "\n")
        except Exception as e:
            print(f"[Meta] Write error: {e}")

    def _load(self):
        import os
        if not os.path.exists(self._filepath):
            return
        try:
            with open(self._filepath) as f:
                for line in f:
                    line = line.strip()
                    if line:
                        self._history.append(ScanRecord.from_dict(json.loads(line)))
            print(f"[Meta] {len(self._history)} scan records loaded.")
        except Exception as e:
            print(f"[Meta] Load error: {e}")
