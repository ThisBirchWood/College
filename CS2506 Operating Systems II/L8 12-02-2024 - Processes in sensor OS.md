---
default_file: Notes/Lecture 6.pdf
---
```slide-note
page: 2
```
- Radio transceiver - one of the most important components in this type of system
```slide-note
page: 3
```
 - These operations are asynchronous
 ```slide-note
 page: 4
```
- OS components + Application components = system software
- Imagine a black box (a *component*), with commands as input on top (with a command handler for each one). Imagine *events* (hardware interrupts) as inputs on the bottom of the box (and for each event, an *event handler*)
	- Within the box, we have a *frame*, which is a register file, which also provides the state
	- Within the box, we also have a set of *tasks*, which is a function
	- Commands can also come out as output, and events can come out as output
- Commands operate on the frame
```slide-note
page: 5-10
```
- Two parts of this program, running asynchronously
- Left side -> communication, sends data to server
- Right side -> sampling
- Small arrow - events
- Big arrow - tasks
```slide-note
page: 11-14
```
- this shit boring bro
```slide-note
page: 15
```
