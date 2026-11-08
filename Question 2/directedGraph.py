"""Directed graph implementation using incoming and outgoing adjacency lists."""

class DirectedGraph:

    # Initialize dictionaries to store outgoing and incoming connections.
    def __init__(self):
        self._outgoing = {}
        self._incoming = {}

    # Add a vertex with empty incoming and outgoing adjacency lists.
    def add_vertex(self, vertex):
        if vertex in self._outgoing:
            return False
        self._outgoing[vertex] = []
        self._incoming[vertex] = []
        return True

    # Create a directed edge from the source vertex to the target vertex.
    def add_edge(self, source, target):
        if source not in self._outgoing or target not in self._outgoing:
            raise KeyError("Both vertices must exist in the graph")
        if target in self._outgoing[source]:
            return False
        self._outgoing[source].append(target)
        self._incoming[target].append(source)
        return True

    # Remove a directed edge and update both adjacency lists.
    def remove_edge(self, source, target):
        if source not in self._outgoing or target not in self._outgoing:
            raise KeyError("Both vertices must exist in the graph")
        if target not in self._outgoing[source]:
            return False
        self._outgoing[source].remove(target)
        self._incoming[target].remove(source)
        return True

    # Check whether the goal vertex is reachable using iterative DFS.
    def has_path(self, start, goal):
        """Return True if goal is reachable from start using iterative DFS."""
        stack, seen = [start], set()
        while stack:
            v = stack.pop()
            if v is goal:
                return True
            if v in seen:
                continue
            seen.add(v)

            # Add connected outgoing vertices to the DFS stack.
            stack.extend(self._outgoing[v])
        return False

    # Return all vertices that have directed edges pointing to this vertex.
    def list_incoming_adjacent_vertex(self, vertex):
        if vertex not in self._incoming:
            raise KeyError("Vertex not found")
        return list(self._incoming[vertex])

    # Return all vertices that this vertex has directed edges pointing to.
    def list_outgoing_adjacent_vertex(self, vertex):
        if vertex not in self._outgoing:
            raise KeyError("Vertex not found")
        return list(self._outgoing[vertex])

    # Return all vertices currently stored in the graph.
    def vertices(self):
        return list(self._outgoing.keys())
