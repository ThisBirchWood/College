class vertex:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"({self.value})"
    
    def element(self):
        return self.value
    
class edge:
    def __init__(self, vert1, vert2, element):
        self.vert1 = vert1
        self.vert2 = vert2
        self.element = element
        
    def __str__(self):
        return f"Vertex 1: {self.vert1}, Vertex 2: {self.vert2}" 
    
    def vertices(self):
        return (self.vert1, self.vert2)
    
    def opposite(self, x):
        if self.vert1 == x:
            return self.vert2
        elif self.vert2 == x:
            return self.vert1
        
    def value(self):
        return self.element
    
    def first_vertex(self):
        return self.vert1
    
    def second_vertex(self):
        return self.vert2
    
class graph:
    def __init__(self):
        self.adjacency_list = {}
        self.all_vertices = []
        self.all_edges = []

    def __str__(self):
        result = ""
        for vertex, neighbors in self.adjacency_list.items():
            result += f"{vertex}: {[str(neighbour) for neighbour in neighbors]}\n"
        return result

    def vertices(self):
        return self.all_vertices
    
    def edges(self):
        return self.all_edges
    
    def num_vertices(self):
        return len(self.all_vertices)
    
    def num_edges(self):
        return len(self.all_edges)
    
    def get_edge(self, x, y):
        edges = self.adjacency_list[x]
        for edge in edges:
            if edge.opposite(x) == y:
                return edge
            
    def degree(self, x):
        return len(self.adjacency_list[x])
    
    def get_edges(self, x):
        return self.adjacency_list[x]
    
    def add_vertex(self, elt):
        new_vertex = vertex(elt)
        self.all_vertices.append(new_vertex)
        self.adjacency_list[new_vertex] = []
        return new_vertex

    def add_edge(self, x, y, elt):
        new_edge = edge(x, y, elt)
        self.adjacency_list[x].append(new_edge)
        self.adjacency_list[y].append(new_edge)
        self.all_edges.append(new_edge)
        return new_edge

    def remove_vertex(self, x):
        old_edges = self.adjacency_list[x]
        for edge in old_edges:
            opposite_vertex = edge.opposite(x)
            self.adjacency_list[opposite_vertex].remove(edge)
            self.all_edges.remove(edge)
        del self.adjacency_list[x]
        self.all_vertices.remove(x)

    def remove_edge(self, e):
        first_vertex = e.first_vertex()
        second_vertex = e.second_vertex()

        self.adjacency_list[first_vertex].remove(e)
        self.adjacency_list[second_vertex].remove(e)
        self.all_edges.remove(e)

class graph:
    def __init__(self):
        self.adjancency_map = {}

    def __str__(self):
        pass

    def vertices(self):
        return self.adjancency_map.keys()
        
    def edges(self):
        return self.adjancency_map
    
    def num_vertices(self):
    
    def num_edges(self):
    
    def get_edge(self, x, y):
            
    def degree(self, x):
    
    def get_edges(self, x):
    
    def add_vertex(self, elt):

    def add_edge(self, x, y, elt):

    def remove_vertex(self, x):

    def remove_edge(self, e):

def test_graph_class(graph_function):
    g = graph_function()
    b = g.add_vertex("B")
    c = g.add_vertex("C")
    d = g.add_vertex("D")
    e = g.add_vertex("E")
    f = g.add_vertex("F")
    g1 = g.add_vertex("G")
    g.add_edge(b, c, "X")
    g.add_edge(b, d, "Y")
    g.add_edge(e, c, "Z")
    g.add_edge(f, g, "")
    print(g)
    print("------------------------------")
    g.remove_vertex(b)
    print(g)