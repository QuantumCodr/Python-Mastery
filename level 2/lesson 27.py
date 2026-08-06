# Lesson 27: Constructors (__init__) and self
# Author: David
# Lesson: 27
'''
What is a Constructor?
A constructor is a special method that Python automatically calls whenever you create an object.
Its job is to initialize (prepare) the object.
'''

class Student:
    def __init__(self):
        print("Student created.")
student = Student() # Student created.

# Creating attributes
class Student:
    def __init__(self):
        self.id = 1
        self.name = "David"
        self.age = 24
        self.course = "Software Engineering"
student = Student()
print(student.id)
print(student.name)
print(student.age)
print(student.course)

'''
What is self?
self simply means this object
'''
# 5. Every object has different data
'''
Instead of hardcoding values.
we can receive values.
'''
class Student:

    def __init__(self, name):
        self.name = name

student1 = Student("David")
student2 = Student("Sarah")
student3 = Student("John")
print(student1.name)
print(student2.name)
print(student3.name)

# 6. Multiple parameters
class Student:

    def __init__(self, id, name, age, course):
        self.id = id
        self.name = name
        self.age = age 
        self.course = course

student = Student(
    1,
    "David",
    24,
    "Software Engineering"
)
print(student.id)
print(student.name)
print(student.age)
print(student.course)

# 7. Creating many objects

class Student:
    def __init__(self, id, name):
        self.id = id
        self.name = name
students = [
    Student(1, "David"),
    Student(2, "Sarah"),
    Student(3, "John")
]

for student in students:
    print(student.id, student.name)

# 8. Accessing attributes
student = Student(1, "David")
print(student.id)
print(student.name)

# 9. Changing attributes
student.name = "Williams"
print(student.name)

# 10. Another example

class Computer:
    def __init__(self, brand, ram, storage):
        self.brand = brand
        self.ram = ram
        self.storage = storage
computer = Computer(
    "Dell",
    "16GB",
    "1TB SSD"
)     
print(computer.brand, computer.ram, computer.storage)

# 11. Bank Account Example
class BankAccount:
    def __init__(self, number, owner, balance):
        self.number = number
        self.owner = owner
        self.balance = balance
account = BankAccount(
    1001,
    "Gleekan David Williams",
    5000
)
print(account.owner, account.balance)

# 12. Pharmacy Example
class Medicine:
    def __init__(self, id, name, price, stock):
        self.id = id
        self.name = name
        self.price = price
        self.stock = stock
medicine = Medicine(
    1,
    "Paracetamol",
    10,
    100
)
print(medicine.name)
print(medicine.stock)

# Exercise 1
class Car:
    def __init__ (self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
car1 = Car("BMW","", 2025)
car2 = Car("Benz", "", "2022")
car3 = Car("Toyota", "Corolla", "2018")

# Exercise 2 
class Phone:
    def __init__(self, brand, storage, color):
        self.brand = brand
        self.storage = storage
        self.color = color
phone1 = Phone("Samsung", 128, "blue")
phone2 = Phone("Iphone", 128, "mauve")
phone3 = Phone("Tekno", 128, "black")
phone4 = Phone("Oppo", 64, "white")

# Exercise 3
class Employee:
    def __init__(self, id, name, salary, department):
        self.id = id
        self.name = name
        self.salary = salary
        self.department = department
employee1 = Employee(1, "David", 5000, "IT")
employee2 = Employee(2, "Sarah", 3000, "Finance")
employee3 = Employee(3, "Mary", 2500, "Marketing")

# Exercise 4
class Product:
    def __init__(self, id, name, price, quantity):
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity

products = [
    Product(1, "Soap", 30, 150),
    Product(2, "Biscuit", 10, 100),
    Product(3, "Milk", 40, 20),
    Product(4, "Pampers", 600, 20)
]
for index, product in enumerate(products):
    print("--------------")
    print(f"   PRODUCT {index}")
    print("--------------")
    print(product.id)
    print(product.name)
    print(product.price)
    print(product.quantity)
    print()
    

# Exercise 5
class BankAccount:
    def __init__(self, account_number, owner, balance):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance

bank_accounts = [
    BankAccount("B001", "David", 250000),
    BankAccount("B002", "Wilfres", 100000),
    BankAccount("B002", "Samuel", 80000)
]

for account in bank_accounts:
    print()
    print("---- Bank Account ----")
    print(f"Account_number: ${account.account_number}")
    print(f"Name: ${account.owner}")
    print(f"Balance: ${account.balance}")

# Mini Project
class Student:
    def __init__(self, id, name, age, course):
        self.id = id 
        self.name= name 
        self.age = age
        self.course = course
student1 = Student(1, "David", 24, "Software Engineering")
student2 = Student(2, "Sarah", 21, "Nursing")
student3 = Student(3, "Tom", 23, "Networking")

class Teacher:
    def __init__(self, id, name, salary, department):
        self.id = id
        self.name = name
        self.salary = salary 
        self.department = department
teachers = [
    Teacher(1, "Musa", 1500, "FICT"),
    Teacher(2, "Sia", 2000, "FBIB"),
    Teacher(3, "John", 2500, "FDI")
]

class Course:
    def __init__(self, id, name, course_hour, department):
        self.id = id 
        self.name = name 
        self.course_hour = course_hour
        self.department = department
courses = [
    Course(1, "Structured Prodramming", 50, "FICT"),
    Course(2, "Software Engineering", 50, "FICT"),
    Course(3, "Database", 50, "FICT")
]

class Department:
    def __init__(self, id, name):
        self.id = id 
        self.name = name
departments = [
    Department(1, "FICT"),
    Department(2, "FDI"),
    Department(3, "FAAB")
]

class Classroom:
    def __init__(self, id, label, status):
        self.id = id 
        self.label = label 
        self.status = status
classrooms = [
    Classroom(1, "Clr 1", "open"),
    Classroom(2, "Clr 2", "closed")
]