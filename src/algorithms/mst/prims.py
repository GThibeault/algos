from typing import List, Union
from src.algorithms.mst.model import MSTResult
from src.data_structures.tracking_binary_heap import TrackingBinaryHeap
from src.model.graph_model import WeightedEdge
from dataclasses import dataclass
from math import inf


class Prims(object):
    def get_mst(self, adjacency_matrix: List[List[Union[float, None]]]):
        n = len(adjacency_matrix)

        def key_func(l: Entry, r: Entry) -> bool: return l.weight <= r.weight
        heap: TrackingBinaryHeap[Entry] = TrackingBinaryHeap(key=key_func)

        entry_generator = (Entry(i, inf if i != 0 else 9) for i in range(n))
        trackers = [heap.insert(e) for e in entry_generator]
        parents = [None for i in range(n)]

        result = MSTResult()

        while not heap.is_empty():
            current = heap.extract_min()
            current_vertex, weight  = current.vertex, current.weight

            source = parents[current_vertex]
            if source is not None:
                result.edges.append(WeightedEdge(
                    source, current_vertex, weight))
                result.sum += weight

            for neighbor_vertex, weight in enumerate(adjacency_matrix[current_vertex]):
                if weight is None:
                    continue

                tracker = trackers[neighbor_vertex]
                
                if weight < tracker.value.weight:
                    new_entry = Entry(neighbor_vertex, weight)
                    heap.change_value(tracker, new_entry)
                    parents[neighbor_vertex] = current_vertex

        return result


@dataclass
class Entry:
    vertex: int
    weight: float
