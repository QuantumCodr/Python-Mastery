# Program: Tuples
# Author: David
# Lesson: 18

# 1. Creating Tuples
numbers = (1, 2, 3)
print(numbers)

# 2. One-Item Tuple
value = (5,) # Tuple
print(type(value)) # <class 'tuple'>

value = (5)
print(type(value)) # <class 'int'>

# 3. Indexing
languages = (
    "Python",
    "Go",
    "Rust"
)
print(languages[0]) # Python
print(languages[1]) # Go 
print(languages[-1]) # Rust

# 4. Slicing
numbers = (20, 30, 40, 40, 60)
print(numbers[0:3])
print(numbers[1: ])
print(numbers[ :-1])
print(numbers[-2:])

# 5. Length
colors = (
    "Red",
    "Blue",
    "Green"
)
print(len(colors))

# 6. Membership
colors = (
    "Red",
    "Blue",
    "Green"
)
print("Red" in colors)
print("orange" in colors)

# 7. Count
numbers = (1,2,2,3,2)
print(numbers.count(2))

# 8. Indices
numbers = (10, 20, 30, 40, 50)
print(numbers.index(50))

# 9. Tuple Packing
person = "David", 25, "Freetown"
print(person) # ("David", 25, "Freetown")

# 10. Tuple Unpacking
name, age, city, = person
print(name)
print(age)
print(city)

# 11. Returning Multiple Values
def divide(a, b):
    quotient = a / b
    remainder = a % b
    return quotient, remainder  # Python secretly returns (3.33, 1)
q, r = divide(10,3)
print(q)
print(r)

# Excercise 1
frameworks = (
    "FastAPI",
    "Flask",
    "Django"
)
print(frameworks[0])
print(frameworks[-1])

# Excercise 2
number = (10,20,30,40,50)
print(number[:3])
print(number[-2:])

# Excercise 3
student = ("David", 24, "Python")
name, age, course = student
print(name)
print(age)
print(course)

# Excercise 4
colors = (
    "Red",
    "Blue",
    "Green",
    "Blue"
)
print(len(colors))
print(colors.count("Blue"))
print(colors.index("Green"))

# Challange 1 - Coordinates
coord = (-7, 48.7)
latitude, longitude = coord
print(f"Latitude: {latitude} deg.")
print(f"Longitude: {longitude} deg.")

# Challage 2 - BaseAPI Version
version = (1,0,3)
major, minor, patch = version
print(f"Version: {major}.{minor}.{patch}")

# Challange 3 - User Profile
profile = (
    "David",
    "Sierra Leone",
    "Backend Developer"
)
name, country, occupation = profile
print(name)
print(country)
print(occupation)

'''
Think like a programmer
1. 2
2. <class 'tuple'>
3. 3
4. 20
5. immutable
'''
'''
Engineering Challange
1. Imutable
2. Create a new tuple
3. Data integrity and consistency
'''

'''
🌟 Engineering Principle of the Day
Use the right data structure to communicate your intent.
'''