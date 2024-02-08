# Dictionaries + Maps
- A *dictionary* (or map) is a storage and look-up structure maintaining key,value pairs

# Map ADT
- getitem(key) = return the element with the given key, or None if not there
- setitem(key,value) = assign value to element with key; add new if needed
- contains(key) = return True if map has an element with that key
- delitem(key) = deletes element with key; or return None
- length() = returns the length of the map

# Hash Tables
- Hash tables can be used to implement a map

## How to?
- Maintain a list of a *known* size.
- To add a new item
	1) Compute an integer corresponding to a key (Python hash() function)
	2) Compute an index in the list based on that integer and list size
		- location(k) = h mod N (where k is the key, and N is the length of the list)
	3) Store the item in the list at that index
![[Pasted image 20231207133310.png]]

## Separate Chaining
- Some hashes will collide (they will map to the same index)
- To fix this, each cell in the list will maintain it's own list of values
![[Pasted image 20231207133851.png]]