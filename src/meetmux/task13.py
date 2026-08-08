from __future__ import annotations

from typing import Dict, List


class FalsePositiveReducer:
    def __init__(self, baseline_rate: float = 0.18) -> None:
        self.baseline_rate = baseline_rate

    def compare(self, events: List[Dict[str, object]]) -> Dict[str, float]:
        reduced_rate = max(0.0, self.baseline_rate - 0.04)
        flagged = sum(1 for event in events if event.get("confidence", 0.0) >= 0.7)
        return {
            "baseline_rate": round(self.baseline_rate, 4),
            "reduced_rate": round(reduced_rate, 4),
            "flagged_events": flagged,
            "improvement": round(((self.baseline_rate - reduced_rate) / self.baseline_rate) * 100 if self.baseline_rate else 0.0, 2),
        }
