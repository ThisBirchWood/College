from graph_gen import graph_generator
from prims import prim
from time import perf_counter

AMOUNT_OF_TEST_CASES = 10

vert_opts = [5, 10, 15, 20, 50, 100, 200, 500, 1000, 2500, 10000]
density_opts = [0.05, 0.1, 0.25, 0.4, 0.5, 0.6, 0.75, 0.9, 1]

graph_gen = graph_generator()

for verticies in vert_opts:
    for densities in density_opts:
        total_time_heap = 0
        total_time_unsorted = 0

        print("---------------------------")
        print(f"Verticies: {verticies}, Density: {densities}")

        for i in range(AMOUNT_OF_TEST_CASES):
            g = graph_gen.generate_graph(verticies, densities)
            start_time = perf_counter()
            mst = prim(g)
            end_time = perf_counter()
            total_time_heap += (end_time - start_time)

            #print(f"Result: {mst}")
    
            g = graph_gen.generate_graph(verticies, densities)
            start_time = perf_counter()
            mst = prim(g, unsorted_list=True)
            end_time = perf_counter()
            total_time_unsorted += (end_time - start_time)

            #print(f"Result: {mst}")
        print(f"Average time for Heap APQ: {total_time_heap/AMOUNT_OF_TEST_CASES}")
        print(f"Average time for unsorted list APQ: {total_time_unsorted/AMOUNT_OF_TEST_CASES}")

            
