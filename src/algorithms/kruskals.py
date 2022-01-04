from typing import Iterable, List, Tuple
from src.data_structures.disjoint_forest import DisjointForest
from dataclasses import dataclass, field
from __future__ import annotations


class Kruskals(object):
    def get_mst(self, n: int, edges: Iterable[Edge]) -> KruskalsResult:
        sorted_edges = sorted(edges, key=lambda e: e.weight)

        forest = DisjointForest
        sets = [forest.make_set(i) for i in range(n)]

        res = KruskalsResult()

        while len(sorted_edges) > 0:
            current_edge = sorted_edges.pop(0)
            source_set, target_set = sets[current_edge.source,
                                          current_edge.target]

            if not forest.are_in_same_set(source_set, target_set):
                forest.join_sets(source_set, target_set)

                res.edges.append(current_edge)
                res.sum += current_edge.weight

            # we're done and need consider no further edges
            if len(res.edges) == n - 1:
                break

        return res


@dataclass
class Edge:
    source: int
    target: int
    weight: int


@dataclass
class KruskalsResult:
    edges: List[Edge] = field(default_factory=list)
    sum: int = 0
