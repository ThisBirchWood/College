#STUDENT NUMBER: 122415616

from computer_part import ComputerPart

class CPU(ComputerPart):
    def __init__(self, manufacturer, model, generation, tdp, price, released, cores, threads, base_clock, boost_clock, integrated_graphics, process_size, chipset):
        super().__init__(manufacturer, model, generation, tdp, price, released)
        self._cores = cores
        self._threads = threads
        self._base_clock = base_clock
        self._boost_clock = boost_clock
        self._integrated_graphics = integrated_graphics
        self._process_size = process_size
        self._chipset = chipset

    def get_cores(self):
        return self._cores
    
    def get_threads(self):
        return self._threads
    
    def get_base_clock(self):
        return self._base_clock
    
    def get_boost_clock(self):
        return self._boost_clock
    
    def get_integrated_graphics(self):
        return self._integrated_graphics
    
    def get_process_size(self):
        return self._process_size
    
    def get_chipset(self):
        return self._chipset
    
    def set_base_clock(self, value):
        self._base_clock = value

    def set_boost_clock(self, value):
        self._boost_clock = value

    cores = property(get_cores)
    threads = property(get_threads)
    base_clock = property(get_base_clock, set_base_clock)
    boost_clock = property(get_boost_clock, set_boost_clock)
    integrated_graphics = property(get_integrated_graphics)
    process_size = property(get_process_size)

    def __str__(self):
        return f"{self._manufacturer} {self._model} / {self._cores} cores / {self._threads} threads / {self._base_clock}GHz base clock / {self._boost_clock}GHz boost clock / {self._process_size}nm process size / {self._tdp}W TDP / ${self._price}"

    def get_performance(self):
        #very rough and inaccurate calculation of performance, but not meant to be accurate. The best I could do with the specs
        return (self._threads * self._boost_clock)/self._process_size
    
    def get_value(self):
        return (self.get_performance()*100)/self._price
    

if __name__ == "__main__":
    cpu = CPU("Intel", "Core 2 Duo E8400", 4, 65, 179, 2006, 2, 2, 3.0, 3.6, False, 45, "LGA775")
    print(cpu)
    print(cpu.get_performance())

    