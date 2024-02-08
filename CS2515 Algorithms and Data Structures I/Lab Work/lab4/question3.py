from question2 import QueueV4

class Packet:
    def __init__(self, content, address, sender):
        self.content = content
        self.address = address
        self.sender = sender
        self.path = QueueV4()

    def path_length(self):
        return self.path.length()

class Client:
    def __init__(self, packets):
        self.packets = packets

    def send(self, packet):
        packet = self.packets.dequeue()
        current_router = packet.path.dequeue()
        current_router.packets.enqueue(packet)

class Router:	
    def __init__(self):
        self.packets = QueueV4()

    def process(self):
        packet = self.packets.dequeue()
        router = packet.path.dequeue()
        router.packets.enqueue(packet)
