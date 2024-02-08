- The Binary Heap is a type of binary tree where:
	- every node has lower (or equal) key than it's children
	- every level (except maybe last) is complete
![[Pasted image 20231126174420.png]]
- For example, in this Binary Heap, the next element to be added would be the right child of 41.

# Adding to a binary heap
![[Pasted image 20231126174550.png]]
- Say we wanted to add 31 to this binary heap

**Method**:
1) We add a node to 41 (it's right child), with the value of 31
2) We check if the value of the new node is bigger or smaller than it's parent value
	1) If it's smaller, then swap with the parent
	2) If it's bigger or equal to, leave it
3) Repeat step 2 until the element is in the right position

# Removing the top from a binary heap
- remove_min()

- Say we want to remove the top element from this heap (25)
![[Pasted image 20231126175102.png]]

**Method**:
1) Swap the latest element added (60) and the top element, so that 60 would now be on the top of the heap
2) Remove the element containing 25 (which is now at the bottom)
3) Keep swapping the 60 element down until it's in the right position
	- Swap with the lower value child always

# Swapping to array-based implementation
