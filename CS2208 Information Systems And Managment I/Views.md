- A view in SQL is a virtual table that's based on the result of a SELECT query.
- It does not store the data itself
- Provides a way to represent the result of a query as if it were a table


- Can be used to restrict the views of full tables for some users
	- For example, we might create a view for an office clerk that hides personal information about the instructions (address, salary)

## Restrictions on modifying data
- Data modification is dangerous through views (may violate relation constraints)
- Some DBMS support data modification through views, others don't allow this at all

# Creating Views
- Syntax:
```
CREATE VIEW <view_name> AS <query_expression>
```
- Example
```
CREATE VIEW faculty AS
SELECT id, name, dept_name
FROM instructor;
```
- We can then use a view as if it were a table
```
SELECT * FROM faculty;
```

# Materialised Views
- Differs from normal views, in that the results of a view are stored in the database
- View is recalculated when data changes.