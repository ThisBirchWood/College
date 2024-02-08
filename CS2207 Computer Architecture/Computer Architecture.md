# Computer Architecture
- The art/science of designing computers that reach their performance, cost and functionality goals
- Hardware choices depend on the goals needed, such as energy efficiency, cost and usage

# Examples of hardware goals
- Examples of some goals that you might need to consider when designing a computer part.

1. Performance
2. Value
3. Energy efficiency
4. Scalability
5. Reliability
6. Security
7. Response time + latency 
8. Maintainability
9. Flexibility

# Implementation
- Imagine a sorting function in Python, normally treated as an abstract black box (you give input, it gives output).
- However there are different **implementations** of a sorting function (Quic, Bubble, Binary Search)
- It's what's the [[Computer Architecture#Abstraction|black box]] is doing within.
- --
- The same can be applied to computer components.
 ![[Pasted image 20230919161523.png]]
- For example, most CPUs generally do the same thing. But the implementation within them is what distinguishes them.
- For example, a Celeron N2920 can do nearly all the things a Core i9-13900k can, but the implementation (clock speed, cores, general performance) is much different in the i9, therefore it's is much much faster.

# Abstraction
-  A method of simplifying complex things by showing only the most important aspects
- Complex objects become black boxes with just inputs and outputs
- Only **specialists** deal with box internals, we deal with just the inputs and outputs
- ### Examples:
	- Software Abstraction with OOP (Classes in Python/Java)
	- Network Abstraction (TCP/IP Layered Model)

# Instruction Set Architecture
![[Pasted image 20230919185859.png]]
- the key interface between the hardware and the low level software
- It defines the Assembly Code of a certain machine, for example MIPS has it's own ISA, as does x86 assembly.

# Binary Files (in Unix)
- ## Formatting
	- **Header**: size and data types within the file, basically metadata
	- **Text Segment**: the main code of the file (.text part) 
	- **Data Segment**: binary representation of the data in the file (.data part)
	- **Relocation Information**: identifies instructions that depend on absolute addresses in the memory
	- **Symbol Table**: associates addresses with external labels (eg: 0xFF437A32 becomes "list1")
	- **Debugging Info**: concise description on how the program was compiled
- ## File Loading
	- Reads the file header to determine file size and data segments
	- Creates an address space for the program
	- Copies text and data to respective memories
	- Copies passed program arguments to the stack
	- Initializes the machine registers
	- Jumps to a start-up routine that copies the program’s arguments from the stack to registers and calls the program’s main routine
