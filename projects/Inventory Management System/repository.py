# Program: Inventory Management Repository Module
# Author: David
# Date: 27/01/2026

from database import products

def get_all_products():
    return products

def get_product(id):
    for product in products:
        if product["id"] == id:
            return product
    return None
    
def insert_product(product):
    products.append(product)

def remove_product(product):
    products.remove(product)

def next_product_id():
    if not products:
        return 1
    highest = max(product["id"] for product in products)
    return highest + 1
