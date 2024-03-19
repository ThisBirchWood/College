# PAGES hold PID
from linked_list import LinkedList
from queue_gs import Queue
from random import randint

PAGE_SIZE = 4
RAM_SIZE = 4096
BLOCK_SIZES = [8, 16, 32, 64, 128, 256, 512, 1024, 2048]

class Page:
    def __init__(self, start_address):
        self.start_address = start_address
        self.pid = None

        self.access_flag = 0

    def __repr__(self):
        return f"Page-SA:0x{self.start_address}/PID:{self.pid}"

    # assigns a process to this page
    def allocate(self, pid: int):
        if self.pid is None:
            self.pid = pid
            self.access_flag = randint(0, 1)    # to simulate it being accessed
            return True
        return False

    # removes the process   
    def deallocate(self):
        self.pid = None

class Block:
    def __init__(self, start_address, no_pages):
        self.start_address = start_address
        self.pages = [Page(start_address+(i*PAGE_SIZE)) for i in range(no_pages)]

        self.free_memory = no_pages * PAGE_SIZE
        self.used_memory = 0
        self.total_memory = no_pages * PAGE_SIZE

        self.block_category = self.total_memory

        # a dictionary with process id's as keys and values as lists of their allocated pages
        self.process_allocations = {}

    def __repr__(self):
        return f":::Block/SA:{self.start_address}/Memory:{self.total_memory}kb/Free Memory:{self.free_memory}kb/Used Memory:{self.used_memory}kb:::"

    # gets the largest run of free pages in the block
    def _largest_run_of_free_pages(self):
        start_index = 0
        end_index = 0
        current_stretch = 0
        max_stretch = 0
        max_start = 0
        max_end = 0
        
        # algorithm to find the longest stretch of free pages
        for i, page in enumerate(self.pages):
            if page.pid == None:
                if current_stretch == 0:
                    start_index = i
                current_stretch += 1
                end_index = i
                if current_stretch > max_stretch:
                    max_stretch = current_stretch
                    max_start = start_index
                    max_end = end_index
            else:
                current_stretch = 0

        return max_start, max_end, max_stretch

    # returns a string representation of the block, 'x' for an allocated page, '-' for a free page
    def view_block(self):
        string = ''
        for page in self.pages:
            if page.pid == None:
                string += '-'
            else:
                string += 'x'
        return string
    # takes in a process id and size and tries to find enough contiguous pages to satisfy the request
    # returns None if not enough contiguous pages were found, otherwise returns a list of pages
    def allocate_memory(self, pid: int, size: int):
        results = self._largest_run_of_free_pages()
        max_start = results[0]
        max_end = results[1]
        max_stretch = results[2]

        # this runs through the free stretch and allocates just enough pages
        pages = []
        if max_stretch*PAGE_SIZE >= size:
            remaining_size = size
            current_index = max_start
            while remaining_size > 0:
                page = self.pages[current_index]
                page.allocate(pid)
                current_index += 1
                remaining_size -= PAGE_SIZE
                pages.append(page)
        else:
            return None
        
        self.process_allocations[pid] = pages
        self.free_memory -= len(pages) * PAGE_SIZE
        self.used_memory += len(pages) * PAGE_SIZE
        return pages

    ## takes in a PID and deallocates it from all pages it's using
    def deallocate_memory(self, pid):
        if pid in self.process_allocations:
            total_memory_saved = 0
            for page in self.process_allocations[pid]:
                page.deallocate()
                total_memory_saved += PAGE_SIZE
            self.used_memory -= total_memory_saved
            self.free_memory += total_memory_saved
            return total_memory_saved
        
    ## will take in a size in kb, will return whether or not the block can hold that much
    def has_amount(self, size: int):
        results = self._largest_run_of_free_pages()
        max_stretch = results[2]

        if max_stretch*PAGE_SIZE >= size:
            return True
        return False

class MemoryRequest:
    def __init__(self, pid, size):
        self.process_id = pid
        self.size = size

