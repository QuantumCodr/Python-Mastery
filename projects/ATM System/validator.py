# Program: ATM Validator Module
# Author: David
# Date: 27/01/2026

def validate_account_number(account_number):
    try:
        account_number = int(account_number)
    except ValueError:
        return None
    if account_number <= 0:
        return None
    return account_number


def validate_amount(amount):
    try:
        amount = float(amount)
    except ValueError:
        return None
    if amount <= 0:
        return None
    return amount