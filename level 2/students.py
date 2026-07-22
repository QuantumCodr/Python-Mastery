# Program: Student Module
# Author: David
# Lesson: 22
students = set()

def add_student(name):
    students.add(name)
    print("Student added succesfully!")

def remove_student(name):
    try:
        students.remove(name)
    except:
        print(f"Student not exist '{name}'.")
    else:
        print("Student removed successfully!")

def show_students():
    print("---------STUDENTS-----------")
    for index, student in enumerate(students):
        print(f"{index + 1}. {student}")

""" add_student("David")
add_student("David")
add_student("Alice")
add_student("Bob")
show_students()
remove_student("David")
remove_student("Paul")
show_students()

food = ["Bread", "Butter", "Egg"]
print(food.index("Bread"))
bread = food[0]
print(type(bread)) """