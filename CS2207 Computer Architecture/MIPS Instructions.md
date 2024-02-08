# Instruction Sets
- The repertoire of instructions of a computer
- They perform 3 basic functions:
	1) Arithmetic & logical operations  
	2) Memory and port transfers  
	3) Flow control
- Hardcoded into the CPU, some CPU's runs on different instruction sets
	- For example, both AMD and Intel use the x86 instruction set
	- Mobile CPU's, such as Snapdragon, run on the ARM instruction set

## Design Approaches 
![[Pasted image 20230920143330.png]]
![[Pasted image 20230921164213.png]]
# MIPS
- MIPS is a RISC.
- Runs in 32 bit, there are 64 bit versions however.
- MIPS is Big Endian
## Main Registers
![[Pasted image 20230921172825.png]]
- In MIPS, a word is defined as 32 bits, instead of the usual 16.
- Registers are used for frequently accessed data

## Integer Arithmetic Instructions  
- MIPS can process both integer and floating point numbers. It has a **special co-processor** for it floating point.

### 2's Complement
- Certain binary numbers are signed and some aren't.
- In signed numbers, the MSB (most significant bit) controls whether or not the number is negative.
	- MSB of 1 = negative number
	- MSB of 0 = positive number
- How to find the negative equivalent of a binary number
	- Say we have the number 5, which in binary is 0101
		1. Invert all the bits, 0101 => 1010
		2. Add one to the number, 1010 + 1 = 1011
	-  5 => 0101
	- -5 => 1011
## Memory Related Instructions
![[Pasted image 20230921175045.png]]
- CPU puts the memory address on the address bus
- CPU activates control line to indicate whether it is a read or write operation
- CPU puts/reads data on/from the data bus from/to one of its registers

## CPU registers vs RAM
- Registers are faster **to access** than memory (RAM)
- Operating on memory takes more instructions due to **load** and **store** operations
- You should use registers as much as possible, because accessing memory slows down the program
## Memory Operands
- Memory (RAM) is used for composite data
	- Arrays, structures, dynamic data
- MIPS memory is byte-addressed (you can only read/write bytes or larger)
- MIPS words are aligned in memory  
	- [[Words]] can only be accessed at memory addresses that are a multiple of 4
- MIPS is [[Big Endian]]

- Say we wanted to access the 8th index of an array
	- Python:
		  index = list[8]
- In MIPS:
	![[Pasted image 20230926134332.png]]
- Array index of 8 requires an offset of 32 bytes, 4 * 8 = 32 (4 bytes per word)

## Signed Extension
- Needed when loading data that is smaller than 32 bits into a register.
- A MIPS register **only** supports 32-bit data.
- How to?
	- **Unsigned Numbers**: Extend with 0's until it's reached the target amount of bits
	- **Signed Numbers**: Extend the sign bit until it's reached the target amount of bits
