from src.algorithms.mst.prims import Prims

import unittest


class TestPrims(unittest.TestCase):
    def test_really_simple_graph(self):
        prims = Prims()

        graph = [[None, 2, None, 1], [2, None, None, 2],
                 [None, None, None, 3], [1, 2, 3, None]]

        result, sum = prims.get_mst(graph)

        self.assertEqual(sum, 6)

    def test_simple_graph(self):
        prims = Prims()

        graph = [[None, 2, None, 1, 5], [2, None, None, 2, None],
                 [None, None, None, 3, 2], [1, 2, 3, None, 3], [5, None, 2, 3, None]]

        result, sum = prims.get_mst(graph)

        self.assertEqual(sum, 8)

    def test_complete_graph(self):
        prims = Prims()

        n = 15
        graph = [
            [i + 1 for i in range(j)] for j in range(n)]

        for i in range(n):
            graph[i].append(None)

            for j in range(len(graph[i]), n):
                graph[i].append(graph[j][i])

        result, sum = prims.get_mst(graph)

        self.assertEqual(sum, 14)

    def test_weird_complete_graph(self):
        prims = Prims()

        n = 15
        graph = [
            [i + j + 1 for i in range(j)] for j in range(n)]

        for i in range(n):
            graph[i].append(None)

            for j in range(len(graph[i]), n):
                graph[i].append(graph[j][i])

        result, result_sum = prims.get_mst(graph)

        expected_sum = sum(range(2, 16))
        self.assertEqual(expected_sum, result_sum)
