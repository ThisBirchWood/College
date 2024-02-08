class process_allocation:
    def __init__(self):
        self.max_processes = 32768
        self.processes = set()
        
    def allocate_id(self) -> None:
        for i in range(self.max_processes):
            if i not in self.processes:
                self.processes.add(i)
                print(f"Allocated id {i}")
                return id
        return -1

    def release_id(self, id: int) -> bool:
        if id in self.processes:
            self.processes.remove(id)
            print(f"Released id {id}")
            return True
        return False

b = process_allocation()
b.allocate_id()
b.allocate_id()
b.allocate_id()
b.allocate_id()
b.allocate_id()
b.allocate_id()
b.allocate_id()
b.allocate_id()
b.release_id(2)
b.release_id(3)
b.release_id(1)
b.allocate_id()
print(b.processes)

