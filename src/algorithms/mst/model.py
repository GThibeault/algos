from dataclasses import dataclass, field
from typing import List
from src.model.graph_model import WeightedEdge


@dataclass
class MSTResult:
    edges: List[WeightedEdge] = field(default_factory=list)
    sum: int = 0
