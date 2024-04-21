# Batch Processing
- The oldest method, the CPU is allocated to one process until completion
- Starves all other processes

# Round-Robin
- Time-sharing the CPU
- If a process doesn't finish during its time slice, it's returned to the end of the queue

## Example: Shortest Process First
- If the CPU is *not* time-shared, the order of processes is important
- Processes can be ordered according to execution time
- ***Turnaround Time***: the amount of time from the moment the process is *ready* to execute (not when it executes) to when it completes execution

- Example: three processes with execution times of:
	- A: 40ms
	- B: 60ms
	- C: 20ms
![[Pasted image 20240415100952.png]]
- However if they're ordered by execution time (C, A, B):
![[Pasted image 20240415101015.png]]

# Priority Scheduling
- Since some processes need to be interactive, and some are computationally demanding, some processes need to be dealt with differently
- We can assign priorities to processes
- Fast, interactive, low-latency processes will have a high priority
	- Computation strong ones will have a low priority
- If there are processes with the same priority, they will be scheduled in a round-robin manner

## Multi-level Feedback Queues
- Several queues, each associated with a priority level

- When a processes gets assigned to a certain priority level, it will move through the queue until it executes
- If it does not finish, it will move down a priority level, **into** another queue (lower priority one)
- This continues until it reaches the lowest priority
	- At this level, the strategy is round-robin
- After being blocked, the processes gets a **priority boost**
![[Pasted image 20240415101621.png]]

## *Idle* Process
- Many systems have an *idle* process
	- Has the lowest priority
- The idle process will take control of the CPU when nothing else is there
- The idle process implements the **kernel power policy manager**
	- It owns decision-making and the set of rules used to determine the appropriate frequency/voltage operating state
	- This is done through the *CPU driver*
## Priority Inversion
- Priority Inversion occurs when a high priority process is blocked from running due to resources by a low priority process

- Say we have 3 processes: A, B, C
	- Process A is high-priority and is waiting for a shared resource from B
	- Process B is low-priority, but is executing code in a critical section
	- Process C has medium priority
- Since A is waiting, Process C will get all the CPU time, because it won't allow B to run

### Solution
- The scheduler randomly boosts the priority of ready processes
- The low priority process will run for long enough to exit the critical section and allow process A to run.

# Two-level Scheduling
- Two Level scheduling is done when there are many processes
- Since storing processes on the disk (and the act of restoring them to main memory) is too expensive
	- Leads to *thrashing phenomenon*

- A *higher-level, long-term* scheduler decides what subset of processes to allow to run in the main memory
- These processes are then managed by the *lower-level, short-term* scheduler

# Real-time Scheduler
- In real-time applications, computing systems reacts to events through interrupts
- Most popular technique for deadlines is *earliest deadline first*

## Earliest Deadline First
- Say we have three processes, A(300ms), B(500ms), C (1000ms), and a time slice is 100ms
- All processes are ready immediately
- *A* is selected first (lowest deadline)
	- Runs for 100ms, new deadline is then 400ms (300 + 100)
- *A* is selected again
	- Runs for 100ms, new deadline is then 500ms (300 + 100 + 100)
- Then *B* is selected (even though they both have the same deadline, B is selected because A ran before)
	- Runs for 100ms, new deadline is then 800ms (500 + 100 + 100 + 100)
![[Pasted image 20240415210249.png]]

