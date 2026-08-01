# Program: Student Management Validator Module
# Author: David
# Date: 27/01/2026

def validate_name(name):
    if not isinstance(name, str):
        return None
    name = name.strip()
    if not name:
        return None
    return name.title()


def validate_age(age):
    try:
        age = int(age)
    except ValueError:
        return None
    if age < 1 or age > 120:
        return None
    return age


def validate_id(id):
    try:
        id = int(id)
    except ValueError:
        return None
    if id <= 0:
        return None
    return id