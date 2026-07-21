# Program: Error Handling
# Author: David
# Lesson: 21

age = int(input("Enter age: ")) # twenty
print(age) # ValueError: invalid literal for int()

# 1. Basic try and except
try:
    age = int(input("Enter age: "))
    print(age)
except:
    print("Invalid Input")

# 2. Catching Specific Error
try:
    number = int(input("Enter number: "))
except ValueError:
    print("Please enter numbers only.")

# 3. Dividing by Zero
try:
    a = int(input("First number: "))
    b = int(input("Second number: "))
    print(a / b)
except ZeroDivisionError:
    print("You cannot divide by zero.")

# 4. Multiple Exception
try:
    a = int(input("First number: "))
    b = int(input("Second number: "))
    print(a / b)
except ValueError:
    print("Numbers only.")
except ZeroDivisionError:
    print("You cannot divide be zero.")

# 5. else - Runs only if no exception occurred.
try:
    age = int(input("Enter age: "))
except ValueError:
    print("Numbers only.")
else:
    print(f"You are {age} years old.")

# 6. Finally - Runs no matter what happens.
try:
    print("Opening database...")
except:
    print("Something went wrong.")
finally:
    print("Closing database...")

# Excercise 1 - Integer Input
try:
    num = int(input("Enter number: "))
except ValueError:
    print("Numbers only.")
else:
    print(num)
# Excercise 2 - Safe Division
try:
    a = int(input("Number 1: "))
    b = int(input("Number 2: "))
    print(a / b)
except ZeroDivisionError:
    print("Cannot divide by zero.") 

# Excercise 3 - Age checker
try:
    age = int(input("Enter age: "))
except ValueError:
    print("Invalid Input")
else:
    print(f"you are {age} years old.")

# Ecercise 4 - Login Registry
try:
    pin = int(input("Enter your PIN: "))
except ValueError:
    print("PIN must contain numbers only.")
else:
    print("PIN accepted")

# Challenge 1 - Mini Calculator
try:
    first_number = int(input("First number: "))
    operator = input("Enter operator (+, -, *, /): ")
    second_number = int(input("Second number: "))
    result = ""
    if operator == "+":
        result = first_number + second_number
    elif operator == "-":
        result = first_number - second_number
    elif operator == "*":
        result = first_number * second_number
    elif operator == "/":
        result = first_number / second_number
    else:
        raise ValueError
except ValueError:
    print("Invalid input")
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print(f"{first_number} {operator} {second_number} = {result}")

# Challenge 2 - ATM
try:
    balance = 500
    withdrawal_amount = int(input("Enter withdrawal amount: "))
except ValueError:
    print("Numbers only")
else:
    if withdrawal_amount <= 0:
        print("Withdrawal amount cannot be negative")
    elif withdrawal_amount == 0:
        print("Withdrawal amount cannot be zero")
    elif withdrawal_amount > balance:
        print("Insufficient funds")
    else:
        balance -= withdrawal_amount
        print(f"Withdrawal successful")
        print(f"Balance: {balance}")

# Challenge 3 - BaseAPI Configuration
try:
    project = input("Enter project: ")
    port = int(input("Enter port: "))
except ValueError:
    print("Invalid port")
else:
    print("Generating project...")
    print(f"Project: {project}")
    print(f"Port: {port}")

'''
Think like a programmer
1. 5
2. Cannot divide 
3. wrong input
4. python, success
5. start, end
'''
'''
Engineering challenge
1. Prepares you for expeced errors
2. except handles the error, finally block runs either wise
3. Database connections to always close after use
'''
'''
Problem-solving challenge
write a function that call for the input
apply value and error checks
if errors or wrong input keep calling the same function except else 
'''