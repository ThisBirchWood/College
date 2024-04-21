- How do we make the most of computer resources?

# Resource Management
- Each application has performance requirements, often referred to as **Quality of Service** (QoS)
- These can be met by a minimal architecture
- These performances requirements can be translated into architectural requirements
	- This is known as a **Virtual Architecture**
	- Example: VA = {core0, core1, 4GB mem}
- Resources that are not allocated to any virtual architecture are called **resources in excess**

## System Management
- The system monitors the load of system resources
	- Takes action when a state of overload or underload is detected
	- It provides feedback to applications/users to inform on resource usage
	
In conclusion, the OS provides:
1) VA scheduler
2) Spatial partition
3) Feedback

# Scheduling
**
- Main challenge of the scheduler
	- Predict the resource needs of each process
	- Minimize shared resource contention
	- Maximize shared resource utilization
- The scheduler needs to be aware of:
	- The structure of the cores
	- Needs of the process
	- Inter-relationships between processes

- Example: a system with 2 packages, dual-core each package.
	- If an application has two processes (or threads), they can be allocated to different packages
	- This is minimize memory contention

## Approaches
1) If processes share data, schedule them on the same package
	- Otherwise, scheduling them together on a package leads to L2 contention
2) Scheduling processes on different packages maximises execution speed
	- But not optimal for energy

- Say all resources are busy
- The OS can still attempt to reduce resource contention
- This is done by grouping processes that use *different resources* onto the same package

## Process Prediction
- What resources a process may need in the future can be predicted using the *micro-architectural history* of said process.
	- Done with *performance counters*
- Sometimes this information might not be available, and the OS must predict what resources will be used through other metrics 

# Scheduling Domains
- *Load Balancing*: balance the load between the cores such that there is no idle core while others are overloaded
- A *domain-based* scheduler will load balance using a new data structure
![[Pasted image 20240417161233.png]]
- Each level is a domain
- Each domain will have it's own policies and properties
- Each domain contains a *core group* (2 cores)
	- The scheduler will balance work between core groups, not between cores

## Parameters for balancing
- What parameters allow for balancing?

**
1) *Balance Frequency*: How often should we balance?
2) *Unbalance*: How unbalanced can something get before we balance?
3) *Idle*: how long can a core sit idle before it loses its *cache affinity*?
4) load of other policy stuff

## Example of Policies
1) if *exec()* is invoked then
	- *exec()* removes cache affinity, so makes sense to leave it
	- determine the highest domain with load balancing flag set
	- move process to the least loaded core of the domain
2) if core is idle
	- determine overloaded core
	- move load to idle core
3) if processes in a core group have high/low priorities
	- idle the low priority core
	- this is to allow the high-priority process better access to the cache

# Active Balancing
- Moves processes within domains when things go out of balance
- *Rebalance Tick*: How often to balance
- If the system tends to stay in balance, the interval is allowed to grow
	- It checks its way up the domain hierarchy


