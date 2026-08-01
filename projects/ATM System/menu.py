# Program: ATM Menu Module
# Author: David
# Date: 27/07/2026

from service import show_balance, deposit_money, withdraw_money, transfer_money


def show_menu():
    print()
    print("===== ATM MODULE SYSTEM =====")
    print("1. Show balance")
    print("2. Deposit money")
    print("3. Withdraw money")
    print("4. Transfer money")
    print("5. Exit")
    print()

def show_balance_menu():
    print()
    print("-----Show Balance-----")
    account_number = input("Account number: ")
    balance = show_balance(account_number)
    if balance:
        print(f"\nAccount balance: {balance}")
    else:
        print("\nFail to retrieve balance.")

def deposit_money_menu():
    print()
    print("-----Deposit Money-----")
    account_number = input('Account number: ')
    amount = input("Amount: ")
    deposit = deposit_money(account_number, amount)
    if deposit:
        print("\nDeposit successfuly.")
    else:
        print("\nFail to deposit.")

def withdraw_money_menu():
    print()
    print("-----Withdraw Money-----")
    account_number = input('Account number: ')
    amount = input("Amount: ")
    withdraw = withdraw_money(account_number, amount)
    if withdraw:
        print(f"\nWithdraw successful, amount Le:{amount}.")
    else:
        print("\nFail to withdraw.")

def transfer_money_menu():
    print()
    print("-----Transfer Money-----")
    sender_number = input("Sender number: ")
    receiver_number = input("Receiver number: ")
    amount = input("Amount: ")
    transfer = transfer_money(sender_number, receiver_number, amount)
    if transfer:
        print("\nTransfer successful.")
    else:
        print("\nFail to transfer.")