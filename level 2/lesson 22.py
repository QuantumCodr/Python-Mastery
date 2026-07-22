# Program: Modules and Imports - A module is simply a Python file.
# Author: David
# Lesson: 22

# 1. Example - math_tools.py
import math_tools 
print(math_tools.add(5, 6))
print(math_tools.subtract(5, 6))

# 2. Importing Individual Functions
from math_tools import add
print(f"Add: {add(19, 37)}")

# 3. Importing Multiple Functions
from math_tools import add, subtract
print(f"Add: {add(1,2)}")
print(f"Subtract: {subtract(2, 1)}")

# 4. Import Everything (Generally Avoid)
from math_tools import *
print(add(3, 2))
print(subtract(7, 2))

# 5. Aliases
import math_tools as mt
print(mt.add(5, 10))

# Or
from math_tools import add as plus
print(plus(5, 20))

# 6. Importing Built-In Modules
import math
print(math.sqrt(64)) # 8

import random
print(random.randint(1, 100)) # 

import datetime
print(datetime.datetime.now())

# 7. Importing your own Module
# Example greetings.py
import greetings
greetings.welcome("Julian")

# Excercise 1 - Calculator Module
from calculator import add, subtract, multiply
print(add(5, 10))
print(subtract(10, 5))
print(multiply(10, 5))

# Excercise 2 - Greeting module
from greetings import hello, goodbye
hello("David")
goodbye("David")

# Challange 3 - BaseAPI Utility Module
import utils
utils.create_project("BaseAPI")
utils.create_folder("App")
utils.show_success()

# 4. Built-In Modules
import math
print(math.sqrt(144))
print(math.pow(2,8))

import random
print(random.randint(1, 100))

# Challenge 1 - Student System
import students
students.add_student("Lamine Yamal")
students.add_student("Marcus Rashford")
students.remove_student("Marcus Rashford")

# Challenge 2 - BaseAPI Generator
from generator import create_project
create_project()

# Challenge 3 - Mini Banking System
import bank
balance = 500
balance = bank.deposit(balance)
balance = bank.withdraw(balance)
print(bank.show_balance(balance))

'''
Think like a programmer
1. Hello
2. 7
3. 8
4. 10
5. 5
'''

'''
Engineerinf challenge
1. avoid naming conflict
2. import module file, import specific module function
3. Better management and seperation of concerns
4. I can easily find and update anything
'''

'''
Engineering Principle of Lesson 22 💡
High cohesion, low coupling.
A module should have one clear responsibility (high cohesion) 
and depend as little as possible on other modules (low coupling).

Engineering Principle of the Day 💡
Separate business logic from input/output (I/O).
'''