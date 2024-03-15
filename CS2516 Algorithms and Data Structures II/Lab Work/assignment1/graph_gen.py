from graph import graph_am, edge, vertex
from random import randint, seed

class graph_generator():
    def __init__(self):
        pass

    def generate_graph(self, n, density):
        max_edges = (n*(n-1))/2
        m = int(round(max_edges*density))

        return self.randomly_generate_graph(n, m)

    def randomly_generate_graph(self, n, m):
        # create graph object
        g = graph_am()

        # list to store the vertex objects
        vertices = []

        # loop n times to create n vertices
        for i in range(n):
            # create vertex and add it to the list and to the graph
            v = vertex(i)
            vertices.append(v)
            g.add_vertex(v)

            # check if i is more than one, otherwise the one vertex would connect to itself
            if i > 0:
                # randomly choose another vertex in the list
                other_vertex = vertices[randint(0, i)]
                while other_vertex == i:    # ensure that it's not the last one added
                    other_vertex = vertices[randint(0, i)]
                weight_of_edge = randint(1, 20) # choose weight

                # add edge to graph
                g.add_edge(v, other_vertex, weight_of_edge)

        # calculate the amount of new edges that can be added
        amount_new_edges = m - (n - 1)
        if amount_new_edges > 0:
            for i in range(amount_new_edges):
                random_vertex_1 = randint(0, n-1)
                random_vertex_2 = randint(0, n-1)
                while random_vertex_2 == random_vertex_1:
                    random_vertex_2 = randint(0, n-1)

                random_vertex_1 = vertices[random_vertex_1]
                random_vertex_2 = vertices[random_vertex_2]

                if not g.is_edge(random_vertex_1, random_vertex_2):
                    g.add_edge(random_vertex_1, random_vertex_2, randint(1, 20))
                

        return g
    
if __name__ == "__main__":
    r = graph_generator()
    print(r.generate_graph(2500, 0.5))
