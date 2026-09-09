#!/usr/bin/python3

print ("Hello there!")

first_name = "Script #"
name_line_0 = "Python "

quantity = 1
print (first_name, quantity)

quantity = quantity + 1
print (first_name, quantity)

name_boolean = True
print ("First boolean :", name_boolean)
name_boolean_2 = not name_boolean
print ("2nd boolean:", name_boolean_2)

print ("Number of the Script equal 2: ", quantity == 2)

equal = quantity != 0
print ("Scritp # is more than 0: ", equal)

#F-string
print (first_name, quantity)
print (f"Script #{quantity - 1}")
print (f"{first_name}{quantity - 1}")
task = "dishes"
print (f"Todo: {task}")

#comperation
print (f"Quantity: {quantity} is less then 0:", quantity < 0)

#type of variuble
print ("Type of Quantity: ", type(quantity))
print("Type of First_name variuble: ", type(first_name))

#Convert srt to integer
age = "20"
print ("Type of Age variuble", type(age))
print ("Convert age to int: ", int(age))

#Convert int to str
print ("int to str :", str(quantity))

print (int(9.99))
print (float(10))

#int with boolen

value_1 = int(name_boolean)
value_2 = int(name_boolean_2)

print (value_1)
print (value_2)

# bool()
str = "string"
str_empty = ""
int = 8.6
int_null = 0
print (bool(str), " ", bool(str_empty), " ", bool(int), " ", bool(int_null) )

# If conditions
if name_boolean:
  print ("If condition works because it is True")

answer = "Answer"
if answer == "Answer":
  print (answer+ " is correct!")
  print (answer, "is correct!")

hours = 20
if hours <= 6:
  print (f"It's night. The time is {hours}")
elif hours <= 12:
  print (f"It's morning. The time is {hours}")
elif hours >= 18:
  print (f"Good evening, The time is {hours}")
elif hours > 12:
  print (f"Good afternoon. The time is {hours}")


if hours >=6 and hours < 12:
  print (f"It's moning. The time is: {hours}")
if hours >=23 and hours <6:
  print (f"It's night. The time is: {hours}")
else:
  print (f"It's afternoon or evenig. The time is: {hours}")  

average_grade = "A"
final_score = 1400
if average_grade == "A" or final_score >= 1500:
  print ("Certificate achieved!")

# loops
number = 100
number += 10
print (f"Added +10 to 100 = {number}")
number -= 20
print (f"Subtract 20 from 100 = {number}")

#while loops
while number >=85:
  print (f"The Number is: {number}")
  number -= 1

#for loops

for i in range (5):
  print ("**********----------")
for i in range (5):
  print ("--------------------") 

# List
list = [ "One", "Two", "Three"]
print (list)
list += [ "Four" ]
print (list)
list.append (25)
print (list)

list_numbers = [20 , 21]
list_numbers += [22]
print (list_numbers)

list_numbers.insert (0, 19)
print (list_numbers)

list.pop()
print (list)
list.pop(1)
print (f"The List: {list}")

list2 = list.pop ()
print (f"I saved a deleted evement from the List in The List2 \"{list2}\"")

print ("Leng of the list", len(list))

# for and List
number_i = 0
print (f"the List: {list}")
for i in list:
  number_i += 1
  print (f"The number of element {number_i}: {i}")

# Operations with lists
temperature = [-3, 0, 2, 10, 7]
temperature_max = max(temperature)
temperature_min = min(temperature)
print (f"The maximum temperature was {temperature_max}")
print (f"The minimum temperature was {temperature_min}")
temperature.sort()
print (f"Sorting of the temperature {temperature}")

orders = [10, 5, 10]
orders_sum = sum(orders)
print (f"The sum of orders is: {orders_sum}")

order_count = orders.count(10)
print (f"The 10 orders in day was the {order_count} times.")
print ("The 10 in number of orders is:", 10 in orders)

new_users = "Alex Anna Tom Tim"
users_list = new_users.split()
print (f"Splited list of users: {users_list}")

#Separator
new_users_1 = "Alex; Anna; Tom; Tim"
users_list_1 = new_users_1.split("; ")
print (f"Seperatored list with the separator \"; \" : {users_list_1}")

#Replace
users_description = "Tim is full name of sportsman"
users_replaced = users_description.replace("Tim", "Timophey")
print (users_replaced)

#Functions
def count (first, second):
  result = first + second
  return result

print (f"The Sum of First and Second is: {count(3, 5)}")
result = count(12, 8)
print (f"The Sum of First and Second is: {result}")

def print_list (list):
  print (f"The orders: {list}")
  print (f"On Mondey it was {list[0]} orders")

print_list(orders)

#Tuple
films_name_date = ("Alian", 1986)
print (films_name_date)

#Tuples inside list
films = [(("Alian", 1986)), ("The time", 2001)]
print (f"Films in the list: {films}")

number = 1
for film in films:
  print (f"Film {number} is: {film}")
  number += 1

#Return multipel values from function by using tuples
def access_age (age):
  drive = age >= 18
  if drive == True:
    message = "are allowed to drive"
  else:
    message = "aren't allowed to drive"  
  return age, message

allow_drive = access_age (17)
print (f"The age is {allow_drive[0]} and you {allow_drive[1]}")

