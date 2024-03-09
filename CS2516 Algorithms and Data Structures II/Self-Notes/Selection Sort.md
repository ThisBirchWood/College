# Sorting using Priority Queues
- A [[Priority Queue]] is a data structure in which we can add item, and from which we can remove the item with the top priority
- Sorting Algorithm: for each item in our list, add it to the PQ, then repeatedly remove the top item from our PQ and put in successive cells in a list
```Python
def pq_sort(mylist):
	pq = PriorityQueue()
	for i in range(len(mylist)):
		pq.add(mylist[i], None)
	for i in range(len(mylist)):
		mylist[i], x = pq.remove_min()
```

# In-place sorting
- Sorting using a separate priority queue uses significantly more space (double the space)
- In many applications, space is limited, so we may only want to use the original input array
	- This is called *in-place* sorting

# Selection Sort
- Not stable
- Quite slow


- Treat the unsorted, input array as the PQ list implementation
- Instead of removing the top item, swap it into the correct cell and shrink "view" of PQ

- Find the smallest item, swap it with cell 0
![[Pasted image 20240305131957.png]]![[Pasted image 20240305132030.png]]
- Continue until sorted
![[Pasted image 20240305132048.png]]

## Implementation
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
- Worst case: O($n^{2}$) comparisons, and *n* swaps

