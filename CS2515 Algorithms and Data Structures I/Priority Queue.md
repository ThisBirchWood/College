- Queues in which items are selected in order of priority
- An [[Abstract Data Type]]

- In the real world queues are not FIFO (first in first out)
- Examples:
	- Hospital waiting lists (order of severity of illness)
	- Air traffic control (airplanes with low fuel land first)
	- Access nodes forwarding packets (packets from video calls prioritised)

# The Element
- Items will now be stored with two pieces of data:
	- the *value*, the item stored
	- the *key*, representing it's priority
- Implementation: 
```
class Element:
	def __init__(self, key, value):
		self._key = key
		self._value = value

	def __eq__(self, other):
		return self._key = other._key

	def __lt__(self, other):
		return self._key < other._key
```

# Priority Queue ADT
- add(key, value)
- min()
- remove_min()
- length()

# Implementations 
![[Pasted image 20231126174118.png]]

- The best implementation we can use is known as a [[Binary Heap]]