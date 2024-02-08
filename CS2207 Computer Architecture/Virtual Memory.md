- *Virtual Memory* allows extending the memory size beyond main memory
- Extends the physical memory to the HDD
- Virtual Memory is managed jointly by the CPU hardware and the OS
![[Pasted image 20231202142304.png]]

- Programs share main memory
	- Each gets a private virtual address space holding the code and data
	- RAM is used as a "cache" for the *virtual memory file*
	- Virtual Memory "block" is called a **page**
	- Virtual Memory "miss" is called a **page fault**

# Virtual Memory Design
- **Goal**: Page Fault rates must be minimized 
- because then the page must be fetched from the disk, which takes *millions* of cycles

## How to achieve this design goal?
- **Fully Associative Placement** in the main memory
- **Smart Page Replacement**: OS prefers least-recently used (LRU) replacement
	- *Reference Bit* (aka use bit) in Page Table set to 1 when a page is accessed
	- Periodically reverted back to 0 by the OS
	- A page with reference bit = 0 has not been used recently
- **Practical Write Policy**
	- *Write through* is impractical
		- Disk writes takes millions of cycles
	- **Write-back** is used
	- *Dirty Bit* in Page Table set when page is written

# Virtual Address Translation
- CPU and OS *translate* virtual addresses to physical addresses
![[Pasted image 20231202143243.png]]

# Page Table
- Array of **Page table entries (PTE)**, indexed by a *virtual page number*
![[Pasted image 20231202143457.png]]

- *If page is present*: -> Page table entry stores the physical page number (valid = 1)
- *If not present*: -> Page table refers to address on disk (valid = 0)

# Address Translation
- *Each program* has it's own page table
	- Hardware includes a register that points to the start of the page table (for the current process)
	- **Page Table Register**

# Improving Address Translation Performance
- By using the **Translation Look-aside Buffer (TLB)**

- This is basically a cache of Page Table Entries within the CPU
- Typically contains between 16-512 *PTE*s
	- *Hit*: 1 cycle
	- *Miss*: 10 - 100 cycles
- 0.01% - 1% miss rate

## Translation Look-aside Buffer (TLB)
### TLB Misses
- Much more frequent than **true page faults**
- PTE is not in the TLB but page is in the RAM/page table
	1) Replaced PTE is copied back to page table