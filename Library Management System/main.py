# Program: Library Management Main Module
# Author: QuantumCodr
# Date: 30/07/2026

from menu import show_menu, borrow_book_menu, return_book_menu, search_book_menu, list_books_menu, list_borrow_records_menu

def main():
    while True:
        show_menu()
        option = input("Option: ")
        if option == '1':
            borrow_book_menu()
        elif option == '2':
            return_book_menu()
        elif option == '3':
            search_book_menu()
        elif option == '4':
            list_books_menu()
        elif option == '5':
            list_borrow_records_menu()
        elif option == '6':
            print('Goodbye.')
            break
        else:
            print("Invalid Option.")            


if __name__ == "__main__":
    main()