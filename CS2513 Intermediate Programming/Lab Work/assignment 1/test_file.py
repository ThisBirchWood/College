#STUDENT NUMBER: 122415616

from cpu import CPU
from gpu import GPU
from ram import RAM
from ssd import SSD
from hdd import HDD
from psu import PSU
from motherboard import Motherboard
from computer import Computer
from computer_part import ComputerPart
from storage_part import StoragePart

#Test 1
print("--------------------")
print("Test 1 - CPU")
cpu = CPU("Intel", "i9-14900k", 14, 150, 550, 2023, 20, 32, 4.6, 5.6, True, 7, "Z790")
print(cpu)
print(cpu.base_clock)
print(cpu.get_value())
print(cpu.get_performance())

#Test 2
print("--------------------")
print("Test 2 - GPU")
gpu = GPU("NVIDIA", "RTX 4090", 40, 400, 1699, 2022, 16384, 24, "GDDR6X", 1313, 2235, 5, True)
print(gpu)
print(gpu.get_performance())
print(gpu.generation)
print(gpu.core_clock)
gpu.core_clock = 2500
print(gpu.core_clock)

#Test 3
print("--------------------")
print("Test 3 - RAM")
ram = RAM("Corsair", "Dominator Platinum", 5, 3, 90, 2022, 8, 6400, "DDR5")
print(ram)
print(ram.overclock(400))
print(ram)
print(ram.size)

#Test 4
print("--------------------")
print("Test 4 - SSD")
ssd = SSD("Samsung", "980 Pro", 5, 3, 90, 2022, 1, "M.2", "NVMe", 5000, 7000)
print(ssd)
print(ssd.read_speed)
print(ssd.get_performance())

#Test 5
print("--------------------")
print("Test 5 - HDD")
hdd = HDD("Seagate", "Barracuda", 2, 10, 40, 2015, 2, "SATA", "3.5", 140, 150)
print(hdd)
print(hdd.get_performance())
print(hdd.capacity)

#Test 6
print("--------------------")
print("Test 6 - PSU")
psu = PSU("Corsair", "RM750x", 4, 65, 100, 2014, 750, "80+ Gold", True)
print(psu)
print(psu.efficiency)
print(psu.modular)

#Test 7
print("--------------------")
print("Test 7 - Motherboard")
motherboard = Motherboard("Asus", "ROG Strix Z790-E Gaming", 10, 125, 300, 2022, 4, "DDR5", "Z790", "ATX")
print(motherboard)
print(motherboard.ram_type)
motherboard.set_cpu(cpu)
print(motherboard.cpu)
motherboard.set_gpu(gpu)
print(motherboard.gpu)
motherboard.set_ram(ram, 0)
motherboard.set_ram(ram, 2)
print(motherboard.ram_slots)
motherboard.set_storage(ssd, 0)
motherboard.set_storage(hdd, 1)
print(motherboard.storage)

#Test 8
print("--------------------")
print("Test 8 - Computer")
computer = Computer(psu)
print(computer)
computer.set_motherboard(motherboard)
print(computer.motherboard)
print(computer.cpu)
print(computer.price)
print(computer.wattage)

