# Program: File Handling Advance
# Author: David
# Lesson: 24
# Date: 01/08/2026
import os

# Handling File Errors
try:
    with open("unknown.txt") as file:
        print(file.read())
except FileNotFoundError:
    print("File does not exist.")

# Reading Large Files
with open("files/students.txt") as file:
    print(file.read())
    for line in file:
        print(line.strip())

# File Pointer
with open("files/notes.txt") as file:
    print(file.readline())
    file.seek(0)
    print(file.readline())

# Current Position
with open("files/notes.txt") as file:
    print(file.tell()) # 0
    print(file.read(5)) # I lik
    print(file.tell()) # 5

# Reading Specific Characters
with open("files/notes.txt") as file:
    print(file.read(18))

# Using os.path
print(os.path.exists("files/notes.txt"))

size = os.path.getsize("files/notes.txt")
print(size)

absolute_path = os.path.abspath("files/notes.txt")
print(absolute_path)

# Renaming Files
# os.rename("files/notes.txt", "files/notes_application")

# Creating Directories
os.mkdir("Applications")

# Nested Folders
os.makedirs("data/files/logs/")

# Removing Directories
os.rmdir("Applications")

# Listing Files
files = os.listdir(".") # root path 
print(files)

# 12. CSV File - comma separated values
import csv

# Reading
with open("files/students.csv") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# Writing
with open("files/students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["ID", "Name", "Age"])
    writer.writerow([1, "David", "24"])

# 13. JSON Files
import json

# Write JSON
student = {
    "name":"David",
    "age":22
}
with open("files/student.json","w") as file:
    json.dump(student,file)

# Read JSON
with open("files/student.json") as file:
    students = file.read()
print(students)


# 12. CSV File - comma separated values
import csv

# Reading
with open("files/students.csv") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# Writing
with open("files/students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["ID", "Name", "Age"])
    writer.writerow([1, "David", "24"])

# 13. JSON Files
import json

# Write JSON
student = {
    "name":"David",
    "age":22
}
with open("files/student.json","w") as file:
    json.dump(student,file)

# Read JSON
with open("files/student.json") as file:
    student = file.read()
print(student)

# 14. Binary Files
'''
Useful for:
    Images
    Videos
    PDFs
    ZIP files
'''

with open("image.jpg","rg") as file:
    data = file.read()