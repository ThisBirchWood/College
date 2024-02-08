- Integrity Constraints ensure that changes made to the database don't cause any inconsistencies
- These constraints are defined when a table is created

# Not Null
- Says that a given attribute cannot have a null value, it must have a value
- Primary Key must be *not null*

# Check
- Check allows us to ensure that attributes satisfy certain conditions
- Example:
```
CREATE TABLE instructor 
( 
	id int, name varchar(20) NOT NULL, 
	dept varchar(20), 
	salary numeric(8,2) CHECK (salary > 0), 
	PRIMARY KEY (id) 
);
```

# Referential Constraints
- We often wish to ensure that a value that appears in one relation also appears in some other relation.
![[Pasted image 20231206165739.png]]
- "REFERENCES"

# Cascades
- When a referential integrity constraint is violated, the attempted operation in rejected
- We can override this with cascades
```
FOREIGN KEY (deptid) REFERENCES department ON DELETE CASCADE
```
- When you try to delete this table, it will also delete the department table.