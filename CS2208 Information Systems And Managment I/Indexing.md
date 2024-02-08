- A technique to optimise operational time of queries by using *data structures*

- We can index an attribute,
	- This creates a binary tree, that allows the system to search more efficiently for tuples with a particular value (O(n) -> O(log n))

- Syntax:
```
CREATE INDEX <index_name> ON <table_name>(<attribute_list>)
```

**Example**
- In this example, we've previously indexed the Primary Key in the Student table
- The index is stored as a B+ tree, so we can perform a Binary Search
![[Pasted image 20231206165541.png]]
