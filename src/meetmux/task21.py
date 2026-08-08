from __future__ import annotations

from typing import Dict, List


class FairnessAudit:
    def __init__(self) -> None:
        self.groups = ["group_a", "group_b"]

    def audit(self, outcomes: List[Dict[str, object]]) -> Dict[str, object]:
        by_group = {}
        for group in self.groups:
            group_outcomes = [item for item in outcomes if item.get("group") == group]
            positive_rate = round(sum(1 for item in group_outcomes if item.get("accepted", False)) / max(1, len(group_outcomes)), 2) if group_outcomes else 0.0
            by_group[group] = positive_rate
        return {
            "audit_started": True,
            "group_rates": by_group,
            "summary": "Fairness audit underway",
        }
