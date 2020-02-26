class Vertex(object):
    """Vertex as part of graph.

    Each vertex has a name and stores the distance of incoming and outgoing edges to other vertexes."""

    def __init__(self, name):
        self.name = name
        self.in_edges = {}
        self.out_edges = {}
