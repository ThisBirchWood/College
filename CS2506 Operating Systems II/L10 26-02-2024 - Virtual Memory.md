---
default_file: Notes/Lecture 10.pdf
---
- Virtual memory is a hierarchy of different units with different characteristics:
	- Size
	- Access time

- Cache L1 - cache L2 - main memory - disks
- Size increase, but access time also increased
	- From nanoseconds to hundreds of milliseconds
- Reason for virtual memory is to keep commonly used data close to the CPU
- Virtual memory is transparent, user is not aware of it


```slide-note
page: 3-4
```
- Address bus = 32 bits
- Main memory = 4GB
- Part of the memory will be allocated to the kernel
	- 1GB = kernel
	- 3GB for user space
	- This 3GB is a hard limit for user processes
- Virtual addresses need to be translated to a real physical address
	- Normally done using paging
	- A page will have a given size (2kb, 4kb.....)
	- Say it's 4KB
```slide-note
page: 7
```
- 32 bit address
	- First 12 bits are used to select within the page
	- Rest of the bits are used to select the page number
	- That means we can have 2^20 pages
- You can have a much larger virtual space then physical space
	- Allows dynamic allocation of memory between programs
- Processes start with a number of *page frames* allocated to them
	- The OS assigns these
- The page table will contain 2^20 entries (PTEs)
```slide-note
page: 8
```
- If a page is modified, and it needs to be replaced in the main memory, its contents need to be saved in the main memory
```slide-note
page: 9
```
- 32 bit address split three ways now
	- First 12 bits
	- 10 bits
	- 10 bits
- The last 10 bits will be in a *directory* table
- The next 10 bits point to the *page table*
- 