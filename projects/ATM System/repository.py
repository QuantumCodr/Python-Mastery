# Program: ATM Repository Module
# Author: David
# Date: 27/01/2026

from database import accounts
from validator import (
    validate_account_number,
    validate_amount
)

def get_account(account_number):
    for account in accounts:
        if account["account_number"] == account_number:
            return account
    return None

def deposit(account, amount):
    account["balance"] += amount

def withdraw(account, amount):
    account["balance"] -= amount

def transfer(sender, receiver, amount):
    sender["balance"] -= amount
    receiver["balance"] += amount