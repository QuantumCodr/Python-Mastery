# Program: Login System Auth Module
# Author: David
# Date: 22/01/26

from database import users
def authenticate(name, password):
    user = users.get(name)
    if user and password == user:
        return True
    return user == password

print(authenticate("David", "python123"))
print(authenticate("Paul", "password"))