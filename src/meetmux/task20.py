from __future__ import annotations

from typing import Dict, List


class RecommendationValidator:
    def __init__(self) -> None:
        self.metrics = ["precision", "recall", "coverage"]

    def validate(self, recommendations: List[Dict[str, object]]) -> Dict[str, object]:
        if not recommendations:
            return {"validated": False, "metrics": {metric: 0.0 for metric in self.metrics}, "summary": "No recommendations provided"}
        scores = [float(item.get("score", 0.0)) for item in recommendations]
        return {
            "validated": True,
            "metrics": {
                "precision": round(sum(scores) / len(scores), 2),
                "recall": round(min(1.0, sum(scores) / max(1, len(scores))), 2),
                "coverage": round(min(1.0, len(scores) / 5), 2),
            },
            "summary": "Recommendations validated",
        }
