# Program: Sets
# Author: David
# Lesson: 19

# 1. Creating Sets
languages = {
    "Python",
    "Java",
    "Go"
}
print(languages) # {'Java', 'Python', 'Go'} Order may vary

# 2. Duplicates automatically Dissapera
numbers = {1, 2, 2, 3, 3, 3}
print(numbers) # {1, 2, 3}

# 3. Add
languages = {"Python", "Java"}
languages.add("Go")
print(languages) # {'Python', 'Java', 'Go'}

# 4. Remove
languages.remove("Java")
print(languages) # {'Python', 'Go'}
print(languages.discard("Rust")) # Safer no error

# 5. Membership
languages = {
    "Python",
    "Rust",
    "Go"
}
print("Python" in languages)
print("Java" in languages) 

# 6. Length
print(len(languages)) # 3

# 7. Union - Combine two sets.
backend = {
    "Python",
    "Go"
}
frontend = {
    "Javascript",
    "Python"
}
print(backend | frontend) # {'Javascript', 'Python', 'Go'}

# 8. Intersection - Only common values.
print(backend & frontend) # {'Python'}

# 9. Difference - Items only in the first set.
print( backend - frontend) # {'Go'}

# 10. Symetric Difference - Items not shared.
print(backend ^ frontend) # {'Javascript', 'Go'}

# Excercise 1
frameworks = {
    "FastAPI",
    "Flask",
    "Django"
}
print(len(frameworks))
print("Flask" in frameworks)

# Excercise 2
numbers ={1, 2, 3}
numbers.add(4)
numbers.remove(2)
print(numbers)

# Excercise 3
colors = {
    "Red",
    "Blue",
    "Green",
    "Blue"
}
print(colors)
print(len(colors))

# Excercise 4
a = {1, 2, 3}
b = {3, 4, 5}
print(a | b) # union
print(a & b) # Intersection
print(a - b) # Difference
print(a ^ b) # Symetric Difference

# Challenge 1 - Student Attendance
students = set()
for i in range(5):
    name = input(f"Enter student name {i+1}: ").strip()
    students.add(name)
print(students)
# No error just removes the duplicate

# Challenge 2 - BaseAPI modules
modules = set()
for i in range(5):
    module = input(f"Enter module {i+1}: ").lstrip().rstrip()
    modules.add(module)
print(modules)
print(len(modules))

# Challenge 3 - Programming Languages
backend = {
    "Python",
    "Go",
    "Rust"
}
frontend = {
    "Javascript",
    "Typescript",
    "Python"
}
print(f"All languages: {backend | frontend}")
print(f"Shared languages: {backend & frontend}")
print(f"Backend languages: {backend - frontend}")

'''
Think like a programmer
1. {1, 2, 3, 4, 5}
2. 3
3. {3}
4. {1, 2, 3}
5. Order is not permanent or important maybe error
'''

'''
Engineering Challange
1. Because it prevents duplicates and operations
2. Intersection
3. Difference
4. Because it does not follow order
'''

'''
🌟 Engineering Principle of the Day
Choose a set when uniqueness matters more than order.
'''