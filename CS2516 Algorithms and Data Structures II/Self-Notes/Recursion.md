# Activation Records
- When a language like *Python* executes a function, it creates an *activation record* that stores:
	- variables passed in as parameters
	- local variables created in the function
	- the point in the function code its reached
- They are pushed onto a *[[Stack]]* of activation records

- Once the function finishes executing:
	- pops the record off the stack, and remembers the return value
	- moves the to the record on the top of the stack, and passes in the return value

# Recursion
- A recursive function is split in two:
	- *Base Case*: a non-recursive codeblock that terminates the recursion
	- *Recursive Case*: a call to the same function, with different parameters
- The recursive case must bring the function closer to the base case
![[Pasted image 20240305123628.png]]
- If a return value is needed, then every path through the function must end in a return statement
	- And must always return the same type of object


# Analysing recursive functions
1) Count the worst-case work done by a single activation, *without* the recursive call
2) Count the worst-case number of recursive calls
3) Multiply together

![[Pasted image 20240305124445.png]]
