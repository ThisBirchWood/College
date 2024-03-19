class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        return f"{self.value}"

class LinkedList:
    def __init__(self):
        self.start = Node(None)
        self.end = Node(None)
        self.size = 0

        self.start.next = self.end
        self.end.prev = self.start

    def __str__(self):
        string = '['
        current = self.start.next
        for i in range(self.size):
            if i > 0:
                string += (', ' + str(current))
            else:
                string += str(current)
            current = current.next

        return string + "]"
    
    def __repr__(self):
        string = '['
        current = self.start.next
        for i in range(self.size):
            if i > 0:
                string += (', ' + str(current))
            else:
                string += str(current)
            current = current.next

        return string + "]"
    
    def __iter__(self):
        cursor = self.start.next
        while cursor != self.end:
            yield cursor
            cursor = cursor.next

    ## PRIVATE METHODS
    def _find_node_at_index(self, index) -> Node:
        if index >= self.size or index < 0:
            raise ValueError("Index out of range")
        current = self.start.next
        for i in range(index):
            current = current.next
        return current
    

    ## PUBLIC METHODS
    def append(self, value) -> Node:
        '''
        Appends a value to the end of the list
        Returns the node object

        Time Complexity: O(1)
        '''
        n = Node(value)

        last_node = self.end.prev
        last_node.next = n
        self.end.prev = n

        n.prev = last_node
        n.next = self.end

        self.size += 1

        return n 
    
    def append_front(self, value) -> Node:
        n = Node(value)

        current_first_node = self.start.next

        current_first_node.prev = n
        self.start.next = n

        n.prev = self.start
        n.next = current_first_node

        self.size += 1

        return n
    
    def pop_front(self) -> Node:
        node_to_remove = self.start.next
        next_first_node = node_to_remove.next

        self.start.next = next_first_node
        next_first_node.prev = self.start

        self.size -= 1

        return node_to_remove.value
    
    def pop(self):
        '''
        Removes a node from the front of the list
        Returns the element

        Time Complexity: O(1)
        '''
        node_to_remove = self.end.prev
        second_last_node = node_to_remove.prev

        self.end.prev = second_last_node
        second_last_node.next = self.end

        self.size -= 1

        return node_to_remove.value
    
    def insert(self, index: int, value) -> Node:
        '''
        Inserts a value into the list at the given index
        Inputs:
            - index: Value will be added before this index
            - value: The value to be added

        Returns the new Node object

        Time Complexity: O(n)
        '''
        n = Node(value)

        insert_before = self._find_node_at_index(index)
        previous_node = insert_before.prev

        insert_before.prev = n
        previous_node.next = n

        n.prev = previous_node
        n.next = insert_before

        self.size += 1

        return n
    
    def insert_before(self, object: Node, value) -> Node:
        n = Node(value)

        previous_node = object.prev

        previous_node.next = n
        object.prev = n

        n.prev = previous_node
        n.next = object

        self.size += 1

        return n
    
    def insert_after(self, object: Node, value) -> Node:
        n = Node(value)

        next_node = object.next

        object.next = n
        next_node.prev = n

        n.prev = object
        n.next = next_node

        self.size += 1

        return n

    def remove_by_index(self, index: int) -> None:
        '''
        Removes a value from the list at the given index
        Inputs:
            - index: Value at this index will be removed
        
        Returns the removed Node object

        Time Complexity: O(n)
        '''
        node_to_remove = self._find_node_at_index(index)

        previous_node = node_to_remove.prev
        next_node = node_to_remove.next

        previous_node.next = next_node
        next_node.prev = previous_node

        self.size -= 1

        return node_to_remove.value
    
    def remove(self, object: Node) -> None:
        '''
        Removes the value from the list
        Inputs:
            Object: The node object to remove

        Returns None

        Time Complexity: O(1)
        '''
        previous_node = object.prev
        next_node = object.next

        previous_node.next = next_node
        next_node.prev = previous_node

        self.size -= 1

    def remove_by_value(self, value):
        element_to_remove = None
        for element in self:
            if element.value == value:
                element_to_remove = element
                self.remove(element_to_remove)
                return
        raise ValueError("Value not in List")




    def last_element(self):
        return self.end.prev.value
        
        
    def length(self) -> int:
        return self.size
    
if __name__ == "__main__":
    l = LinkedList()
    l.append(4)
    l.append(6)
    l.append(65)
    print(l)
    l.pop_front()
    print(l)
    l.append(583)