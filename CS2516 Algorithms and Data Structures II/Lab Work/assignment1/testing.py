from graph_gen import graph_generator
from prims import prim, prim_unsorted
from time import perf_counter

AMOUNT_OF_TEST_CASES = 3

vert_opts = [5000, 10000, 15000, 30000]
density_opts = [0]

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
            
    
            start_time = perf_counter()
            mst = prim_unsorted(g)
            end_time = perf_counter()
            total_time_unsorted += (end_time - start_time)

            #print(f"Result: {mst}")
        print(f"Average time for Heap APQ: {total_time_heap/AMOUNT_OF_TEST_CASES}")
        print(f"Average time for unsorted list APQ: {total_time_unsorted/AMOUNT_OF_TEST_CASES}")


input()

            