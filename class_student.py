#!/usr/bin/python3
# Create a class Student.

# Each student should have:
# - name
# - age
# - grades, stored in a list

# Add these methods:
# 1. add_grade(grade)
#    Adds a grade to the student's list.

# 2. average_grade()
#    Returns the average of all grades.

# 3. display_info()
#    Prints something like:
#    Name: Anna
#    Age: 20
#    Grades: [85, 90, 78]
#    Average: 84.33

class Student():
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

    def add_grade(self, grade):
           self.grades.append(grade)

    def average_grade(self):
        if self.grades :
            return sum(self.grades) / len(self.grades)
        else:
            return 0
    
    def display_info(self):
        print (f"Name: {self.name}")
        print (f"Age: {self.age}")
        if self.grades :
            print (f"Grades: {self.grades}")
        else:
            print (f"The Student {self.name} doesn't have grades")
        print (f"Average: {self.average_grade()}")

name = "Anna"
age = 20
grades = [85, 90, 78]

student = Student(name, age, grades)
student.display_info()
student.add_grade(95)
student.display_info()

tom = Student("Tom", 19, [])
tom.display_info()