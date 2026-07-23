# Program: Login System Login Module
# Author: David
# Date: 22/07/2026

from validator import validate_username
from auth import authenticate
def login(username, password):
    username = validate_username(username)
    if not username:
        return None
    return authenticate(username, password)
# Test
# print(login("David", "python1234"))