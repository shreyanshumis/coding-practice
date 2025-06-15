class Student:
    def __init__(self, firstname, course, roll, batch, institute):
        self.firstname = firstname
        self.course = course
        self.roll = roll
        self.batch = batch
        self.institute = institute

    def Student(self):
        print("============================")
        print("|| First name :",self.firstname)
        print("|| Course : ",self.course)
        print("|| Roll : ",self.roll)
        print("|| Batch :",self.batch)
        print("|| Institute : ", self.institute)
        print("============================")

n = int(input("How many students are there?"))
for i in range(n):
    firstname = input("Enter name: ")
    course = input("Enter course: ")
    roll = int(input("Enter roll: "))
    batch = input("Enter batch: ")
    institute = input("Enter institute: ")

    chua = Student(firstname, course, roll, batch, institute)
    chua.Student()