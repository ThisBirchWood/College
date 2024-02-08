class Person(object):

    def __init__(self, name, job, salary): 
        self._name = name
        self._job = job
        self._salary = salary

    def __str__(self):
        return ("%s %s %i" % (self._name, self._job, self._salary))

    def givePayRaise(self, percentage):
        self._salary += self._salary * (percentage / 100)

    def getName(self):
        return self._name
    
    def getJob(self):
        return self._job
    
    def setJob(self, jobTitle):
        self._job = jobTitle

    def getSalary(self):
        return self._name

    def setSalary(self, salary):
        
        if type(salary) != int:
            print("Pass a number")
            return

        self._salary = salary

    name = property(getName)
    job = property(getJob, setJob)
    salary = property(getSalary, setSalary)
  
def main():
    cathal = Person(123, "Cathal", "Software person", 120000)

    cathal.givePayRaise(10)
    print(cathal)

if __name__ == "__main__":
    main()