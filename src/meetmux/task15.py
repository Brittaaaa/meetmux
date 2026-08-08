from __future__ import annotations

from typing import Dict, List


class TrustLayer:
    def __init__(self) -> None:
        self.signoff_checks = ["proctoring", "parsing", "ontology"]

    def summarize(self, checks: List[str] | None = None) -> Dict[str, object]:
        active_checks = checks or self.signoff_checks
        return {
            "signed_off": all(check in active_checks for check in self.signoff_checks),
            "checks": active_checks,
            "summary": "AI trust features signed off" if all(check in active_checks for check in self.signoff_checks) else "AI trust features pending",
        }
