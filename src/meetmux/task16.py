from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List


@dataclass
class RecommendationCandidate:
    candidate_id: str
    score: float
    reasons: List[str]


class RecommendationEngineV1:
    def __init__(self) -> None:
        self.name = "recommendation-v1"

    def design(self, candidates: List[Dict[str, object]]) -> List[RecommendationCandidate]:
        ranked = []
        for candidate in candidates:
            score = 0.5 + min(0.4, float(candidate.get("match_score", 0.0)) * 0.4)
            reasons = [
                f"match:{round(score, 2)}",
                candidate.get("strength", "strong fit"),
            ]
            ranked.append(RecommendationCandidate(candidate_id=str(candidate.get("candidate_id", "unknown")), score=round(score, 2), reasons=reasons))
        return sorted(ranked, key=lambda item: item.score, reverse=True)
