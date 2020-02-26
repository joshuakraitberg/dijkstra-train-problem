import pytest

from trains_problem.graph import (
    Graph,
    EdgeDoesNotExistsError,
    VertexDoesNotExistError,
    EdgeAlreadyExistsError
)


@pytest.fixture(scope='module')
def simple_graph():
    graph = Graph()
    graph.add_edge('A', 'B', 5)
    graph.add_edge('B', 'C', 4)
    graph.add_edge('B', 'A', 1)
    graph.add_edge('B', 'D', 1)
    graph.add_edge('D', 'A', 11)
    graph.add_edge('C', 'A', 7)
    return graph


def test_add_edge(simple_graph):
    with pytest.raises(EdgeAlreadyExistsError):
        simple_graph.add_edge('A', 'B', 5)


@pytest.mark.parametrize("vertexes, path", [
    pytest.param(('A', 'B', 'C', 'A',), (5, 4, 7), id="ABCA"),
    pytest.param(('A',), None, id='A'),
    pytest.param((), None, id='None'),
])
def test_build_path(simple_graph, vertexes, path):
    assert simple_graph.build_path(*vertexes) == path


def test_build_path_missing_vertex(simple_graph):
    with pytest.raises(VertexDoesNotExistError):
        simple_graph.build_path('A', 'F')


def test_build_path_missing_edge(simple_graph):
    with pytest.raises(EdgeDoesNotExistsError):
        simple_graph.build_path('A', 'D')


def test_find_shortest_path_by_distance(simple_graph):
    assert (
        simple_graph.find_shortest_path_by_distance('A', 'A') ==
        ('A', 'B', 'A')
    )


def test_find_paths_with_n_stops(simple_graph):
    assert (
        simple_graph.find_paths_with_n_stops('A', 'A', 3) ==
        {('A', 'B', 'C', 'A'), ('A', 'B', 'D', 'A')}
    )


def test_find_paths_with_maximum_n_stops(simple_graph):
    assert (
        simple_graph.find_paths_with_maximum_n_stops('A', 'A', 3) ==
        {('A', 'B', 'A'), ('A', 'B', 'C', 'A'), ('A', 'B', 'D', 'A')}
    )


def test_find_paths_shorter_than_n_distance(simple_graph):
    assert (
            simple_graph.find_paths_shorter_than_n_distance('A', 'A', 17) ==
            {('A', 'B', 'A'), ('A', 'B', 'A', 'B', 'A'), ('A', 'B', 'C', 'A')}
    )
