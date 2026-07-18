# Program: Functions
# Author: David
# Lesson: 13

# Creating your first function
def greet():
    print("Hello you")
greet()

# Calling it multiple times
def greet():
    print("Welcome")
greet()
greet()
greet()

# Functions with parameter
def greet_person(name):
    print(f"Hello {name}!")
greet_person("Sarah")
greet_person("David")
greet_person("John")

# More than one parameter
def introduce(name, age):
    print(f"My name is {name},")
    print(f"I am {age} old.")
introduce("David", 24)

# Returning Values
def add(a, b):
    return a + b
answer = add(5, 5)
print(answer)

def welcome():
    print("======================")
    print("       WELCOME        ")
    print("======================")
welcome()
welcome()

# Excercise 1 - First Function
def say_hello():
    print("Hello Python")
say_hello()

# Excercise 2 - Welcome Function
def welcome():
    print("===============================")
    print("      Welcome To BaseAPI      ")
    print("===============================")
welcome()

# Excercise 3 - Function With Parameter
def greet(name):
    print(f"Hello {name}!")
greet("Mary")
greet("John")

# Excercise 4 - Two Parameters
def student(name, course):
    print(f"Student: {name}")
    print(f"Course: {course}")
student("David", "Python")

# Challange 1 - Calculator Function
def add(a, b):
    return a + b
output = add(8, 6)
print(output)

# Challange 2 - Rectangle Area
def area(length, breadth):
    return length * breadth
result= area(5, 6)
print(result)

# Challange 3 - Login Function
def login(username, password):
    if username == "David" and password == "python123":
        return("Access Granted!")
    else:
        return("Access Denied!")
print(login("David", "python123"))
print(login("Tom", "1234"))

'''
Think like a programmer
1. Hello
2. David
3. 5
4. Python Python
5. No arguement
'''

# MINI CHALLANGE