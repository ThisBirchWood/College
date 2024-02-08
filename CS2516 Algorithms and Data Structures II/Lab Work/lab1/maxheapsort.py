import random, math, time

test_list = [random.randint(0, 100000) for i in range(10000)]
print(test_list)

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

max_heap_sort(test_list)
print(test_list)

