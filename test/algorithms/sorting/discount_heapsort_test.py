from src.algorithms.sorting.discount_heapsort import DiscountHeapsort

import unittest


class TestDiscountHeapsort(unittest.TestCase):
    def test_simple_array(self):
        discount_heapsort = DiscountHeapsort()

        array = [5, 2, 4, 7, 6, 8, 1]
        expected = sorted(array)

        sorted_array = discount_heapsort.sort(array)

        self.assertEqual(expected, sorted_array)

    def test_simple_array_no_2(self):
        discount_heapsort = DiscountHeapsort()

        array = [5, 2, 4, 2, 6, 8, 1]
        expected = sorted(array)

        sorted_array = discount_heapsort.sort(array)

        self.assertEqual(expected, sorted_array)

    def test_binary(self):
        discount_heapsort = DiscountHeapsort()

        n = 1250
        array = [i % 2 for i in range(n)]
        expected = sorted(array)

        sorted_array = discount_heapsort.sort(array)

        self.assertEqual(expected, sorted_array)

    def test_larger_array(self):
        discount_heapsort = DiscountHeapsort()

        n = 125000
        array = [(n - i) * 2 % 50 for i in range(n)]
        expected = sorted(array)

        sorted_array = discount_heapsort.sort(array)

        self.assertEqual(expected, sorted_array)
