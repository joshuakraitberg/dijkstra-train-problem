import heapq

from .tile import Tile, _add_edges_to_heap, _create_path_from_tiles, _distance_dst, _step_dst
from .vertex import Vertex


class EdgeAlreadyExistsError(Exception):
    pass


class EdgeDoesNotExistsError(Exception):
    pass


class VertexDoesNotExistError(Exception):
    pass


class Graph(object):
    """Directed graph composed of vertexes.

    Vertexes are stored in a dictionary by name.
    """

    def __init__(self):
        self._vertexes = {}

    def _test_vertexes(self, *vertexes):
        missing = [v for v in vertexes if v not in self._vertexes]
        if missing:
            raise VertexDoesNotExistError(f'Missing vertex(es): {", ".join(missing)}.')
        return (self._vertexes[v] for v in vertexes)

    def add_edge(self, origin_name, destination_name, distance):
        """Creates the edge in the graph, adding new vertexes if required.

        :param origin_name: Name of origin vertex.
        :param destination_name: Name of destination vertex.
        :param distance: Distance between vertexes.
        """

        # Get or create vertexes
        origin = self._vertexes.setdefault(origin_name, Vertex(origin_name))
        destination = self._vertexes.setdefault(destination_name, Vertex(destination_name))

        # Check if edge already exists
        if destination in origin.out_edges:
            raise EdgeAlreadyExistsError(f'Edge "{origin_name}" -> "{destination_name}" already exists.')

        # Added edge to vertexes
        origin.out_edges[destination] = distance
        destination.in_edges[origin] = distance

    def build_path(self, *args):
        """Builds a path dictated by vertex names in args

        :param args: Names of vertexes to build path.
        :return: List of distances in path if possible to build else None.
        """

        def _build_path(vertexes):
            it = iter(vertexes)
            current = next(it)
            for v in it:
                if v not in current.out_edges:
                    raise EdgeDoesNotExistsError(f"No edge for {current.name} -> {v.name}")
                yield current.out_edges[v]
                current = v

        path = None
        if len(args) > 1:
            vertexes = tuple(self._test_vertexes(*args))
            path = tuple(_build_path(vertexes))
        return path

    def find_shortest_path_by_distance(self, start_name, end_name):
        """Find shortest path between start and end based on distance

        :param start_name: Name of start vertex.
        :param end_name: Name of end vertex.
        :return: Iterable of shortest route or None.
        """

        start, end = self._test_vertexes(start_name, end_name)

        heap = []
        current = Tile(start, None, 0)
        _add_edges_to_heap(heap, current, _distance_dst)
        visited = {current.vertex}

        while heap:
            current = heapq.heappop(heap)
            if current.vertex == end:
                return _create_path_from_tiles(current)
            if current.vertex not in visited:
                _add_edges_to_heap(heap, current, _distance_dst)
            visited.add(current.vertex)

    def find_paths_with_n_stops(self, start_name, end_name, n):
        """Find every path going from start to end with exactly n stops

        :param start_name: Name of start vertex.
        :param end_name: Name of end vertex.
        :param n: Number of stops that must be taken.
        :return: Iterable of possible routes.
        """

        start, end = self._test_vertexes(start_name, end_name)

        heap = []
        paths = set()
        current = Tile(start, None, 0)
        _add_edges_to_heap(heap, current, _step_dst)

        while heap:
            current = heapq.heappop(heap)
            if current.vertex == end and current.distance == n:
                paths.add(_create_path_from_tiles(current))
            elif current.distance < n:
                _add_edges_to_heap(heap, current, _step_dst)

        return paths

    def find_paths_with_maximum_n_stops(self, start_name, end_name, n):
        """Find every path going from start to end with maximum n stops

        :param start_name: Name of start vertex.
        :param end_name: Name of end vertex.
        :param n: Number of stops that can taken.
        :return: Iterable of possible routes.
        """

        start, end = self._test_vertexes(start_name, end_name)

        heap = []
        paths = set()
        current = Tile(start, None, 0)
        _add_edges_to_heap(heap, current, _step_dst)

        while heap:
            current = heapq.heappop(heap)
            if current.vertex == end and current.distance <= n:
                paths.add(_create_path_from_tiles(current))
            if current.distance < n:
                _add_edges_to_heap(heap, current, _step_dst)

        return paths

    def find_paths_shorter_than_n_distance(self, start_name, end_name, n):
        """Find every path going from start to end with less than n distance

        :param start_name: Name of start vertex.
        :param end_name: Name of end vertex.
        :param n: Number of distance that route must be less than.
        :return: Iterable of possible routes.
        """

        start, end = self._test_vertexes(start_name, end_name)

        heap = []
        paths = set()
        current = Tile(start, None, 0)
        _add_edges_to_heap(heap, current, _distance_dst)

        while heap:
            current = heapq.heappop(heap)
            if current.vertex == end and current.distance < n:
                paths.add(_create_path_from_tiles(current))
            if current.distance < n:
                _add_edges_to_heap(heap, current, _distance_dst)

        return paths
