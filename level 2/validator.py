# Program: Validator Module
# Author: David
# Lesson: 22

def validate_name(name):
    try:
        name = name.strip().title().replace(" ", "_")
    except AttributeError:
        print(f"Error: Invalid Input {type(name)}")
        raise AttributeError
    else:
        # print(f"Success: name validated '{name}'.")
        return name
