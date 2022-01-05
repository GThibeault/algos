from dataclasses import dataclass, field
from typing import List
from src.model.graph_model import WeightedDirectedEdge


@dataclass
class MSTResult:
    edges: List[WeightedDirectedEdge] = field(default_factory=list)
    sum: int = 0
