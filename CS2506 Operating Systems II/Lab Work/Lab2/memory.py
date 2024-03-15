from queue_gs import Queue

PAGE_SIZE_KB = 4
RAM_SIZE_KB = 4096

memory_splitup = {1024: 1, 512: 2, 256: 4, 128: 8}

def adds_up(dic: dict, mem_lim: int) -> bool:
    mem = 0
    for kb, block_amount in dic.items():
        mem += (kb * block_amount)
    if mem == mem_lim:
        return True
    return False


class Page:
    def __init__(self, start_address):
        self.start_address = start_address

    def __str__(self):
        return f"Page-SA:{self.start_address}"

class Block:
    def __init__(self, start_index, end_index, size):
        self.start_index = start_index
        self.end_index = end_index
        self.size = size

    def __repr__(self):
        return f"Start:{self.start_index}->End:{self.end_index}"
    

class MemoryRequest:
    def __init__(self, pid: int, size_kb: int):
        self.pid = pid
        self.size = size_kb

class MainMemory:
    def __init__(self, memory_config):
        self.size = RAM_SIZE_KB
        self.memory_config = memory_config
        self.memory_requests = Queue()

        # store all pages in a list
        # might change to linked lists
        self.pages = [Page(i) for i in range(0, 4096, 4)]
        
        # these will contain the *free* blocks in memory
        self.free_memory = {}


        # creates all the keys (which are block sizes) and empty lists in the free_memory dict
        i = 0
        size = 0
        while size < RAM_SIZE_KB:
            size = 2 ** i
            if size >= PAGE_SIZE_KB:
                self.free_memory[size] = []

            i += 1

        # adds the block objects to their respective keys in the free_memory dict
        i = 0
        for kb, block_amount in self.memory_config.items():
            page_amount = kb / PAGE_SIZE_KB
            for j in range(block_amount):
                self.free_memory[kb].append(Block(i, page_amount+i-1, kb))
                i += page_amount
    
    def _closest_power_of_two(self, size_kb: int) -> int:
        if size_kb <= 0:
            return 1  # The closest power of 2 to 0 or negative numbers is 1

        power = 1
        while 2 ** power < size_kb:
            power += 1

        return 2 ** power


    def queue_request(self, request: MemoryRequest) -> Block:
        self.memory_requests.enqueue(request)



m = MainMemory(memory_splitup)
print(m.free_memory)
print(m.request_memory(128))
