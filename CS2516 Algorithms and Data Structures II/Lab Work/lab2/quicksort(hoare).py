import random

#random.seed(10)
test_list = [random.randint(0, 100) for i in range(10)]
print(test_list)

def quicksort_hoare(mylist):
    _quicksort_hoare(mylist, 0, len(mylist)-1)

def _quicksort_hoare(mylist, start, end):
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


quicksort_hoare(test_list)
print(test_list)