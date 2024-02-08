from time import perf_counter

def grow_by_append(size):
    my_list = []

    for i in range(size):
        my_list.append(i)

def grow_by_insert0(size):
    my_list = []

    for i in range(size):
        my_list.insert(0, i)
    
for i in range(6):
    size = 10**i

    start_time = perf_counter()
    grow_by_append(size)
    end_time = perf_counter()
    append_result = '{:.30f}'.format(end_time - start_time)

    start_time = perf_counter()
    grow_by_insert0(size)
    end_time = perf_counter()
    insert_result = '{:.30f}'.format(end_time - start_time)

    print("Append: Result with " + str(size) + " items: " + str(append_result) + "s")
    print("Insert: Result with " + str(size) + " items: " + str(insert_result) + "s")