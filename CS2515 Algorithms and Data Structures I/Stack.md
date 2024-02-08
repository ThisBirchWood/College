- A stack is a collection of items, which uses the LIFO (last-in first-out) principle
- Uses of the Stack in CS:
	1. A stack of actions in a text editor, easy UNDO option
	2. A back button on a browser
	3. In programming languages, useful for non-leaf procedures/functions

# The Stack [[Abstract Data Type|ADT]]
- **Methods**:
	1. push: add an item to the stack
	2. pop: remove the most recently added item
	3. top: report the most recently added item
	4. length: report how many elements are in the stack

- Sometimes an "is_empty" method is added

## Implementation
```
class Stack:
	def __init__(self):
		self.alist = []

	def push(self, element):
		self.alist.append(element)

	def pop(self):
		if len(self.alist) == 0:
			return None
		return self.alist.pop()

	def top(self):
		if len(self.alist) == 0:
			return None
		return self.alist[-1]

	def length(self):
		return len(self.alist)

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
i1 = stack.top()
i2 = stack.pop()
i3 = stack.pop()
i4 = stack.pop()
```

- What's happening inside?
![[Pasted image 20231026164948.png]]

## Complexity of Operations
- push - O(1) on *average* due to only using append()
- pop - O(1) on *average* due to using pop()
- top - O(1)
- length - O(1)

## Providing and protecting
![[Pasted image 20231026165238.png]]

