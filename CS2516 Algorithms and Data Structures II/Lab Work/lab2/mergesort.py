import random
from time import perf_counter

test_list = [random.randint(0, 1000) for i in range(10000)]
print(test_list)

def merge(list1, list2, output_list):
    t1 = 0
    t2 = 0

    while t1 + t2 < len(output_list):
        if t1 == len(list1):
            output_list[t1+t2] = list2[t2]
            t2 += 1
        elif t2 == len(list2):
            output_list[t1+t2] = list1[t1]
            t1 += 1
        elif list1[t1] > list2[t2]:
            output_list[t1+t2] = list2[t2]
            t2 += 1
        else:
            output_list[t1+t2] = list1[t1]
            t1 += 1


def merge_sort(input_list):
    if len(input_list) > 1:
        mid = len(input_list) // 2
        list1 = input_list[:mid]
        list2 = input_list[mid:]

        merge_sort(list1)
        merge_sort(list2)

        merge(list1, list2, input_list)

start = perf_counter()
merge_sort(test_list)
print(test_list)
end = perf_counter()
print(end-start)