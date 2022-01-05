from typing import Iterable
from src.algorithms.mst.model import MSTResult
from src.data_structures.disjoint_forest import DisjointForest
from src.model.graph_model import Edge


class Kruskals(object):
    def get_mst(self, n: int, edges: Iterable[Edge]) -> MSTResult:
        sorted_edges = sorted(edges, key=lambda e: e.weight)

        forest = DisjointForest()
        sets = [forest.make_set(i) for i in range(n)]

        res = MSTResult()

        while len(sorted_edges) > 0:
            current_edge = sorted_edges.pop(0)
            source_set, target_set = sets[current_edge.source], sets[current_edge.target]

            if not forest.are_in_same_set(source_set, target_set):
                forest.join_sets(source_set, target_set)

                res.edges.append(current_edge)
                res.sum += current_edge.weight

            # we're done and need consider no further edges
            if len(res.edges) == n - 1:
                break

        return res
