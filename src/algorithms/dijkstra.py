from math import dist, inf
from src.data_structures.tracking_binary_heap import TrackingBinaryHeap


class Dijkstra(object):
    def find_shortest_path(self, origin, n, adjacency):
        distance = [inf if i != origin else 0 for i in range(n)]
        predecessor = [None for i in range(n)]

        trackers = []

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

        paths = self.build_shortest_paths(predecessor)

        return DijkstraResult(distance, paths)

    # inefficient but simple
    def build_shortest_paths(self, predecessor):
        paths = [[] for i in range(len(predecessor))]

        for i in range(len(predecessor)):
            p = predecessor[i]

            while p is not None:
                paths[i].insert(0, p)
                p = predecessor[p]

        return paths


class Entry(object):
    def __init__(self, vertex, weight):
        self.vertex = vertex
        self.weight = weight


class DijkstraResult(object):
    def __init__(self, distances, paths):
        self.distances = distances
        self.paths = paths
