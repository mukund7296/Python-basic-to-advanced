# Python Classes and Objects - Example Program

class STUDENT:
    'Common base class for all employees'
    totalStudent = 0

    def __init__(self, name, fee,add):
        self.name = name
        self.fee = fee
        self.add=add
        STUDENT.totalStudent = STUDENT.totalStudent + 1

    def displayCount(self):
        print("Total Student = %d" % STUDENT.totalStudent)

    def displayStudent(self):
        print(f"Name:", self.name, ", \nFee:", self.fee,",\nAddress :",self.add)
        print("##################################")


stud1 = STUDENT("Devraj", 2500,"Beijing")
stud2 = STUDENT("Alok", 2150,"Shanghai")
stud3 = STUDENT("Satyam", 3200,"Hongkong")
stud1.displayStudent()
stud2.displayStudent()
stud3.displayStudent()
print("Total Student = %d" % STUDENT.totalStudent)