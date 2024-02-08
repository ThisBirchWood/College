# Memory Technologies
- SRAM - keeps the data as long as it's powered
	- used in cache
- DRAM - keeps the charge for a few milli-sec -> needs to be refreshed
	- used in RAM (DDR)
- Flash memory (EEPROM)
	- used in embedded systems, usb sticks
- Magnetic Disk
	- Platters having tracks split into sectors
	- Large access time

# Memory Hierarchy
![[Pasted image 20231123134425.png]]

## Principle of Locality
- Programs access a small proportion of their address space at any time 
- Two main types of locality
	1) *Temporal Locality*
		- If you access a piece of data in memory, you're likely to access it again in the near future
		- Example: a variable in a loop will be accessed again and again
	2) *Spatial Locality*
		- If you access a piece of data in memory, you're likely to access nearby data
		- Example: if you read an element in an array, you'll probably read the next elements in the array
## Memory Performance
- Memory Hierarchy is transparent to the programmer
	- The machine should automatically assign locations depending on runtime usage patterns (locality)
- Memory organization impacts the computer's performance massively

# Memory Blocks

## Main Memory Blocks
- Contains the code and data of active applications stored in units called blocks (sometimes they're called lines)
## Cache Blocks
- Cache blocks contain a subset of main memory blocks
- When transferring data between cache and main memory, it's done entirely in blocks
## Processor Access
- The processor deals *only* with cache, it never directly accesses or writes to the main memory.
- The processor requests **data/code** words using their *physical memory address*
![[Pasted image 20231123135500.png]]

## Memory Dynamics
- Let's say the processor needs to access data in *Block X*
	- **Memory Hit**: processor finds *Block X* in the cache
	- **Memory Miss**: *Block X* is not currently in the cache
		- *Block X* to be copied from main memory to cache (delay penalty)
![[Pasted image 20231127121704.png]]

**What happens on cache misses?**
1. Stall the CPU pipeline (Send PC value to memory)
2. Fetch block from a lower level of hierarchy
	- Instruct memory to perform a read and wait for memory to complete access
	- Update the cache
3) Resume execution

## Measure Memory Performance
- Hit/miss ratio
	- percentage of memory accesses that results in a memory hit/miss
	- hit ratio α
- Average memory access time -> (t^a)
	- t^a = αt^h + (1-α)t^m
		- A *high hit ratio* is good
		- A small hit time (t^h) is good
		- A smaller miss penalty (t^m) is good

# Direct Mapped Memory Organization
## Where can a block be placed?
- The physical address -> cache block location
- Physical address is split into three parts
 ![[Pasted image 20231127123934.png]]

### Example
- Consider a 64-block cache with 16 bytes/block
- To which cache block does address 1200 belong to?
![[Pasted image 20231127124110.png]]
- Belongs to block 001011 (block 11)

## How is a block found?
- Store the tag of the memory blocks in cache
- Check if the tag exists in the memory or no.
- The claimed cache size refers to the data space without the additional overhead such as the TAG or VALID bits.

### How do we know the cache block has valid data?
- *Valid Bit*: 1 = present, 0 = not present
- On machine boot, all is 0

## Hardware Implementation
![[Pasted image 20231127125438.png]]
- Index refers to each cache memory location (in this example there are 1024)
- When the CPU searches for a memory address, it goes to the index and checks if the tag and upper 20 bits of the address match (and if the valid bit is 1), if it is, then it's a match

### Cache Size
- Cache size = number of blocks * (block size + tag size + valid field size)
- Tag size = Address size - (index bits + offset bits)

## What block is replaced on a miss?
- In directly-mapped memory, there's only one possible place for every block

## How are cache writes handled?
### Write Hit (Block is in cache)
#### Write-through technique
- Update *both* cache and next lower level memory hierarchy (slow but consistent)

- Often this is done using a *write buffer*
	- A buffer holds data waiting to be written to memory
	- CPU continues working
		- Will only stall when the write buffer is full
#### Write-back technique
- Update the main memory only when the entire block is replaced (fast but inconsistency between levels)
- Good option when there are frequent block writes and/or slower memory

### Write Miss (Block is not in cache)
#### Write-Allocate
- Load the block into the cache and update the cache
#### No Write Allocate
- Update the written address using write through without loading the block.

## Large or small block size?
- **Large Blocks**
	- Reduces miss rate due to spatial locality
	- Larger miss penalty
	- Higher miss rate (fewer blocks in a fixed cache size)???

# Measuring Cache Performance
- CPU time = (# CPU execution cycles + CPU stalls cycles) * cycle period
- Memory-Stall clock cycles = (Read-stall cycles + Write-stall cycles)
	- Read-stall cycles = (reads/program) * Read miss rate * Read miss penalty
	- Write-stall cycles = ((writes/program) * Write miss rate * Write miss penalty) + Write buffer stalls

## Example
- Find the actual CPI
**Info**
- Instruction-cache miss rate = 2%
- Data-cache miss rate = 4%
- Miss penalty = 100 cycles
- Base CPI = 2
- Load and stores are 36% of instructions

**Calculations**
- 2% of 100 = 2 (Find the average CPI that the instruction cache misses add)
- 36% of 4% of 100 = 1.44 (Average CPI of memory cache misses)
- 2 (base CPI) + 2(instruction cache) + 1.44 (memory cache)
			= 5.44 (actual CPI)

## Average Memory Access Time (AMAT)
- AMAT = Hit time + (Miss rate x Miss penalty)


# Associative + N-Way Set Associative Cache 
## How do we reduce miss rate?
- Flexible block location to reduce the competition for cache blocks
- This is known as associative caches

## Fully Associative caches
- Any memory block can go to any cache entry
- We must search all entries at once to reduce hit time (HW solution)

## N-Way Set-Associative Caches
- A memory block can be located to a set of n cache blocks
- There are now multiple places (n places) for a block to be stored
- One tag can map to n places
- Downside is, we must now check n places to find a tag

![[Pasted image 20231202140919.png]]

## How Much Associativity?
- *Increased* associativity decreases miss rate (but has diminishing returns)
- Better performance requires additional hardware
![[Pasted image 20231202141316.png]]

## Replacement Policy with Set Associative
- Which set to use?
### Least-Recently Used (LRU)
- Choose the one unused for the longest time
- Simple for 2-way, manageable for 4-way, too hard beyond that
### Random
- Randomly choose one
- Gives roughly the same performance as LRU

# Improving Cache Performance
## Multi-Level Cache
- Level 1 cache (Primary Cache): service the CPU, very small (~KB), but very fast
- Level 2 cache (~MB): services misses from primary cache
![[Pasted image 20231202141900.png]]

- L1 cache and block size smaller than L2 cache