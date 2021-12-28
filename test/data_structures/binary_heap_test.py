from src.data_structures.binary_heap import BinaryHeap

import unittest


class TestBinaryHeap(unittest.TestCase):
    def test_empty_true(self):
        heap = BinaryHeap()

        empty = heap.is_empty()

        self.assertTrue(empty)

    def test_empty_false(self):
        heap = BinaryHeap()

        heap.insert(1)
        empty = heap.is_empty()

        self.assertFalse(empty)

    def test_insert_respects_min(self):
        heap = BinaryHeap()

        n = 45
        data = list(range(n, -1, -1))

        for d in data:
            heap.insert(d)

        min = heap.peek_min()

        self.assertEqual(min, 0)

    def test_insert_respects_min_with_custom_key(self):
        def gt_func(l, r): return l > r
        heap = BinaryHeap(key=gt_func)

        n = 45
        data = list(range(n, -1, -1))

        for d in data:
            heap.insert(d)

        max = heap.peek_min()

        self.assertEqual(max, n)

    def test_empty_peek_min_returns_none(self):
        heap = BinaryHeap()

        min = heap.peek_min()

        self.assertIsNone(min)

    def test_extract_min_on_empty_raises(self):
        heap = BinaryHeap()

        with self.assertRaises(LookupError):
            heap.extract_min()

    def test_trivial_extract_min(self):
        heap = BinaryHeap()

        v = 1
        heap.insert(v)

        m = heap.extract_min()

        self.assertEqual(m, v)

    def test_extract_min_removes(self):
        heap = BinaryHeap()

        v = 1
        heap.insert(v)
        heap.extract_min()

        m = heap.peek_min()

        self.assertIsNone(m)

    def test_extract_min_extracts_minimum(self):
        heap = BinaryHeap()

        n = 45
        data = list(range(n, -1, -1))

        for d in data:
            heap.insert(d)

        res = []
        while not heap.is_empty():
            m = heap.extract_min()
            res.append(m)

        expected = list(range(0, n + 1))
        self.assertEqual(expected, res)

    def test_extract_min_extracts_minimum_with_custom_key(self):
        def gt_func(l, r): return l > r
        heap = BinaryHeap(key=gt_func)

        n = 45
        data = list(range(n, -1, -1))

        for d in data:
            heap.insert(d)

        res = []
        while not heap.is_empty():
            m = heap.extract_min()
            res.append(m)

        self.assertEqual(data, res)
