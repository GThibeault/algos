from src.data_structures.binary_heap import BinaryHeap


class TrackingBinaryHeap(BinaryHeap):
    def __swap_values(self, i, r):
        super().__swap_values(i, r)

        self.values[i].index, self.values[r].index = i, r

    def __get_value(self, i):
        tracker = self.values[i]

        if tracker is not None:
            return tracker.value

    def __create_value(self, val, index):
        return Tracker(val, index)


class Tracker(object):
    def __init__(self, val, i):
        self.value = val
        self.index = i
