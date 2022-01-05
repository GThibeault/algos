from __future__ import annotations
from typing import List, TypeVar, Generic, Callable

E, V = TypeVar("E"), TypeVar("V")

class BinaryHeap(Generic[E, V]):
    def __init__(self, key: Callable[[V, V], bool] = None) -> None:
        self.entries: List[E] = []

        if key is not None:
            self.compare_values = key
        else:
            self.compare_values = self._default_compare

    def is_empty(self) -> bool:
        return len(self.entries) == 0

    def peek_min(self) -> V:
        if self.entries:
            return self._get_value(0)
        else:
            return None

    def insert(self, val: V) -> E:
        current_index = len(self.entries)
        new_entry = self._create_entry(val, current_index)
        self.entries.append(new_entry)

        self._heap_up(current_index)

        return new_entry

    def extract_min(self) -> V:
        if not self.entries:
            raise LookupError("Empty heap")

        min = self._get_value(0)

        self._swap_values(0, -1)
        del self.entries[-1]

        self._heap_down(0)

        return min

    def _heap_down(self, i: int) -> None:
        while i < len(self.entries):
            child_indices = self._get_children_indices(i)

            m = i
            for c in child_indices:
                if c < len(self.entries):
                    if self._compare_indices(c, m):
                        m = c

            if m == i:
                break
            else:
                self._swap_values(m, i)
                i = m

    def _heap_up(self, i: int) -> None:
        while i != 0:
            parent_index = self._get_parent_index(i)

            if self._compare_indices(i, parent_index):
                self._swap_values(i, parent_index)

                i = parent_index
            else:
                break

    def _get_children_indices(self, i: int) -> int:
        base = 2 * i

        return base + 1, base + 2

    def _get_parent_index(self, i: int) -> int:
        return (i - 1) // 2

    def _swap_values(self, i: int, r: int) -> None:
        self.entries[i], self.entries[r] = self.entries[r], self.entries[i]

    def _create_entry(self, val: V, index: int) -> E:
        return val

    def _get_value(self, i: int) -> V:
        return self.entries[i]

    def _compare_indices(self, li: int, ri: int) -> bool:
        return self.compare_values(self._get_value(li), self._get_value(ri))

    def _default_compare(self, l: V, r: V) -> bool:
        return l <= r
