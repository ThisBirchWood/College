class Dog:
    def __init__(self, name, human_years):
        self._name = name
        self._human_years = human_years
        self._dog_years = human_years * 7

sam = Dog("Sam", 11)