- We will look into processor hardware design using simple instruction subsets which shows most of how a CPU works.
	- Memory reference: lw, sw
	- Arithemtic/logical: add, sub, and, or, slt
	- Control: beq, j
- Two implementations:
	- Simplified *single clock cycle* processor
	- A *pipelined* version (better)

# Non-pipelined Implementation
![[Pasted image 20231108165007.png]]
- We must add a control unit, which takes the instruction that was fetched and adds certain control values so the processor knows what to do in certain situations
- These are the control values in MIPS:
	1. RegDst
		- Determines which register the result of an operation should be written to (for I-Format instructions, bits 20-16 are the destination, but for R-Format, bits 15-11 are the destination)
	2. Jump
		- Whether or not the instruction is a 26 bit jump, takes bits 0-25 and jumps to it
	3. Branch
		- Whether or not the instructions contains something to branch to. If it's conditional, ALU is set to subtract, if value is zero, then it branches.
	4. MemRead
		- Specifies whether the CPU should read data from memory during this operation.
	5. MemtoReg
		- Determines whether the data coming from memory should be written to a register.
	6. ALUOp
		- Selects the operation the Arithmetic Logic Unit (ALU) should perform (e.g., addition, subtraction).
	7. MemWrite
		- Indicates whether the CPU should write data to memory during this operation.
	8. ALUSrc
		- Specifies the source of data for the ALU operation (e.g., immediate value or a register).
	9. RegWrite
		- Determines whether the result of the operation should be written back to a register.
- MIPS CPU with Control (excluding Jump)
![[Pasted image 20231115211223.png]]

## MIPS Datapath

### [[MIPS Instructions#R-Format (Register instruction format)|R-Format]] Instructions
- Read two register operands
- Perform arithemtic/logical operation
![[Pasted image 20231115194628.png]]
![[Pasted image 20231115194646.png]]

### Load/Store Instructions
![[Pasted image 20231115195350.png]]
- Read register operands
	- rs = register to read
	- rt = register offset
- Calculate address using the offset
	- Use ALU, and [[MIPS Instructions#Signed Extension|sign extend]]
- Load: Read memory and update register

### Conditional Branch Instructions
![[Pasted image 20231115210805.png]]
- Read 2 register operands
- Compare operands
	- Use ALU, **subtract** and check if it equals zero
- Calculate target address by:
	1. Sign-extend the offset address
	2. Shift left 2 places (to convert from word offset to byte offset)
	3. Add to PC + 4
### Unconditional Jumps
- Jump again uses a word address
- Extra signal needed from control module
![[Pasted image 20231115213026.png]]
## MIPS Control

### Main Control Unit
![[Pasted image 20231115213945.png]]

### ALU Control ![[Pasted image 20231115215049.png]]
- ALU is used for various instructions
	- Load/Store: ALU is set to *add*
	- Branch: ALU is set to *subtract*
	- [[#MIPS Instructions R-Format (Register instruction format) R-Format Instructions|R-Type]]: Depends
![[Pasted image 20231115214226.png]]

- If we assume that two bits come from *ALUOp* (thicker line)
![[Pasted image 20231115214900.png]]

## Performance Issues
- Different instructions need different execution times
	- The load word instruction takes the longest because it uses all main stages (Instruction memory, register file, ALU, data memory, register file)
	- This means that the load word is the **Critical Path**, as in order to maintain a consistent clock cycle, all instructions must artificially take this amount of time, even if they don't need it.
		![[Pasted image 20231115215614.png]]
- All instructions operate at the speed of the slowest one
- The solution is **[[Pipelined Processor|pipelining]]**
