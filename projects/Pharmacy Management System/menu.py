# Program: Pharmacy Management Menu Module
# Author: QuantumCodr
# Date: 31/07/2026

from service import sell_medicine, restock_medicine, search_medicine, list_medicines, view_sales
def show_menu():
    print()
    print("===== PHARMACY MANAGEMENT SYSTEM =====")
    print('1. Sell Medicine')
    print("2. Restock Medicine")
    print("3. Search Medicine")
    print("4. List Medicines")
    print("5. View Sales")
    print("6. Exit")
    print()

def sell_medicine_menu():
    print()
    print("----- Sell Medicine -----")
    customer_id = input("Customer ID: ")
    medicine_id = input("Medicine ID: ")
    quantity = input("Quantity: ")
    sale = sell_medicine(customer_id, medicine_id, quantity)
    if not sale:
        print("\nFailed to sell medicine.")
    else:
        print("\nMedicine sold successfully.")

def restock_medicine_menu():
    print()
    print("----- Restock Medicine -----")
    medicine_id = input("Medicine ID: ")
    quantity = input("Quantity: ")
    restock = restock_medicine(medicine_id, quantity)
    if not restock:
        print("\nFail to restock medicine.")
    else:
        print("\nMedicine restocked successfully.")

def search_medicine_menu():
    print()
    print('\n----- Search Medicine ----')
    medicine_id = input('Medicine ID: ')
    search = search_medicine(medicine_id)
    if not search:
        print('\nNo product was found.')
    else:
        print("\n Found Product ")
        print("---------------------")
        print(f'\nID  : {search['id']}')
        print(f'Name  : {search['name']}')
        print(f'Price : {search['price']}')
        print(f'Stock : {search['stock']}')

def list_medicines_menu():
    print()
    print('----- List Medicines -----')
    medicines = list_medicines()
    if not medicines:
        print("\nNo product(s) was found.")
    else:
        print('\n  Medicine Found ')
        print("---------------------")        
        for medicine in medicines:
            print(f'ID    : {medicine['id']}')
            print(f'Name  : {medicine['name']}')
            print(f'Price : {medicine['price']}')
            print(f'Stock : {medicine['stock']}')
            print("---------------------") 

def view_sales_menu():
    print()
    print('----- View Sales -----')
    sales = view_sales()
    if not sales:
        print('\nNo sales found.')
    else:
        print('\n  Found Sales ')
        print("---------------------")     
        for sale in sales:
            print(f'ID: {sale['id']}')
            print(f"Customer_ID   : {sale['customer_id']}")
            print(f"Customer_name : {sale['customer_name']}")
            print(f"Medicine_ID   : {sale['medicine_id']}")
            print(f"Medicine_Name : {sale['medicine_name']}")
            print(f'Quantity      : {sale['quantity']}')
            print(f'Price         : {sale['price']}')
            print(f'Total         : {sale['total']}')
            print("---------------------") 