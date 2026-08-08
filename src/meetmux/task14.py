from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List


@dataclass
class OntologyNode:
    name: str
    type: str
    attributes: Dict[str, object] = field(default_factory=dict)


class OntologyBuilder:
    def __init__(self) -> None:
        self.nodes: List[OntologyNode] = []

    def ingest_skills(self, skills: List[str]) -> List[OntologyNode]:
        self.nodes = [OntologyNode(name=skill, type="skill") for skill in skills]
        return self.nodes
