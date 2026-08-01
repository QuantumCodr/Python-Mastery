# Program: Inventory Management Module
# Author: David
# Date: 27/01/2026

from menu import *

def main():
    while True:
        show_menu()
        option = input("option: ")
        if option == "1":
            add_product_menu()
        elif option == "2":
            update_product_menu()
        elif option == "3":
            search_product_menu()
        elif option == "4":
            delete_product_menu()
        elif option == "5":
            list_products_menu()
        elif option == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()