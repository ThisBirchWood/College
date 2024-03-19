from queue_gs import Queue
from linked_list import LinkedList

# in kb
PAGE_SIZE = 4
RAM_SIZE = 4096

def ram_amount(dic: dict) -> int:
    mem = 0
    for kb, block_amount in dic.items():
        mem += (kb * block_amount)
    return mem


class Page:
    def __init__(self, start_address):
        self.start_address = start_address

    def __repr__(self):
        return f"Page-SA:0x{self.start_address}"

class Block:
    def __init__(self, start_address, no_pages):
        self.start_address = start_address
        self.pages = [Page(start_address+(i*PAGE_SIZE)) for i in range(0, no_pages)]
        self.size = no_pages *  PAGE_SIZE

        self._process_id = None

    def __repr__(self):
        #return str([page for page in self.pages])
        return f":::Block@0x{self.start_address:08d}/{self.size}kb/PID:{self._process_id}:::"

    def allocate(self, pid) -> bool:
        if self._process_id is None:
            self._process_id = pid
            return True
        return False
    
    def deallocate(self):
        self._process_id = None


class MemoryRequest:
    def __init__(self, pid: int, size_kb: int):
        self.pid = pid
        self.size = size_kb

class MemoryManager:
    def __init__(self, memory_config):
        self.memory_config = memory_config

        self.all_memory = []
        self.free_memory = {}
        self.number_of_free_blocks = 0

        i = 2
        while 2 ** i < RAM_SIZE:
            self.free_memory[2**i] = LinkedList()
            i += 1
        del i

        addr = 0
        for key, value in self.memory_config.items():
            for i in range(key):
                b = Block(addr, int(value/PAGE_SIZE))
                self.free_memory[value].append(b)
                self.all_memory.append(b)
                addr += value
                self.number_of_free_blocks += 1
                
    def _get_closest_power_of_two(self, size: int) -> int:
        i = 0
        block_sizes = list(self.memory_config.values())

        while 2 ** i < size:
            i += 1
        return 2 ** i
            
    def allocate_memory(self, request: MemoryRequest):
        pid = request.pid
        size = request.size

        block_size = self._get_closest_power_of_two(size)
        print(block_size)
        
        # if there is space in the memory
        if self.number_of_free_blocks > 0:
            print(f"Searching memory for {size}kb for Process PID: {pid}.")
            if self.free_memory[block_size].length() > 0:
                block: Block = self.free_memory[block_size].pop()
                block.allocate(pid)
                print(f"Allocated {block} to PID: {pid}")
                return block
            print(f"No suitable block exists for Process: {pid} of size: {size}kb.")
            return None
        else:
            ## page replacement system here
            pass

    def deallocate_memory(self, block: Block):
        block.deallocate()
        self.free_memory.append(block)

    def clock_algorithm(self, buffer):
        first_hand = 0
        second_hand = 0

        all_pages = [x.pages for x in self.all_memory]
        print(all_pages)

        #while first_hand < len()

class OperatingSystem:
    def __init__(self, memory_config):
        self.memory_config = memory_config
        self.memory_manager = MemoryManager(memory_config)
        self.memory_requests = Queue()

        self.process_blocks = {}

    def queue_memory_request(self, request: MemoryRequest):
        self.memory_requests.enqueue(request)

    def process_memory_requests(self):
        for i in range(self.memory_requests.length()):
            request = self.memory_requests.dequeue()

            block = self.memory_manager.allocate_memory(request)
            self.process_blocks[request.pid] = block

    def process_finished(self, pid: int):
        block = self.process_blocks[pid]
        del self.process_blocks[pid]
        self.memory_manager.deallocate_memory(block)


memory_splitup = {8: 128, 4: 256, 2: 512, 1: 1024}
os = OperatingSystem(memory_splitup)

request1 = MemoryRequest(1, 1000)
request2 = MemoryRequest(2, 100)
request3 = MemoryRequest(3, 400)
request4 = MemoryRequest(4, 50)
os.queue_memory_request(request1)
os.queue_memory_request(request2)
os.queue_memory_request(request3)
os.queue_memory_request(request4)
os.process_memory_requests()

for block in os.memory_manager.all_memory:
    print(block)


