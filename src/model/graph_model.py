from dataclasses import dataclass


@dataclass
class WeightedDirectedEdge:
    source: int
    target: int
    weight: int
