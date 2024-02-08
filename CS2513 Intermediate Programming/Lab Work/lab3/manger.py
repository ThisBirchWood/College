from person import Person

class Manager(Person):

    def __init__(self, identity, name, job, salary, project):
        super().__init__(identity, name, job, salary)
        self._project = project

    def getProject(self):
        return self._project

    def setProject(self, project):
        self._project = project

    project = property(getProject, setProject)

    def getPayRaise(self, percentage):
        #self._salary += self._salary * (percentage / 50)

        super().givePayRaise(percentage * 2)

    def __str__(self):
        return ("%s with job %s" % (super().__str__(), self._project))

if __name__ == "__main__":
    luca = Manager(125, "Luca", "Manger", 120000, "The Big Job")
    print(luca)
    luca.getPayRaise(10)
    print(luca)
    print(luca.project)