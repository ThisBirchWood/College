from time import sleep
from random import randint, uniform
from process_allocation import process_allocation
import sys, math


class Queue:
    def __init__(self):
        self.body = [None] * 10
        self.head = 0    #index of first element, but 0 if empty
        self.tail = 0    #index of free cell for next element
        self.size = 0    #number of elements in the queue


    def __str__(self):
            output = '<-'
            if self.size == 0:
                return '<-->'
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
            return output


    def grow(self):
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

        #if length of internal list is less than 1/4 of the number of items in the queue then shrink
        if len(self.body) > 10 and self.size < len(self.body)/4:
            self.shrink()

        return item

    def length(self):
        """ Return the number of items in the queue. """
        return self.size

    def first(self):
        """ Return the first item in the queue. """
        return self.body[self.head]      # will return None if queue is empty

# 0 = success
# 1 = finished running
# 2 = blocked

class process:
    def __init__(self, pid):
        self.pid = pid
        self.lifespan = uniform(0.1, 2.0)

    def __str__(self):
        return f"({self.pid})"

    # runs for the given time
    def run_for(self, time):
        ### this is to simulate a process being blocked
        chance_of_blocked = randint(0, 5)
        if chance_of_blocked == 1:
            return 2
        
        self.lifespan -= time
        sleep(time)
        
        # if process is finished executing
        if self.lifespan <= 0:
            return 1
        # if process has ran out of time
        return 0

class scheduler:
    def __init__(self, amount_of_queues):
        # Initialize a list to hold queues and blocked queue
        self.queues = []
        self.blocked_queue = Queue()

        for i in range(amount_of_queues):
            self.queues.append(Queue())

        # current number of processes
        self.amount_of_processes = 0

        self.initial_quantum = 0.1

    def _print_queues(self):
        for queue in range(len(self.queues)):
            print(f"Queue {queue+1} : {self.queues[queue]}")
        print(f"Blocked Queue: {self.blocked_queue}")
        print("------------------")

    #adds a process to the specified priority queue
    def add_process(self, process, priority):
        self.queues[priority].enqueue(process)
        self.amount_of_processes += 1

    # runs the next process in the given priority queue
    def run_process(self, priority):
        # get the process next in queue or randomly from the blocked queue
            # this is only to simulate blocked processes randomly returning
        random_number = randint(1, 5)

        if random_number == 1 and self.blocked_queue.length() > 0:
            # if process was blocked, take from the blocked queue
            current_process = self.blocked_queue.dequeue()
            priority = -1
        else:
            # process was not blocked
            current_process = self.queues[priority].dequeue()

        # if priority at the lowest priority queue
        if priority < len(self.queues)-1:
            new_priority = priority + 1
            quantum = self.initial_quantum * (priority+1)
        else:
            new_priority = priority
            quantum = current_process.lifespan

        result = current_process.run_for(quantum)
        self.amount_of_processes -= 1

        if result == 0:
            self.add_process(current_process, new_priority)
        elif result == 2:
            self.blocked_queue.enqueue(current_process)
            self.amount_of_processes -= 1

    # run next highest priority process
    def run_next_process(self):
        for i in range(len(self.queues)):
            if self.queues[i].length() > 0:
                self.run_process(i)
                break


    def start_cpu(self):
        while self.amount_of_processes > 0:
            # print the contents of the queues
            self._print_queues()
            # execute next process
            self.run_next_process()
        self._print_queues()
        
            
s = scheduler(4)
p = process_allocation()
for i in range(8):
    s.add_process(process(p.allocate_id()), randint(0, 3))
s.start_cpu()
