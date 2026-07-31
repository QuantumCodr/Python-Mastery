# Program: Library Management Vallidate Module
# Author: QuantumCodr
# Date: 30/07/2026

def validate_id(id):
    try:
        id = int(id)
    except ValueError:
        return None
    if id >= 0:
        return id

def validate_name(name):
    if not isinstance(name, str):
        return None
    name = name.strip()
    if not name:
        return None
    return name.title()
    