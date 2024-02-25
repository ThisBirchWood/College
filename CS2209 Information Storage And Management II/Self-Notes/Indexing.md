- Indexing is a technique to optimise operational time of database queries using data structures
- This leads to faster query results
![[Pasted image 20240220131005.png]]

- The index exists as a file/table entity in the database
- Two types of indexes
	1) A **Primary Index** is an index specified on the primary key of the table
	2) A **Secondary Index** allows us to index on any non-primary fields of a file (the values would be unique or have duplicates)
# Measuring Query Efficiency
- To retrieve the details of a SQL query, we can use the "EXPLAIN" function
```SQL
EXPLAIN SELECT * FROM exampledata WHERE time = 26340
```

![[Pasted image 20240220130843.png]]

- We can see in the result that
	- There's no index (key is NULL)
	- All 541533 rows had to be examined to find all possible occurrences of the values

# How do Indexes work?
- Database is loaded into the main memory by reading files in the disk
	- It's stored in [[Computer Memory Organization#Memory Blocks|blocks]]
- When a query is executed, data is read from the memory (or worse, read from the disk) and it searches all the blocks in the memory for results
- Indexing helps us locate the specific blocks needed for that query
	- It gives a pointer to the needed blocks

- **Dense Index** -> The index has an entry for each row in the database table
- **Non-dense/Sparse Index** -> Index has an entry for some rows in database table
## Non-dense Primary Index
![[Pasted image 20240220160135.png]]
- On the left is the index file
	- The diagram shows a simplified version of the index file
	- In reality the index file contains a B+ tree
- On the right is the database itself, split into blocks
## Cluster Index
![[Pasted image 20240220160824.png]]

## Dense Secondary Index + Record Pointers for unordered key
![[Pasted image 20240220161036.png]]
# Indexing in SQL
- When we create an index in SQL, it creates a data structure ([[B+ Trees]])
- This allows the system to efficiently search for tuples that have a particular attribute.
	- It can then access that data pointer to the block it's stored in
- SQL index definition:
```MySQL
CREATE INDEX <index_name> ON <relation>(<attributelist>)
```

## Example
```mySQL
CREATE INDEX example ON exampledata('time');
```
![[Pasted image 20240220133316.png]]
- We can see that, after running this query, only one row needs to be accessed, as opposed to all 541,533 rows before the index


# Multi-level Indexes


