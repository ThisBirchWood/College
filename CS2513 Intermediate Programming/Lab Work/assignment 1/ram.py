#STUDENT NUMBER: 122415616

from computer_part import ComputerPart

class RAM(ComputerPart):
    def __init__(self, manufacturer, model, generation, tdp, price, released, size, speed, type):
        super().__init__(manufacturer, model, generation, tdp, price, released)
        self._size = size
        self._initial_speed = speed
        self._current_speed = speed
        self._type = type

        self._overclock_max = 400

    def get_size(self):
        return self._size
    
    def get_speed(self):
        return self._speed
    
    def get_type(self):
        return self._type
    
    def __str__(self):
        return self._manufacturer + " " + self._model + " " + str(self._size) + "GB " + str(self._current_speed) + "MHz " + self._type + " RAM"
    
    def overclock(self, overclock_amount):
        """Overclocks the RAM by a given amount, if the amount is within the maximum overclock amount."""
        if (self._current_speed - self._initial_speed) + overclock_amount <= self._overclock_max:
            self._current_speed += overclock_amount
            return "Overclocked Successfully by " + str(overclock_amount) + " MHz!"
        else:
            return "System crashed!"
    
    size = property(get_size)
    speed = property(get_speed)
    type = property(get_type)

if __name__ == "__main__":
    ram = RAM("Corsair", "Vengeance LPX", 4, 65, 100, 2014, 8, 3200, "DDR4")
    print(ram)
    print(ram.overclock(400))
    print(ram)
    print(ram.overclock(500))
    print(ram)