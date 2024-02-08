class cartesianPoint:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def __str__(self):
        return "X: " + str(self._x) + ", Y: " + str(self._y)

    def getX(self):
        return self._x
    
    def getY(self):
        return self._y
    
    def setX(self, x):
        self._x = x

    def setY(self, y):
        self._y = y

    x = property(getX, setX)
    y = property(getY, setY)

if __name__ == "__main__":
    point1 = cartesianPoint(24, 73)
    point1.y = 79
    print(point1)
    