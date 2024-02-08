from queues import QueueV2
from stackA import Stack
import sys, time, math

#part ii)
def reverse_queue(queue):
    new_queue = QueueV2()
    stack = Stack()

    while queue.length() > 0:
        stack.push(queue.dequeue())

    while stack.length() > 0:
        new_queue.enqueue(stack.pop())

    return new_queue

#implementation of queue, adding a shrink method, part iii)
class QueueV3:
    """ A queue using a python list, with internal wrap-around..

    Head and tail of the queue are maintained by internal pointers.
    When the list is full, a new bigger list is created.
    When the list is less than 25% of the reserved space, a new smaller list is made.
    """
    def __init__(self):
        self.body = [None] * 10
        self.head = 0    #index of first element, but 0 if empty
        self.tail = 0    #index of free cell for next element
        self.size = 0    #number of elements in the queue

    def __str__(self):
        output = '<-'
        i = self.head
        if self.head < self.tail:
            while i < self.tail:
                output = output + str(self.body[i]) + '-'
                i = i+1
        else:
            while i < len(self.body):
                output = output + str(self.body[i]) + '-'
                i = i+1
            i = 0
            while i < self.tail:
                output = output + str(self.body[i]) + '-'
                i = i+1
        output = output +'<'
        output = output + '     ' + self.summary()
        return output

    def get_size(self):
        """ Return the internal size of the queue. """
        return sys.getsizeof(self.body)

    def summary(self):
        """ Return a string summary of the queue. """
        return ('Head:' + str(self.head)
               + '; tail:' +  str(self.tail)
               + '; size:' + str(self.size))
        
    def grow(self):
        """ Grow the internal representation of the queue.

        This should not be called externally.
        """
        # print('growing')
        # print('Before growing:')
        # print(self)
        oldbody = self.body
        self.body = [None] * (2*self.size)
        oldpos = self.head
        pos = 0
        if self.head < self.tail:     #data is not wrapped around in list
            while oldpos <= self.tail:
                self.body[pos] = oldbody[oldpos]
                oldbody[oldpos] = None           
                pos = pos + 1
                oldpos = oldpos + 1
        else:                         #data is wrapped around
            while oldpos < len(oldbody):
                self.body[pos] = oldbody[oldpos]
                oldbody[oldpos] = None           
                pos = pos + 1
                oldpos = oldpos + 1
            oldpos = 0
            while oldpos <= self.tail:
                self.body[pos] = oldbody[oldpos]
                oldbody[oldpos] = None
                pos = pos + 1
                oldpos = oldpos + 1
        self.head = 0
        self.tail = self.size 

    def shrink(self):
        """Shrink the internal representation of the queue.

        Should not be called externally
        """

        oldbody = self.body
        self.body = [None] * math.floor(len(self.body) / 2)
        oldpos = self.head
        pos = 0

        if self.head < self.tail:
            while oldpos <= self.tail:
                self.body[pos] = oldbody[oldpos]
                pos += 1
                oldpos += 1
        else:
            while oldpos < len(oldbody):
                self.body[pos] = oldbody[oldpos]
                pos += 1
                oldpos += 1
            oldpos = 0
            while oldpos <= self.tail:
                self.body[pos] = oldbody[oldpos]
                pos += 1
                oldpos += 1

        self.head = 0
        self.tail = self.size

    def enqueue(self,item):
        """ Add an item to the queue.

        Args:
            item - (any type) to be added to the queue.
        """
        # An improved representation would use modular arithmetic
        if self.size == 0:
            self.body[0] = item      # assumes an empty queue has head at 0
            self.size = 1
            self.tail = 1
        else:
            self.body[self.tail] = item
            # print('self.tail =', self.tail, ': ', self.body[self.tail])
            self.size = self.size + 1
            if self.size == len(self.body):  # list is now full
                self.grow()                  # so grow it ready for next enqueue
            elif self.tail == len(self.body)-1:  # no room at end, but must be at front
                self.tail = 0
            else:
                self.tail = self.tail + 1
        #print(self)

    def dequeue(self):
        """ Return (and remove) the item in the queue for longest. """
        # An improved implementation would use modular arithmetic
        if self.size == 0:     # empty queue
            return None
        item = self.body[self.head]
        self.body[self.head] = None
        if self.size == 1:  # just removed last element, so rebalance
            self.head = 0
            self.tail = 0
            self.size = 0
        elif self.head == len(self.body) - 1:  # if head was the end of the list
            self.head = 0  # we must have wrapped round, so point to start
            self.size = self.size - 1
        else:            
            self.head = self.head + 1  # just move the pointer on one cell
            self.size = self.size - 1
        # we haven't changed the tail, so nothing to do

        if self.size > 10 and self.size < len(self.body)/4:
            self.shrink()

        return item

    def length(self):
        """ Return the number of items in the queue. """
        return self.size

    def first(self):
        """ Return the first item in the queue. """
        return self.body[self.head]      # will return None if queue is empty


