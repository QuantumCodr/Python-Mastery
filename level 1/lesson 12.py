# Program: For Loops - Repeat this code a certain number of times.
# Author: David
# Lesson: 12


for number in range(5):
    print(number) # 0 1 2 3 4

# range(start, stop)
for number in range(1, 6):
    print(number) # 1 2 3 4 5

# range(start, stop, step)
for number in range(2, 11, 2):
    print(number)

# Counting Backwards
for number in range(10, 0, -1):
    print(number)

# Example 1 - Print name five times.
name = "David"
for i in range(5):
    print(name)

# Example 2 - Multiplication Table
number = 7
for i in range(1, 11):
    print(f"{number} * {i} = {number * i}")

# Example 3 - Add Numbers
total = 0
for number in range(1, 6):
    total += number
print(total)

# Excercise 1 - Count to 20
for number in range(1, 21):
    print(number)

# Excercise 2 - Even Numbers
for number in range(2, 21, 2):
    print(number)

# Excercise 3 - Countdown
for number in range(10, 0, -1):
    print(number)
print("Lift Off!")

# Excercise 4 - Squares
for number in range(1, 11):
    print(f"{number}^2 = {number ** 2}")

# Challange 1 - Multiplication Table
number = int(input("Enter a number: "))
for i in range(1, 13):
    print(f"{number} * {i} = {number * i}")

# Challange 2 - Sun of Numbers
total = 0
number = int(input("Enter a number: "))
for i in range(1, number + 1):
    total += i
print(total)

# Challange 3 - Mini Login Attempts
for attempt in range(3):
    password = input("Enter password: ")
    if password == "python123":
        print("Access Granted")
    else:
        print("Access Denied")

'''
Think like a programmer:
1. 0 1 2 3 4
2. 2 3 4 5 6 7
3. 8 6
4. 6
5. Improper range values
'''

# Mini Challange
for create in range(5):
    if create == 0:
        print("Creating Project...")
    elif create == 1:
        print("Creating app/")
    elif create == 2:
        print("Creating test/")
    elif create == 3:
        print("Creating alembic/")
    else:
        print("Creating docs/")
print("Project created successfully!")