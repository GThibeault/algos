from typing import List, TypeVar, Union

T = TypeVar("T")

class Quicksort:
    def sort(self, array: List[T], start: int = 0, end: Union[int, None] = None) -> List[T]:
        if end is None:
            end = len(array)
        if (end - start <= 1):
            return array

        pivot_index = self.get_pivot_index(array, start, end)

        self.swap(array, start, pivot_index)

        pivot_index = start

        for i in range(start, end):
            if array[i] <= array[start]:
                self.swap(array, i, pivot_index)
                pivot_index += 1

        pivot_index -= 1
        self.swap(array, start, pivot_index)

        self.sort(array, start, pivot_index)
        self.sort(array, pivot_index + 1, end)

        return array

    def swap(self, array: List[T], l: int, r: int) -> None:
        if l != r:
            array[l], array[r] = array[r], array[l]

    def get_pivot_index(self, array: List[T], start: int, end: int) -> int:
        size = end - start

        options = (start, start + size // 2, end - 1)
        sorted_options = sorted([(option, array[option])
                                for option in options], key=lambda o: o[1])

        return sorted_options[1][0]
