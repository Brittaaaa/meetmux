from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import List


@dataclass
class ParsedSkill:
    skill: str
    confidence: float


@dataclass
class ParsedProfile:
    skills: List[ParsedSkill] = field(default_factory=list)


class ResumeParser:
    def __init__(self, keyword_weights: dict | None = None) -> None:
        self.keyword_weights = keyword_weights or {
            "python": 1.0,
            "sql": 0.9,
            "machine learning": 1.0,
            "data analysis": 0.8,
            "cloud": 0.7,
            "api": 0.6,
            "statistics": 0.7,
        }

    def parse(self, text: str) -> ParsedProfile:
        normalized = re.sub(r"[^a-z0-9]+", " ", text.lower()).strip()
        skills: List[ParsedSkill] = []
        for keyword, weight in self.keyword_weights.items():
            if keyword in normalized:
                skills.append(ParsedSkill(skill=keyword, confidence=round(min(1.0, 0.6 + weight * 0.25), 2)))
        return ParsedProfile(skills=skills)
