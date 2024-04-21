- **Stable**: doesn't change the order of elements of the same value
- **In-place**: doesn't create a new list
	- Saves space
# Bubble Sort
- Worst case: O(n^2)
- Stable + in-place
- Bubbles the biggest element to the top, over and over
- Very slow, never used

# Selection Sort
- Worst case: O(n^2)
- In-place + not stable
- Uses a PQ to sort
![[Pasted image 20240418122413.png]]

# Insertion Sort
- Worst case: O(n^2) (usually better than this)
- In-place + stable
- Uses a PQ in theory, but in practise it's not needed
![[Pasted image 20240418122727.png]]

# Heap Sort
- Worst case: O(n log n)
- In place possible + not stable
- Uses a binary heap PQ
- Puts everything into a heap PQ, and then constantly takes the top element out
- Slower than other O(n log n) algorithms

# Merge Sort
- Worst case: O(n log o)
- In-place (possible but difficult) + stable
![[Pasted image 20240418124012.png]]
- Splits list up until in sizes of 2 or 1 and sorts back up
- Divide, conquer, combine

# Quick Sort
- Worst case: O(n^2) but still faster than most O(n log n) algorithms
- In-place + not stable
- Similar to merge sort, but instead splits on a chosen pivot
	- **Lomuto**: chooses last item as pivot value
		- It puts all values less than the pivot on the left
		- All values bigger than the pivot of the right
		- [4, 7, 2, 1, 5, 9, 3] -> [2, 1, 3, 4, 5, 9, 7]
		- It is then split into [2, 1] and [4, 5, 9, 7] (pivot is left out and is in the right place)
	- **Hoare**: choses first item as pivot value
		- Searches the list from the left, looking for the first value bigger than the pivot
		- Searches the list from the right, looking for the first value smaller than the pivot
		- Swap items if list hasn't been fully searched
- Recursive
- Very fast, only practically beaten by Timsort
# Counting Sort
- Worst case: O(n + k)
	- Where *k* is the range of possible numbers in the list
	- List contains integers from the set {0,1,......, k-1}
	- If k is smaller than n, then it's O(n), if *k* is much bigger, then it's O(n^2)
- Stable (2nd version) + in-place
- 2nd version does things slightly differently (in order to keep the original items)
	- In the count list, it loops through and adds the previous value in the list to the current one
		- It *sums* the entries so far
	- This gives the amount of elements less than or equal to that element in the input list
# Radix Sort
- Worst case time complexity not clear
	- Based on number of items in key words, and number of items
- Not in place
- Is based off of Counting Sort
	- Counting sort is ran twice
	- First on the second element
	- Then on the first
![[Pasted image 20240418143811.png]]
- O(n + k) for the first sort
- O(n + k) for the second sort
- k is 100, or k = 63 if you know the range is (32-93)