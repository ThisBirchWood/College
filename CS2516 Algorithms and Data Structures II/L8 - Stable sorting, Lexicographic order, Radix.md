- Stable sort maintains the input order (excluding the ones moved due to the sorting itself)
- It keeps the original order of a pair of items that have equal keys
- **Formal Definition**: A sorting algorithm is *stable* if and only if for any pair (i, j) where xi.k == xj.k and i < j, then p(xi) < p(xj)

## Which sorting algorithms are stable?
- Bubblesort - yes
- Selectionsort - no
- Insertionsort - yes
- Heapsort - no
- Mergesort - yes
- Quicksort - no
- Countingsort - yes, version 2

# Lexicographic order
- For two strings of characters, add a sequence of 'a' chars to the end of the shorter one, so that they are the same length
- string *s* is *lexicographically* before *t* if and only if 
	- s[0] < t[0], or
	- s[0] == t[0] and s[1] < t[1], or
	- s[0] == t[0] and s[1] == t[1] and s[2] < t[2]......

# Radix Sort
- Counting Sort(v2) is called *Radix* sort
- Say you have a list of tuples
	- [(4,1), (7,1), (3, 2), [7,2], [9, 2]]
	- Sort the list by the 2nd element
	- Then sort by the 1st element
	- This sorts the list lexicographically
- Can also be used to sort integers in a list
	- By sorting by the second digit of the int first
	- Then the first digit
- More efficient than counting sort
# Summary of Sorting Algos
## Bubblesort
- Simple, easy to understand, stable and in-place
- Worst case: O(n^2)
- Very slow, almost never used
## Selectionsort
- Reasonably easy to write + understand, in-place
- Not stable
- O(n^2)
- Quite slow (not as bad as bubblesort), still rarely used
## Insertionsort
- Reasonably easy to write + understand, in-place, stable
- O(n^2)
- Usually better than other O(n^2), reasonably fast of smaller inputs
- Used in recursive algorithms when the input list gets below a certain size
- Used for online streaming of incoming data
## Heapsort
- Complex to write, requiring a heap data structure
- Can be written in place, not stable
- O(n log n)
- Slower than other O(n log n) algorithms, not used anymore (heap is used, just not heapsort)
## Mergesort
- Reasonably easy to understand (good for linked lists)
- Difficult to write as in-place
- Most implementations are stable
- O(n log n)
## Quicksort
- Basic idea is simple, but tricky to implement
- Can be written as in-place
- Not stable
- O(n^2), though average complexity is O(n log n), and is usually faster than other O(n log n) algorithms
- For a long time, thought to be the best practical algorithm, now thought to be [[#Timsort]]
## Counting Sort
- Not based on comparisons
- Simple to understand and write
- Normally stable
- O(n+k), where k is the range of values to be sorted
- Requires O(k) additional space
## Radix Sort
- Not based on comparisons
- Multiple iterations of counting sort on different keys
- Stable, not in-place
- Worst case time complexity is not clear

# Timsort
- Used in Python under the hood since 2002, by Tim Peters
- Combines mergesort and insertion sort
- Designed to perform well when the data is already partially sorted. 
- Stable
- Timsort:
	- Looks for 'runs', sequences of items that are already sorted
	- merges runs together
	- runs of short length are combined with largers ones using insertion sort
	- but too complex to explain fully
- Worst case: O(n log n), best case: O(n)
- Believed to be faster than Quicksort in most cases