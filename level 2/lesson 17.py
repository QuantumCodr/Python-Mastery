'''
Program: Advanced Lists
Author: David
Lesson: 17
'''

# 1. Append - Adds to the end.
modules = [
    "auth",
    "users",
    "products"
]
modules.append("payments")
print(modules) # ['users', 'auth', 'payments']

# 2. Insert - Adds at a specific position.
modules.insert(2,"orders")
print(modules) # ['users', 'auth', 'orders', 'products', 'payments']

# 3. Pop - Removes by index.
modules = ["auth", "users", "products"]
modules.pop(1) # ["auth", "products"]
modules.pop() # pops last item
print(modules) # ["auth"]

# 4. Remove - Removes by value.
modules.remove("auth")
print(modules) # []

# 5. Index - Find where something is.
modules = ["auth", "users", "products"]
print(modules.index("products"))

# 6. Count - Count occurrences.
numbers = [1, 2 , 2, 3, 2]
print(numbers.count(2)) # 3

# 7. Sort - Sort alphabetically.
names = [
    "David",
    "Mary",
    "Alice"
]
names.sort()
print(names) # ["Alice", "David", "Mary"]

numbers = [3, 5, 4, 1, 2]
numbers.sort()
print(numbers) # [1, 2, 3, 4, 5]

# Reverse Sort
numbers.sort(reverse=True)
print(numbers) # [5, 4, 3, 2, 1]

# 8. Reverse - Simply flips the current order.
numbers = [1, 3, 8, 5]
numbers.reverse()
print(numbers) # [5, 8, 3, 1]

# 9. Clear - Deletes everything.
cart = [
    "Rice",
    "Milk"
]
cart.clear()
print(cart) # []

# 10. Copying Lists
a = [1, 2, 3]
b = a
b.append(4)
print(a) # [1, 2, 3, 4]

b = a.copy()
b.append(5)
print(a) # [1, 2, 3, 4]
print(b) # []?

# 11. List Slicing
numbers = [10, 20, 30, 40, 50]
print(numbers[:3]) # first three - [10, 20, 30]
print(numbers[1:4]) # middle - [20, 30, 40]
print(numbers[-2:]) # last two - [40, 50]

# Excercise 1 
frameworks = [
    "Flask",
    "Django"
]
frameworks.append("FastAPI")
print(frameworks)

# Excercise 2
cities = ["Bo", "kenema"]
cities.insert(0, "Freetown")
print(cities)

# Excercise 3
numbers = [10, 20, 30, 40]
numbers.pop() 
print(numbers)

# Excercise 4
fruits = [
    "Apple",
    "Banana",
    "Orange"
]
print(fruits.index("Banana"))
print(len(fruits))
print(fruits[-2:])

# Challange 1 - Shopping Cart
cart = []
def shopping_cart():
    print("\nProgram: Enter Name of 5 Products")
    print("__________________________________")
    for i in range(6):
        product = input(f"Enter product {i+1}: ")
        cart.append(product)
    product = input("\nEnter product to delete: ")
    cart.remove(product)
    print(f"{product.title()} deleted successfully!")
    print(f"Cart: {cart}")
shopping_cart()

# Challange 2 - BaseAPI Modules
modules = []
def ask_for_five_modules():
    print("\nProgram: Enter Name of 5 Modules")
    print("__________________________________")
    for i in range(6):
        module = input(f"Enter module {i+1}: ")
        modules.append(module)
    modules.sort()
    print(modules)
ask_for_five_modules()

# Challange 3 - Student Database
students = []
def ask_for_five_students():
    print("\nProgram: Enter Name of 5 Students")
    print("_____________________________________")
    for i in range(5):
        student = input(f"Enter name of student {i+1}: ")
        students.append(student)
    return students
list1 = ask_for_five_students()
list2 = list1.copy()
list2.append("Teacher")
print(f"Originl List: {list1}")
print(f"Copied List: {list2}")

'''
Think like a programmer
1. [2, 5, 9]
2. ["A", "B"]
3. [1, 2, 3]
4. [20, 30]
5. Name not found "John"
'''

'''
Engineering Challange
1. remove()
2. append()
3. sort()
4. copy()
'''

'''
Engineering Principle of the Day
Good programmers don't just store data—they choose the right operation for the job.
'''