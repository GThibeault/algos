from dataclasses import dataclass
from math import inf
from typing import List, Tuple, Union
from src.algorithms.shortest_path.model import ShortestPathResult
from src.algorithms.shortest_path.path_builder import PathBuilder
from src.data_structures.tracking_binary_heap import Tracker, TrackingBinaryHeap


class Dijkstra:
    def find_shortest_path(self, origin: int, n: int, adjacency: List[List[Tuple[int, float]]]) -> ShortestPathResult:
        distance: List[float] = [inf if i != origin else 0 for i in range(n)]
        predecessor: List[Union[int, None]] = [None for i in range(n)]

        trackers: List[Tracker[Entry]] = []

        def key_func(l, r): return l.weight <= r.weight
        heap = TrackingBinaryHeap(key=key_func)

        for i in range(n):
            weight = inf if i != origin else 0
            entry = Entry(i, weight)

            trackers.append(heap.insert(entry))

        while not heap.is_empty():
            source_entry = heap.extract_min()
            source = source_entry.vertex

            for destination, weight in adjacency[source]:
                new_distance = distance[source] + weight

                if new_distance < distance[destination]:
                    predecessor[destination] = source
                    distance[destination] = new_distance

                    new_entry = Entry(destination, new_distance)
                    heap.change_value(trackers[destination], new_entry)

        path_builder = PathBuilder()
        paths = path_builder.build_shortest_paths(predecessor)

        return ShortestPathResult(distance, paths)


@dataclass
class Entry:
    vertex: int
    weight: float