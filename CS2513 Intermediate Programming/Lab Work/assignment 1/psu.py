#STUDENT NUMBER: 122415616

from computer_part import ComputerPart

class PSU(ComputerPart):
    def __init__(self, manufacturer, model, generation, tdp, price, released, wattage, efficiency, modular):
        super().__init__(manufacturer, model, generation, tdp, price, released)
        self._wattage = wattage
        self._efficiency = efficiency
        self._modular = modular

    def get_wattage(self):
        return self._wattage
    
    def get_efficiency(self):
        return self._efficiency
    
    def get_modular(self):
        return self._modular
    
    def __str__(self):
        return f"{self._manufacturer} {self._model} / {self._wattage}W / {self._efficiency} efficiency / {self._tdp}W TDP / ${self._price}"
    
    wattage = property(get_wattage)
    efficiency = property(get_efficiency)
    modular = property(get_modular)

if __name__ == "__main__":
    psu = PSU("Corsair", "RM750x", 4, 65, 100, 2014, 750, "80+ Gold", True)
    print(psu)
