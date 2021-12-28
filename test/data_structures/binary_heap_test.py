from src.data_structures.binary_heap import BinaryHeap

import unittest

class TestBinaryHeap(unittest.TestCase):
    def test_insert_respects_min(self):
        heap = BinaryHeap()
        
        n = 45
        data = list(range(n, -1, -1))
        
        for d in data:
            heap.insert(d)

        min = heap.peek_min()

        self.assertEqual(min, 0)

    def test_insert_respects_min_with_custom_key(self):
        gt_func = lambda l, r: l > r
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