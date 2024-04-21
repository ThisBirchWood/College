- With mobile devices, we must *save energy* wherever possible, but also utilising fully the computing power of the CPU
- CPU designers created two types of cores, *little* and *big*
	- *little*: lower performance, lower energy usage
	- *big*: better performance, worse energy usage

# big.LITTLE model
- Schedulers starts by using little cores
- When workload increases, use big cores
	- Little cores to go sleep
- If workload decreases, switch to little cores

# Scheduling Strategies
## CPU migration
- Process gets assigned to a pair of cores
	- A pair can have a little core and a big core, or two of the same
- High workload = processes are swapped to the big cores in the pairs
- Low workload = processes are swapped to the little cores in the pairs

## Cluster Migration
- Cores are grouped into two clusters of two/four cores
- Workload is moved between clusters
![[Pasted image 20240418120947.png]]

## Global Scheduling
- A process can be executed by any core
- This load is then managed
![[Pasted image 20240418121453.png]]

# Apple MacBook Air M1/2
- M1 is an Apple CPU chip using 5nm technology (16B transistors)
- 4 little cores + 4 big cores
	- 7/8 GPU cores
- Total power consumption is 10W

- M2 has 8 big cores + 4 little cores
	- 19 GPU cores