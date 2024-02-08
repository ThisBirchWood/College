- A queue is a collection of objects where the FIFO (first-in, first-out) principle is used.
- Queues are essential in computer science:
	1) Packets being transmitted between clients would be queued at a router.
	2) Input and output buffers
	3) Path planning algorithms maintain a queue of edges or locations
	4) Cloud computing maintains queues of work, queries and updates.


# The Queue [[Abstract Data Type|ADT]]
- List of methods:
	- enqueue: add an item to the queue
	- dequeue: remove and return the item that's been in for the longest time
	- front: report the item that's been there the longest
	- length: report how many items in the queue

# Queue Implementation 1
```
class QueueV0:  
	def __init__(self):  
		self.body = []

	def enqueue(self, element):
		self.body.append(element)

	def dequeue(self):
		if len(self.body) == 0:
			return None
		return self.body.pop(0)

	def front(self):
		if len(self.body) == 0:
			return None
		return self.body[0]

	def length(self):
		return len(self.body)

```

## Complexity of operations
1) enqueue - O(1) on *average*
2) dequeue - **O(n)** due to pop(0) being inefficient because it needs to copy the array every time
3) front - O(1)
4) length - O(1)

- We must avoid using pop(0)

# Queue Implementation 2
- This implementation keeps a pointer (*self.head*) to the first item in the list.
- This prevents us from needing to use pop(0).
```
class QueueV1:  
	def __init__(self):  
		self.body = []
		self.head = 0

	def enqueue(self, element):
		self.body.append(element)

	def dequeue(self):
		if self.length() == 0:
			return None
		item = self.body[self.head]
		self.body[self.head] = None
		self.head -= 1
		return item

	def front(self):
		if len(self.body) - self.head

	def length(self):
		if self.length() == 0:
			return None
		return self.body[self.head]
```

## Issues
- While this improves the time complexity for the *dequeue* method (to O(1) time), this implementation still has issues of it's own.
- If we enqueue and dequeue many times, we end up with a very short queue, but a unnecessarily long internal list.
![[Pasted image 20231026170727.png]]

- We need a third implementation to which avoids growing the space

# Queue Implementation 3
- This version is complex, however it improves upon the last two versions immensely.
- Two pointers are kept, *self.head* and *self.tail*
![[Pasted image 20231026171146.png]]
- However the list can also wrap around, meaning the tail would contain a smaller value than the head.
- When the head pointer reaches the tail pointer (or when the *self.size* variable reaches the *len(self.body)* variable), the list grows it's size with a *self.grow()* function.
- Similarly when the size of the list is less than half of the internal list length, a *self.shrink()* function is called.
![[Pasted image 20231030171051.png]]

```
class QueueV2():
	def __init__(self):
		self.body = [None] * 10
		self.head = 0
		self.tail = 0
		self.size = 0

	def enqueue(self, item):
		if self.size == 0:
			self.body[0] = item
			self.size = 1
			self.tail = 1
		else:
			self.body[self.tail] = item
			self.size += 1

			if self.size == len(self.body):
				self._grow()
			elif self.tail == len(self.body)-1:
				self.tail = 0
			else:
				self.tail += 1

	def dequeue(self):
		if self.size == 0:
			return None
		item = self.body[self.head]
		self.body[self.head] = None
		if self.size == 1:
			self.head = 0
			self.tail = 0
			self.size = 0
		elif self.head == len(self.body) - 1:
			self.head = 0
			self.size -= 1
		else:
			self.head += 1
			self.size -= 1
		return item

	def length(self):
		return self.size

	def front(self):
		return self.body[self.head]

	def _grow(self):
		oldbody = self.body
		self.body = [None] = (2*self.size)
		oldpos = self.head
		pos = 0
		if self.head < self.tail:
			while oldpos <= self.tail:
				self.body[pos] = oldbody[oldpos]
				oldbody[oldpos] = None
				pos += 1
				oldpos += 1
		else:
			while oldpos < len(oldbody):
				self.body[pos] = oldbody[oldpos]
				oldbody[oldpos] = None
				pos += 1
				oldpos += 1
			oldpos = 0
			while oldpos <= self.tail:
				self.body[pos] = oldbody[oldpos]
				oldbody[oldpos] = None
				pos += 1
				oldpos += 1
		self.head = 0
		self.tail = self.size
```

- An extra function could be added *self.shrink()*, which shrinks the internal list when 