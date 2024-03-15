- A thread is a *lightweight* process.
- A [[Processes|process]] can have one or more threads.
- All threads share the process context, including code and variables

- There is **private context** to a thread, which contains:
	- Register files
	- Stack
	- Priority
	- Thread ID

- When a process starts execution, a single thread is executed.
- Generally, switching threads in a process is handled by the *thread library*, and doesn't call the kernel

## Thread Affinity
- Also known as process affinity, this indicates on which cores the thread/process can run
- The system represents affinity with a bitmask called a **processor affinity mask**
- **Thread Affinity** forces a thread to run on a specific subset of cores and should generally be avoided, because it can interfere with the scheduler's ability to schedule threads effectively across cores