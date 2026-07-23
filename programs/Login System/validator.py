# Program: Login System Validator Module
# Author: David 
# Date: 22/07/26

def validate_username(username):
    username = username.strip().title()
    if not username:
        return None
    return username
