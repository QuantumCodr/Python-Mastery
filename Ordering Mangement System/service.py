from validator import validate_id, validate_quantity
from repository import (
    get_product, 
    get_customer, 
    next_order_id, 
    place_customer_order, 
    get_order,
    list_all_orders,
    cancel_customer_order
)

def place_order(customer_id, product_id, quantity):
    customer_id = validate_id(customer_id)
    product_id = validate_id(product_id)
    quantity = validate_quantity(quantity)
    if not customer_id or not product_id or not quantity:
        return False
    customer = get_customer(customer_id)
    product = get_product(product_id)
    if not customer or not product:
        return False
    if product['stock'] < quantity:
        return False
    order = {
        'id': next_order_id(),
        'customer_id': customer_id,
        'product_id': product_id,
        'quantity': quantity,
        'total':   product['price'] * quantity,
        'status': 'pending'
    }
    place_customer_order(order)
    return True

def search_order(order_id):
    order_id = validate_id(order_id)
    if not order_id:
        return False
    order = get_order(order_id)    
    if not order:
        return False
    return order

def list_orders():
    orders = list_all_orders()
    if not orders:
        return False
    return orders

def cancel_order(order_id):
    order_id = validate_id(order_id)
    if not order_id:
        return False
    order = get_order(order_id)
    if not order:
        return False
    cancel_customer_order(order_id)
    return True