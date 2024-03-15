class Element:
    def __init__(self, k, v, i):
        self._key = k
        self._value = v
        self._index = i

    def __str__(self):
        return f"Value: {self._value} : Key: ({self._key}) : Index {self._index}"
    
    def __repr__(self):
        return f"Element : Value: {self._value} : Key: ({self._key}) : Index {self._index}"

    def __eq__(self, other):
        return self._key == other._key
    
    def __lt__(self, other):
        return self._key < other._key
    
    def _wipe(self):
        self._key = None
        self._index = None
        self._value = None

class AdaptablePriorityQueue():
    def __init__(self):
        self.queue = []

    def __str__(self):
        return f"{[str(e) for e in self.queue]}"

    ### PRIVATE METHODS
    ## checks if a given index is within the queue
    def _within_bounds(self, index: int) -> bool:
        if index < 0 or index >= len(self.queue):
            return False
        return True

    ## gets the parent of a given index
    def _get_parent(self, index: int) -> int:
        new = (index-1)//2
        return new

    ## returns left child of a given index
    def _get_left_child(self, index: int) -> int:
        new = (index*2)+1
        return new

    ## returns the right child of a given index
    def _get_right_child(self, index: int) -> int:
        return self._get_left_child(index)+1
    
    ## given an index, will bubble that index in the queue downwards until it reaches the right place
    def _bubble_up(self, index):
        parent = self._get_parent(index)
        if self._within_bounds(parent):
            if self.queue[index]._key < self.queue[parent]._key:
                self.queue[index], self.queue[parent] = self.queue[parent], self.queue[index]
                self.queue[parent]._index = parent
                self.queue[index]._index = index
                return self._bubble_up(parent)
            return index
        return index

    ## given an index, will bubble that index in the queue upwards until it reaches the right place
    def _bubble_down(self, index):
        left_child = self._get_left_child(index)
        right_child = left_child + 1  # No need to calculate right child separately

        # Check if left child is within bounds and choose the child to swap with
        if left_child < len(self.queue):
            child_to_swap = left_child
            if right_child < len(self.queue) and self.queue[right_child]._key < self.queue[left_child]._key:
                child_to_swap = right_child
        else:
            return index  # If no children, no need to bubble down further

        # Swap if necessary and recursively bubble down
        if self.queue[child_to_swap]._key < self.queue[index]._key:
            self.queue[index], self.queue[child_to_swap] = self.queue[child_to_swap], self.queue[index]
            self.queue[index]._index = index
            self.queue[child_to_swap]._index = child_to_swap
            return self._bubble_down(child_to_swap)

        return index

    ## calls both bubble_up and bubble_down, and will simply put a given index in the right place, and return the new index
    def _bubble(self, index):
        n1 = self._bubble_down(index)
        n2 = self._bubble_up(index)

        if n1 == index:
            return n2
        else:
            return n1

    ### PUBLIC METHODS
    ## adds an element to the queue, given its key and value, returns that element
    def add(self, key: int, item) -> Element:
        index = len(self.queue)
        e = Element(key, item, index)
        self.queue.append(e)

        new_index = self._bubble(index)
        e._index = new_index

        return e
        
    ## returns the highest priority element
    def min(self) -> Element:
        return self.queue[0]

    ## removes the highest priority element from the queue and returns it
    def remove_min(self) -> Element:
        self.queue[0], self.queue[-1] = self.queue[-1], self.queue[0]
        element = self.queue.pop()

        if self.length() > 0:
            self.queue[0]._index = 0

            new_index = self._bubble(0)
            self.queue[new_index]._index = new_index
        return element

    ## returns the amount of items in the queue
    def length(self) -> int:
        return len(self.queue)

    ## updates the key of an item, given the reference to the item and its new key
    def update_key(self, element: Element, newkey: int) -> Element:
        element_index = element._index
        element._key = newkey

        new_index = self._bubble(element_index)
        element._index = new_index

        return element

    ## returns the key of a given element object
    def get_key(self, element: Element) -> int:
        return element._key

    ## removes an object from the queue given its element object
    def remove(self, element: Element):
        element_index = element._index

        if element_index >= self.length()-1:
            self.queue.pop()
        else:
            self.queue[element_index], self.queue[-1] = self.queue[-1], self.queue[element_index]
            self.queue.pop()
            
            new_index = self._bubble(element_index)
            self.queue[element_index]._index = new_index

        return (element._value, element._key)

## uses an unsorted list, very inefficient on purpose (in case anyone thinks I'm dumb)
class UnsortedListPriorityQueue:
    def __init__(self):
        self.queue = []

    def __str__(self):
        return f"{[str(e) for e in self.queue]}"

    def add(self, key: int, value) -> Element:
        e = Element(key, value, len(self.queue))
        self.queue.append(e)
        return e
    
    def min(self) -> Element:
        min_element = self.queue[0]
        for i in range(1, len(self.queue)):
            if self.queue[i] < min_element:
                min_element = self.queue[i]

        return min_element
    
    def remove_min(self) -> Element:
        min_element_index = 0
        for i in range(len(self.queue)):
            if self.queue[i]._key < self.queue[min_element_index]._key:
                min_element_index = i

        if min_element_index >= len(self.queue)-1:
            return self.queue.pop()
        
        self.queue[min_element_index], self.queue[-1] = self.queue[-1], self.queue[min_element_index]
        e = self.queue.pop()
        self.queue[min_element_index]._index = min_element_index
        return e
    
    def length(self) -> int:
        return len(self.queue)
    
    def update_key(self, element: Element, newkey: int) -> Element:
        element._key = newkey
        return element

    def get_key(self, element: Element) -> int:
        return element._key
    
    def remove(self, element: Element):
        element_index = 0
        for i in range(len(self.queue)):
            if self.queue[i] == element:
                element_index = i
                break

        if element_index >= len(self.queue)-1:
            return self.queue.pop()
        
        self.queue[element_index], self.queue[-1] = self.queue[-1], self.queue[element_index]
        e = self.queue.pop()
        self.queue[element_index]._index = element_index
        return e