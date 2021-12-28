from src.data_structures.tracking_binary_heap import TrackingBinaryHeap


class Prims(object):
    def get_mst(self, adjacency_matrix):
        heap = TrackingBinaryHeap()

        picked = [False for i in range(adjacency_matrix)]
        costs = [None for i in range(adjacency_matrix)]
        edges = [None for i in range(adjacency_matrix)]

        result = []
        sum = 0

        start_vertex = 0
        heap.insert(start_vertex)

        while not heap.is_empty():
            current_vertex = heap.extract_min()
            picked[current_vertex] = True

            if current_vertex != start_vertex:
                neighbor = edges[current_vertex]

                result.append(current_vertex, neighbor)
                sum += adjacency_matrix[current_vertex][neighbor][1]

            for vertex, edge_weight in adjacency_matrix[current_vertex]:
                if picked[vertex]:
                    continue

                previous_cost = costs[vertex]

                if previous_cost is None:
                    costs[vertex] = heap.insert(edge_weight)
                    edges[vertex] = current_vertex

                elif edge_weight < previous_cost:
                    heap.change_value(costs[vertex], edge_weight)
                    edges[vertex] = current_vertex

        return result.sum
