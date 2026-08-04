# Program: CSV, JSON, Binary Files & Pickle
# Author: QuantumCodr
# Lesson: 25

# 1. CSV Files - Comma Separated Values
import csv

# Reading CSV
try:
    with open("files/students.csv") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
except FileNotFoundError:
    print("File does not exist.")
print()

# Skip Header
try:
    with open("files/students.csv") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            print(row)
except FileNotFoundError:
    print("File does not exist.")
print()

# Access Individual Columns
try:
    with open("files/students.csv") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            print(row[1])
except FileNotFoundError:
    print("File does not exist.")

# Writing CSV
try:
    with open("files/output.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["id", 'name', "age"])
        writer.writerow([1, "David", 22])
        writer.writerow([2, "Sarah", 20])
except FileNotFoundError:
    print("File does not exist.")

# Writing Many Rows
rows = [
    [1,"David",22],
    [2,"Sarah",20],
    [3,"John",30]
]

try:
    with open("files/output.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["id", "name", "age"])
        writer.writerows(rows)
except FileNotFoundError:
    print("File does not exist.")

# Dictionary CSV 
try:
    with open('files/students.csv') as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(row["age"])
except FileNotFoundError:
    print("File does not exist.")

# 2. JSON - JavaScript Object Notation
import json

# json.dump()
students = {
    "id": 1,
    "name": "David",
    "age": 22
}

try:
    with open("files/students.json", "w") as file:
        json.dump(students,file, indent=4)
except FileNotFoundError:
    print("File does not exist.")

# json.load()
try:
    with open("files/students.json") as file:
        students = json.load(file)    
except FileNotFoundError:
    print("File does not exist.")
print(students)

# 3. Binary Files
try:
    with open("files/image.jpg","rb") as file:
        data = file.read()
except FileNotFoundError:
    print("File does not exist.")

else:
    # print(data)
    print(type(data))

try:
    with open("files/copy.jpg", "wb") as file:
        file.write(data)
except FileNotFoundError:
    print("file does not exist.")

# 4. Pickle - Pickle stores Python objects directly.
import pickle

# Save Object
students = [
    {"id":1,"name":"David"},
    {"id":2,"name":"Sarah"}
]

try:
    with open("files/students.pkl", "wb") as file:
        pickle.dump(students,file)
except FileNotFoundError:
    print("File does not exist.")

# Load Object
try:
    with open("files/dtudents.pkl", "rb") as file:
        data = pickle.load(file)
except FileNotFoundError:
    print("File does not exist")
else:
    # print(data)
    print(type(data))

# Exercises

# 1 - Create CSV
rows = [
    [1,"David",22],
    [2,"Sarah",20],
    [3,"John",30]
]

try:
    with open("files/students.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["id", "name", "age"])
        writer.writerows(rows)
except FileNotFoundError:
    print("Filee does not exist")

# 2. Read the CSV and print only names.
try:
    with open("files/students.csv") as file:
        students = csv.DictReader(file)
        for row in students:
            print(row["name"])
except FileNotFoundError:
    print("File does not exist.")

# 3. Read the CSV and calculate the average age.
try:
    with open("files/students.csv") as file:
        students = csv.DictReader(file)
        next(students)
        total_age = 0
        count = 0
        for row in students:
            total_age += int(row["age"])
            count += 1
except FileNotFoundError:
    print("File was not found.")
else:
    average_age = total_age/count
    print(f"Average age: {average_age}")

# 4. Create products.csv
rows = [
    ["id", "name", "price"],
    [1, "Laptop", 950],
    [2, "Mouse", 20],
    [3, "Keyboard", 45]
]

try:
    with open("files/products.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(rows)
except FileNotFoundError:
    print("File does not exists.")

# 5. Create student.json
student = {
    "id":1,
    "name":"David",
    "course":"Computer Science"
}

try: 
    with open("files/student.json", "w") as file:
        json.dump(student,file,indent=4)
except FileNotFoundError:
    print("File does not exists.")

# 6. Read student.json
try:
    with open("files/student.json") as file:
        student = json.load(file)
except FileNotFoundError:
    print("Filedoes not exist")
else:
    print(student)

# 7. List of three dictionaries of books
books = [
    {
        "id": 1,
        "title": "Python Basics",
        "author": "Sarah"
    },
    {
        "id": 2,
        "title": "Applied Accounting",
        "author": "David"
    },
    {
        "id": 3,
        "title": "Introduction to OS",
        "author": "John"
    }
]

try:
    with open("files/books.json", "w") as file:
        json.dump(books,file,indent=4)
except FileNotFoundError:
    print("File doesnot exist")
else:
    with open("files/books.json") as file:
        books = json.load(file)
        print()
        print("    Book Titles")
        print("--------------------")
        for index,book in enumerate(books, start=1):
            print(f"{index}. {book['title']}")

# 8. Copy an image
try:
    with open("files/image.jpg", "rb") as file:
        reader = file.read()
except FileNotFoundError:
    print("File does not exist.")
else:
    with open("files/backup.jpg","wb") as file:
        file.write(reader)

# 9. Create a dictionary representing a game save:
game = {
    "player": "David",
    "level": 5,
    "score": 1200,
    "lives": 3
}

try:
    with open("files/save.pkl", "wb") as file:
        pickle.dump(game,file)
except FileNotFoundError:
    print("File does not exist.")
else:
    with open("files/save.pkl", "rb") as file:
        game_save = pickle.load(file)
        print(game_save)
        print(type(game_save))

# 10. Mini Project
# Program: CSV, JSON, Binary Files & Pickle
# Author: QuantumCodr
# Lesson: 25

# 10. Mini Project
import json,csv,pickle

def file_manager_menu():
    print()
    print("===========================")
    print("    Student File Manager")
    print("===========================")
    print("1. Save student to JSON")
    print("2. Load student from JSON")
    print("3. Export students to CSV")
    print("4. Backup students using Pickle")
    print("5. Restore students from Pickle")
    print("6. Exit")

def save_student_json(student):
    try:
        with open("files/student.json", "w") as file:
            json.dump(student, file, indent=4)
    except FileNotFoundError:
        print("File does not exist.")
        return False
    else:
        return True

def load_student_from_json():
    try:
        with open("files/student.json") as file:
            data = json.load(file)
    except FileNotFoundError:
        print("File foes not exist.")
        return False
    else:
        return data
    
def export_students_to_CSV():
    try:
        with open("files/student.json") as file:
            student = json.load(file)
    except FileNotFoundError:
        print("File does not exist.")
        return False
    else:
        with open("files/student.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["id", "name", "age","course"])
            writer.writerow([student["id"], student["name"], student["age"], student["course"]])
        return True

def backup_student_using_pickle():
    try:
        with open("files/student.json") as file:
            data = json.load(file)
    except FileNotFoundError:
        return False
    else:
        with open("files/student.pkl", "wb") as file:
            pickle.dump(data,file)
        return True
def restore_from_pickle():
    try:
        with open("files/student.pkl", "rb") as file:
            data = pickle.load(file)
    except FileNotFoundError:
        print("File does not exist.")
        return False
    else:
        return data

def file_manager():
    student_data = {
        "id": 1,
        "name": "Gleekan David Williams",
        "age": 24,
        "course": "Software Engineering and Multimedia"
    } 
    while True:
        file_manager_menu()
        option = input("Option: ")
        if option == "1":
            save = save_student_json(student_data)
            if not save:
                print("Fail to save student.")
            else:
                print("Student saved successfully.")
        elif option == "2":
            load = load_student_from_json()
            if not load:
                print("No student was found.")
            else:
                print("Student loaded successfully")
                print("---------------------------")
                print(load)
        elif option == "3":
            export_csv = export_students_to_CSV()
            if not export_csv:
                print("Fail to export to csv.")
            else:
                print("Export to csv successfull.")
        elif option == "4":
            backup = backup_student_using_pickle()
            if not backup:
                print("Fail to pickle backup.")
            else:
                print("Pickle backup successful.")
        elif option == "5":
            student_data = restore_from_pickle()
            if not student_data:
                print("No student data was found.")
            else:
                print("----- Student Data Restored -----")
                print(student_data)
        elif option == "6":
            print("Goodbye.")
            break
        else:
            print("Invalid Option.")
if __name__ == "__main__":
    print("Program started and running...")
    file_manager()