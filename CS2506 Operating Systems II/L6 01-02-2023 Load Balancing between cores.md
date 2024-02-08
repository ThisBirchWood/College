---
default_file: Notes/Lecture 5.pdf
---
- For many CPU cores, different types of process scheduling include:
	- group-based sch
	- load balancing


```slide-note
file: Notes/Lecture 4.pdf
page: 10
```
- Each domain contains one or more core groups
```slide-note
file: Notes/Lecture 4.pdf
page: 11
```
- Fabrics connect the L2 cache to main memory
- A B package is more powerful than an A package, C more powerful than B
- The cores are organised hierarchally
	- Can be organised into a binary tree, with A packages as the leaf nodes and the C package as the root
	- If there is a low load on the CPU, it will only use the lower levels (A packages), however more load and it will move up the tree
- How do they decide how to balance the load?
```slide-note
file: Notes/Lecture 4.pdf
page: 12
```
- Moving processes from one core to another is time consuming, therefore balancing is costly and shouldn't be done extremely often
- In the above diagram, 2 cores have the same L2 cache, which means that when a process needs to be moved to a different package, it's memory in cache too needs to be moved.
- A process is said to have no *cache affinity* if it's memory in the L2 cache does not depend on any other process and doesn't affect any other process
	- A process with no cache affinity is viable for migration (to another package/core) because it can be moved without memory issues

- Packages have flags, which allow or disallow the moving of processes between domains/cores
	- For instance if you want to move a process from one "A" domain to another "A" domain, the parent "B" must have the flag set which allows the moving of processes
```slide-note
file: Notes/Lecture 4.pdf
page: 13-14
```
- For point 3, when it says "stop" the low priority process, it means cut off it's ability to use the L2 cache, meaning the high priority core has full use of the cache
```slide-note
file: Notes/Lecture 4.pdf
page: 15
```
- "Rebalance tick" refers to how often the system checks the load balance and if it's unbalanced, it balances it
- If the load stays balanced, then you can increase the *rebalance tick*
```slide-note
file: Notes/Lecture 4.pdf
page: 16
```
1) Load can be represented as number of processes
	- If there are 1 or 2 processes, then the core is underloaded
	- If there are 20 processes, then the core is overloaded
	- However different processes can have different workloads

- Formula for the power consumption of a circuit
- P = fV^2C + L
	- P = Dynamic power consumption
	- f = clock frequency
	- V = voltage
	- C = capacitive load
	- L = fraction of transistors being switched in a clock cycle

```slide-note
page: 2-3
```
- Intel now uses big.LITTLE arch (or something similar)