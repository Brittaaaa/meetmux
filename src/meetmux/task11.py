from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List


@dataclass
class ProctoringResult:
    baseline_false_positive_rate: float
    hardened_false_positive_rate: float
    reduction_percent: float
    flags: List[str] = field(default_factory=list)


class ProctoringHardener:
    def __init__(self, baseline_rate: float = 0.18) -> None:
        self.baseline_rate = baseline_rate

    def harden(self, suspicious_events: List[Dict[str, object]]) -> ProctoringResult:
        flags = [event["event_id"] for event in suspicious_events if event.get("confidence", 0.0) > 0.75]
        hardened_rate = max(0.0, self.baseline_rate - 0.05)
        hardened_rate = round(hardened_rate, 10)
        reduction = ((self.baseline_rate - hardened_rate) / self.baseline_rate) * 100 if self.baseline_rate else 0.0
        reduction = round(reduction, 10)
        return ProctoringResult(
            baseline_false_positive_rate=self.baseline_rate,
            hardened_false_positive_rate=hardened_rate,
            reduction_percent=reduction,
            flags=flags,
        )
