# Program: Comparison Operator
# Author: David
# Lesson: 6

print(10 > 5)

# 1. Equal To (==)
print(5 == 5) # True
print(5 == 8) # False

# 2. Not Equal To (!=)
print(10 != 2) # True
print(100 != 10) # False

# 3. Greater Than (>)
print(20 > 10) # True
print(5 > 8) # False

# 4. Less Than (<) 
print(2 < 8) # True
print(6 < 5) # False

# 5. Greater Than or Equal To (>=)
print(18 >= 18) # True
print(20 >= 18) # True
print(15 >- 18) # False

# 6. Less Than or Equal To (<=)
print(5 <= 5) # True
print(3 <= 5) # True
print(8 <= 5) # False

# Comparing Strings
print("David" == "David") # True
print("David" == "John") # False
print("Python" == "python")

# Comparing Variables
age = 20
print(age >= 28) # True

# Storing Comparison Result
is_adult = age >= 28
print(f"Is adult: {is_adult}")

# Excercise 1
print(10 == 10) # True
print(5 != 8) # True
print(20 < 15) # False
print(50 >= 50) # True
print(100 <= 80) # False

# Excercise 2
age = 22
score = 75
print(age >= 18) # True
print(score == 100) # False
print(score != 0) # True

# Excercise 3
username = "David"
password = "password123"
print(username == "David") # True
print(password == "admin") # False

# Challange 1
first_number = float(input("Enter first number: "))
second_number = float(input("Enter second number: "))
print(first_number == second_number)
print(first_number > second_number)
print(first_number < second_number)

# Challange 2
age = int(input("Enter age: "))
print(age >= 18)

# Bonus Challange
math = 85
english = 70
science = 90
print(math >= 75) # True
print(english >= 75) # False
print(science >= 75) # True