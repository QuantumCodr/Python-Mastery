# Program: Elif Statement
# Author: David
# Lesson: 9

# Example 1
score = 85
if score >= 90:
    print("Grade A")
elif score >= 80:
    print("Grade B")
else:
    print("Below B")

# Example 2
age = 15
if age >= 18:
    print("Addult")
elif age >= 13:
    print("Teenager")
else:
    print("Child")

# Example 3
temperature = 35
if temperature >= 40:
    print("Very Hot")
elif temperature >= 30:
    print("Hot")
elif temperature >= 20:
    print("Ward")
elif temperature >= 10:
    print("Cool")
else:
    print("Cold")

# Excercise 1 - Grade Checker
score = int(input("Enter score: "))
if score >= 90:
    print("Grade A")
elif score >= 80:
    print("Grade B")
elif score >= 70:
    print("Grade C")
elif score >= 60:
    print("Grade D")
else:
    print("Grade F")

# Excercise 2 - Age Categories
age = int(input("Enter age: "))
if age >= 18:
    print("Adult")
elif age >= 13:
    print("Teenager")
else:
    print("Child")

# Excercise 3 - Temperature
temperature = float(input("Enter temperature: "))
if temperature >= 40:
    print("Very Hot")
elif temperature >= 30:
    print("Hot")
elif temperature >= 20:
    print("Warm")
elif temperature >= 10:
    print("Cool")
else:
    print("Cold")

# Excercise 4 - ATM
balance = 1000
withdrawal_amount = float(input("Enter withdrawal amount: "))
if withdrawal_amount <= 0:
    print("Invalid Amount")
elif withdrawal_amount <= balance:
    print("Withdrawal Approved")
else:
    print("Insufficient Funds")

# Challange 1
number = float(input("Enter a number: "))
if number < 0:
    print("Negative")
elif number == 0:
    print("Zero")
else:
    print("Positive")

# Challange 2
username = input("Enter username: ")
if username == "Admin":
    print(f"Welcome {username}!")
elif username == "David":
    print(f"Welcome {username}!")
elif username == "Guest":
    print("Welcome Guest!")
else:
    print("Unknown User")

# Challange 3
age = int(input("Enter age: "))
if age <= 12:
    print("$5")
elif age <= 17:
    print("$8")
elif age <= 59:
    print("$12")
else:
    print("$7")

'''
Think like a programmer:
1. A
2. C
3. Child
4. Zero
5. logical error
'''