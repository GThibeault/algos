from src.algorithms.mst.prims import Prims
import unittest

from src.model.graph_model import WeightedEdge


class TestPrims(unittest.TestCase):
    def test_really_simple_graph(self):
        prims = Prims()

        graph = [[None, 2, None, 1], [2, None, None, 2],
                 [None, None, None, 3], [1, 2, 3, None]]

        result = prims.get_mst(graph)

        self.assertEqual(result.sum, 6)

    def test_really_simple_graph_result(self):
        prims = Prims()

        graph = [[None, 2, None, 1], [2, None, None, 2],
                 [None, None, None, 3], [1, None, 3, None]]

        result = prims.get_mst(graph)

        self.assertIn(WeightedEdge(0, 1, 2), result.edges)
        self.assertIn(WeightedEdge(0, 3, 1), result.edges)
        self.assertIn(WeightedEdge(3, 2, 3), result.edges)

    def test_simple_graph(self):
        prims = Prims()

        graph = [[None, 2, None, 1, 5], [2, None, None, 2, None],
                 [None, None, None, 3, 2], [1, 2, 3, None, 3], [5, None, 2, 3, None]]

        result = prims.get_mst(graph)

        self.assertEqual(result.sum, 8)

    def test_complete_graph(self):
        prims = Prims()

        n = 15
        graph = [
            [i + 1 for i in range(j)] for j in range(n)]

        for i in range(n):
            graph[i].append(None)

            for j in range(len(graph[i]), n):
                graph[i].append(graph[j][i])

        result = prims.get_mst(graph)

        self.assertEqual(result.sum, 14)

    def test_weird_complete_graph(self):
        prims = Prims()

        n = 15
        graph = [
            [i + j + 1 for i in range(j)] for j in range(n)]

        for i in range(n):
            graph[i].append(None)

            for j in range(len(graph[i]), n):
                graph[i].append(graph[j][i])

        result = prims.get_mst(graph)

        expected_sum = sum(range(2, 16))
        self.assertEqual(expected_sum, result.sum)
