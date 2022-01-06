from src.algorithms.sorting.mergesort import Mergesort

import unittest


class TestMergesort(unittest.TestCase):
    def test_simple_array(self):
        merge = Mergesort()

        array = [5, 2, 4, 7, 6, 8, 1]
        expected = sorted(array)

        sorted_array = merge.sort(array)

        self.assertEqual(expected, sorted_array)

    def test_simple_array_no_2(self):
        merge = Mergesort()

        array = [5, 2, 4, 2, 6, 8, 1]
        expected = sorted(array)

        sorted_array = merge.sort(array)

        self.assertEqual(expected, sorted_array)

    def test_binary(self):
        merge = Mergesort()

        n = 1250
        array = [i % 2 for i in range(n)]
        expected = sorted(array)

        sorted_array = merge.sort(array)

        self.assertEqual(expected, sorted_array)

    def test_larger_array(self):
        merge = Mergesort()

        n = 125000
        array = [(n - i) * 2 % 50 for i in range(n)]
        expected = sorted(array)

        sorted_array = merge.sort(array)

        self.assertEqual(expected, sorted_array)