#Dictionary
locations = {
  "headquarters" : "New York",
  "flagship" : "Paris",
  "shipping" : ["12", "15", "17"]
}
print(locations)
print(f"The Headquarter is in {locations['headquarters']}")

students = {
  "Tim": 20,
  "Mia": 22,
  "Tom": 19,
  ("Art", "Stet"): 44,
  "student": ["Masha, Dima, Tanya"]
}

for student in students:
  print(f"Age of a student {students[student]}")

students["Tom"] = 20
print(students)

students["Teme"] = 23
print(students)
print("Teme is in Students:", 'Teme' in students)

if "Teme" in students:
  teme_students = students.pop("Teme")

print(f"Remove Teme from students {students}")
print(f"Teme is removed: {teme_students}")

# Set
set_zip = {"Z123", "P321", "f123"}
print(f"The Set: {set_zip}")

set_zip.add("A123")
print(f"Add into the Set: {set_zip}")

set_zip.remove("P321")
print(f"Remove from the Set: {set_zip}")

#List to set
list.append ("One")
list += ["Three", "Four"]
print (f"The list: {list}")

set_list = set(list)
print("Transform the List to a Set:", set_list)
print("The Length of a Set:", len(set_list))

#Subset
number_list = {"One", "Four"}
print (f"The Number_list is subset in set_list: {number_list.issubset(set_list)}")

#Union with Sets
classmates = {"Tim", "Art", "Tom"}
friends = {"Tim", "Svet", "Tom"}
union_sets = classmates.union(friends)
print(f"The Union is {union_sets}")

#Intersection
union_intersection = classmates.intersection(friends)
print(f"The Intersection is {union_intersection}")

#Difference
dif_piople = classmates.difference(friends)
print(f"The Dif between Classmates and Friends is: {dif_piople}")

#Comprehensions
prices = [12, 34, 54, 66]
halved = [price/2 for price in prices]
print(halved)

scores = [12 , 15, 34, 5, 32]
high_score = [score for score in scores if score >= 15]
print(high_score)

#Negative indexes
latest = scores[-1]
print(latest)

#Delet an element
print(f"The Scores is before deleting {scores}")
del scores[-2]
print(f"Deleted the element -2 in Scores {scores}")

#Retreave
print(f"Elements in the Scores from 2nd: {scores[2:]}")
print(f"Elements in the Scores from 2nd with step 2: {scores[0:3:2]}")

#Class
class First_class:
  print ("Inside the class!")
  variable1 = 13

  #Function in a class
  def bark (self):
    print ("barks")

  def variable_in_class (self):
    print (f"Access to a variable in the same class {self.variable1}")
  
  #the List inside a class
  list1 = ["USA", "Canada", "Alaska"]

  #constructor metod
  def __init__ (self, color, number):
    self.color = color
    self.number = number


class_inside = First_class("", "")
#Access to the variable in a class
class_color = First_class("white", 12)

print (f"The Color is {class_color.color}")
print (f"The Number is {class_color.number}")

print (f"Variable inside the class is: {class_inside.variable1}")

#Access to the function in a class
class_inside.bark()
class_inside.variable_in_class()
print (f"Access to the list in a class {class_inside.list1[1]}")

#Class2
class Pie:
  def __init__(self, flavor, ingredients):
    self.flavor = flavor
    self.ingredients = ingredients

  def perint_ingredients(self):
    for i in self.ingredients:
      print (i)

applePie = Pie("apple", ["flour", "eggs", "apples", "butter"])
applePie.perint_ingredients()

#Oject-orientated-programming
class Piggy:
  value = 0

  def addModey (self, amound):
    self.value = self.value + amound

myPiggy = Piggy()

print (f"In the Piggy bank are: ${myPiggy.value}")

myPiggy.addModey(100)
print (f"Add Money into Piggy bank: ${myPiggy.value}")

#Example
class Rectangle:
  base = 10
  height = 3

  def getArea(self):
    return self.base * self.height

rectangle_area = Rectangle()
area = rectangle_area.getArea()
print (f"The Aria is: {area}")

#Inheritance of class
class Parent():
  def __init__(self):
    self.eyes = "green"

class Child (Parent):
  def __init__(self):
    super().__init__()
    self.age = 7

child = Child()
child_eyes = child.eyes
child_age = child.age
print (f"The child has parent's eye color {child_eyes} and his age is {child_age}")

#One more test class with inheritance
class Person():
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def greed(self):
    print ("Hi!")

class Student(Person):
  def __init__(self, name, age, major):
    super().__init__(name, age)
    self.major = major

student = Student("Artem", "24", "IT")

print (f"The Student's major is: {student.major} and his name is {student.name}")
student.greed()

#Class polymorphism
class Feline():
  def speak (self):
    print ("Meow")

class Cat(Feline):
  def lick(self):
    print("Licking paw")

class Lion(Feline):
  def prey(self):
    print("Pounces on prey")
  def speak(self):
    return "ROAR!"

cat = Cat()
cat.speak()
lion = Lion()
print (f"Lion speak like {lion.speak()}")

#Modules
import math

print ("The value of pi is", math.pi)
#help (math)
#Import only one function
from math import pi
print ("The value of pi is", pi)

#rename the name of module
import math as mth
print ("The value of pi is", mth.pi)