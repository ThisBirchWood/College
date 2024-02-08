- Pipelining makes the CPU "overlap the execution of instructions"
	- Parallelism improves performance
- Laundry Example:
	![[Pasted image 20231115215845.png]]

## MIPS Pipeline
- The MIPS pipeline is split into 5 stages:
	1. **IF**: **I**nstruction **f**etch from memory
	2. **ID**: **I**nstruction **d**ecode & register read
	3. **EX**: **Ex**ecute operation / Calculate address
	4. **MEM**: Access **mem**ory operand (*optional*)
	5. **WB**: **W**rite result back to register (*optional*)

![[Pasted image 20231120163321.png]]
- **Critical Path** is the time it takes for the longest instruction, in this table it's 800ps for the lw instruction

![[Pasted image 20231120163509.png]]
a) 
	- In a pipelined processor, the clock cycle is defined by the longest **stage**, which in this example is 350ps, (Instruction Decode)
	- In a non-pipelined processor, it's all of them put together, which is 1250ps.
b)
	- The total latency is the same in both of them, as one singular instruction still takes the same amount of time.

## Pipeline Speed-up Factor
- If all stages are balanced
	- all *N* pipeline stages take *T* time and we have *I* instructions
	- Non-pipelined Processor time = I\*N\*T
	- Pipelined Processor Time = N\*T + (I-1)T
	- Speed-up factor = I\*N\*T / N\*T + (I-1)T

## Pipeline Hazards
- What if the processor needs to fetch a piece of data that hasn't yet been calculated
- Take this example
	![[Pasted image 20231120165548.png]]
	- In a pipelined processor, by the time the processor is trying to fetch $s0 in the second instruction, it's still being calculated in the first one.
- This is known as a pipeline hazard
- There are three types of hazards, *structure*, *data* and *control* hazards

### Structure Hazards
- When two instructions need to access the same resource at the same time
- For example, when two instructions both need to access the ALU for a calculation

**The Solution**
- Add "registers" between the stages that store both the instruction and data required for the instruction
- Split the CPU into different stages
![[Pasted image 20231120171100.png]]

### Data Hazards
- When an instruction depends on a piece that may not yet be available.
- Example:
![[Pasted image 20231120165548.png]]
- $s0 would not be available for the second instruction.
- This causes bubbles/stalls in the code
![[Pasted image 20231120171252.png]]

#### Solution 1 - Forwarding (aka Bypassing)
- A hardware solution that connects the output of the ALU to the Instruction Decode stage
- Doesn't wait for the data to be stored in a register
- Higher cost due to extra hardware (+ extra control wires)
![[Pasted image 20231120171720.png]]

- Forwarding isn't a perfect solution, as it would still require one stall between the consecutive instructions (still an improvement over two stalls)
![[Pasted image 20231120172042.png]]

#### Solution 2 (Code Rescheduling)
- A software solution which involves re-ordering your code to avoid data being used directly after.
![[Pasted image 20231120172600.png]]

### Control Hazards
- More challenging than data and structure hazards
- Need to be considered when branching, as if the program must branch, it invalidates the pipeline fetch/decode (next instructions that have already been half completed are useless)

#### Solution 1: Stall on Branch (do nothing)
- Wait until outcome has been determined
![[Pasted image 20231120173524.png]]
- Simple but inefficient
#### Solution 2: Optimized Waiting
- Decide when decoding (requires extra hardware)
- You only have to wait for one cycle

#### Solution 3: Prediction
- Adopted by most architectures
- Only stalls when prediction is wrong
- MIPS simply assumes the branch will not be taken and continues to the next instruction (example of static)
##### Static
- Based on typical branch behaviour
	- Backward Taken Forward Not Taken (BTFNT)
	- if-statements
##### Dynamic 
- Hardware tracks branch behaviour
- Assumes future behaviour continues trends

- **Brach Prediction Buffer** (Branch History Table)
	- Stores the outcome of branching
	- Uses this to predict outcome