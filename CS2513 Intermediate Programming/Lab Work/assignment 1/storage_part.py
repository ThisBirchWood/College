#STUDENT NUMBER: 122415616

from computer_part import ComputerPart

class StoragePart(ComputerPart):
    """Base class for a storage part."""
    def __init__(self, manufacturer, model, generation, tdp, price, released, capacity, type):
        super().__init__(manufacturer, model, generation, tdp, price, released)
        self._capacity = capacity
        self._type = type

    def get_capacity(self):
        return self._capacity
    
    def get_type(self):
        return self._type
    
    capacity = property(get_capacity)
    type = property(get_type)
