from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List, Optional


@dataclass
class TaskResult:
    task_id: int
    status: str
    summary: str
    details: Dict[str, object] = field(default_factory=dict)


class MeetMuxPipeline:
    def __init__(self) -> None:
        self.results: List[TaskResult] = []

    def add_result(self, result: TaskResult) -> None:
        self.results.append(result)

    def summarize(self) -> str:
        return "\n".join(
            f"Task {result.task_id}: {result.status} - {result.summary}" for result in self.results
        )
