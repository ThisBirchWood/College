import random, time

test_list = [random.randint(0, 100) for i in range(10000)]

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

start = time.perf_counter()
insertion_sort(test_list)
end = time.perf_counter()
print(end-start)