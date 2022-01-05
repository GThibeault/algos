from dataclasses import dataclass, field
from typing import List, Tuple


@dataclass
class ShortestPathResult:
    distances: List[float] = field(default_factory=list)
    paths: List[Tuple[int, int]] = field(default_factory=list)
    negative_loop: bool = False