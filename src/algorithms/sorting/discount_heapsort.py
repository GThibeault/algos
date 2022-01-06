from typing import List, TypeVar
from src.data_structures.binary_heap import BinaryHeap

T = TypeVar("T")

class DiscountHeapsort:
    def sort(self, array: List[T]) -> List[T]:
        sorted_array = []

        heap = BinaryHeap()

        for value in array:
            heap.insert(value)
            
        while not heap.is_empty():
            sorted_array.append(heap.extract_min())
            
        return sorted_array
