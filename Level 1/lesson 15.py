'''
Program: Lists - An ordered collection of items.
Author: David
Lesson: 15
'''
# Creating List
projects = ["School Api", "Shop Api", "Blog Api"]
fruits = ["apple", "mango", "banana"]
numbers = [0, 1, 2, 3, 4]
data = ["David", 95, True, 5.8]

# Accessing Items
fruits = ["apple", "banana", "orange"]
print(fruits[0]) # apple
print(fruits[1]) # banana
print(fruits[2]) # orange
print(fruits[-1]) # orange

# Finding Length
print(len(fruits))

# Changing An Item
fruits[1] = "grapes"
print(fruits)

# Adding Items
fruits = ["Apple", "Banana"]
fruits.append("Orange")
print(fruits)

# Removing Items
fruits.remove("Banana")
print(fruits)

# Looping Through a List
fruits = ["Apple", "Banana", "Orange"]
for fruit in fruits:
    print(fruit) # fruits[0], fruits[1], fruits[2]

# Checking Membership
print("Apple" in fruits) # True

# Real-World Example
modules = [
    "auth",
    "users",
    "products",
    "orders"
]
modules.append("payments")
for module in modules:
    print(module)

# Excercise 1 - First List
languages = ["Python", "Java", "Go"]
print(languages[0])
print(languages[-1])

# Excersise 2 - Favorite Food
foods = ["Rice", "Beans", "Nut", "Cerelac", "Egg"]
for food in foods:
    print(food)

# Excercise 3 - Update List
cities = ["Freetown", "Bo", "Kenema"]
cities[1] = "Makeni"
print(cities)

# Excercse 4 - Add and Remove
frameworks = ["Flask", "Django"]
frameworks.append("FastAPI")
frameworks.remove("Flask")
print(frameworks)

# Challange 1 - Student Register
students = []
for i in range(3):
    name = input("Enter student name: ")
    students.append(name)
for student in students:
    print(student)

# Challange 2 - Shopping Cart
cart = []
for i in range(5):
    product = input("Enter product name: ")
    cart.append(product)
print("Your Cart")
for product in cart:
    print(product)

# Challange 3 - BaseAPI modules
modules = []
for i in range(4):
    module = input("Enter module name: ")
    modules.append(module)
print("Generating...")
for module in modules:
    print(module) # auth, users, product, payment
print("Generation Complete!") 

'''
Think like a programmer
1. 10
2. ["A", "B". "C", "D"]
3. ["Freetown", "Kenema"]
4. 2
5. List out of range
'''

