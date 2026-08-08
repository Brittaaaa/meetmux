from __future__ import annotations

from typing import Dict, List


class DriftMonitor:
    def __init__(self, threshold: float = 0.15) -> None:
        self.threshold = threshold

    def monitor(self, baseline_metrics: List[Dict[str, object]], current_metrics: List[Dict[str, object]]) -> Dict[str, object]:
        drift_scores = []
        for baseline, current in zip(baseline_metrics, current_metrics):
            drift_score = abs(float(current.get("score", 0.0)) - float(baseline.get("score", 0.0)))
            drift_scores.append(drift_score)
        max_drift = max(drift_scores, default=0.0)
        retrain = max_drift > self.threshold
        return {
            "drift_detected": retrain,
            "max_drift": round(max_drift, 2),
            "threshold": self.threshold,
            "summary": "Retraining recommended" if retrain else "Drift within tolerance",
        }
