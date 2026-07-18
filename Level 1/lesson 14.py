'''
Program: Strings Advance
Author: David
Lesson: 14
'''

# 1. Accessing characters
name = "David"
print(name[1]) # a
print(name[4]) # d

# Negative Indexing
print(name[-1]) # d
print(name[-3]) # v

'''
 D  a  v  i  d
 0  1  2  3  4

-5 -4 -3 -2 -1
'''

# 2. Finding Length
language = "python"
print(len(language)) # 6

text = "Hello Wolrd"
print(len(text)) # 11

# 3. Uppercase
language = "python"
print(language.upper()) # PYTHON

# 4. Lowercase
fruit = "BANANA"
print(fruit.lower()) # banana

# 5. Title Case
name = "tom holland"
print(name.title()) # Tom Holland

# 6. Removing Spaces
name = "   Bob    "
print(name.strip()) # Bob

# 7. Replace
sentence = "I love Java"
print(sentence.replace("Java", "Python"))

# 8. Find
text = "BaseAPI"
print(text.find("A")) # 4 0 1 2 3 4 

# Not Found
print(text.find("q")) # -1

# 9. Memberhip
language = "Python"
print("py" in language) # True
print("java" in language) # False

# 10. Slicing
word = "Programming"
'''
P r o g r a m m i n g
0 1 2 3 4 5 6 7 8 9 10
'''
# First three letters
print(word[0:3]) # Pro
# Middle
print(word[3:7]) # gram (7 minus 1)
# Last 3
print(word[-3:])

# Real-world Example
project = input('Enter project: ').strip() # Input Validation

# Excercise 1 - Indexing
name = "python"
print(name[0])
print(name[-1])

# Excercise 2 - Length
full_name = input("Enter your full-name: ")
print(f"Total characters: {len(full_name)}")

# Excercise 3 - Case Conversion
language = input("Enter favorite programming language: ")
print(f"Uppercase: {language.upper()}")
print(f"Lowercase: {language.lower()}")
print(f"Title Case: {language.title()}")

# Excercise 4 - Strip
name = input("Name: ")
print(name.strip())

# Challange 1 - Password Checker
password = input("Enter password: ")
checker = password.strip()
if checker == "python123" or checker == "Python123":
    print("Access Granted")
else: 
    print("Access Denied")

# Challange 2 - Email Validator
email = input("Enter email: ")
if "@" in email:
    print("Valid Email")
else:
    print("Invalid Email")

# Challange 3 - Username formatter
fullname = input("Enter full-name: ").strip().title()
print(fullname)

'''
Think like a programmer:
1. t
2. 11
3. DAVID
4. Hello
5. True
'''

# Engineering Challange
def normalize_project_name(name):
    return name.strip().lower().replace(" ","_" )
normalizer = normalize_project_name("     DaveOps          ")
print(normalizer)