- **Examples** (8 bit to 16 bit):
	- +2: 0000 0010 => *0000 0000* 0000 0010
	- - 2: [[MIPS Instructions#2's Complement|1111 1110]] => *1111 1111* 1111 1110
- In MIPS
	- lh => Load half-word into a register using Signed Extension
	- lb => Load byte into a register using Signed Extension

## Logical Operators (+ uses)

- ### AND operator
	- Good for checking the value of certain bits in a word.
		- Is the third bit 0 or 1?
		- Is the light switch on?
	- You need a mask word/register to check.
	- $t0 AND $t1 (Mask register) = $t2
		1. $t0 -> 0000 0000 0000 0000 0000 1101 1100 0000
		2. $t1 -> 0000 0000 0000 0000 0011 1100 0000 0000
		3. $t2 -> 0000 0000 0000 0000 0000 1100 0000 0000
	- As you can see with the mask register $t1, we are checking bits 10 to 14
	- The result in $t2 tells us that bit 10 and 11 are on, but 12 and 13 aren't
	
- ### OR operator
	- Useful to **set** certain bits to 1 and leave others unchanged.
		- Turning a light on?
	- You cannot set something to 0 with this
	- $t0 OR $t1 (Mask register) = $t2
		1. $t0 -> 0000 0000 0000 0000 0000 1101 1100 0000
		2. $t1 -> 0000 0000 0000 0000 0011 1100 0000 0000
		3. $t2 -> 0000 0000 0000 0000 0011 1101 1100 0000
	- $t2 is the same as $t0, only with two bits changed

- ### NOT operator
	- Useful to **invert** bits
		- 0 to 1, 1 to 0
	- MIPS only has a NOR instruction, but by replacing the third register with $zero, it acts as a NOT operator.
		- NOR $t0, $t1, $zero
	 ![[Pasted image 20231003173327.png]]

## Instructions Encoding / Instruction Format
- MIPS instructions have a fixed size of 32 bits.
- The layout of these 32 bits is known as the **Instruction Format**
- MIPS has 3 different types
	1. R-Format
	2. I-Format
	3. J-Format
- MIPS needs only 5 bits to address all the registers, (2^5) = 32, one for each register

### R-Format (Register instruction format)
![[Pasted image 20231003180626.png]]
1. op -> Operation to be performed (opcode)
2. rs -> first source register number
3. rt -> second source register number
4. rd -> destination register
5. shamt -> shift amount
6. funct -> function code (extends opcode)

#### Example
![[Pasted image 20231003181133.png]]

### I-Format (Immediate arithmetic and load/store instructions)
![[Pasted image 20231003182148.png]]
1. op -> Operation to be performed (opcode)
2. rs -> first source register number
3. rt -> second source register number
4. constant -> the address/address label
- Offset is added to the constant.

![[Pasted image 20231003182858.png]]

### Values over 16 bits
- As we see in the I-Format instruction format, constants are limited to 16 bits, what about values over that?
- 16 bits is sufficient for the most part ([[make the common case fast]])
- For the occasional larger value, MIPS automatically does this:
	1. lui $at, constant
		- Copies the 16 most significant bits into the upper 16 bits of $at
		- $at (register #1) = assembler temporary
	2. ori $t0, $at, constant


## Branching
### Unconditional Branching
- Jump straight to the provided address
```
j Label     #jump to address "Label"
```
- Uses the [[MIPS Instructions#MIPS Instructions Encoding / Instruction Format|J-format]] instruction format.
![[Pasted image 20231004165642.png]]
1. opcode -> 6 bits
2. address -> 26 bits
- Giving the address 26 bits allows for large jumps.

### Conditional Branching
- Compare values then decide whether or not to jump to address or continue with next instruction
```MIPS
beq $t0, $t1, my_label      #if ($t0 === $t1) then jump to my_label

bne $t0, $t1, my_label      #if ($t0 !== $t1) then jump to my_label
```
- I-Format Instruction Format
![[Pasted image 20231010164315.png]]

- Other instructions:
	1. bgtz (branch if greater than zero)
	2. bltz (branch if less than zero)
	3. bgez (branch if greater than or equal to zero)
	4. blez (branch if less than or equal to zero)
- The reason that there is no bge (branch if more than) or ble (branch if less than) is because you can achieve those with a combination of the others.
	- MIPS is RISC
	
### Extra conditionals
- The slt command

```
slt rd, rs, rt      #if (rs < rt) then set rd to 1; otherwise set to 0

slti rd, rs, const    #if (rs < const) then set rd to 1; otherwise set to 0
```
![[Pasted image 20231010165031.png]]

- There is also the unsigned versions:
	- sltu, sltui

### If statements
- High Level Python code:
```
if i == j:
	f = g + h
else:
	f = g - h
```
- MIPS code: (say f, g, h, i, j == $s0, $s1, $s2, $s3, $s4)
```
bne $s3, $s4, ELSE
add $s0, $s1, $s2
j EXIT
ELSE:
	sub $s0, $s1, $s2
EXIT:
	#rest of program
```

## Procedures
- Procedures are basically functions within MIPS
- Used to write modular, clean code
![[Pasted image 20231010171316.png]]

### How to use a procedure?
- 2 Steps
	1) **Procedure Call** (jump and link (jal))
		- "jal my_function"
		- This instructs the processor to jump to 'my_function'
		- $PC <- address with the first instruction of 'my_function'
		- $ra <- address of the instruction right after the jal call
	2) **Return Call** (jr -> meaning to jump register)
		- jr $ra
		- Jumps to the address stored at $ra, which was right after the jal call

### General Rules for Arguments and Return values
- $a0 - $a3, used for arguments into the procedure
- $v0, $v1, used for procedure return values
- The $t registers can be overwritten by the procedure, while the $s registers cannot

### Leaf Procedures
- A leaf procedure is a procedure which does not call another procedure
- Therefore the $ra can be left unchanged and you don't need to worry about it

### Non Leaf Procedures
- A non-leaf procedure calls another procedure (including recursive calls)
- The $ra must be kept track of (normally using the stack)
![[Pasted image 20231017171655.png]]

### The Stack
- A last-in-first-out (LIFO) queue for storing register content
- Used for procedures, where variables need to be stored, including the $ra
- The MIPS stack must be managed manually
![[Pasted image 20231017172037.png]]


