# Program: Library Management Database Module
# Author: QuantumCodr
# Date: 30/07/2026

books = [
    {
        "id": 1,
        "title": "Python Basics",
        "author": "David",
        "available": True
    },
    {
        "id": 2,
        "title": "Database Design",
        "author": "Sarah",
        "available": True
    },
    {
        "id": 3,
        "title": "Computer Networks",
        "author": "John",
        "available": True
    }
]


members = [
    {
        "id": 1,
        "name": "David"
    },
    {
        "id": 2,
        "name": "Sarah"
    },
    {
        "id": 3,
        "name": "John"
    }
]


borrow_records = [
    {
        "id": 1,
        "member_id": 3,
        "member_name": "John",
        "book_id": 3,
        "book_title": "Computer Networks"
    }
]