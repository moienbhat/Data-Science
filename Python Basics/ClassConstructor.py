class Student:

    college_name = "Technology College"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name


stu1 = Student("Bashar", 27)
stu2 = Student("Mo", 24)
print(stu1.name)

print(stu1.get_name())

print(stu1.college_name)
print(stu2.college_name)
