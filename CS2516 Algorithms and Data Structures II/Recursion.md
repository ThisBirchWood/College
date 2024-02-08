# Activation Records
- When Python executes a function, it creates an *activation record* that stores:
	- variables passed in parameters
	- local variables
	- the point in the function code currently executing
- and pushes it onto a stack of activation records
- When a function completes, the activation record is destroyed


# Recursion
- Every recursive function, must have a *return* statement (including base and recursive cases)
- There must be a base case, otherwise the stack of activation records would not stop growing
	- Python throws an error, might be dangerous in other languages