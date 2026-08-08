from __future__ import annotations

from typing import Dict, List


class ProductionMonitor:
    def __init__(self, alert_threshold: float = 0.2) -> None:
        self.alert_threshold = alert_threshold

    def monitor(self, metrics: List[Dict[str, object]]) -> Dict[str, object]:
        if not metrics:
            return {"status": "no-data", "alert": False, "summary": "No production metrics received"}
        latest = metrics[-1]
        score = float(latest.get("score", 0.0))
        alert = score < self.alert_threshold
        return {
            "status": "alert" if alert else "healthy",
            "alert": alert,
            "score": round(score, 2),
            "summary": "Production monitoring active",
        }
