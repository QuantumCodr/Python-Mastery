# Program: Inventory Management Menu
# Author: David
# Date: 27/07/2026

from inventory_services import (
    add_product,
    update_product,
    search_product,
    delete_product,
    list_products
)

def show_menu():
    print()
    print("===== INVENTORY MANAGEMENT SYSTEM =====")
    print("1. Add product")
    print("2. Update product")
    print("3. Search product")
    print("4. Delete product")
    print("5. List products")
    print("6. Exit")
    print()

def add_product_menu():
    print()
    print("------Add Product------")
    name = input("Name: ")
    price = float(input("Price: "))
    quantity = int(input("Quantity: "))
    if add_product(name, price, quantity):
        print("\nProduct added successfully.")
    else:
        print("\nInvalid product information.")

def update_product_menu():
    print()
    print("-----Update Product-----")
    id = input("Product ID: ")
    name = input("Name: ")
    price = input("Price: ")
    quantity = input("Quantity: ")
    if update_product(id, name, price, quantity):
        print("\nProduct updated successfully.")
    else:
        print("\nUnable to update product.")

def search_product_menu():
    print()
    print("-----Search Student-----")
    id = input("Product ID: ")
    product = search_product(id)
    if product:
        print('\nProduct Found')
        print("--------------------")
        print(f"ID       :  {product['id']}")
        print(f"Name     :  {product['name']}")
        print(f"Price    :  {product['price']}")
        print(f"Quantity :  {product['quantity']}")
    else:
        print("\nProduct not found.")

def delete_product_menu():
    print()
    print("-----Delete Product-----")
    id = input("Product ID: ")
    if delete_product(id):
        print("\nProduct deleted successfully.")
    else:
        print("\nUnable to delete product.")

def list_products_menu():
    print()
    products = list_products()
    if products:
        print("ID     Name      Price   Quantity")
        print("----------------------------------")
        for product in products:
            print(f'{product["id"]}  |  {product["name"]}  |  {product["price"]}  |  {product["quantity"]}')
    else:
        print("\nNo products available.")