#implementation using arthimetic to track the tail instead of an extra variable, part iv)
class QueueV4:
    def __init__(self):
        self.body = [None] * 10
        self.size = 0
        self.head = 0

    def __str__(self):
        output = '<-'
        current_pos = self.head
        if self.head < (self.head + self.size) % len(self.body):
            while self.body[current_pos] != None:
                output += str(self.body[current_pos]) + '-'
                current_pos += 1
        else:
            while current_pos < len(self.body):
                output += str(self.body[current_pos]) + '-'
                current_pos += 1
            current_pos = 0
            while self.body[current_pos] != None:
                output += str(self.body[current_pos]) + '-'
                current_pos += 1

        return output + '<'

    def enqueue(self, item):
        next_item_index = (self.head + self.size) % len(self.body)

        if self.body[next_item_index] != None:
            self.grow()

        self.body[next_item_index] = item

        self.size += 1

    def dequeue(self):
        item = self.body[self.head]
        self.body[self.head] = None
        self.head = (self.head + 1) % len(self.body)

        if self.size > 10 and self.size <= len(self.body)/4:
            self.shrink()

        self.size -= 1
        return item

    def front(self):
        return self.body[self.head]

    def grow(self):
        oldbody = self.body
        oldpos = self.head
        pos = 0
        self.body = [None] * (self.size * 2)

        if self.head < (self.head + self.size) % len(oldbody):   
            while oldpos <= (self.head + self.size) % len(oldbody):
                self.body[pos] = oldbody[oldpos]
                oldbody[oldpos] = None           
                pos = pos + 1
                oldpos = oldpos + 1
        else:
            while oldpos < len(oldbody):
                self.body[pos] = oldbody[oldpos]
                oldbody[oldpos] = None           
                pos = pos + 1
                oldpos = oldpos + 1
            oldpos = 0
            while oldpos <= (self.head + self.size) % len(oldbody):
                self.body[pos] = oldbody[oldpos]
                oldbody[oldpos] = None
                pos = pos + 1
                oldpos = oldpos + 1
        self.head = 0

    def shrink(self):
        oldbody = self.body
        oldpos = self.head
        pos = 0
        self.body = [None] * math.floor(len(self.body) / 2)

        if self.head < (self.head + self.size) % len(oldbody):
            while oldpos <= (self.head + self.size) % len(oldbody):
                self.body[pos] = oldbody[oldpos]
                oldbody[oldpos] = None
                pos += 1
                oldpos += 1
        else:
            while self.head < len(oldbody):
                self.body[pos] = oldbody[oldpos]
                oldbody[oldpos] = None
                pos += 1
                oldpos += 1
            oldpos = 0
            while oldpos <= (self.head + self.size) % len(oldbody):
                self.body[pos] = oldbody[oldpos]
                oldbody[oldpos] = None
                pos += 1
                oldpos += 1
        self.head = 0

    def length(self):
        return self.size
    
    def get_size(self):
        return sys.getsizeof(self.body)
    
def test_queues(n):
    """ Compare performance of different queue implementations. 

    Args:
        n - the (int) number of items to be added to each queue during evaluations
    """

    print("Creating a queue of each type.")
    q1 = QueueV3()
    q2 = QueueV4()
    qlist = [q1, q2]

    print("Lengths of empty queues: ", end = " ")
    for q in qlist:
        print("", q.length(), end=" ")
    print()
    print("First basic enqueuing and dequeuing:")
    for i in range(len(qlist)):
        qlist[i].enqueue(1)
        qlist[i].enqueue('a')
        qlist[i].dequeue()
        qlist[i].enqueue(2)
        qlist[i].enqueue(3)
        qlist[i].enqueue(4)
        qlist[i].enqueue('b')
        qlist[i].enqueue('c')
        qlist[i].dequeue()
        print('q', i, ':', qlist[i])
        print(qlist[i].get_size())

    print('enqueuing', str(n), 'items, then dequeuing', \
          str(n), 'in each queue:')
    for i in range(len(qlist)):
        start_time = time.perf_counter()
        for j in range(n):
            qlist[i].enqueue(1)
        for j in range(n):
            qlist[i].dequeue()
        end_time = time.perf_counter()
        print(i, 'took', end_time - start_time,
              'and has size', qlist[i].get_size(),
              'but length', qlist[i].length())

    print('now start again, and maintain a queue of size 20 through',
          str(n), 'operations')
    qlist[0] = QueueV3()
    qlist[1] = QueueV4()
    for i in range(len(qlist)):
        start_time = time.perf_counter()
        for j in range(20):
            qlist[i].enqueue(1)
        for j in range(n):
            qlist[i].enqueue(1)
            qlist[i].dequeue()
        end_time = time.perf_counter()
        print(i, 'took', end_time - start_time,
              'and has size', qlist[i].get_size(),
              'but length', qlist[i].length())
        
test_queues(100000)