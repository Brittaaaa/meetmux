from __future__ import annotations

from typing import Dict, List


class ExplainabilityLayer:
    def __init__(self) -> None:
        self.template = "Recommended because it aligns with {skill} and has strong evidence in {evidence}."

    def explain(self, recommendations: List[Dict[str, object]]) -> List[Dict[str, object]]:
        explained = []
        for recommendation in recommendations:
            skill = recommendation.get("skill", "core requirements")
            evidence = recommendation.get("evidence", "historical placement data")
            explained.append({
                **recommendation,
                "explanation": self.template.format(skill=skill, evidence=evidence),
            })
        return explained
