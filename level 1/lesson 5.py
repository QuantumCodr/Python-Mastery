# Program: Type Casting and Arithmic Operation
# Author: David
# Lesson: 5

age = int(input("Enter age: "))
print(type(age))

price = float(input("Enter price: "))
print(type(price))

print(5 + 3) # 8
print(10 - 4) # 6
print(6 * 7) # 42
print(10 / 2) # 5.0 float
print(10 // 3) # 3 int
print( 10 % 3) # 1
print(2 ** 3) # 2*2*2 = 8


# Operator Precedence
print(2 + 3 * 4) # 14
print((2 + 3) * 4) # 20
print("5" + "3") # 53
print(5 + 3) # 8

# Excercise 1
first_number = float(input("Enter first number: "))
second_number = float(input("Enter second number: "))
print(f"Sum: {first_number + second_number}")
print(f"Difference: {first_number - second_number}")
print(f"Product: {first_number * second_number}")
print(f"Quotient: {first_number / second_number}")

# Excercise 2
length = float(input("Enter length: "))
breadth = float(input("Enter breadth: "))
area = length * breadth
print(f"Area: {area}")

# Excercise 3
birth_year = int(input("Enter birth year: "))
age = 2026 - birth_year
print(f"Age: {age}")

# Excercise 4
number = float(input("Enter any number: "))
print(f"Square: {number ** 2}")
print(f"Cube: {number ** 3}")

# Challange 1 - BMI Calculator
weight = float(input("Enter weight(kg): "))
height = float(input("Enter height(m): "))
bmi = weight / (height ** 2)
print(f"BMI: {bmi}")

# Challange 2 - Mini Calculator
first_number = float(input("Enter first number: "))
second_number = float(input("Enter second number: "))
print(f"Addition: {first_number + second_number}")
print(f"Ssubtraction: {first_number - second_number}")
print(f"Multiplication: {first_number * second_number}")
print(f"Division: {first_number / second_number}")
print(f"Integer Division: {first_number // second_number}")
print(f"Remainder: {first_number % second_number}")
print(f"Power: {first_number ** second_number}")    

