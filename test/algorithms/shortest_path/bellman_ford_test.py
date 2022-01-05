from src.algorithms.shortest_path.bellman_ford import BellmanFord

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

    def test_cormens_graph(self):
        bellman = BellmanFord()

        n = 5
        edges = [(0, 1, 6), (0, 2, 7), (1, 2, 8), (1, 3, 5),
                 (1, 4, -4), (2, 3, -3), (2, 4, 9), (3, 1, -2), (4, 0, 2), (4, 3, 7)]

        result = bellman.find_shortest_path(0, n, edges)

        self.assertFalse(result.negative_loop)
        self.assertEqual(result.distances, [0, 2, 7, 4, -2])
        self.assertEqual(
            result.paths, [[], [0, 2, 3], [0], [0, 2], [0, 2, 3, 1]])

    def test_cormens_with_negative_loop(self):
        bellman = BellmanFord()

        n = 5
        edges = [(0, 1, 6), (0, 2, 7), (1, 2, 8), (1, 3, 5),
                 (1, 4, -4), (2, 3, -3), (2, 4, 9), (3, 1, -2), (4, 0, -5), (4, 3, 7)]

        result = bellman.find_shortest_path(0, n, edges)

        self.assertTrue(result.negative_loop)
