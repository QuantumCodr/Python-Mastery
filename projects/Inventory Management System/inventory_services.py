# Program: Student Management Service Module
# Author: David
# Date: 27/01/2026

from repository import get_all_products
from repository import get_product
from repository import insert_product
from repository import remove_product
from repository import next_product_id

from validator import validate_product_name
from validator import validate_id
from validator import validate_price
from validator import validate_quantity


def add_product(name, price, quantity):
    name = validate_product_name(name)
    price = validate_price(price)
    quantity = validate_quantity(quantity)
    if not name or not price or not quantity:
        return False
    product = {
        "id": next_product_id(),
        "name": name,
        "price": price,
        "quantity": quantity
    }
    insert_product(product)
    return True

def update_product(id, name, price, quantity):
    id = validate_id(id)
    name = validate_product_name(name)
    price = validate_price(price)
    quantity = validate_quantity(quantity)
    if not all([id, name, price, quantity]):
        return False
    product = get_product(id)
    if not product:
        return False
    product['id'] = id
    product['name'] = name
    product['price'] = price
    product['quantity'] = quantity
    return True

def search_product(id):
    id = validate_id(id)
    if not id:
        return None
    product = get_product(id)
    return product

def delete_product(id):
    id = validate_id(id)
    if not id:
        return False
    product = get_product(id)
    remove_product(product)
    return True

def list_products():
    return get_all_products()
