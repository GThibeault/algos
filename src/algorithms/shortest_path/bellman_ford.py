from math import inf
from src.algorithms.shortest_path.path_builder import PathBuilder
from src.algorithms.shortest_path.model import ShortestPathResult
from src.model.graph_model import WeightedEdge


class BellmanFord(object):
    def find_shortest_path(self, origin: int, n: int, edges: WeightedEdge) -> ShortestPathResult:
        distance = [inf if i != origin else 0 for i in range(n)]
        predecessor = [None for i in range(n)]

        for _ in range(n - 1):
            for source, destination, weight in edges:
                new_distance = distance[source] + weight

                if new_distance < distance[destination]:
                    predecessor[destination] = source
                    distance[destination] = new_distance

        for source, destination, weight in edges:
            new_distance = distance[source] + weight

            if new_distance < distance[destination]:
                return ShortestPathResult(negative_loop=True)

        path_builder = PathBuilder()
        paths = path_builder.build_shortest_paths(predecessor)

        return ShortestPathResult(distance, paths)