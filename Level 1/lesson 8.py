# Program: Else Statement
# Author: David
# Lesson: 8

age = 20
if age >= 18:
    print("Adult")
else:
    print("Minor")

age = 20
if age >= 18:
    print("Adult")
else:
    print("Minor")

password = input("password: ")
if password == "python123":
    print("Access Granted")
else:
    print("Access Denied")

number = int(input("Enter a number: "))
if number > 0:
    print(f"Postive number, {number}.")
else:
    print(f"Zero or Negative number, {number}.")

# Excercise 1
age = int(input("Enter your age: "))
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# Excercise 2
password = input("Enter password: ")
if password == "python123":
    print("Login Successful")
else:
    print("Incorrect Password")

# Excercise 3
score = float(input("Enter score: "))
if score == 100:
    print("Perfect Score!")
else:
    print("Keep Practicing!")

# Excercise 4
number = int(input("Enter a number: "))
if number > 0:
    print("Positive Number")    
else:
    print("Zero or Negative Number")

# Challange 1
username = input("Enter username: ")
if username == "David":
    print(f"Welcome {username}!")
else:
    print("Unknown User!")

# Challange 2
first_number = float(input("Enter first  number: "))
second_number = float(input("Enter second number: "))
if first_number > second_number:    
    print("First number is larger.")
else:
    print("Second number is larger or equal.")

# Challange 3 (ATM)
balance = 500
withdrawal_amount = float(input("Enter withdrawal amount: "))
if withdrawal_amount < balance:
    balance = balance - withdrawal_amount
    print("Withdrawal successful!")
    print(f"Remaining balance: {balance}")
else:
    print("Insufficient funds!")