class MemoryManager:
    def __init__(self, memory_config):
        self.memory_config = memory_config
        self.total_memory = sum([value*key for key, value in self.memory_config.items()])
        self.used_memory = 0

        # clock variables
        self.clock_buffer = 10

        self.all_blocks = []
        self.free_blocks = {}

        self.processes_in_blocks = {}

        for block_size in BLOCK_SIZES:
            self.free_blocks[block_size] = LinkedList()

        addr = 0
        for key, value in self.memory_config.items():
            for i in range(key):
                block = Block(addr, int(value/PAGE_SIZE))
                self.free_blocks[value].append(block)
                self.all_blocks.append(block)
                addr += value

    # PRIVATE METHODS
    # takes a size in kb as input and returns the closest power of two that is smaller than it
    def _get_closest_power_of_two(self, size: int) -> int:
        for i, block_size in enumerate(sorted(BLOCK_SIZES)):
            if block_size >= size:
                return block_size
            
    # the same as the previous function except for that it gets the closest that is bigger than it
    def _get_closest_power_of_two_bigger(self, size: int) -> int:
        for i, block_size in enumerate(sorted(BLOCK_SIZES, reverse=True)):
            if block_size <= size:
                return block_size

    ## this method uses the _get_closest_power_of_two to search the dictionary for the smallest block that will 
    def allocate_memory(self, request: MemoryRequest):
        pid = request.process_id
        size = request.size
        smallest_block_size = self._get_closest_power_of_two(size)

        print(f"Attempting to allocate {size}kb of memory to process {pid}.")
        if size <= (self.total_memory - self.used_memory) and smallest_block_size != None:
            # starts with the smallest possible block for the request, works way up should they not be avaliable
            for block_size in [x for x in BLOCK_SIZES if x >= smallest_block_size]:
                if self.free_blocks[block_size].length() > 0:
                    block = self.free_blocks[block_size].pop_front()

                    block.allocate_memory(pid, size)

                    memory_left = block.free_memory
                    new_block_size = self._get_closest_power_of_two_bigger(memory_left)
                    if new_block_size:
                        self.free_blocks[new_block_size].append(block)
                        block.block_category = new_block_size
                    else:
                        block.block_category = None

                    print(f"Successfully allocated {size}kb to process {pid}.")

                    # update process id dictionary
                    if pid in self.processes_in_blocks:
                        self.processes_in_blocks[pid].append(block)
                    else:
                        self.processes_in_blocks[pid] = []
                        self.processes_in_blocks[pid].append(block)

                    return True
            
            # if the algorithm gets here, it means it wasn't able to find a suitable block, therefore page replacement is needed
            self.clock_algorithm(request)
            return True
        else:
            print("Not enough memory.")
            return False
           
    # takes in a PID and removes it from every block that it's in
    def deallocate_memory(self, pid: int):
        print(f"Attempting to deallocate Process {pid}.")
        for block in self.processes_in_blocks[pid]:
            if block.block_category:
                self.free_blocks[block.block_category].remove_by_value(block)
            block.deallocate_memory(pid)
            new_size_category = self._get_closest_power_of_two_bigger(block.free_memory)
            if new_size_category:
                self.free_blocks[new_size_category].append(block)
                block.block_category = new_size_category
            else:
                block.block_category = None

            print(f"Deallocated process {pid} from {block}.")

        del self.processes_in_blocks[pid]
            
    # prints every block in memory
    def string_main_memory(self):
        string = ''
        for block in self.all_blocks:
            string += (block.view_block() + "\n")
        return string
    
    # replaces pages by looping through blocks until it 
    #finds one with enough space and replaces pages based off the access flag
    def clock_algorithm(self, request: MemoryRequest):
        pid = request.process_id
        size = request.size

        print(f"Attempting to replace pages for Process {pid}")
        # searches through all blocks to find suitable pages
        for block in self.all_blocks:
            if block.total_memory >= size:
                first_hand = 0
                second_hand = 0
                remaining_size = size
                possible_pages = []
                no_pages = 0

                # clock system to find pages that haven't been accessed
                while first_hand < len(block.pages)-1:
                    if second_hand >= self.clock_buffer:
                        first_hand += 1

                        if block.pages[first_hand] in possible_pages and block.pages[first_hand].access_flag == 0:
                            old_pid = block.pages[first_hand].pid
                            block.pages[first_hand].pid = pid
                            remaining_size -= PAGE_SIZE
                            
                            if pid in block.process_allocations:
                                block.process_allocations[pid].append(block.pages[first_hand])
                            else:
                                block.process_allocations[pid] = []
                                block.process_allocations[pid].append(block.pages[first_hand])
                                
                            if old_pid:
                                block.process_allocations[old_pid].remove(block.pages[first_hand])
                            no_pages += 1

                            if remaining_size <= 0:
                                break

                    if second_hand < len(block.pages)-1:
                        second_hand += 1

                        block.pages[second_hand].access_flag = 0
                        possible_pages.append(block.pages[second_hand])

                print(f"Successfully replaced {no_pages} pages for Process {pid} in {block}")

                # update process ids in the dictionary
                if pid in self.processes_in_blocks:
                    self.processes_in_blocks[pid].append(block)
                else:
                    self.processes_in_blocks[pid] = []
                    self.processes_in_blocks[pid].append(block)

                return
                            

class OperatingSystem():
    def __init__(self):
        self.memory_requests = Queue()
        self.memory_config = {32: 64, 16: 128, 8: 256, 2: 512}
        self.memory_manager = MemoryManager(self.memory_config)

    def __str__(self):
        return self.memory_manager.string_main_memory()

    def add_memory_request(self, request: MemoryRequest):
        self.memory_requests.enqueue(request)

    def process_memory_requests(self):
        while self.memory_requests.length() > 0:
            request = self.memory_requests.dequeue()
            self.memory_manager.allocate_memory(request)

    def process_finished(self, pid: int):
        self.memory_manager.deallocate_memory(pid)

os = OperatingSystem()

for i in range(200):
    os.add_memory_request(MemoryRequest(i, randint(15, 150)))

os.process_memory_requests()
print(os)
for i in range(200):
    if randint(0, 2) == 0:
        os.process_finished(i)

print(os)










            



