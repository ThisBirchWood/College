- The set of rules governing the exchange or transmission of data between devices
- It defines how messages between devices should be formatted

![[Pasted image 20240229154702.png]]

# Computer Protocols
- Humans are very good at adapting to nuances of speech and social interaction
- Computers are not. Rules must be specified with computers
	- No room for ambiguity

# Request-Response Protocol
- Most networks use a request-response protocol
- A client (normally a browser) sends a **request** for a file to a server
- The server then **responds** with that file
![[Pasted image 20240229155028.png]]

# Specifying Protocols
- How are protocols specified?
	- The set of message types
		- Examples: request, response, reject, error
	- The format of the messages![[Pasted image 20240229155346.png]]
	- The action taken when a message is received
		- And what to respond with

# Implementing Protocols
- Implemented in software
- Must be implemented **faithfully** 
- Choice of programming language / operating system does not matter
- Software must be installed on both client and server

![[Pasted image 20240229160043.png]]

	