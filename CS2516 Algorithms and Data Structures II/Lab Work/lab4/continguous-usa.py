from graphs import graph_am

g = graph_am()

with open("contiguous-usa.dat", "r") as f:
    data = []
    for line in f.readlines():
        line = line.strip()
        country1, country2 = line.split()
        
        a = g.add_vertex(country1)
        b = g.add_vertex(country2)
        g.add_edge(a, b, (country1+country2))


print(g)