# Program: Logical Operators
# Author: David
# Lesson: 10

# AND Operator
age = 22
has_id = True
if age >= 18 and has_id:
    print("You may enter.")


# OR Operator
day = "Saturday"
if day == "Saturday" or day == "Sunday":
    print("It's the weekend!")

score = 95
if score == 100 or score >= 90:
    print("Excellent!")

# NOT Operator
is_logged_in = False
print(not is_logged_in)  # True

password_correct = True
print(not password_correct)  # False

# Student Pass
score = 75
attendance = 90
if score >= 50 and attendance >= 75:
    print("Pass")

# Weekend Checker
day = input("Enter day: ")
if day == "Saturday" or day == "Sunday":
    print("No school today!")

# Website Access
logged_in = False
if not logged_in:
    print("Please log in first")

# Excercise 1 - Login System
username = input("Enter username: ")
password = input("Enter password: ")
if (username == "David" or username == "Admin") and password == "python123":
    print("Login Successful")
else:
    print("Login Failed")

# Excercise 2 - Voting Eligibility
age = int(input("Enter age: "))
is_citizen = input("Are you a citizen yes/no: ")
if age >= 18 and is_citizen == "yes":
    print("Eligible to vote")
else:
    print("Not eligible")

# Excercise 3 - Weekend Checker
day = input("Enter day: ")
if day == "Saturday" or day == "Sunday":
    print("weekend")
else:
    print("Weekday")

# Excercise 4 - Admin Access
username = input("Enter username: ")
if username == "Admin" or username == "David":
    print("Access Granted")
else:
    print("Access Denied")

# Challange 1 - Scholarship
score = int(input("Enter score: "))
attendance = int(input("Enter attendance: "))
if score >= 85 and attendance >= 90:
    print("Scholarship Awarded")
else:
    print("Scholarship Not Awarded")

# Challange 2 - Movie Entry
age = int(input("Enter age: "))
has_parent = input("Have you a parent yes/no: ")
if age >= 18:
    print("Allowed")
elif age < 18 and has_parent == "yes":
    print("Allowed")
else:
    print("Not Allowed")

# Challange 3 - Account Lock
locked = False
if not locked:
    print("Access Granted")
else:
    print("Access Denied")

'''
Think like a programmer
1. True
2. True
3. True
4. Fail
5. Incomplete condition
'''