from __future__ import annotations

from src.data_structures.binary_heap import BinaryHeap
from dataclasses import dataclass
from typing import TypeVar, Generic

V = TypeVar("V")

@dataclass
class Tracker(Generic[V]):
    value: V
    index: int
    deleted: bool = False

class TrackingBinaryHeap(BinaryHeap[Tracker[V], V]):
    def delete(self, tracker: Tracker[V]) -> None:
        if tracker.deleted == True:
            return

        i = tracker.index

        self._swap_values(i, -1)
        del self.entries[-1]

        if i < len(self.entries):
            self._heap_down(i)
            
        tracker.deleted = True

    def change_value(self, tracker: Tracker[V], new_value: V) -> None:
        if tracker.deleted == True:
            return

        tracker.value, old_value = new_value, tracker.value

        if self.compare_values(new_value, old_value):
            self._heap_up(tracker.index)
        else:
            self._heap_down(tracker.index)
            
    def extract_min(self) -> V:
        if self.entries:
            self.entries[0].deleted = True
            
        return super().extract_min()

    def _sanitize_index(self, i: int) -> int:
        if i < 0:
            return len(self.entries) + i
        else:
            return i

    def _get_value(self, i: int) -> V:
        tracker = self.entries[i]

        if tracker is not None:
            return tracker.value

    def _create_entry(self, val: V, index: int) -> Tracker[V]:
        return Tracker(val, index)

    def _swap_values(self, i: int, r: int) -> None:
        super()._swap_values(i, r)

        i = self._sanitize_index(i)
        r = self._sanitize_index(r)

        self.entries[i].index, self.entries[r].index = i, r
