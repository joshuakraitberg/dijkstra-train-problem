import logging
import re

from trains_problem.graph import Graph, EdgeDoesNotExistsError, VertexDoesNotExistError


class InvalidSimpleRouteError(Exception):
    pass


class RoutePlanner(object):
    """Allows for planning of train routes"""

    def __init__(self, connections):
        """
        :param connections: Iterable of tuples containing (source_name, destination_name, distance)
        """
        self._graph = None
        self._build_route(connections)

    def _build_route(self, connections):
        # TODO: Check connections for valid distance
        self._graph = Graph()
        for (o, d, x) in connections:
            self._graph.add_edge(o, d, x)

    def get_route_distance_from_stops(self, *stops):
        """Gets the total distance to complete route.

        :param stops: List of terminals to pass through, including first.
        :return: Distance of journey or "NO SUCH ROUTE" if impossible.
        """

        return self._get_distance_of_route(stops)

    def _get_distance_of_route(self, route):
        path = None
        try:
            path = self._graph.build_path(*route)
        except (EdgeDoesNotExistsError, VertexDoesNotExistError) as e:
            logging.error(e)
        return 'NO SUCH ROUTE' if path is None else sum(path)

    def get_number_of_routes_with_maximum_n_stops(self, start, end, n):
        return len(self._graph.find_paths_with_maximum_n_stops(start, end, n))

    def get_number_of_routes_with_exactly_n_stops(self, start, end, n):
        return len(self._graph.find_paths_with_n_stops(start, end, n))

    def get_length_of_shortest_route(self, start, end):
        return self._get_distance_of_route(self._graph.find_shortest_path_by_distance(start, end))

    def get_number_of_routes_with_distance_less_than_n(self, start, end, n):
        return len(self._graph.find_paths_shorter_than_n_distance(start, end, n))

    @staticmethod
    def build_simple_route_planner(route):
        """Builds a route planner using the string described in README.md testing.

        String must be like so:
            One letter, source terminal
            One letter, destination terminal
            At least one number, distance between terminals

        Multiple connections must be separated by commas and optionally spaces.
        """

        # Check valid route
        if not re.search(r'^\w\w\d+(, *\w\w\d+)*$', route):
            raise InvalidSimpleRouteError(f'Simple route is invalid: {route}.')

        # Turn simple route into connections
        connections = [(v.group(1), v.group(2), int(v.group(3))) for v in re.finditer(r'(\w)(\w)(\d+)', route)]
        return RoutePlanner(connections)
