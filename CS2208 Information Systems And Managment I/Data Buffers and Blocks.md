- Data in 'non-volatile' storage (HDDs and SSDs) are organized into blocks.
- Most DBMS have a *memory based data buffer* to improve performances

# Data Buffer Manager
- Data Buffer Managers manages buffer requests
![[Pasted image 20231209202258.png]]

## Data Buffer Replacement
- Least Recently Used scheme when removing another block

# Pinning Blocks
- Blocks can be pinned to ensure consistency
- For instance, if a block has been read into to memory and is being accessed, if that block was evicted and replaced, the read operation would be corrupt
	- Pinning prevents this

# Block Locks
- Blocks are locked to ensure consistency
- Certain actions are permitted for one or a subset of users if they hold a lock
	- Others users must wait to carry out their actions until they have a lock too
- There can be shared or exclusive blocks
	- Exclusive means only one process can work on a locked block