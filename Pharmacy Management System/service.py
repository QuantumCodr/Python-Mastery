# Program: Pharmacy Management Service Module
# Author: QuantumCodr
# Date: 31/07/2026

from validator import validate_id, validate_quantity
from repository import (
    get_medicine,
    get_customer,
    get_all_medicines,
    get_all_sales,
    insert_sale,
    reduce_medicine_stock,
    increase_medicine_stock,
    next_sale_id
)

def sell_medicine(customer_id, medicine_id, quantity):
    customer_id = validate_id(customer_id)
    medicine_id = validate_id(medicine_id)
    quantity = validate_quantity(quantity)
    if not all([medicine_id, customer_id, quantity]):
        return False
    customer = get_customer(customer_id)
    medicine = get_medicine(medicine_id)
    if not customer or not medicine:
        return False
    if medicine['stock'] < quantity:
        return False
    sale_record = {
        'id': next_sale_id(),
        'customer_id': customer['id'],
        'customer_name': customer['name'],
        'medicine_id': medicine['id'],
        'medicine_name': medicine['name'],
        'quantity': quantity,
        'price': medicine['price'],
        'total': medicine['price'] * quantity
    }
    reduce_medicine_stock(medicine_id, quantity)
    insert_sale(sale_record)
    return True

def search_medicine(medicine_id):
    medicine_id = validate_id(medicine_id)
    if not medicine_id:
        return False
    medicine = get_medicine(medicine_id)
    if not medicine:
        return False
    return medicine

def restock_medicine(medicine_id, quantity):
    medicine_id = validate_id(medicine_id)
    quantity = validate_quantity(quantity)
    if not medicine_id or not quantity:
        return False
    restock = increase_medicine_stock(medicine_id, quantity)
    if not restock:
        return False
    return True

def list_medicines():
    medicines = get_all_medicines()
    if not medicines:
        return False
    return medicines

def view_sales():
    return get_all_sales()

    

print(sell_medicine(1, 4, 5))
print(list_medicines())
print(view_sales())