#STUDENT NUMBER: 122415616

class ComputerPart:
    def __init__(self, manufacturer, model, generation, tdp, price, released):
        self._manufacturer = manufacturer
        self._model = model
        self._generation = generation
        self._tdp = tdp
        self._price = price
        self._released = released

    def get_manufacturer(self):
        return self._manufacturer
    
    def get_model(self):
        return self._model
    
    def get_generation(self):
        return self._generation
    
    def get_tdp(self):
        return self._tdp
    
    def get_price(self):
        return self._price
    
    def get_released(self):
        return self._released
    
    def set_price(self, value):
        self._price = value

    manufacturer = property(get_manufacturer)
    generation = property(get_generation)
    model = property(get_model)
    tdp = property(get_tdp)
    price = property(get_price, set_price)
    released = property(get_released)