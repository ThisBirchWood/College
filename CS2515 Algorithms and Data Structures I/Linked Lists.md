
# Singly Linked Lists

![[Pasted image 20231030173926.png]]
- The list is made up of nodes
- Each node contains a pointer to the element, and a pointer to the next element in the list
- A majority of the time, there's a dummy head and tail pointer.

## 1st Implementation
```
class SLLNode():
	def __init__(self, item, nextnode):
		self.element = item
		self.next = nextnode

class SLinkedList():
	def __init__(self):
		self.first = None
		self.size = 0

	def add_first(self, item):
		node = SLLNode(item, self.first)
		self.first = node
		self.size += 1

	def get_first(self):
		if self.size == 0:
			return None
		return self.first.element

	def remove_first(self):
		if self.size == 0:
			return None
		item = self.first.element
		self.first = 
		self.first.next
		self.size -= 1
		return item
```

- All of these methods are of O(1) complexity
- Something missing is access to the end of the list, we can add this easily however

## 2nd Implementation
```
class SLLNode():
	def __init__(self, item, nextnode):
		self.element = item
		self.next = nextnode

class SLinkedList():
	def __init__(self):
		self.first = None
		self.last = None
		self.size = 0

	def add_first(self, item):
		node = SLLNode(item, self.first)
		self.first = node
		self.size += 1

	def add_last(self, item):
		node = SLLNode(item, self.last)
		self.last = node
		self += 1

	def get_first(self):
		if self.size == 0:
			return None
		return self.first.element

	def get_last(self):
		if self.size == 0:
			return None
		return self.last.element

	def remove_first(self):
		if self.size == 0:
			return None
		item = self.first.element
		self.first = self.first.next
		self.size -= 1
		return item
```



# Doubly Linked Lists
- Same as singly Linked Lists, except they also have a back pointer, pointing to the element that comes before them in the list.
![[Pasted image 20231101213846.png]]
- Usually a dummy tail and head node are added.
![[Pasted image 20231101222206.png]]
