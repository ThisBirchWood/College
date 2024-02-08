- *Protocols* define the format and order of messages sent and received among network entities, and actions takes on msg transmission
- Word originates from Middle English where it referred to the *fine details* of an agreement
![[Pasted image 20240118155028.png]]
- Protocols ensure that their is no ambiguity in communication between computers

# Request-Response Protocol
- Most network protocols are called *request-response*
![[Pasted image 20240118155655.png]]

# Specifying Protocols
- Protocols are specified as follows
	- The set of message types (e.g. request, response, reject, error)
	- The format of each message
	- The action taken when a message is received
	- What response to send to messages
- Example:
![[Pasted image 20240118155850.png]]

# Implementing Protocols
- Protocols are usually implemented in software
	- WiFi is an exception
- The software *must* faithfully implement the protocol specification
- The software must be installed at the client and the server computers