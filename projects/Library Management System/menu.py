# Program: Library Management Menu Module
# Author: QuantumCodr
# Date: 30/07/2026

from service import (
    borrow_book,
    return_book,
    search_book,
    list_books,
    list_borrow_records
)

def show_menu():
    print()
    print("===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Borrow Book")
    print("2. Return Book")
    print("3. Search Book")
    print("4. List Books")
    print("5. List Borrow Records")
    print("6. Exit")
    print()

def borrow_book_menu():
    print()
    print("---- Borrow Book ----")
    member_id = input("Member ID: ")
    book_id = input("Book ID: ")
    borrow = borrow_book(member_id, book_id)
    if not borrow:
        print("\nFailed to borrow book.")
    else:
        print("\nBook borrowed successfully.")

def return_book_menu():
    print()
    print("----- Return Book ----")
    borrow_id = input("Borrow ID: ")
    if not return_book(borrow_id):
        print("\nFail to return book.")
    else:
        print("\nBook returned succcessfully.")

def search_book_menu():
    print()
    print("----- Search Book -----")
    book_id = input("Book ID: ")
    search = search_book(book_id)
    if not search:
        print('\nNo book was found.')
    else:
        print("\n   Book Found    ")
        print("---------------------")
        print(f"ID: {search['id']}")
        print(f"Name: {search['title']}")
        print(f"Author: {search['author']}")
        print(f"Available: {search['available']}")

def list_books_menu():
    books = list_books()
    if not books:
        print("\nNo book(s) was found.")
    else:
        print("\n     Books Found   ")
        print("----------------------")
        for book in books:
            print(f"ID: {book['id']}")
            print(f"Name: {book['title']}")
            print(f"Author: {book['author']}")
            print(f"Available: {book['available']}")
            print("----------------------")

def list_borrow_records_menu():
    member_id = input("Member ID: ")
    records = list_borrow_records(member_id)
    if not records:
        print("\nNo record(s) was found.")
    else:
        print("\n    Records Found   ")
        print("-----------------------")
        for record in records:
            print(f"ID: {record['id']}")
            print(f"Member name: {record['member_name']}")
            print(f"Book title: {record['book_title']}")
            print("----------------------")