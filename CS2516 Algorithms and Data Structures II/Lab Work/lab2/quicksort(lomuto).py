import random
from time import perf_counter

test_list = [random.randint(0, 1000) for i in range(10)]
print(test_list)

def quicksort_lomuto(mylist):
    _quicksort_lomuto(mylist, 0, len(mylist)-1)

def _quicksort_lomuto(mylist, start, end):
    if start < end:
        b = start
        pivot_index = random.randint(start, end)
        pivot = mylist[pivot_index]

        mylist[end], mylist[pivot_index] = mylist[pivot_index], mylist[end]
        
        for i in range(start, end+1):
            if mylist[i] < pivot:
                mylist[i], mylist[b] = mylist[b], mylist[i]
                b += 1

        mylist[end], mylist[b] = mylist[b], mylist[end]

        _quicksort_lomuto(mylist, start, b-1)
        _quicksort_lomuto(mylist, b+1, end)

start = perf_counter()
quicksort_lomuto(test_list)
print(test_list)
end = perf_counter()
print(end-start)