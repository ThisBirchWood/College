#STUDENT NUMBER: 122415616

from cpu import CPU
from gpu import GPU
from ram import RAM
from ssd import SSD
from hdd import HDD
from psu import PSU
from motherboard import Motherboard

def format_object_list(object_list):
    """Formats a list of objects to be printed"""
    formatted_list = []
    for object in object_list:
        formatted_list.append(str(object))
    return formatted_list

class Computer:
    def __init__(self, psu):
        """
        Motherboard must be set with CPU, GPU and RAM before put in case
        """
        self._motherboard = None
        self._psu = PSU(psu.manufacturer, psu.model, psu.generation, psu.tdp, psu.price, psu.released, psu.wattage, psu.efficiency, psu.modular)

    def __str__(self):
        if self._motherboard != None:
            return f"Computer with {self._motherboard} and {self._psu}"
        else:
            return f"Computer without motherboard and a {self._psu} PSU"

    def list_specs(self):
        """Returns a list of all components in computer"""
        if self._motherboard != None:
            print("Motherboard: " + str(self._motherboard))
            print("CPU: " + str(self._motherboard.cpu))
            print("GPU: " + str(self._motherboard.gpu))
            print("RAM slots: " + str(format_object_list(self._motherboard.ram_slots)))
            print("Storage slots: " + str(format_object_list(self._motherboard.storage)))
            print("PSU: " + str(self._psu))
        else:
            print("Motherboard not set!")

    def total_price(self):
        """Returns total price of computer in euros"""
        if self._motherboard != None:
            total_price = self._motherboard.price
            total_price += self._motherboard.cpu.price
            total_price += self._motherboard.gpu.price
            for ram in self._motherboard.ram_slots:
                if ram != None:
                    total_price += ram.price
            for storage in self._motherboard.storage:
                if storage != None:
                    total_price += storage.price
            return total_price
        else:
            return "Motherboard not set!"
        
    def total_wattage(self):
        """Returns total wattage of computer"""
        if self._motherboard != None:
            total_wattage = self._motherboard.tdp
            total_wattage += self._motherboard.cpu.tdp
            total_wattage += self._motherboard.gpu.tdp
            for ram in self._motherboard.ram_slots:
                if ram != None:
                    total_wattage += ram.tdp
            for storage in self._motherboard.storage:
                if storage != None:
                    total_wattage += storage.tdp
            return total_wattage
        else:
            return "Motherboard not set!"
    
    def get_motherboard(self):
        return self._motherboard
    
    def remove_motherboard(self):
        """Removes motherboard from computer and returns it"""
        motherboard = self._motherboard
        self._motherboard = None
        return motherboard
    
    def get_cpu(self):
        return self._motherboard.cpu
    
    def get_gpu(self):
        return self._motherboard.gpu
    
    def get_ram(self):
        return self._motherboard.ram_slots
    
    def get_storage(self):
        return self._motherboard.storage
    
    def set_motherboard(self, motherboard):
        """Sets motherboard in computer if compatible with case and returns error message if not"""
        if motherboard.cpu != None and motherboard.has_ram():
            self._motherboard = motherboard
        else:
            return "Motherboard form factor not compatible with case or motherboard not properly set!"
          
    def boot(self):
        """Returns if the computer can boot or not based on if all components are compatible and present"""
        if self._motherboard.cpu != None and self._motherboard.gpu != None and self._motherboard.has_ram() and self.motherboard.storage[0] != None and self.wattage <= self._psu.wattage:
            return "Computer booted!"
        else:
            return "Some components are missing or not compatible!"
        
    motherboard = property(get_motherboard, set_motherboard)
    cpu = property(get_cpu)
    gpu = property(get_gpu)
    ram = property(get_ram)
    storage = property(get_storage)
    price = property(total_price)
    wattage = property(total_wattage)

if __name__ == "__main__":
    psu = PSU("Corsair", "RM750x", 4, 65, 100, 2014, 750, "80+ Gold", True)
    computer = Computer(psu)
    motherboard = Motherboard("ASUS", "TUF GAMING B650-Plus Wifi", 6, 5, 150, 2021, 4, "DDR5", "B650", "ATX")
    cpu = CPU("AMD", "Ryzen 9 7800x3d", 7, 160, 500, 2020, 8, 16, 4.2, 5, False, 7, "B650")
    gpu = GPU("NVIDIA", "GeForce RTX 4090", 4000, 450, 1699, 2022, 16384, 24, "GDDR6X", 1313, 2235, 5, True)
    ram1 = RAM("Corsair", "Dominator Titanium", 5, 3, 90, 2022, 8, 6400, "DDR5")
    ram2 = RAM("Corsair", "Dominator Titanium", 5, 3, 90, 2022, 8, 6400, "DDR5")
    ram3 = RAM("Corsair", "Dominator Titanium", 5, 3, 90, 2022, 8, 6400, "DDR5")
    ram4 = RAM("Corsair", "Dominator Titanium", 5, 3, 90, 2022, 8, 6400, "DDR5")
    storage1 = SSD("Samsung", "970 EVO Plus", 1, 8, 100, 2018, 2, "M.2", "NVMe", 3500, 3300)
    storage2 = HDD("Seagate", "Barracuda", 2, 10, 40, 2015, 2, "SATA", "3.5", 140, 150)

    motherboard.set_cpu(cpu)
    motherboard.set_gpu(gpu)
    motherboard.set_ram(ram1, 0)
    motherboard.set_ram(ram2, 1)
    motherboard.set_ram(ram3, 2)
    motherboard.set_ram(ram4, 3)
    motherboard.set_storage(storage1, 0)
    motherboard.set_storage(storage2, 1)
    computer.set_motherboard(motherboard)
    print(computer.list_specs())
    print(computer.price)
    print(computer.wattage)
    print(computer.boot())

    motherboard.remove_cpu()
    print(computer.boot())

    old_psu = PSU("Thermaltake", "Smart RGB", 4, 65, 100, 2009, 450, "None", False)
    bad_computer = Computer(old_psu)

    bad_motherboard = Motherboard("Asrock", "970M Pro3", "9", 5, 50, 2015, 4, "DDR3", "970", "Micro ATX")
    bad_cpu = CPU("AMD", "FX-8350", 8, 125, 200, 2012, 8, 8, 4, 4.2, False, 32, "970")
    bad_gpu = GPU("Nvidia", "GT 210", 200, 30, 50, 2009, 16, 0.5, "DDR3", 400, 520, 57, False)
    bad_ram = RAM("Kingston", "HyperX Fury", 3, 5, 30, 2014, 4, 1600, "DDR3")
    bad_ram2 = RAM("Kingston", "HyperX Fury", 3, 5, 30, 2014, 4, 1600, "DDR3")
    bad_storage = HDD("Seagate", "Barracuda", 2, 10, 40, 2015, 2, "SATA", "3.5", 140, 150)

    bad_motherboard.set_cpu(bad_cpu)
    bad_motherboard.set_gpu(bad_gpu)
    bad_motherboard.set_ram(bad_ram, 0)
    bad_motherboard.set_ram(bad_ram2, 2)
    bad_motherboard.set_storage(bad_storage, 0)
    bad_computer.set_motherboard(bad_motherboard)
    print(bad_computer.list_specs())
    print(bad_computer.price)
    print(bad_computer.wattage)
    print(bad_computer.boot())



    