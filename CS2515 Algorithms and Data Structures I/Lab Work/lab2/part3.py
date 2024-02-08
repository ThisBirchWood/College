from time import perf_counter

def read_garda_stations_tuples():
    """ Read and return a list of garda stations. """
    all_stations = []
    file = open('garda_stations.txt', 'r')
    for line in file:
        line = line.replace('\n','')
        new_tuple = tuple(line.split('\t'))
        all_stations.append(new_tuple)
    file.close()
    return all_stations

def linear_search(name):
    data = read_garda_stations_tuples()
    result = None
    for tup in data:
        if tup[0] == name:
            result = tup
    
    if result == None:
        return "Does not exist"
    else:
        return result
    
def binary_search(name):
    data = read_garda_stations_tuples()

    start = 0
    end = len(data) - 1
    
    while end > start:
        middle = (start+end) // 2
        middle_value = data[middle][0]

        if middle_value > name:
            end = middle - 1
        elif middle_value < name:
            start = middle + 1
        else:
            return middle, middle_value
        
'''
start_time = perf_counter()
linear_search("Youghal")
end_time = perf_counter()
pop_result = '{:.30f}'.format(end_time - start_time)

start_time = perf_counter()
binary_search("Youghal")
end_time = perf_counter()
pop0_result = '{:.30f}'.format(end_time - start_time)

print("Linear Search Results: " + str(pop_result) + "s")
print("Binary Search Results: " + str(pop0_result) + "s")
'''

def bubble_sort():
    data = read_garda_stations_tuples()

    for i in range(len(data)):
        for j in range(len(data) - i - 1):
            if int(data[j][2]) < int(data[j + 1][2]):
                data[j], data[j + 1] = data[j + 1], data[j]

    return data

start_time = perf_counter()
bubble_sort()
end_time = perf_counter()
bubble = '{:.30f}'.format(end_time - start_time)

start_time = perf_counter()
read_garda_stations_tuples().sort()
end_time = perf_counter()
builtin = '{:.30f}'.format(end_time - start_time)

print(bubble)
print(builtin)