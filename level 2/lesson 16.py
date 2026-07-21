# Program: Nested Loops
# Author: David
# Lesson: 16

# Example 1
for row in range(3):
    for column in range(4):
        print("*", end="")
    print()

# Example 2 - Multiplication Table
for row in range(1, 4):
    for column in range(1, 4):
        print(f"{row * column}", end=" ")
    print()

# Example 3 - Cordinates
for row in range(3):
    for column in range(2):
        print(f"({row}, {column})")

# Excercise 1 - Rectangle of Stars
for row in range(3):
    for column in range(3):
        print("*", end="")
    print()

# Excercise 2 - Number Grid
print("\nNumber Grid")
for row in range(3):
    for column in range(1, 4):
        print(column, end=" ")
    print()

# Excercise 3 - Coordinates
for row in range(3):
    for column in range(3):
        print(f"({row}, {column})")
    print()

# Excercise 4 - Student Attendance
students = ["David", "Mary", "John"]
days = ["Monday", "Tuesday"]
for student in students:
    for day in days:
        print(f"{student} - {day}")

# Challange 1 - Mini Multiplication Table
for number in range(3):
    value = int(input("Enter number: "))
    for table in range(1, 11):
        print(f"{value} * {table} = {value * table}")
    print()

# Challange 2 - Classroom Seating
rows = ["A", "B", "C"]
for row in rows:
    for column in range(1, 5):
        print(f"{row}{column}")

# Challange 3 - BaseAPI Generator
folders = [
    "app",
    "test",
    "docs"
]
modules = [
    "users",
    "auth",
    "products"
]
for folder in folders:
    for module in modules:
        print(f"Creating {folder}/{module}")
    print()

'''
Think like a programmer:
1. ****
   ****
2. 0 1
3. 0 0
   0 1
   1 0
   1 1
4. A 1
   A 2
   B 1
   B 2
5. No statement or block for second loop
'''

# Engineering Challange
numbers = [2, 5, 8, 11, 2]
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        print(numbers[i], numbers[j])

'''
How many pairs are generated?
Why does j start at i + 1?
Which pairs are skipped?
What's the algorithm trying to accomplish?
'''
'''
It's generating all unique pairs.

This is an incredibly common algorithm.

For example:

Compare every student with every other student.
Compare every city with every other city.
Calculate distances between every pair of locations.
Check every pair of products for similarity.
Find duplicates by comparing each item with every other item.

You'll see this pattern again in sorting algorithms, 
graph algorithms, collision detection in games, 
duplicate detection, recommendation systems, 
and many interview questions.
'''

'''
Engineering Principle of the Day
----------------------------------
Whenever you have "for every X, do something with every Y", 
think about nested loops.
'''