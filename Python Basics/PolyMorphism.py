# Multiple forms

class Employee:
    def get_designation(self):
        print("designation = Employee")

class Teacher(Employee):
    def get_designation(self):
        print("designation = teacher")

t1 = Teacher()
t1.get_designation()


#Duck Typing

class Assistant(Employee):
    def get_designation(self):
        print("designation = Assistant")

class Accountant(Employee):
    def get_designation(self):
        print("designation = accountant")

as1 = Assistant()
as1.get_designation()

ac1 = Accountant()
ac1.get_designation()
