# all in kb
PAGE_SIZE = 4
RAM_SIZE = 4096

class Page:
    def __init__(self, start_adr: int):
        self.start_address = start_adr

    def __str__(self):
        return f"Page-SA:{self.start_address}"

class Block:
    pass

class MemoryRequest:
    def __init__(self, pid: int, size: int):
        self.process_id = pid
        self.size = size

class MemoryManager:
    def __init__(self, ram_size):
        self.ram_size = ram_size


class OperatingSystem:
    def __init__(self):
        pass

    def request_memory(self, request: MemoryRequest):
        pass





