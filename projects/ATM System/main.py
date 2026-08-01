# Program: ATM Module
# Author: David
# Date: 27/01/2026

from menu import *

def main():
    while True:
        show_menu()
        option = input("option: ")
        if option == "1":
            show_balance_menu()
        elif option == "2":
            deposit_money_menu()
        elif option == "3":
            withdraw_money_menu()
        elif option == "4":
            transfer_money_menu()
        elif option == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()