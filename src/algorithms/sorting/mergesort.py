from typing import List, TypeVar, Union
from itertools import chain
from math import inf

T = TypeVar("T")

class Mergesort:
    def sort(self, array: List[T], start: int = 0, end: Union[int, None] = None) -> List[T]:
        if end is None:
            end = len(array)
        size = end - start 
        if (size <= 1):
            return array[start:end]
        
        mid_point = start + size // 2

        left_sorted_array = self.sort(array, start, mid_point)
        right_sorted_array = self.sort(array, mid_point, end)

        sorted_array = self._merge(left_sorted_array, right_sorted_array)

        return sorted_array

    def _merge(self, left_array: List[T], right_array: List[T]) -> List[T]:
        merged_array = [] 
        total_size  = len(left_array) + len(right_array)

        left_it, right_it = chain(left_array, [inf]), chain(right_array, [inf])
        l, r = next(left_it), next(right_it)
        
        while len(merged_array) < total_size:
            if l <= r:
                merged_array.append(l)
                l = next(left_it)
            else:
                merged_array.append(r)
                r = next(right_it)
                
        return merged_array