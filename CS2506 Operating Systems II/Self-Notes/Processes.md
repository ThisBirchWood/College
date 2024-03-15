- Process Definitions
	- An instance of a running program
	- A process is the *context* associated with a program in execution
- A process performs a job
- User processes and OS processes exist

## Process Structure
- Consists of executables, its data, stack, other buffer memory and administrative information.
- Most of the administrative information is stored in the kernel.
## Context
- The context represents state information
	- program variables/values, stored in the user space
	- process ID, priority, owner, current directory.....

# Management Operations
1) **Create**: the internal representation of the process is created; initial resources are allocated
2) **Terminate**: release all resources; free the PID
3) **Change Program**: Replace the executable (by calling the system call *exec*)
4) **Block**: wait for an event; e.g., the completion of an I/O operation
5) **Awaken Process**
6) **Switch process**: process context switching
7) **Schedule process**: takes control of the CPU
8) **Set Process Parameters**
9) **Get Process Parameters**
![[Pasted image 20240311103639.png]]

# Child processes
- A process can create a child process, which is identical to it (except for PID)
- This can be done by calling *fork()*, which is a Unix function
- They will continue to execute asynchronously, competing for the CPU
- Normally the child will execute something different.
	- This can be done by using the *fork()* function again.
	- It returns 0 if called in the child
	- Returns the child ID if called in the parent
![[Pasted image 20240311103944.png]]

# Init Process
- All processes are descendants of the *init* process
	- The *init* process has a PID of 1
- The kernel start the *init* process as the last step of the boot process
- The init process then reads system init-scripts which execute more start-up programs