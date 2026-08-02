# Program: File Handling Fundamentals
# Author: David
# Lesson: 22
# Date: 01/08/2026

'''
A file is simply data stored permanently on a storage device.
Examples:
    notes.txt
    photo.jpg
    music.mp3
    report.pdf
    students.csv
    database.db
'''

# Opening a file
file = open("files/notes.txt")

# Reading everything
file = open("files/notes.txt")
contents = file.read()
# print(contents)
file.close()

# Better Way
with open("files/notes.txt") as file:
    contents = file.read()
# print(contents)

# Reading one line
with open("files/notes.txt") as file:
    line = file.readline()
# print(line)

# Second line
with open("files/notes.txt") as file:
    print(file.readline())
    print(file.readline())

# Reading all lines
with open("files/notes.txt") as file:
    line = file.readlines()
print(line)   # ['Apple\n', 'Banana\n', 'Orange']

# Looping through a file
with open("files/notes.txt") as file:
    for line in file:
        print(f"\n{line.strip()}")

# Write Mode
with open("files/notes.txt", "w") as file:
    # file.write("Hello World.")
    pass

# Append Mode
with open("files/notes.txt", "a") as file:
    file.write("\nPython")

# Creating a file
with open("files/students.txt", "w") as file:
    pass

# Writing multiple lines
with open("files/notes.txt", "w") as file:
    file.write("David\n")
    file.write("Python\n")
    file.write("Programming")

# Use writelines
lines = [
    "David\n",
    "Sarah\n",
    "John\n"
]

with open("students.txt", "w") as file:
    file.writelines(lines)

# Checking if a file exists
import os
print(os.path.exists('files/notes.txt'))

# Delete file
# print(os.remove("files/notes.txt"))

# Example 1 - Read file
with open("files/notes.txt") as file:
    print(file.read())

# Example 2 - Copy a file
with open("files/source.txt") as source:
    data = source.read()

with open("files/destination.txt", "w") as destination:
    destination.write(data)
    destination.write("\nI am the second\n")
    destination.write("Order of destination")

# Example 3 - Append a log
name = input("Enter name: ")
with open("files/log.txt", "a") as log:
    log.write(f"{name}\n")

# Example 4 - Count lines
count = 0
with open("files/notes.txt") as file:
    for line in file:
        count += 1
print(f"Count line: {count}")

# Example 5 - Count words
with open("files/notes.txt") as file:
    text = file.read()
words = text.split()
print(f"Word counts: {len(words)}")

# Example 6 - Search for a word
word = input("Search: ")
with open("files/notes.txt") as file:
    text = file.read()
if word in text:
    print("Found")
else:
    print("Not found")

# Example 7 - Save user information
name = input("Name: ")
age =  input("Age: ")
with open("files/users.txt", "a") as users:
    users.write(f"{name}, {age}\n")

# Excercise 1 - Create hello.txt
with open("files/hello.txt","w") as file:
    file.write("Hello Python\n")

# Excercise 2 - Read hello.txt
with open("files/hello.txt", "r") as file:
    text = file.read()
    print(text)

# Excercise 3 - Append "Learning Python"
with open("files/hello.txt", "a") as file:
    file.write("Learning Python")

# Excercise 4 - add 5 names entered by the user into students.txt
with open("files/students.txt", "w") as students:
    for i in range(2):
        name = input(f"Name {i+1}: ")
        students.write(f"{name}\n")

# Excercise 5 - Read every line and print
with open("files/students.txt", "r") as students:
    lines = students.readlines()
for line in lines:
    print(f"Student: {line.strip()}")

# Excercise 6 - Count students 
count = 0
with open("files/students.txt", "r") as students:
    for line in students:
        count += 1
print(f"Count students: {count}")

# Excercise 7 - Search for David in students
with open("files/students.txt", 'r') as file:
    students = file.read()
if "David" in students:
    print("Found")
else:
    print("Not Found.")

# Excercise 8 - copy students into backup.txt
with open("files/students.txt", "r") as students:
    student_contents = students.read()

with open("files/backup.txt", "w") as backup:
    content = backup.write(student_contents)

# Excercise 9 - Delete backup.txt
import os
os.remove("files/backup.txt")

# Excercise 10 - Mini Note project
def note_menu():
    print("1. Add Note") 
    print("2. View Notes")
    print("3. Clear Notes")
    print("4. Exit")

while True:
    print()
    print("===== Mini Note Application =====")
    note_menu()
    print()
    option = input("Option: ")
    if option == '1':
        print()
        print("----- Add Note -----")
        note = input("Enter note: ")        
        with open("files/notes.txt", "a") as file:
            file.write(f"{note}\n")
    elif option == '2':
        print()
        print("----- Print Notes -----")
        with open("files/notes.txt", 'r') as file:
            notes = file.read()
            if not notes:
                print("No notes found.")
            else:
                print(notes)
    elif option == '3':
        print()
        with open("files/notes.txt", "w") as file:
            pass
        print("Notes deleted.")
    elif option == '4':
        print()
        print("Goodbye.")
        break
    else:
        print("Invalid Option.")
