# Program: User Input
# Author: David
# Lesson: 4

name = input("What is your name? ")
print(f"Hello {name}!")

age = input('Enter age: ')
print(age)
print(type(age))

country = input("Which country are you from? ")
print(f"You are from {country}.")

# Multiple Inputs
name = input("Name: ")
country = input("Country: ")
food = input("Favorite food: ")
print()
print("==========PROFILE==========")
print(f"Name: {name}")
print(f"country: {country}")
print(f"Fovorite food: {food}")

# Excercise 1
name = input("What is your name? ")
print(f"Hello {name}!")

# Excercise 2
name = input("What is your name? ")
age = input("What is your age? ")
country = input("Which country are you from? ")
print()
print("##########################")
print("#         PROFILE        # ")
print("##########################")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Country: {country}")

# Excercise 3
dream_job = input("What is your dream job? ")
print(f"I pray you become a {dream_job}!")

# Excercise 4
language = input("What is your favourite programming language? ")
food = input("What is your favorite food? ")
color = input("What is your favorite color? ")
print(f"Favorite programming language: {language}")
print(f"Favorite food: {food}")
print(f"Favorite color: {color}")

# Excercise 4 (simple registration form)
print("    REGISTRATION FORM    ")
print("___________________________")
first_name = input("First name: ")
last_name = input("Last name: ")
email = input("Email: ")
country = input("Country: ")
phone_number = input('Phone number: ')
print()
print("____________________________")
print("            USER            ")
print("----------------------------")
print(f"First Name: {first_name}")
print(f"Last Name: {last_name}")
print(f"Country: {country}")
print(f"Phone Number: {phone_number}")
print("____________________________")