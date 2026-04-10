#Reusing attributes and methods of parent class in child class

class Employee:
    start_time = "10am"
    end_time = "6pm"

    def change_time(self, new_end_time):
        self.end_time = new_end_time

class Teacher(Employee):
    def __init__(self, subject):
        self.subject = subject

class AdminStaff(Employee):
    def __init__(self, role):
        self.role = role

class Accountant(AdminStaff):
    def __init__(self, salary, role):
        super().__init__(role)              #calling constructore of parent class by super keyword
        self.salary = salary

t1 = Teacher("maths")

print(t1.start_time, t1.end_time, t1.subject)

s1 = AdminStaff("Manager")
print(s1.start_time, s1.end_time, s1.role)

a1  = Accountant(30000, "CA")
print(a1.start_time, a1.end_time, a1.role, a1.salary)

