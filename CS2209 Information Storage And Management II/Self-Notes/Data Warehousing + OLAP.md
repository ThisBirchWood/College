# Operational Databases
- An operational database is a database that supports the day-to-day operations of a company
- These databases can't easily be analysed
- These databases use what is known as an **OLTP** System

# OLTP (Online Transaction Processing)
- Processes a transaction according to rules (ACID)
- Performs all elements of a transaction with very low latency
- Is able to support concurrent transactions

- OLTP systems are used in many sectors, such as:
	- Order tracking
	- Invoicing
	- Credit Card processing
	- Banking
	- Airline Reservations
- OLTP is commonly used in businesses that require real-time transactions, and they ensure consistency so that no data is lost or corrupted.

# OLAP (Online Analytical Processing)
## Requirements
- Must support multidimensional analysis
	- These types of databases must provide tools to examine dimensional data (cubes)
- Fast retrieval times
- Calculation engine that can handle specialized multidimensional math

# OLTP vs OLAP
- OLTP:
	- Handles recent operational data
	- Smaller size, ranging from 100MB to 10GB
	- Used for day-to-day operations
	- Uses simple queries
	- Fast processing speeds
	- Read/write operations
- OLAP
	- All historical data
	- Very large size, ranging from 1TB to 100PB
	- Goal is to provide analytical data that business decisions can be made from
	- Complex queries
	- Slower processing speeds
	- Only write operations (periodically updated)

# Data Warehouse
- Data Warehouse is an *integrated*, *subject-oriented*, *time-oriented*, *non-volatile* database that provides support for decision-making in business
- Most of the time, the database is read-only
	- Has very powerful read capabilities, able to provide multi-dimensional data in many different forms
- Centralized database
- Periodically updated, data is never removed from it
- Is *very* costly to make

![[Pasted image 20240226100748.png]]

## Integrated
- These databases are constructed by *integrating* multiple, heterogeneous data sources
	- Old, smaller relational databases, flat files, online transaction records
- *Data cleaning* and *data integration* techniques are applied to ensure consistency

## Subject-oriented
- Organized around major subjects, such as customer, product, sales....
- These databases are focused on analysis of data for decision makers
	- Not concerned with transactions or real-time processing
- Excludes data not useful in decision making

## Time-oriented
- An operational database only stores the current value data
	- However a *data warehouse* stores data for much longer
	- Could be more than 10 years
- Almost every key structure in a data warehouse contains an element of **time**, explicitly or implicitly

## Non-volatile
- Independence
	- A physically separate store of data different from the operational environment
- Operational update does not occur
- Doesn't require transaction processing, recovery or concurrency control mechanisms

# Benefits of Data Warehouses
- Return on investment
	- Data warehouses are extremely expensive
	- However, they've been shown to provide a return on investment of over 400% per annum
- Provide a competitive advantage
	- Gives complex information that is useful in identifying new markets, predictive analytics and trends
	- Still requires clever analysts