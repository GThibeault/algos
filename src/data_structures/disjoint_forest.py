from __future__ import annotations
from dataclasses import dataclass
from typing import TypeVar, Generic


T = TypeVar("T")


class DisjointForest(Generic[T]):
    def make_set(self, value: T) -> DisjointForestSet[T]:
        return DisjointForestSet(value, 0)

    def are_in_same_set(self, set_1: DisjointForestSet[T], set_2: DisjointForestSet[T]) -> bool:
        if set_1 is None or set_2 is None:
            return False

        repr_1, repr_2 = self.get_representative(
            set_1), self.get_representative(set_2)

        return repr_1 is repr_2

    def join_sets(self, set_1: DisjointForestSet[T], set_2: DisjointForestSet[T]) -> DisjointForestSet[T]:
        if set_1.rank < set_2.rank:
            set_1.parent = set_2
        elif set_2.rank < set_1.rank:
            set_2.parent = set_1
        # set_1.rank == set_2.rank
        else:
            set_2.parent, set_1.rank = set_1, set_1.rank + 1

    def get_representative(self, set: DisjointForestSet[T]) -> DisjointForestSet[T]:
        if set.parent is not set:
            set.parent = self.get_representative(set.parent)

        return set.parent


@dataclass(eq=False)
class DisjointForestSet(Generic[T]):
    value: T

    rank: int
    parent: DisjointForestSet[T] = None

    def __post_init__(self):
        self.parent = self
