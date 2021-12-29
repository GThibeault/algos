class BellmanFord(object):
    def find_shortest_path(self, origin, n, edges):
        distance = [None if i != origin else 0 for i in range(n)]
        predecessor = [None for i in range(n)]

        for i in range(n - 1):
            for source, destination, weight in edges:
                if distance[source] is None:
                    continue

                new_distance = distance[source] + weight

                if distance[destination] is None or new_distance < distance[destination]:
                    predecessor[destination] = source
                    distance[destination] = new_distance

        for source, destination, weight in edges:
            if distance[source] is None:
                continue

            new_distance = distance[source] + weight

            if new_distance < distance[destination]:
                return BellmanFordResult(True)

        paths = self.build_shortest_paths(predecessor)

        return BellmanFordResult(False, distance, paths)

    def build_shortest_paths(self, predecessor):
        paths = [[] for i in range(len(predecessor))]

        for i in range(len(predecessor)):
            p = predecessor[i]

            while p is not None:
                paths[i].insert(0, p)
                p = predecessor[p]

        return paths


class BellmanFordResult(object):
    def __init__(self, negative_loop, distances=None, paths=None):
        self.negative_loop = negative_loop
        self.distances = distances
        self.paths = paths
