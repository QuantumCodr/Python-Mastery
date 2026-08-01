# Program: Pharmacy Management Validator Module
# Author: QuantumCodr
# Date: 31/07/2026

from database import medicines, customers, sales

def get_medicine(medicine_id):
    for medicine in medicines:
        if medicine['id'] == medicine_id:
            return medicine
    return None

def get_customer(customer_id):
    for customer in customers:
        if customer['id'] == customer_id:
            return customer
    return None

def get_sale(sale_id):
    for sale in sales:
        if sale['id'] == sale_id:
            return sale
    return None

def insert_sale(record):
    sales.append(record)

def reduce_medicine_stock(medicine_id, quantity):
    for medicine in medicines:
        if medicine['id'] == medicine_id:
            medicine['stock'] -= quantity
            return True
    return False

def increase_medicine_stock(medicine_id, quantity):
    for medicine in medicines:
        if medicine['id'] == medicine_id:
            medicine['stock'] += quantity
            return True
    return False

def next_sale_id():
    if not sales:
        return 1
    highest = max(sale['id'] for sale in sales)
    return highest + 1 

def get_all_medicines():
    return medicines

def get_all_sales():
    return sales
