---
default_file: Notes/Lecture 5.pdf
---
```slide-note
page: 5-6
```

- Goal is keep little cores as busy as possible, this saves energy
```slide-note
page: 7
```
- For some manufacturers, performance is the main goal, for others, energy saving is the main goal
```slide-note
page: 8-9
```
- CPUs with one core have quite a simple scheduler (just take the next process with the highest priority), however nowadays because CPUs have multiple cores (sometimes even different types of cores), schedulers are now quite complex.
- 1 core CPU -> many-core CPU -> big.LITTLE core CPU -> big.LITTLE-GPU cores CPU
```slide-note
file: Notes/Problems I.pdf
page: 2-4
```
- Multiple queues (among user processes only, kernel have higher priority, kernel processes execute before any user processes)
	- Each queue has a priority level
	- When a processes finishes it's time slice, it goes to the next lower priority queue
	- When a processes returns after an I/O block, it's priority is increased
- Time slices increase with lower priorities
	- Time quantum for each level *i* determined by equation t = (2^i)q
```slide-note
file: Notes/Problems I.pdf
page: 5-6
```
- There is a network bus between L2 and L3 cache
- Domain: common features of the cores + policies
- Say we have a B package for a load:
	- If load is low, keep one package disabled (power saving)
	- Move process when affinity is lost
		- By doing this, memory access requests are reduced (he spells it req.mb)
```slide-note
file: Notes/Problems I.pdf
page: 7
```
- Unit for *load* : 4 million instructions per second
	- This could very well be in EXAM!!!!!!!!?!?!?!?!??!?!?!?!!?!??!!??!?!?!? (WTF???)
```slide-note
file: Notes/Problems I.pdf
page: 8
```
- W = P x T (Work (joules) = power * time)
- Little cores:
	- 4 little cores, each 1 watt = 4 watts
	- For 22 seconds
	- 4 x 22 = 88J
- Big Cores:
	- 2 big cores, each 1.5 watts = 3 watts
	- For 22 seconds
	- 3 x 22 = 66J
- 88 + 66 = 154 J

- Question 2
- Two smalls are better than one big core because big cores comes in packages of 2, therefore you can't just use one big core