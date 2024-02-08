---
default_file: Lecturers Notes/01-basics.pdf
---

```slide-note
page: 73
```
- "traceroute" allows you to trace the route that your bits take
	- Gives you the ip address and length of each router you "hop" to
	- It sends 3 identical probes (packets) to the first router, and it measures the time
		- Only difference between the 3 probes is they contain sequence numbers, probe 1 probably contains "1"
```slide-note
page: 74
```
- The reason the delays on the first few are so low, is likely because these routers are very physically close
	- In fact, number 1 is a router in the WGB
- The reason for the variations in the ping is due to queueing delays
- A reason that number 17 and 18 didn't reply is because some companies don't want to give out their ip addresses
```slide-note
page: 75
```
- https://computerscience.unicam.it/marcantoni/reti/applet/QueuingAndLossInteractive/1.html
```slide-note
page: 76
```
- Throughput is generally means as "end to end" throughput
	- From sender to receiver
```slide-note
page: 77
```
- First example, average speed is Rs
- Second example, average end-end throughput is Rc
	- It could send at Rs bits/sec in the first pipe, but this would cause dropped packets, because the second pipe cannot handle it.
	- Therefore, the end-end throughput is the speed of the bottleneck link
```slide-note
page: 78
```
- Bottleneck links are nearly always found at the edge of the network
```slide-note
page: 80-82
```
- How can we ensure the internet remains consistent and reliable when gaming/streaming/browsing?
- ***LAYERS!***
- Similarly to OOP, each layer has it's own well defined API
```slide-note
page: 85
```
```slide-note
page: 86
```
- People often refer to these layers by numbers in industry
	- People might say, "I'm on an L3 project", meaning "I'm on a network layer project"
```slide-note
page: 87
```
- End-to-end clients run all 5 layers (PCs, servers, phones, etc)
- Headers are added when you go down the layers
	- The headers could be the same size as the message itself