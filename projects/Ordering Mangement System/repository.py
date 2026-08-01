from database import customers, products, orders


def get_customer(customer_id):
    for customer in customers:
        if customer['id'] == customer_id:
            return customer
    return None

def get_product(product_id):
    for product in products:
        if product['id'] == product_id:
            return product
    return None

def get_order(order_id):
    for order in orders:
        if order['id'] == order_id:
            return order
    return None

def place_customer_order(order):
        for product in products:
            if product['id'] == order['product_id']:
                product['stock'] -= order['quantity']
                break
        customer = get_customer(order['customer_id'])
        order['customer_name'] = customer['name']
        product = get_product(order['product_id'])
        order['product_name'] = product['name']
        orders.append(order)
        return True       

def list_all_orders():
    if not orders:
        return None
    return orders

def cancel_customer_order(order_id):
    for order in orders:
        if order['id'] == order_id:
            for product in products:
                if product['id'] == order['product_id']:
                    product['stock'] += order['quantity']
                    break
            orders.remove(order)
            break

def next_order_id():
    if not orders:
        return 1
    highest = max(order['id'] for order in orders)
    return highest + 1

next_order_id()