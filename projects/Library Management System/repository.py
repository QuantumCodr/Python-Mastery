# Program: Library Management Repository Module
# Author: QuantumCodr
# Date: 30/07/2026

from database import books, borrow_records, members

def get_member(id):
    for member in members:
        if member['id'] == id:
            return member
    return None
    

def get_book(id):
    for book in books:
        if book['id'] == id:
            return book
    return None

def get_record(id):
    for record in borrow_records:
        if record['id'] == id:
            return record

def next_record_id():
    if not borrow_records:
        return 1
    highest = max(record["id"] for record in borrow_records)
    return highest + 1

def insert_record(borrow_record):
    borrow_records.append(borrow_record)

def get_all_records():
    return borrow_records

def get_all_books():
    return books

def get_borrow_records(member_id):
    if not borrow_records:
        return None
    matches = []
    for record in borrow_records:
        if record['member_id'] == member_id:
            matches.append(record)
    return matches

def delete_record(record_id):
    for record in borrow_records:
        if record['id'] == record_id:
            borrow_records.remove(record)
            return True
    return False


    