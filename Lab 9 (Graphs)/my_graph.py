"""Lab 9 Connected Graphs
Author: Parth Ray
"""

from queues import QueueLinked
from stacks import StackLinked

class Vertex:
    '''Add additional helper methods if necessary.'''
    def __init__(self, key):
        '''Add other attributes as necessary'''
        self.key = key
        self.adjacent_to = []
        self.color = None
        self.visited = False

    def __eq__(self, other):
        return self.key == other.key and \
                self.adjacent_to == other.adjacent_to and \
                self.color == other.color and \
                self.visited == other.visited

    def __repr__(self):
        return f"Vertex({self.key}, {self.adjacent_to}, {self.color}, {self.visited})"


class MyGraph:
    ''''''
    def __init__(self, filename):
        '''reads in the specification of a graph and creates a graph using an adjacency list representation.
           You may assume the graph is not empty and is a correct specification.  E.g. each edge is
           represented by a pair of vertices.  Note that the graph is not directed so each edge specified
           in the input file should appear on the adjacency list of each vertex of the two vertices associated
           with the edge.'''
        self.is_bicolor = False
        self.graph = {}
        with open(filename, "r") as graph_file:
            lines = graph_file.readlines()
            for line in range(2, len(lines)):
                verts = lines[line].strip().split()
                vert1, vert2 = verts[0], verts[1]
                self.add_vertex(vert1)
                self.add_vertex(vert2)
                if not vert1 in self.graph[vert2].adjacent_to \
                    and vert2 not in self.graph[vert1].adjacent_to:
                    self.add_edge(vert1, vert2)

    def __eq__(self, other):
        return self.graph == other.graph and \
               self.is_bicolor == other.is_bicolor

    def __repr__(self):
        return f"Graph({self.graph}, {self.is_bicolor})"

    def add_vertex(self, key):
        '''Add vertex to graph, only if the vertex is not already in the graph.'''
        if key not in self.graph:
            self.graph[key] = Vertex(key)

    def get_vertex(self, key):
        """Return the Vertex object associated with the id. If id is not in the graph,
           return None"""
        try:
            return self.graph[key]
        except KeyError:
            return None

    def add_edge(self, vert1, vert2):
        '''v1 and v2 are vertex id's. As this is an undirected graph, add an
           edge from v1 to v2 and an edge from v2 to v1.  You can assume that
           v1 and v2 are already in the graph'''
        self.graph[vert1].adjacent_to.append(vert2)
        self.graph[vert2].adjacent_to.append(vert1)

    def get_vertices(self):
        '''Returns a list of id's representing the vertices in the graph, in ascending order'''
        lst = [i for i in self.graph]
        lst.sort()
        return lst

    def get_conn_components(self, is_dfs=True):
        """Returns a list of lists.  For example, if there are three connected components
           then you will return a list of three lists.  Each sub list will contain the
           vertices (in ascending order) in the connected component represented by that list.
           The overall list will also be in ascending order based on the first item of each sublist.
        """
        self.bicolor()
        if is_dfs:
            return self.dfs(self.get_vertices(), [])
        return self.bfs(self.get_vertices(), [])

    def dfs(self, vert, component):
        stack = StackLinked()
        while len(vert) > 0:
            vertex = vert[0]
            stack.push(vertex)
            self.get_vertex(vertex).visited = True
            vert.remove(vertex)
            lst = [vertex]
            while not stack.is_empty():
                current = self.get_vertex(stack.pop())
                for adj_vert in current.adjacent_to:
                    if not self.get_vertex(adj_vert).visited:
                        self.get_vertex(adj_vert).visited = True
                        lst.append(adj_vert)
                        stack.push(adj_vert)
                        vert.remove(adj_vert)
            component.append(sorted(lst))
        for i in self.graph:
            self.get_vertex(i).visited = False
        return component

    def bfs(self, vert, component):
        queue = QueueLinked(len(vert))
        queue.enqueue()
        while not queue.is_empty():
            vertex = queue.dequeue()
            lst = [vertex]
            for adj_vert in vertex.adjacent_to:
                return



    def bicolor(self):
        '''Returns True if the graph is bicolorable and False otherwise.
           This method MUST use Breadth First Search logic!'''
        verts = self.get_vertices()
        for vert in verts:
            if not self.get_vertex(vert).visited:
                queue = QueueLinked(len(verts))
                self.get_vertex(vert).visited = True
                self.graph[vert].color = "black"
                queue.enqueue(vert)
                while not queue.is_empty():
                    source = queue.dequeue()
                    for adj_vert in self.graph[source].adjacent_to:
                        if not self.get_vertex(adj_vert).visited:
                            self.get_vertex(adj_vert).visited = True
                            if self.graph[source].color == "black":
                                self.graph[adj_vert].color = "red"
                            else:
                                self.graph[adj_vert].color = "black"
                            queue.enqueue(adj_vert)
                        else:
                            if self.graph[source].color == self.graph[adj_vert].color:
                                self.is_bicolor = False
                                return self.is_bicolor
        self.is_bicolor = True
        return self.is_bicolor
