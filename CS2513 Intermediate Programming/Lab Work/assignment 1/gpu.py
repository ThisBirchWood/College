#STUDENT NUMBER: 122415616

from computer_part import ComputerPart

class GPU(ComputerPart):
    def __init__(self, manufacturer, model, generation, tdp, price, released, shaders, vram, vram_type, memory_clock, core_clock, process_size, ray_tracing):
        super().__init__(manufacturer, model, generation, tdp, price, released)
        self._shaders = shaders
        self._vram = vram
        self._vram_type  = vram_type
        self._memory_clock = memory_clock
        self._core_clock = core_clock
        self._process_size = process_size
        self._ray_tracing = ray_tracing

    def get_shaders(self):
        return self._shaders
    
    def get_vram(self):
        return self._vram
    
    def get_vram_type(self):
        return self._vram_type
    
    def get_memory_clock(self):
        return self._memory_clock
    
    def get_core_clock(self):
        return self._core_clock
    
    def get_process_size(self):
        return self._process_size
    
    def get_ray_tracing(self):
        return self._ray_tracing
    
    def set_memory_clock(self, memory_clock):
        self._memory_clock = memory_clock

    def set_core_clock(self, core_clock):
        self._core_clock = core_clock
    
    shaders = property(get_shaders)
    vram = property(get_vram)
    vram_type = property(get_vram_type)
    memory_clock = property(get_memory_clock, set_memory_clock)
    core_clock = property(get_core_clock, set_core_clock)
    process_size = property(get_process_size)
    ray_tracing = property(get_ray_tracing)

    def __str__(self):
        return f"{self._manufacturer} {self._model} / {self._shaders} shaders / {self._vram}GB {self._vram_type} / {self._core_clock}MHz core clock / {self._memory_clock}MHz memory clock / {self._process_size}nm process size / {self._tdp}W TDP / ${self._price}"

    def get_performance(self):
        """Returns a rough estimate of the GPU's performance based on the number of shaders and VRAM (beyond 8GB there's no difference)."""
        #very rough and inaccurate calculation of performance, but not meant to be accurate.
        if self._vram >= 8:
            return self._shaders / 10
        else:
            return (self._shaders /10 ) * 0.8
        
    def is_better_than(self, gpu):
        """Returns True if the GPU is better than the one passed as an argument, False otherwise."""
        return self.get_performance() > gpu.get_performance()
    
    def percentage_difference(self, gpu):
        """Returns the percentage difference in performance between the GPU and the one passed as an argument."""
        if self.get_performance() > gpu.get_performance():
            return (self.get_performance() - gpu.get_performance()) / gpu.get_performance() * 100
        else:
            return (gpu.get_performance() - self.get_performance()) / self.get_performance() * 100
        
if __name__ == "__main__":
    gpu = GPU("Nvidia", "RTX 2080 Ti", "Turing", 250, 1199.99, "Q4'18", 4352, 11, "GDDR6", 14000, 1350, 12, True)
    gpu2 = GPU("NVIDIA", "RTX 4090", "Ada Lovelace", 350, 1599.99, "Q4'22", 16384, 24, "GDDR6X", 1313, 2235, 5, True)
    print(gpu)
    print(gpu.get_performance())
    print(gpu.is_better_than(gpu2))
    print(gpu2.percentage_difference(gpu))

    print(gpu2.get_performance())
    print(gpu2.is_better_than(gpu))
    print(gpu2.percentage_difference(gpu))



    
