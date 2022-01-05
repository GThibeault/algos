from dataclasses import dataclass


@dataclass
class WeightedEdge:
    vertex_1: int
    vertex_2: int
    weight: int
