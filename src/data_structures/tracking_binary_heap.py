from src.data_structures.binary_heap import BinaryHeap


class TrackingBinaryHeap(BinaryHeap):
    def delete(self, tracker):
        i = tracker.index

        self.swap_values(i, -1)
        del self.values[-1]

        if i < len(self.values):
            self.heap_down(i)

    def change_value(self, tracker, new_value):
        tracker.value, old_value = new_value, tracker.value

        if self.compare_values(new_value, old_value):
            self.heap_up(tracker.index)
        else:
            self.heap_down(tracker.index)

    def sanitize_index(self, i):
        if i < 0:
            return len(self.values) + i
        else:
            return i

    def get_value(self, i):
        tracker = self.values[i]

        if tracker is not None:
            return tracker.value

    def create_value(self, val, index):
        return Tracker(val, index)

    def swap_values(self, i, r):
        super().swap_values(i, r)

        i = self.sanitize_index(i)
        r = self.sanitize_index(r)

        self.values[i].index, self.values[r].index = i, r


class Tracker(object):
    def __init__(self, val, i):
        self.value = val
        self.index = i
