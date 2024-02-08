from person import Person

class Engineer(Person):
    def __init__(self, name, job, salary, speciality):
        super().__init__(name, job, salary)
        self._speciality = speciality

    def __str__(self):
        return super().__str__() + " " + self._speciality

    def getSpeciality(self):
        return self._speciality

    def setSpeciality(self, s):
        self._speciality = s

    speciality = property(getSpeciality, setSpeciality)

if __name__ == "__main__":
    e = Engineer("dylan", "engineer", 328582, "civil")
    print(e)