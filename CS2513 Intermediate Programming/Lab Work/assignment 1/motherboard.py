#STUDENT NUMBER: 122415616

from computer_part import ComputerPart
from cpu import CPU
from gpu import GPU
from ram import RAM
from ssd import SSD

class Motherboard(ComputerPart):
    """Class for a motherboard."""
    def __init__(self, manufacturer, model, generation, tdp, price, released, ram_slots_number, ram_type, chipset, form_factor, storage_slots_number = 6):
        super().__init__(manufacturer, model, generation, tdp, price, released)
        self._ram_slots = [None] * ram_slots_number
        self._ram_type = ram_type
        self._chipset = chipset
        self._form_factor = form_factor
        self._storage_slots = [None] * storage_slots_number

        self._cpu = None
        self._gpu = None

    def get_ram_slots(self):
        return self._ram_slots
    
    def get_ram_type(self):
        return self._ram_type
    
    def get_chipset(self):
        return self._chipset
    
    def get_form_factor(self):
        return self._form_factor
    
    def get_cpu(self):
        return self._cpu
    
    def get_gpu(self):
        return self._gpu
    
    def get_storage(self):
        return self._storage_slots
    
    def set_cpu(self, cpu):
        if cpu.get_chipset() == self._chipset:
            self._cpu = cpu
        else:
            return "CPU chipset not compatible with motherboard socket!"

    def set_gpu(self, gpu):
        self._gpu = gpu

    def set_storage(self, storage, slot):
        """Sets storage in a storage slot if it's empty"""
        if self._storage_slots[slot] == None:
            self._storage_slots[slot] = storage
        else:
            return "Storage slot already occupied!"

    def set_ram(self, ram, slot):
        """Sets RAM in a RAM slot if it's empty and RAM type is compatible"""
        if ram.get_type() == self._ram_type and self._ram_slots[slot] == None:
            self._ram_slots[slot] = ram
        else:
            return "RAM type not compatible with motherboard RAM type or RAM slot already occupied!"
    
    def has_ram(self):
        """Returns true if the motherboard has any RAM in it"""
        for ram in self._ram_slots:
            if ram != None:
                return True
        return False
    
    def remove_cpu(self):
        """Removes CPU from motherboard and returns it"""
        cpu = self._cpu
        self._cpu = None
        return cpu
    
    def remove_gpu(self):
        """Removes GPU from motherboard and returns it"""
        gpu = self._gpu
        self._gpu = None
        return gpu
    
    def remove_ram(self, slot):
        """Removes RAM from motherboard and returns it"""
        ram = self._ram_slots[slot]
        self._ram_slots[slot] = None
        return ram

    ram_slots = property(get_ram_slots)
    ram_type = property(get_ram_type)
    chipset = property(get_chipset)
    form_factor = property(get_form_factor)
    cpu = property(get_cpu, set_cpu)
    gpu = property(get_gpu, set_gpu)
    storage = property(get_storage)
    
    def __str__(self):
        return f"Motherboard: {self._manufacturer} {self._model} {self._chipset} {self._form_factor}"
    
if __name__ == "__main__":
    motherboard = Motherboard("Asus", "ROG Strix Z490-E Gaming", 10, 125, 300, 2020, 4, "DDR4", "Z490", "ATX")
    print(motherboard)
    print(motherboard.cpu)
    motherboard.set_cpu(CPU("Intel", "Core i9-10900K", 10, 125, 500, 2020, 10, 20, 3.7, 5.3, True, 14, "Z490"))
    motherboard.set_gpu(GPU("Nvidia", "RTX 3090", 3000, 350, 1500, 2020, 12000, 24, "GDDR6X", 1395, 1695, 8, True))
    print(motherboard.storage)
    print(motherboard.cpu)
    print(motherboard.gpu)
    motherboard.set_ram(RAM("Corsair", "Vengeance LPX", 4, 15, 60, 2020, 8, 3200, "DDR4"), 0)
    motherboard.set_ram(RAM("Corsair", "Vengeance LPX", 4, 15, 60, 2020, 8, 3200, "DDR4"), 2)
    print(motherboard.get_ram_slots())

