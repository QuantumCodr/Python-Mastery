from menu import (
    show_menu,
    place_order_menu,
    search_order_menu,
    list_orders_menu,
    cancel_order_menu
)

def main():
    while True:
        show_menu()
        option = input("Option: ")
        if option == '1':
            place_order_menu()
        elif option == '2':
            search_order_menu()
        elif option == '3':
            list_orders_menu()
        elif option == '4':
            cancel_order_menu()
        elif option == '5':
            print("Goodbye.")
            break
        else:
            print("Invalid Option.")

if __name__ == "__main__":
    main()