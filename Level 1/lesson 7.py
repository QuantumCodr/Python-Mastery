# Program: If statement
# Author: David
# Lesson: 7

age = 20
if age >=18:
    print("You are an adult.")

age = 16
if age >= 18:
    print("You are an adult.")


age = int(input("Enter you age: "))
if age >= 18:
    print(f"You are an adult, {age} years old.")

password = input("Enter password: ")
if password == "python123":
    print("Access Granted")

name = input("Enter your name: ")
if name == "David":
    print("Welcome {name}!")

age = 18
if age >= 18:
    print("Adult")
    print("Can vote.")
    print("Can drive.")

# Excercise 1
age = int(input("Enter yout age: "))
if age >= 18:
    print(f"You are an adult, {age} years old.")

# Excercise 2
password = input("Enter password: ")
if password == "python123":
    print("Login Successful")   

# Excercise 3
score = float(input("Enter score: "))
if score == 100:
    print("Perfect score!")

# Excecise 4
language = input("Enter favorite language: ")
if language == "Python":
    print("Excellent choice!")

# Challange 1
number = int(input("Enter a number: "))
if number > 0:
    print("Positive number.")

# Challange 2
first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))
if first_number > second_number:
    print("The first number is larger.")

# Challange 3

username = input("Enter username: ")
password = input("Enter password: ")
if username == "David":
    if password == "python123":
        print(f"Welcome {username}!")
