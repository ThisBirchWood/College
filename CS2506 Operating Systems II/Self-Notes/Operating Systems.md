- The OS manages applications as [[Processes]]
- The purpose of the OS is to allocate necessary resources for the execution of processes during their lifetimes

## Types of Resources
- There is more than one physical unit of a type of resource
- For example:
	- CPU cores
	- Memory pages
	- Disk sectors
	- Networking cards
	- Cameras
- Many operating systems use the *virtualisation* of resources such as cores and memory pages for more efficiency.

# Goals of OS
- To meet user requirements with
	- lowest execution time
	- quickest response
	- least cost
	- fairness
	- best user experience
	- security
- To meet system admin requirements
	- optimal use of resources
	- least amount of energy
	- maximise revenue

![[Pasted image 20240229131310.png]]

# Kernel 
- The bottom "layer" of a computer is the hardware
	- Hardware accepts basic commands such as, "seek the disk arm to track 79, select head 3 and read sector 5"
- Kernel is software that interacts with the hardware directly is *non-portable* and contains low level details: data for control and state registers, interrupt priorities

- The OS *kernel* has several key components:
	- *Device drivers* are the hardware units' managers, they hide low level details
	- *Process management* handles processes, allocating them resources and scheduling their execution
	- *Memory management* is responsible for physical and virtual memory management
	- *File system manager* is the code that organizes the data storage into files and directories, hiding low level details
	- *Network services* provide host-to-host and process-to-process communication across networks.

## Access to kernel services
- The kernel is a collection of services, and *some* of them are available to user processes
- To enter the kernel, the user process makes a *system call*
	- Which executes a [[#Trap services|trap instruction]] of some sort
- The instruction switches the processer into a privileged operating state called the *kernel mode*
- Parameters passed with the trap instruction say what service is requested of the kernel
- When the function is completed, the processer returns to *user mode*

## Trap services
- There are certain functions that require specific knowledge of handling resources (control registers, state register, sequence of operations)
	- The delicate resources accessed by these functions should *not* be manipulated by user processes
- They are accessed through well controlled and protected service routines
	- Also known as *system calls*
![[Pasted image 20240229132859.png]]
- Trap instructions are used to implement system calls


# Types of OS
- There isn't one OS that can work with all types of hardware
- A large range of computing devices require customized OS's

## General purpose OS
- Built to deal with a wide range of different types of processes 
- Examples: Windows, Unix, Linux
## Mobile Devices
- Built to deal with event driven (touchscreen) processes
- Concerned with power-saving and user experience
- Examples: iPhone OS, Android, TinyOS
## Embedded Systems (IoT)
- Scaled down versions of OS
- Real time, event-driven

