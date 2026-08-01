# Program: Inventory Management Validator Module
# Author: David
# Date: 27/01/2026

def validate_id(id):
    try:
        id = int(id)
    except ValueError:
        return None
    if id <= 0:
        return None
    return id

def validate_product_name(name):
    name = name.strip()
    if not name:
        return None
    return name.title()

def validate_price(price):
    if not isinstance(price, float):
        return None
    if price < 0:
        return None
    return price

def validate_quantity(qty):
    try:
        qty = int(qty)
    except ValueError:
        return None
    if qty <= 0:
        return None
    return qty
