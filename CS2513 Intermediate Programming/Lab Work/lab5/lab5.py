class Student(object):

    def __init__(self, name, studentid, credits):
        self._name = name
        self._studentid = studentid
        self._credits = credits

    def __str__(self):
        return "%s %d %d" % (self._name, self._studentid, self._credits)
    
    def __eq__(self, other):
        if self._studentid == other.studentid:
            return True
        return False
    
    def __ne__(self, other):
        return not self.__eq__(other)
    
    def __lt__(self, other):
        if self._credits < other.credits:
            return True
    
    def __gt__(self, other):
        if self._credits > other.credits:
            return True
    
    def setName(self, newName):
        self._name = newName

    def getName(self):
        return self._name
    
    def getStudentId(self):
        return self._studentid
    
    def setCredits(self, newCredits):
        self._credits = newCredits

    def getCredits(self):
        return self._credits
    
    name = property(getName, setName)
    studentid = property(getStudentId)
    credits = property(getCredits, setCredits)

if __name__ == "__main__":
     
    student1 = Student("John", 123, 250)
    student2 = Student("Bob", 456, 400)

    if student1 > student2:
        print("Student 1 has more credits")
    else:
        print("Student 2 has more credits")

    if student1 == student2:
        print("Student 1 and Student 2 have the same student id")
    else:
        print("Student 1 and Student 2 have different student ids")
    
    
