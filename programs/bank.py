# Program: Mank Module
# Author: David
# Lesson: 22

def deposit(balance):
    try:
        amount = float(input("Enter deposit amount SLL: "))
    except ValueError:
        print("Invalid amount!")
        return balance
    if amount <= 0:
        print("Zero or negative amount")
    else:
        balance += amount
        print(f"Deposit successful {amount}, new balance SLL{balance}!")
        return balance 
    
def withdraw(balance):
    try:
        amount = float(input("Enter withdraw amount SLL: "))
    except:
        print("Invalid amount.")
    else:
        if amount <= 0:
            print("Incorrect amount.")
        elif amount > balance:
            print('Insufficient funds.')
        else:
            balance -= amount
            print(f"Withdrawal successful {amount}, new balance SLL{balance}!")
            return balance
    
def show_balance(balance):
    return (f"Balance: SLL{balance}")
