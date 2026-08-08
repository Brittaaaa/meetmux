from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List


@dataclass
class RecommendationResult:
    candidate_id: str
    score: float
    explanation: str


class RecommendationEngine:
    def __init__(self) -> None:
        self.version = "v1"

    def recommend(self, candidate_profiles: List[Dict[str, object]]) -> List[RecommendationResult]:
        results = []
        for profile in candidate_profiles:
            score = 0.5 + float(profile.get("match_score", 0.0)) * 0.4
            explanation = f"Strong fit for {profile.get('role', 'role')} with {profile.get('strength', 'relevant skills')}"
            results.append(RecommendationResult(candidate_id=str(profile.get("candidate_id", "unknown")), score=round(score, 2), explanation=explanation))
        return sorted(results, key=lambda item: item.score, reverse=True)
