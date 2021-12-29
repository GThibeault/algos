from src.algorithms.bellman_ford import BellmanFord

import unittest


class TestBellmanFord(unittest.TestCase):
    def test_really_simple_paths(self):
        bellman = BellmanFord()

        n = 3
        edges = [(0, 1, 1), (0, 2, 5), (1, 2, 1)]

        result = bellman.find_shortest_path(0, n, edges)

        self.assertFalse(result.negative_loop)
        self.assertEqual(result.distances, [0, 1, 2])
        self.assertEqual(result.paths, [[], [0], [0, 1]])
