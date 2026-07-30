# Program: Student Management Service Module
# Author: David
# Date: 27/01/2026

from validator import validate_name
from validator import validate_age
from validator import validate_id

from repository import get_student
from repository import insert_student
from repository import next_student_id
from repository import remove_student


def add_student(name, age, course):

    name = validate_name(name)
    age = validate_age(age)
    course = validate_name(course)

    if not all([name, age, course]):
        return False

    student = {
        "id": next_student_id(),
        "name": name,
        "age": age,
        "course": course
    }

    insert_student(student)

    return True

def update_student(id, name, age, course):
    id = validate_id(id)
    name = validate_name(name)
    age = validate_age(age)
    course = validate_name(course)
    if not all([id, name, age, course]):
        return False
    student = get_student(id)
    if not student:
        return False
    student["name"] = name
    student["age"] = age
    student["course"] = course
    return True

def search_student(id):
    id = validate_id(id)
    if not id:
        return None
    return get_student(id)
        
def delete_student(id):
    id = validate_id(id)
    if not id:
        return False
    student = get_student(id)
    if not student:
        return False
    remove_student(student)
    return True

