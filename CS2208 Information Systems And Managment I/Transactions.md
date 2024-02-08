![[Pasted image 20231209203532.png]]
- If any of these steps failed, the state of the user's overall wealth would be inconsistent.

# ACID
- Transactions are said to have ACID properties
	- **Atomicity** - all operations are completed or none at all
	- **Consistency** - Any change maintains data integrity or the transaction is cancelled
	- **Isolation** - Any read or write of a transaction will not be impacted by another read of write of a transaction
	- **Durability** - After a transaction has completed, the changes will be persistent


# Serial vs Concurrent Execution
- Serial execution implies that transactions execute one after another
- Concurrent execution means transactions can run in parallel
- 