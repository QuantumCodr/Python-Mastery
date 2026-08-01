from service import (
    place_order,
    search_order,
    list_orders,
    cancel_order
)

def show_menu():
    print()
    print("===== ORDER MANAGEMENT SYSTEM =====")
    print("1. Place order")
    print("2. Search order")
    print("3. List orders")
    print("4. Cancel order")
    print("5. Exit")
    print()

def place_order_menu():
    print()
    print("----- Place Order -----")
    customer_id = input("Customer ID: ")
    product_id = input("Product ID: ")
    quantity = input("Quantity: ")
    order = place_order(customer_id, product_id, quantity)
    if order:
        print("\nOrder placed successfully.")
    else:
        print("\nUnable to place order.")

def search_order_menu():
    print()
    print("----- Search Order -----")
    order_id = input("Order ID: ") 
    order = search_order(order_id)
    if order:
        print('\n     Order Found    ')
        print('=======================')
        print(f"ID    :  {order['id']}")
        print(f"Customer  :  {order['customer_name']}")
        print(f"Product   :  {order['product_name']}")
        print(f"Quantity  :  {order['quantity']}")
        print(f"Total     :  SLL{order['total']}")
    else:
        print("No product returned")

def list_orders_menu():
    print()
    print("----- List Orders -----")
    orders = list_orders()
    if orders:
        print('\n      Order(s) Found       ')
        print('==========================')
        for order in orders:
            print(f"ID    :  {order['id']}")
            print(f"Customer  :  {order['customer_name']}")
            print(f"Product   :  {order['product_name']}")
            print(f"Quantity  :  {order['quantity']}")
            print(f"Total     :  SLL{order['total']}")
            print("----------------------------")
    else:
        print("\nNo products returned")

def cancel_order_menu():
    print()
    print("----- Cancel Order -----")
    order_id = input("Order ID: ")
    order = cancel_order(order_id)
    if order:
        print('\nOrder canceled successfully.')
    else:
        print("\nOrder failed to cancel.")