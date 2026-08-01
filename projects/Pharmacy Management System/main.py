# Program: Pharmacy Management Main Module
# Author: QuantumCodr
# Date: 31/07/2026

from menu import (
    show_menu,
    sell_medicine_menu,
    search_medicine_menu,
    restock_medicine_menu,
    list_medicines_menu,
    view_sales_menu
)

def main():
    while True:
        show_menu()
        option = input('Option: ')
        if option == '1':
            sell_medicine_menu()
        elif option == '2':
            restock_medicine_menu()
        elif option == '3':
            search_medicine_menu()
        elif option == '4':
            list_medicines_menu()
        elif option == '5':
            view_sales_menu()
        elif option == '6':
            print('Goodbye.')
            break
        else:
            print("Invalid Option.")

if __name__ == "__main__":
    main()