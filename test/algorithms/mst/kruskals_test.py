from src.algorithms.mst.kruskals import Kruskals, Edge

import unittest


class TestKruskals(unittest.TestCase):
    def test_really_simple_graph(self):
        kruskals = Kruskals()

        graph = [[None, 2, None, 1], [2, None, None, 2],
                 [None, None, None, 3], [1, 2, 3, None]]
        n, edges = self._build_kruskals_params(graph)

        result = kruskals.get_mst(n, edges)

        self.assertEqual(result.sum, 6)

    def test_simple_graph(self):
        kruskals = Kruskals()

        graph = [[None, 2, None, 1, 5], [2, None, None, 2, None],
                 [None, None, None, 3, 2], [1, 2, 3, None, 3], [5, None, 2, 3, None]]
        n, edges = self._build_kruskals_params(graph)

        result = kruskals.get_mst(n, edges)

        self.assertEqual(result.sum, 8)

    def test_complete_graph(self):
        kruskals = Kruskals()

        n = 15
        graph = [
            [i + 1 for i in range(j)] for j in range(n)]

        for i in range(n):
            graph[i].append(None)

            for j in range(len(graph[i]), n):
                graph[i].append(graph[j][i])

        n, edges = self._build_kruskals_params(graph)

        result = kruskals.get_mst(n, edges)

        self.assertEqual(result.sum, 14)

    def test_weird_complete_graph(self):
        kruskals = Kruskals()

        n = 15
        graph = [
            [i + j + 1 for i in range(j)] for j in range(n)]

        for i in range(n):
            graph[i].append(None)

            for j in range(len(graph[i]), n):
                graph[i].append(graph[j][i])
        n, edges = self._build_kruskals_params(graph)

        result = kruskals.get_mst(n, edges)

        expected_sum = sum(range(2, 16))
        self.assertEqual(expected_sum, result.sum)

    def _build_kruskals_params(self, adjacency):
        edges = []

        for i in range(len(adjacency)):
            for j in range(len(adjacency[i])):
                edge_weight = adjacency[i][j]

                if edge_weight is not None:
                    edge = Edge(i, j, edge_weight)
                    edges.append(edge)

        return (len(adjacency), edges)
