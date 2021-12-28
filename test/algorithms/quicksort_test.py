from src.algorithms.quicksort import Quicksort

import unittest


class TestQuicksort(unittest.TestCase):
    def test_simple_array(self):
        quick = Quicksort()

        array = [5, 2, 4, 2, 6, 8, 1]
        expected = sorted(array)

        quick.sort(array)

        self.assertEqual(expected, array)

    def test_binary(self):
        quick = Quicksort()

        n = 1250
        array = [i % 2 for i in range(n)]
        expected = sorted(array)

        quick.sort(array)

        self.assertEqual(expected, array)

    def test_larger_array(self):
        quick = Quicksort()

        n = 12500
        array = [(n - i) * 2 % 50 for i in range(n)]
        expected = sorted(array)

        quick.sort(array)

        self.assertEqual(expected, array)
