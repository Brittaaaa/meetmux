from __future__ import annotations

from typing import Dict, List


class WeakItemFlagger:
    def __init__(self, threshold: float = 0.4) -> None:
        self.threshold = threshold

    def flag(self, items: List[Dict[str, object]]) -> List[Dict[str, object]]:
        flagged = []
        for item in items:
            quality_score = float(item.get("quality_score", 0.0))
            if quality_score < self.threshold:
                flagged.append({**item, "flagged": True, "reason": "quality below threshold"})
            else:
                flagged.append({**item, "flagged": False, "reason": "acceptable quality"})
        return flagged
