from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List


@dataclass
class ModelRecord:
    name: str
    version: str
    status: str = "registered"


@dataclass
class FeatureSnapshot:
    name: str
    values: List[float] = field(default_factory=list)


class MLOpsFoundation:
    def __init__(self) -> None:
        self.models: List[ModelRecord] = []
        self.features: List[FeatureSnapshot] = []

    def register_model(self, name: str, version: str) -> ModelRecord:
        record = ModelRecord(name=name, version=version)
        self.models.append(record)
        return record

    def snapshot_features(self, name: str, values: List[float]) -> FeatureSnapshot:
        snapshot = FeatureSnapshot(name=name, values=values)
        self.features.append(snapshot)
        return snapshot
