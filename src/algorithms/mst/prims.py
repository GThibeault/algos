from src.data_structures.tracking_binary_heap import TrackingBinaryHeap


class Prims(object):
    def get_mst(self, adjacency_matrix):
        def key_func(l, r): return l.weight <= r.weight
        heap = TrackingBinaryHeap(key=key_func)

        picked = [False for i in range(len(adjacency_matrix))]
        costs = [None for i in range(len(adjacency_matrix))]
        edges = [None for i in range(len(adjacency_matrix))]

        result = []
        sum = 0

        start_vertex = 0
        start_entry = Entry(0, 0)
        heap.insert(start_entry)

        while not heap.is_empty():
            current_vertex, weight = heap.extract_min()
            picked[current_vertex] = True

            if current_vertex != start_vertex:
                neighbor = edges[current_vertex]

                result.append((current_vertex, neighbor))
                sum += weight

            for vertex, edge_weight in enumerate(adjacency_matrix[current_vertex]):
                if picked[vertex] or edge_weight is None:
                    continue

                previous_cost = costs[vertex]

                if previous_cost is None:
                    costs[vertex] = heap.insert(Entry(vertex, edge_weight))
                    edges[vertex] = current_vertex

                elif edge_weight < previous_cost.value.weight:

                    heap.change_value(
                        costs[vertex], Entry(vertex, edge_weight))
                    edges[vertex] = current_vertex

        return (result, sum)


class Entry(object):
    def __init__(self, vertex, weight):
        self.vertex = vertex
        self.weight = weight

    def __iter__(self):
        return iter((self.vertex, self.weight))
