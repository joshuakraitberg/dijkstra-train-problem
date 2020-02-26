import pytest

from trains_problem.graph import (
    EdgeDoesNotExistsError,
    VertexDoesNotExistError
)
from trains_problem.route_planner import InvalidSimpleRouteError, RoutePlanner


@pytest.fixture(scope='module')
def simple_route_planner():
    return RoutePlanner.build_simple_route_planner('AB5, BC4, CD8, DC8, DE6, AD5, CE2, EB3, AE7')


@pytest.mark.parametrize('route', (
        'AB5, BC, CD8, DC8, DE6, AD5, CE2, EB3, AE7',
        'AB5, BC4, CD8, DC8, DE6, AD5 CE2, EB3, AE7',
        'ABA5, BC4, CD8, DC8, DE6, AD5, CE2, EB3, AE7')
)
def test_build_simple_route_planner(route):
    with pytest.raises(InvalidSimpleRouteError):
        RoutePlanner.build_simple_route_planner(route)


@pytest.mark.parametrize(
    'route, expected', (
        (('A', 'B', 'C'), 9),
        (('A', 'D'), 5),
        (('A', 'D', 'C'), 13),
        (('A', 'E', 'B', 'C', 'D'), 22),
        (('A', 'E', 'D'), 'NO SUCH ROUTE'),
        (('A', 'F'), 'NO SUCH ROUTE'),
    )
)
def test_get_route_distance_from_stops(simple_route_planner, route, expected):
    assert simple_route_planner.get_route_distance_from_stops(*route) == expected


@pytest.mark.parametrize(
    'start, end, n, expected', (
        ('C', 'C', 3, 2),
    )
)
def test_get_number_of_routes_with_maximum_n_stops(simple_route_planner, start, end, n, expected):
    assert simple_route_planner.get_number_of_routes_with_maximum_n_stops(start, end, n) == expected


@pytest.mark.parametrize(
    'start, end, n, expected', (
        ('A', 'C', 4, 3),
    )
)
def test_get_number_of_routes_with_exactly_n_stops(simple_route_planner, start, end, n, expected):
    assert simple_route_planner.get_number_of_routes_with_exactly_n_stops(start, end, n) == expected


@pytest.mark.parametrize(
    'start, end, expected', (
        ('A', 'C', 9),
        ('B', 'B', 9),
    )
)
def test_get_length_of_shortest_route(simple_route_planner, start, end, expected):
    assert simple_route_planner.get_length_of_shortest_route(start, end) == expected


@pytest.mark.parametrize(
    'start, end, n, expected', (
        ('C', 'C', 30, 7),
    )
)
def test_get_number_of_routes_with_distance_less_than_n(simple_route_planner, start, end, n, expected):
    assert simple_route_planner.get_number_of_routes_with_distance_less_than_n(start, end, n) == expected
