import heapq


class Tile(object):
    def __init__(self, vertex, prev, distance):
        self.vertex = vertex
        self.prev = prev
        self.distance = distance

    def __lt__(self, other):
        return self.distance < other.distance


def _create_path_from_tiles(goal):
    path = []
    while goal:
        path.append(goal.vertex.name)
        goal = goal.prev
    return tuple(path[::-1])


def _add_edges_to_heap(heap, current, dst_func, heap_push=heapq.heappush):
    for k, v in current.vertex.out_edges.items():
        heap_push(heap, Tile(k, current, dst_func(current, k, v)))


def _distance_dst(current, k, v):
    return current.distance + v


def _step_dst(current, k, v):
    return current.distance + 1
