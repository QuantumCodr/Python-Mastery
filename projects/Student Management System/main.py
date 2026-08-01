# Program: Student Management Module
# Author: David
# Date: 27/01/2026

from menu import *


def main():
    while True:
        show_menu()
        option = input("Option: ")
        if option == "1":
            add_student_menu()
        elif option == "2":
            update_student_menu()
        elif option == "3":
            search_student_menu()
        elif option == "4":
            delete_student_menu()
        elif option == "5":
            print("Goodbye.")
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()