# Program: Dictionary
# Author: David
# Lesson: 20

# 1. Creating a Dictionary
student = {
    "name": "David",
    "age": 24,
    "country": "Sierra Leone"
}
print(student) # {'name': 'David', 'age': 24, 'country': 'Sierra Leone'}

# 2. Assessing Values
print(student["name"]) # David
print(student["age"]) # 24
print(student["country"]) # Sierra Leone 
try:
    print(student[0]) # Key Error
except:
    print("Key Error")

# 3. Changing Values
student["age"] = 23
print(student)

# 4. Adding New Items
student["course"] = "Software Engineering"
print(student) # {'name': 'David', 'age': 23, 'country': 'Sierra Leone', 'course': 'Software Engineering'}

# 5. Removing Items
student.pop("country") 
print(f"Pop: {student}")
student.popitem()
student.popitem()
print(f"Pop Item: {student}")

# 6. Using get()
print(student.get("namee"))
try:
    print(student["namee"]) # Error
except:
    print("Key Error!")

# 7. Membership 
print("David" in student) # False
print("name" in student) # True

# 8. Length
print(len(student))

# 9. Keys, Values and Pairs
print(student.keys())
print(student.values())
print(student.items())

# 10. Iteration
for key in student:
    print(key)

for key, value in student.items():
    print(f"{key}: {value}")

# Excercise 1
book = {
    "title": "Python Basics",
    "auhor": "David",
    "pages": 250
}
print(f"Title: {book["title"]}")
print(f"Author: {book['auhor']}")

# Excercise 2 
car = {
    "brand": "Toyota",
    "year": 2020
}
car["color"] = "Deep Blue"
print(f"\nCar: {car}")

# Excercise 3
employee = {
    "name": "Sarah",
    "salary": 25000
}
employee["salary"] = 15000
print(f"Employee: {employee}")

# Excercise 4 
country = {
    "name": "Sierra Leone",
    "capital": "Freetown",
    "currency": "Leones"
}
for key, value in country.items():
    print(f"{key}: {value}")
for key in country.keys():
    print(key)
for key in country.values():
    print(key)

# Challange 1 - Student Profile
student = dict()
def student_profile():
    name = input("Enter name: ").strip()
    age = int(input("Enter age: "))
    course = input("Enter course: ").strip()
    student["name"] = name
    student["age"] = age
    student["course"] = course
    print("_________STUDENT_________")
    print(student)
student_profile()

# Challange 2 - BaseAPI Generator
manifest = {
    "project_name": "",
    "auhtor": "",
    "version": "",
    "database": ""
}

def build():
    name = input("Enter project name: ").strip()
    author = input("Enter author: ").strip()
    version = input("Enter version: ").strip()
    database = input("Enter database connection: ")
    manifest["project_name"] = name
    manifest["auhtor"] = author
    manifest["version"] = version
    manifest["database"] = database
    print(f"Manifest: {manifest}")
build()
for key, value in manifest.items():
    print(f"{key}: {value}")

# Challange 3 - Product Database
product = dict()

def enter_product():
    name = input("Enter product name: ").strip()
    price = float(input("Enter price: "))
    quantity = int(input("Enter qusntity: "))
    product['name'] = name
    product['price'] = price
    product['quantity'] = quantity
    total_value = price * quantity
    print(f"Product: {product}")
    print(f"Total value: {total_value}")
enter_product()
    
'''
Think like a programmer
1. David
2. 2
3. None
4. True
5. Key error
'''
'''
Engineering challange
1. Because you can use readable keys to get values that makes extraction easier
2. print("key" in dict)
3. One raise an error the other doesn't it gives None
4. Readable and extractable
'''
'''
💡 Engineering Principle of the Day
Use dictionaries when your data has names, not positions.
'''