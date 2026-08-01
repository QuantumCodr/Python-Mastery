# Program: Library Management Service Module
# Author: QuantumCodr
# Date: 30/07/2026

from validator import validate_name, validate_id
from repository import (
    get_member, 
    get_book, 
    get_record, 
    next_record_id, 
    insert_record, 
    get_all_records,
    get_all_books, 
    delete_record,
    get_borrow_records
    )


def borrow_book(member_id, book_id):
    member_id =  validate_id(member_id)
    book_id = validate_id(book_id)
    if not member_id or not book_id:
        return False
    member = get_member(member_id)
    book = get_book(book_id)
    if not member or not book:
        return False
    if not book['available']:
        return False
    borrow_record = {
        'id': next_record_id(),
        'member_id': member['id'],
        'member_name': member['name'],
        'book_id': book['id'],
        'book_title': book['title'] 
    }
    insert_record(borrow_record)
    book['available'] = False
    return True

def return_book(record_id):
    record_id = validate_id(record_id)
    if not record_id:
        return False
    record = get_record(record_id)
    if not record:
        return False
    book_id = record['book_id']
    book = get_book(book_id)
    if not book:
        return False
    book['available'] = True
    delete_record(record_id)
  
    return True

def search_book(book_id):
    book_id = validate_id(book_id)
    if not book_id:
        return False
    return get_book(book_id)
    

def list_books():
    return get_all_books()
   

def list_borrow_records(member_id):
    member_id = validate_id(member_id)
    if not member_id:
        return False
    return get_borrow_records(member_id)

