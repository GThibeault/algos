class BinaryHeap(object):
    def __init__(self, key=None) -> None:
        self.values = []

        if key is not None:
            self.__compare_values = key
        else:
            self.__compare_values = self.__default_compare

    def is_empty(self):
        return len(self.values) == 0

    def peek_min(self):
        if self.values:
            return self.__get_value(0)
        else:
            return None

    def insert(self, val) -> None:
        current_index = len(self.values)
        new_entry = self.__create_value(val, current_index)
        self.values.append(new_entry)

        self.__heap_up(current_index)

        return new_entry

    def extract_min(self):
        if not self.values:
            raise LookupError("Empty heap")

        min = self.__get_value(0)

        self.__swap_values(0, -1)
        del self.values[-1]

        self.__heap_down(0)

        return min

    def __heap_down(self, i) -> None:
        while i < len(self.values):
            child_indices = self.__get_children_indices(i)

            m = i
            for c in child_indices:
                if c < len(self.values):
                    if self.__compare_indices(c, m):
                        m = c

            if m == i:
                break
            else:
                self.__swap_values(m, i)
                i = m

    def __heap_up(self, i) -> None:
        while i != 0:
            parent_index = self.__get_parent_index(i)

            if self.__compare_indices(i, parent_index):
                self.__swap_values(i, parent_index)

                i = parent_index
            else:
                break

    def __get_children_indices(self, i):
        base = 2 * i

        return base + 1, base + 2

    def __get_parent_index(self, i):
        return (i - 1) // 2

    def __swap_values(self, i, r):
        self.values[i], self.values[r] = self.values[r], self.values[i]

    def __create_value(self, val, index):
        return val

    def __get_value(self, i):
        return self.values[i]

    def __compare_indices(self, li, ri):
        return self.__compare_values(self.__get_value(li), self.__get_value(ri))

    def __default_compare(self, l, r):
        return l <= r
