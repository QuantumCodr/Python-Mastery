# Program: Pharmacy Management Validator Module
# Author: QuantumCodr
# Date: 31/07/2026

def validate_id(id):
    try:
        id = int(id)
    except ValueError:
        return None
    if id <= 0:
        return False
    return id

def validate_quantity(quantity):
    try:
        quantity = int(quantity)
    except ValueError:
        return None
    if quantity <= 0:
        return False
    return quantity