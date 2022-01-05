from dataclasses import dataclass, field
from typing import List
from src.model.graph_model import Edge


@dataclass
class MSTResult:
    edges: List[Edge] = field(default_factory=list)
    sum: int = 0
