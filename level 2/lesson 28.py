# Program: Instance Methods
# Author: David
# Lesson: 28

# 1. What is an Instance Method?
'''
An instance method is simply a function that belongs to a class.
'''
# account.deposit(500)

# 2. Your First Method
class Student:
    def __init__(self, name):
        self.name = name 

    def introduce(self):
        print(f"My name is {self.name}.")
student = Student("name")
student.introduce()

# 3. Understanding self
class Student:
    def __init__(self, name):
        self.name = name 
    def greet(self):
        print(self.name)
student = Student("Sarah")
student.greet()

# 4. Methods Can Change Attributes
class BankAccount:
    def __init__(self,
     account_number, owner, balance):
        self.account_number = account_number 
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
account = BankAccount("B001", "David", 1000000)
account.deposit(50000)
print(account.balance)

# 5. Multiple Methods
class BankAccount:
    def __init__(self, account_number, owner, balance):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

account = BankAccount("B001", "Naomi", 100000)
account.deposit(200000)
account.withdraw(80000)
print(account.balance)

# 6. Returning Values
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height

rectangle = Rectangle(500, 500)
print(f"Area: {rectangle.area()}")

# 7. Computer Example
class Computer:
    def __init__(self, brand, ram):
        self.brand = brand
        self.ram = ram
        self.power = False

    def turn_on(self):
        self.power = True
        print("Computer is ON")

    def turn_off(self):
        self.power = False
        print("Computer is OFF")   

computer = Computer("Dell", 16) 
computer.turn_on()
computer.turn_off()

# 8. Pharmacy Example
class Medicine:
    def __init__(self, name, stock):
        self.name = name
        self.stock = stock

    def sell(self, quantity):
        self.stock -= quantity

    def restock(self, quantity):
        self.stock += quantity
medicine = Medicine("Paracetamol", 15)
medicine.sell(5)
medicine.restock(100)
print(medicine.stock)

# 9. Shopping Cart
class ShoppingCart:
    def __init__(self):
        self.total = 0
    def add(self, amount):
        self.total += amount
    def checkout(self):
        print(f"Total; {self.total}")
cart = ShoppingCart()
print()
cart.add(50)
cart.add(120)
cart.checkout()

# 10. Student Example
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def pass_exam(self):
        self.grade += 10

    def show(self):
        print(self.name)
        print(self.grade)

student = Student("Name", 80)
student.pass_exam()
student.show()

# Exercise 1
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.speed = 0

    def accelerate(self, speed):
        self.speed += speed

    def brake(self, speed):
        self.speed -= speed

    def show(self):
        print(f"Brand : {self.brand}")
        print(f"Model : {self.model}")
        print(f"Speed : {self.speed} MPH.")

car = Car("BMW", "CS")
car.accelerate(20)
car.accelerate(10)
car.show()
car.brake(10)
car.show()

# Exercise 2
class Phone:
    def __init__(self, brand, battery):
        self.brand = brand
        self.battery = battery

    def charge(self):
        self.battery = 100

    def use(self, percent):
        self.battery -= percent

    def show(self):
        print(f"Brand : {self.brand}")
        print(f"Battery : {self.battery}%")

# Exercise 3
class Employee:
    def __init__(self, id, name, salary):
        self.id = id 
        self.name = name
        self.salary = salary

    def increase_salary(self, amount):
        self.salary += amount

    def decrease_salary(self, amount):
        self.salary -= amount

    def display(self):
        print(f"Name   : {self.name}")
        print(f"Salary : {self.salary}")

class Product:
    def __init__(self, id, name, price, stock):
        self.id = id 
        self.name = name
        self.price = price
        self.stock = stock

    def restock(self, quantity):
        self.stock += quantity

    def sell(self, quantity):
        self.stock -= quantity

    def display(self):
        print(f"Name : {self.name}")
        print(f"Stock : {self.stock}")

class BankAccount:
    def __init__(self, account_number, owner, balance):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdrawal(self, amount):
        self.balance -= amount

    def display(self):
        print(f"Account_number : {self.account_number}")
        print(f"Owner : {self.owner}")
        print(f"Balance : {self.balance}")

# Mini Project - School Management System
class Student:
    def __init__(self, id, name, course):
        self.id = id 
        self.name= name 
        self.course = course
        self.fees = 23000

    def pay_fees(self, amount):
        self.fees -= amount

    def display(self):
        print("---- Student ----")
        print(f"ID   : {self.id}")
        print(f"Name : {self.name}")
        print(f"Course : {self.course}")
        print(f"Fees : {self.fees}")

class Teacher:
    def __init__(self, id, name, salary):
        self.id = id 
        self.name = name 
        self.salary = salary

    def increase_salary(self,amount):
        self.salary += amount

    def display(self):
        print("---- Teacher ----")
        print(f"ID   : {self.id}")
        print(f"Name : {self.name}")
        print(f"Salary : {self.salary}")

class Course:
    def __init__(self, id, name, duration):
        self.id = id
        self.name = name
        self.duration = duration

    def display(self):
        print("---- Course ----")
        print(f"Id : {self.id}")
        print(f"Name : {self.name}")
        print(f"Duration : {self.duration}")

class ClassRoom:
    def __init__(self, id, label, capacity):
        self.id = id
        self.label = label
        self.capacity = capacity

    def display(self):
        print("---- ClassRoom ----")
        print(f"ID  :  {self.id}")
        print(f"Label : {self.label}")
        print(f"Capacity : {self.capacity}")

class Department:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def display(self):
        print("---- Department ----")
        print(f"ID : {self.id}")
        print(f"Name : {self.name}")