from dataclasses import dataclass


@dataclass
class Edge:
    source: int
    target: int
    weight: int
