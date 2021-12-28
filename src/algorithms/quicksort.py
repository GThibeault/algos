from logging import error


class Quicksort(object):
    def sort(self, array):
        if (len(array) <= 1):
            return array

        pivot_index = self.get_pivot_index(array)

        self.swap(array, 0, pivot_index)

        pivot_index = 0

        for i in range(len(array)):
            if array[i] < array[pivot_index]:
                self.swap(array, i, pivot_index + 1)
                self.swap(array, pivot_index, pivot_index + 1)

                pivot_index += 1

        array[:pivot_index] = self.sort(array[:pivot_index])
        array[pivot_index + 1:] = self.sort(array[pivot_index + 1:])

        return array

    def swap(self, array, l, r):
        array[l], array[r] = array[r], array[l]

    def get_pivot_index(self, array):
        options = (0, len(array) // 2, len(array) - 1)
        sorted_options = sorted([(option, array[option])
                                for option in options], key=lambda o: o[1])

        return sorted_options[1][0]
