from src.algorithms.shortest_path.dijkstra import Dijkstra

import unittest


class TestDijkstra(unittest.TestCase):
    def test_really_simple_paths(self):
        dijkstra = Dijkstra()

        n = 3
        adjacency = [[(1, 1), (2, 5)], [(2, 1)], []]

        result = dijkstra.find_shortest_path(0, n, adjacency)

        self.assertEqual(result.distances, [0, 1, 2])
        self.assertEqual(result.paths, [[], [0], [0, 1]])

    def test_cormens_graph(self):
        dijkstra = Dijkstra()

        n = 5
        adjacency = [[(1, 10), (2, 5)], [(2, 2), (3, 1)],
                     [(1, 3), (3, 9), (4, 2)], [(4, 4)], [(0, 7), (3, 6)]]

        result = dijkstra.find_shortest_path(0, n, adjacency)

        self.assertEqual(result.distances, [0, 8, 5, 9, 7])
        self.assertEqual(
            result.paths, [[], [0, 2], [0], [0, 2, 1], [0, 2]])

    def test_cormens_graph_with_extra_vertex(self):
        dijkstra = Dijkstra()

        n = 6
        adjacency = [[(1, 10), (2, 5), (5, 15)], [(2, 2), (3, 1)],
                     [(1, 3), (3, 9), (4, 2)], [(4, 4), (5, 1)], [(0, 7), (3, 6)], []]

        result = dijkstra.find_shortest_path(0, n, adjacency)

        self.assertEqual(result.distances, [0, 8, 5, 9, 7, 10])
        self.assertEqual(
            result.paths, [[], [0, 2], [0], [0, 2, 1], [0, 2], [0, 2, 1, 3]])
