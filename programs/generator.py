# Program: Generator Module
# Author: David
# Lesson: 22

from validator import validate_name
files = [
    "main.py",
    "config.py",
    "auth.py",
    "users.py",
    "README.md",
    ".env"
]

def create_project():
    project = input("Enter project: ")
    try: 
        project = validate_name(project)
    except:
        print("Invalid project name")
        return
    else:
        print(f"Creating project {project} ...")
        create_structure()
        print(f"Project created sucessfully!")

def create_structure():
    for file in files:
        print(f"Creating {file}")

create_project()