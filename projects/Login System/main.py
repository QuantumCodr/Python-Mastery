# Program: Login System
# Author: David
# Date: 22/01/26

from login import login

def main():
    username = input("Enter username: ")
    password = input("Enter password: ")
    logged_in = login(username, password)
    if logged_in:
        print("Login Successful!")
    else:
        print("Login Unsuccessful!")
main()