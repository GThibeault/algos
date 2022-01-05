from typing import Iterable
from src.algorithms.mst.model import MSTResult
from src.data_structures.disjoint_forest import DisjointForest
from src.model.graph_model import WeightedDirectedEdge


class Kruskals(object):
    def get_mst(self, n: int, edges: Iterable[WeightedDirectedEdge]) -> MSTResult:
        sorted_edges = sorted(edges, key=lambda e: e.weight)

        forest = DisjointForest()
        sets = [forest.make_set(i) for i in range(n)]

        res = MSTResult()

        for current_edge in sorted_edges:
            source_set, target_set = sets[current_edge.source], sets[current_edge.target]

            if not forest.are_in_same_set(source_set, target_set):
                forest.join_sets(source_set, target_set)

                res.edges.append(current_edge)
                res.sum += current_edge.weight

            # we're done and need consider no further edges
            if len(res.edges) == n - 1:
                break

        return res
