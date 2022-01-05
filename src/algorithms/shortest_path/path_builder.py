
from typing import List, Tuple, Union


class PathBuilder:
    # inefficient but simple
    def build_shortest_paths(self, predecessor: List[Union[int, None]]) -> List[Tuple[int, int]]:
        paths = [[] for i in range(len(predecessor))]

        for i in range(len(predecessor)):
            p = predecessor[i]

            while p is not None:
                paths[i].insert(0, p)
                p = predecessor[p]

        return paths