from src.algorithms.kruskals import Kruskals, Edge

import unittest


class TestKruskals(unittest.TestCase):
    def test_really_simple_graph(self):
        kruskals = Kruskals()

        n = 4
        edges = [Edge(0, 1, 2), Edge(0, 3, 1), Edge(1, 0, 2),
                 Edge(1, 3, 2), Edge(2, 3, 3), Edge(3, 0, 1), Edge(3, 1, 2), Edge(3, 2, 3)]

        result = kruskals.get_mst(n, edges)

        self.assertEqual(result.sum, 6)

#    def test_simple_graph(self):
#        kruskals = Kruskals()
#
#        graph = [[None, 2, None, 1, 5], [2, None, None, 2, None],
#                 [None, None, None, 3, 2], [1, 2, 3, None, 3], [5, None, 2, 3, None]]
#
#        result, sum = kruskals.get_mst(graph)
#
#        self.assertEqual(sum, 8)
#
#    def test_complete_graph(self):
#        kruskals = Kruskals()
#
#        n = 15
#        graph = [
#            [i + 1 for i in range(j)] for j in range(n)]
#
#        for i in range(n):
#            graph[i].append(None)
#
#            for j in range(len(graph[i]), n):
#                graph[i].append(graph[j][i])
#
#        result, sum = kruskals.get_mst(graph)
#
#        self.assertEqual(sum, 14)
#
#    def test_weird_complete_graph(self):
#        kruskals = Kruskals()
#
#        n = 15
#        graph = [
#            [i + j + 1 for i in range(j)] for j in range(n)]
#
#        for i in range(n):
#            graph[i].append(None)
#
#            for j in range(len(graph[i]), n):
#                graph[i].append(graph[j][i])
#
#        result, result_sum = kruskals.get_mst(graph)
#
#        expected_sum = sum(range(2, 16))
#        self.assertEqual(expected_sum, result_sum)
#
