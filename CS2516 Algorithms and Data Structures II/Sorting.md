# Bubble Sort
```Python
def bubble_sort(mylist):
	n = len(mylist)
	for i in range(n-1):
		for j in range(0, n-i-1):
			if mylist[j] > mylist[j+1]:
				mylist[j], mylist[j+1] = mylist[j+1], mylist[j]
```
- Worst case: O(n^2)
- Very poor algorithm, not really used, only reason it's used it's because of it's ease of writing

# Sorting using [[Priority Queue|Priority Queues]]
- You can use a priority queue to sort items
- For each item in our list, we add it to the PQ, then repeatedly remove the top item from the PQ and add it to another list
```Python
def pq_sort(mylist):
	pq = PriorityQueue()
	for i in range(len(mylist)):
		pq.add(mylist[i], None)
	for i in range(len(mylist)):
		mylist[i], x = pq.remove_min()
```
- This is a poor algorithm if you're worried about space, this takes up double the amount of space compared to a normal sorting algorithm 
# In-place Selection Sort
- Treat the unsorted input array as the PQ list implementation (so no build cost)

- Find the smallest item, swap it with cell 0
- So on and so forth [[Database Management Systems (DBMS)]]

```Python
def selection_sort(mylist):
	n = len(mylist)
	i = 0
	while i < n:
		smallest = i
		j = i+1
		while j < n:
			if mylist[j] < mylist[smallest]:
				smallest = j
			j += 1
		mylist[i], mylist[smallest] = mylist[smallest], mylist[i]
		i += 1
```
- Worst case: O(n^2)
- Best case: O(n^2)

# Sorting with a *sorted* linked list PQ
- *Insertion sort*: main task is inserting each item in the right place
- 