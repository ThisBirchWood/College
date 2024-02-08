- Objectives are to understand how computers deal with:
	- Multiplication and division
	- Floating-point numbers (for software and hardware)
# Overflow
- **Overflow:** the result of an operation cannot be represented by the rightmost hardware bits
- Adding a positive and a negative number won't result in overflow

## Handling Overflow
- In MIPS, the add, addi, sub instructions raise an **exception** by invoking the *exception handler*
- NOTE: This uses a different co-processor from floating point numbers
	1) Save PC in **exception program counter (EPC)** register
	2) Jump to predefined handler address (KERNEL code)
	3) mfc0 (move from coprocessor reg) instruction can retrieve the EPC value, to return to the program, after corrective action
![[Pasted image 20231017181456.png]]

# Integer Multiplication 
- Example: Multiply 1000 by 1001 (8 * 9)
- When the multiplier number is 1, then the multiplicand is copied down, shifted by the amount of numbers you've already done, otherwise it's just 0000
![[Pasted image 20231017185001.png]]
## Hardware Implementation
### First Implementation
- Takes 32 clock cycles to finish a calculation
	![[Pasted image 20231017184903.png]]

### Second Implementation
	![[Pasted image 20231017184924.png]]
	- Faster than the first implementation.
	- Perform operations in parallel: add/shift
	- Splits the 64-bit register into two, one for the result, the other for shifting the multiplier
### Third Implementation
	![[Pasted image 20231017184939.png]]


## MIPS Multiplication Instructions
- MIPS uses 2 special 32-bit registers for product
	- **HI:** Most significant 32 bits
	- **LO:** Least significant 32 bits
- MIPS instructions:
	- *mult rs, rt* / *multu rs, rt*
		- Multiply 2 registers (+unsigned)
	- *mfhi rd / mflo rd*
		- Move from HI/LO register to rd
		- Can test HI register to test for overflow




# Integer Division
- Harder than multiplication :(
- Example: dividing 1001010 by 1000
	1) 
