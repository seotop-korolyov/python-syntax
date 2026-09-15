#!/usr/bin/python3
# ============================================
# STUDENT MANAGEMENT SYSTEM
# ============================================


# 1. Create a class Student.
#
# Each student should have:
# - name
# - age
# - grades, stored in a list
#
# Add these methods:
#
# add_grade(grade)
#   Adds one new grade to the student's grades.
#
# average_grade()
#   Returns the average of all grades.
#   If the student doesn't have any grades,
#   return 0.
#
# display_info()
#   Prints:
#   Name: Anna
#   Age: 20
#   Grades: [85, 90, 78]
#   Average: 84.33


# ============================================


# 2. Create a class School.
#
# Each school should have:
# - name
# - students, stored in an empty list at the beginning
#
# Example:
# school name -> "Python Academy"
# students -> []


# Add these methods to School:


# add_student(student)
#
#   Receives a Student object and adds it
#   to the school's list of students.
#
#   Example idea:
#
#   anna = Student("Anna", 20, [85, 90])
#   school.add_student(anna)
#
#   After that:
#   school.students contains Anna.


# show_students()
#
#   Goes through ALL students using a for loop.
#   For every student, call:
#
#   student.display_info()
#
#   If we have Anna, Tom and Mia, it should
#   display information about all three.


# find_student(name)
#
#   Goes through the list of students.
#
#   Compare the name we are searching for
#   with each student's name.
#
#   If the student is found:
#       return that Student object
#
#   If no student has that name:
#       return None

# remove_student(student_name)
#
# It receives the NAME of a student.
#
# Go through self.students.
#
# If a student's name matches student_name:
#     remove that Student object from self.students
#     return True
#
# If you finish searching and nobody was found:
#     return False

# ============================================
# 3. CREATE OBJECTS
# ============================================


# Create the school:
#
# school = School("Python Academy")


# Create 3 Student objects:
#
# Anna
# age: 20
# grades: 85, 90, 78
#
# Tom
# age: 19
# grades: no grades
#
# Mia
# age: 21
# grades: 92, 88


# ============================================
# 4. ADD STUDENTS TO THE SCHOOL
# ============================================


# Use the add_student() method to add:
#
# Anna
# Tom
# Mia
#
# to the school.


# ============================================
# 5. DISPLAY ALL STUDENTS
# ============================================


# Call:
#
# school.show_students()
#
# It should print information about
# Anna, Tom and Mia.


# ============================================
# 6. SEARCH FOR A STUDENT
# ============================================


# Search for Tom:
#
# found_student = school.find_student("Tom")
#
# If Tom was found, display his information.
#
# Think about:
#
# if found_student ...
#
#     What method could you call here?


# ============================================
# 7. SEARCH FOR A STUDENT WHO DOESN'T EXIST
# ============================================


# Search for:
#
# school.find_student("Alex")
#
# Alex doesn't exist.
#
# The method should return None.
#
# Use an if condition to print:
#
# Student not found
#
# when the result is None.

# ============================================
# MAIN MENU
# ============================================
#
# Create an infinite while loop.
#
# Inside the loop print:
#
# 1. Add student
# 2. Show all students
# 3. Find student
# 4. Remove student
# 5. Add grade
# 6. Exit
#
# Ask the user:
#
# Choose an option:
#
# Save the answer in a variable called choice.
#
#
# For now implement ONLY:
#
# choice == "2"
#     call school.show_students()
#
# choice == "6"
#     print "Goodbye!"
#     stop the while loop
#
# Any other choice:
#     print "This option is not implemented yet."

#File for students
file_name = "school.json"

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
            print (f"The Student {self.name} doesn't have grades yet")
        print (f"Average: {self.average_grade()}")

class School():
    def __init__(self, name):
        self.name = name
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def show_students(self):
        for stud in self.students :
            stud.display_info()
            print ("///")

    def find_student(self, student_name):
        for stud in self.students :
            if stud.name == student_name :
                return stud
        return None

    def remove_student(self, student_name):
        for stud in self.students :
            if stud.name == student_name:
               self.students.remove(stud)
               return True 
        return False

#Add_student_menu
def add_student_menu(school):
    while True:
        name = input("Enter the name of the student: ").strip()
        if not name:
            print("Name cannot be empty.")
            continue
        break
    while True:
        try:
            age = int(input("Enter the student age: "))
            if age < 5 or age > 100:
                print("Invalid age. Please enter a number between 5 and 100.")
                continue
            break
        except ValueError:
            print("Invalid age. Please enter a valid number.")
    new_student = Student(name , age, [])
    school.add_student(new_student)
    print(f"Student {name} was added to the school {school.name}")

#Find_student_menu
def find_student_menu(school):
    while True:
        name = input("Enter the name of the student to find: ").strip()
        if not name:
            print("Name cannot be empty.")
            continue
        break
    student = school.find_student(name)
    if student:
        student.display_info()
    else:
        print(f"Student {name} was not found")

#Remove_student_menu
def remove_student_menu(school):
    while True:
        name = input("Enter the name of the student to remove: ").strip()
        if not name:
            print("Name cannot be empty.")
            continue
        break
    removed = school.remove_student(name)
    if removed:
        print(f"Student {name} was removed")
    else:
        print(f"Student {name} was not found")

#Add_grade_menu
def add_grade_menu(school):
    while True:
        name = input("Enter the name of the student to add a grade:").strip()
        if not name:
            print("Name cannot be empty.")
            continue
        break
    student = school.find_student(name)
    if student:
        while True:
            try:
                grade = int(input("Enter the grade to add:"))
                if grade < 0 or grade > 100:
                    print("Invalid grade. Please enter a number between 0 and 100.")
                    continue
                student.add_grade(grade)
                print(f"Grade {grade} was added to student {name}")
                break
            except ValueError:
                print("Invalid grade. Please enter a valid number.")
    else:
        print(f"Student {name} was not found")     

import json
#Save students to a file
def save_students(school):
    student_data = []

    for student in school.students:
        data = {
            "name": student.name,
            "age": student.age,
            "grades": student.grades
        }
        student_data.append(data)

    with open(file_name, "w") as file:
        json.dump(student_data, file, indent=4)
#Load students from a file
def load_students(school):
    try:
        with open(file_name, "r") as file:
            students_data = json.load(file)

        for data in students_data:
            new_student = Student(data["name"], data["age"], data["grades"])
            school.add_student(new_student)
    except FileNotFoundError:
        print(f"The file {file_name} is not found")

#Add a school
school = School("Python Academy")

#Load students from the file
load_students(school)

#Add students
#student_anna = Student("Anna", 20, [85, 90, 78])
#student_tom = Student("Tom", 19, [])
#student_mia = Student("Mia", 21, [92, 88])

#Add at the school
#school.add_student(student_anna)
#school.add_student(student_tom)
#school.add_student(student_mia)

#Main Menu
while True:
    print("1. Add student")
    print("2. Show all students")
    print("3. Find student")
    print("4. Remove student")
    print("5. Add grade")
    print("6. Save Students")
    print("7. Exit")

    choice = input("Choose an option: ")

#Add student 
    if choice == "1":
        add_student_menu(school)
#Show students
    elif choice == "2":
        school.show_students()
#Find student
    elif choice == "3":
        find_student_menu(school)
#Remove student
    elif choice == "4":
        remove_student_menu(school)
#Add grade
    elif choice == "5":
        add_grade_menu(school)
#Save students
    elif choice == "6":
        save_students(school)
#Exit
    elif choice == "7":
        print("Goodbye!")
        break
    else:
        print("This option is not implemented yet.")