# Program: Student Management Menu
# Author: David
# Date: 27/07/2026

from student_services import (
    add_student,
    update_student,
    search_student,
    delete_student
)


def show_menu():
    print()
    print("===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. Update Student")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")
    print()


def add_student_menu():
    print()
    print("----- Add Student -----")
    name = input("Name   : ")
    age = input("Age    : ")
    course = input("Course : ")
    if add_student(name, age, course):
        print("\nStudent added successfully.")
    else:
        print("\nInvalid student information.")


def update_student_menu():
    print()
    print("----- Update Student -----")

    id = input("Student ID : ")
    name = input("Name       : ")
    age = input("Age        : ")
    course = input("Course     : ")

    if update_student(id, name, age, course):
        print("\nStudent updated successfully.")
    else:
        print("\nUnable to update student.")


def search_student_menu():
    print()
    print("----- Search Student -----")

    id = input("Student ID : ")

    student = search_student(id)

    if student:
        print("\nStudent Found")
        print("-------------------------")
        print(f"ID     : {student['id']}")
        print(f"Name   : {student['name']}")
        print(f"Age    : {student['age']}")
        print(f"Course : {student['course']}")
    else:
        print("\nStudent not found.")


def delete_student_menu():
    print()
    print("----- Delete Student -----")

    id = input("Student ID : ")

    if delete_student(id):
        print("\nStudent deleted successfully.")
    else:
        print("\nStudent not found.")