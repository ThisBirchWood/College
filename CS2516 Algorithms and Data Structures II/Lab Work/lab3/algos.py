import random, math
from time import perf_counter

################################
########### PRIVATE  ###########
################################
def _merge(list1, list2, output_list):
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

def _quicksort_lomuto(mylist, start, end):
    if start < end:
        b = start
        pivot = mylist[end]
        
        for i in range(start, end+1):
            if mylist[i] < pivot:
                mylist[i], mylist[b] = mylist[b], mylist[i]
                b += 1

        mylist[end], mylist[b] = mylist[b], mylist[end]

        _quicksort_lomuto(mylist, start, b-1)
        _quicksort_lomuto(mylist, b+1, end)


def _quicksort_hoare(mylist, start, end):
    if start < end:
        pivot = mylist[start]
        b = start - 1
        s = end + 1

        while True:
            b += 1
            while mylist[b] < pivot:
                b += 1

            s -= 1
            while mylist[s] > pivot:
                s -= 1

            if b >= s:
                break

            mylist[b], mylist[s] = mylist[s], mylist[b]

        _quicksort_hoare(mylist, start, s)
        _quicksort_hoare(mylist, s+1, end)


def _quicksort_lomuto_random(mylist, start, end):
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


def _quicksort_hoare_random(mylist, start, end):
    if start < end:
        pivot_index = random.randint(start, end)
        pivot = mylist[pivot_index]
        mylist[pivot_index], mylist[end] = mylist[end], mylist[pivot_index]
        b = start - 1
        s = end + 1

        while True:
            b += 1
            while mylist[b] < pivot:
                b += 1

            s -= 1
            while mylist[s] > pivot:
                s -= 1

            if b >= s:
                break

            mylist[b], mylist[s] = mylist[s], mylist[b]

        _quicksort_hoare(mylist, start, s)
        _quicksort_hoare(mylist, s+1, end)


################################
########### PUBLIC #############
################################


def merge_sort(mylist):
    if len(mylist) > 1:
        mid = len(mylist) // 2
        list1 = mylist[:mid]
        list2 = mylist[mid:]

        merge_sort(list1)
        merge_sort(list2)

        _merge(list1, list2, mylist)

def insertion_sort(mylist):
    n = len(mylist)
    i = 1
    while i < n:
        j = i-1
        while mylist[i] < mylist[j] and j > -1:
            j -= 1
        temp = mylist[i]
        k = i-1
        while k > j:
            mylist[k+1] = mylist[k]
            k -= 1
        mylist[k+1] = temp
        i += 1

def max_heap_sort(mylist):
    length = len(mylist)

    for i in range(length):
        if i > 0:
            j = i
            parent_index = math.floor((j-1)/2)
            while mylist[parent_index] < mylist[j] and j > 0:
                mylist[parent_index], mylist[j] = mylist[j], mylist[parent_index]
                j = parent_index
                parent_index = math.floor((j-1)/2)

    j = length-1

    while j > 0:
        mylist[0], mylist[j] = mylist[j], mylist[0]
        j -= 1
        
        index = 0
        if (index*2)+1 > j:
            break
        elif (index*2)+2 > j or mylist[(index*2)+1] >= mylist[(index*2)+2]: 
            next = (index*2)+1
        else:
            next = (index*2)+2

        while mylist[index] < mylist[next]:
            mylist[index], mylist[next] = mylist[next], mylist[index]
            index = next
            if (index*2)+1 > j:
                break
            elif (index*2)+2 > j or mylist[(index*2)+1] >= mylist[(index*2)+2]: 
                next = (index*2)+1
            else:
                next = (index*2)+2

def quicksort_lomuto(mylist):
    _quicksort_lomuto(mylist, 0, len(mylist)-1)

def quicksort_hoare(mylist):
    _quicksort_hoare(mylist, 0, len(mylist)-1)

def quicksort_lomuto_random(mylist):
    _quicksort_lomuto_random(mylist, 0, len(mylist)-1)

def quicksort_hoare_random(mylist):
    _quicksort_hoare_random(mylist, 0, len(mylist)-1)



