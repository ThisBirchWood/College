# 1NF
- This will transform an unnormalized schema into a 1NF scheme (First Normal Form)
- 1NF requires that:
	- Each column in a table must contain *atomic* values.
	- Each row must have at least one unique identifier, a primary key

# 2NF
- 2NF requires that:
	- The DBMS already be in 1NF
	- **No Partial Dependencies**: If there are multiple primary keys in a table, then the other non-key attributes must depend on both of the primary keys, not just one
# 3NF
- 3NF requires that:
	- The DMBS already be in 2NF
	- There are no **transitive dependencies** 
		- No non-key attribute is dependant on another non-key attribute

# BCNF
- BCNF requires that:
	- The DBMS already be in 3NF
	- 