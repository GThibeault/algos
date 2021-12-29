from src.algorithms.dijkstra import Dijkstra

import unittest


class TestDijkstra(unittest.TestCase):
    def test_really_simple_paths(self):
        dijkstra = Dijkstra()

        n = 3
        adjacency = [[(1, 1), (2, 5)], [(2, 1)], []]

        result = dijkstra.find_shortest_path(0, n, adjacency)

        self.assertEqual(result.distances, [0, 1, 2])
        self.assertEqual(result.paths, [[], [0], [0, 1]])
