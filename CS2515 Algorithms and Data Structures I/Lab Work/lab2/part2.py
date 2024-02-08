from time import perf_counter

def pop_test(size):
    my_list = [1] * size

    for i in range(size):
        my_list.pop()

def pop0_test(size):
    my_list = [1] * size

    for i in range(size):
        my_list.pop(0)
    
for i in range(6):
    size = 10**i

    start_time = perf_counter()
    pop_test(size)
    end_time = perf_counter()
    pop_result = '{:.30f}'.format(end_time - start_time)

    start_time = perf_counter()
    pop0_test(size)
    end_time = perf_counter()
    pop0_result = '{:.30f}'.format(end_time - start_time)

    print("Pop: Result with " + str(size) + " items: " + str(pop_result) + "s")
    print("Pop0: Result with " + str(size) + " items: " + str(pop0_result) + "s")