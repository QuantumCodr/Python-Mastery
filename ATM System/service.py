# Program: ATM Service Module
# Author: David
# Date: 27/01/2026

from repository import transfer, get_account, deposit, withdraw
from validator import validate_amount, validate_account_number

def show_balance(account_number):
    account_number = validate_account_number(account_number)
    if not account_number:
        return False
    account = get_account(account_number)
    if not account:
        return False
    return account['balance']

def deposit_money(account_number, amount):
    account_number = validate_account_number(account_number)
    amount = validate_amount(amount)
    if not account_number or not amount:
        return False
    account = get_account(account_number)
    if not account:
        return False
    deposit(account, amount)
    return True
    

def withdraw_money(account_number, amount):
    account_number = validate_account_number(account_number)
    amount = validate_amount(amount)
    if not account_number or not amount:
        return False
    account = get_account(account_number)
    if not account:
        return False
    if amount > account["balance"]:
        return False
    withdraw(account, amount)
    return True
        

def transfer_money(sender_number, receiver_number, amount):
    sender_number = validate_account_number(sender_number)
    receiver_number = validate_account_number(receiver_number)
    amount = validate_amount(amount)
    if not all([sender_number, receiver_number, amount]):
        return False
    if sender_number == receiver_number:
        return False
    sender = get_account(sender_number)
    receiver = get_account(receiver_number)
    if not sender or not receiver:
        return False
    if sender["balance"] < amount:
        return False
    transfer(sender, receiver, amount)
    return True