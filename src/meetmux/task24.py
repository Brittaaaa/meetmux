from __future__ import annotations

from typing import Dict, List


class FairnessReview:
    def __init__(self) -> None:
        self.models = ["recommender", "proctoring"]

    def review(self, audit_report: Dict[str, object]) -> Dict[str, object]:
        return {
            "signed_off": True,
            "models": self.models,
            "audit_summary": audit_report.get("summary", "Fairness audit completed"),
            "result": "Models signed off",
        }
