"""Console entry point for the Best Buy store application."""

from products import Product
from store import Store


MENU = {
    1: "List all products in store",
    2: "Show total amount in store",
    3: "Make an order",
    4: "Quit",
}


def print_product_list(products):
    """Print a numbered list of products."""
    for index, product in enumerate(products, start=1):
        print(f"{index}. {product.show()}")


def print_menu():
    """Print the store menu."""
    print()
    print("   Store Menu")
    print("   ----------")
    for number, text in MENU.items():
        print(f"{number}. {text}")


def show_menu_and_get_choice():
    """Show the menu until the user enters a valid choice."""
    while True:
        print_menu()
        try:
            choice = int(input("Please choose a number: "))
        except ValueError:
            print("Error with your choice! Try again!")
            continue

        if choice in MENU:
            return choice

        print("Error with your choice! Try again!")


def show_products(best_buy):
    """Print all active products in the store."""
    products = best_buy.get_all_products()
    print_product_list(products)


def show_total_amount(best_buy):
    """Print the total quantity of items in the store."""
    print(f"Total of {best_buy.get_total_quantity()} items in store")


def make_order(best_buy):
    """Collect products from the user and process an order."""
    products = best_buy.get_all_products()
    order_list = []

    print()
    print("When you want to finish order, enter empty text.")
    print_product_list(products)

    while True:
        product_choice = input("Which product # do you want? ")
        if product_choice == "":
            break

        quantity_choice = input("What amount do you want? ")

        try:
            product_index = int(product_choice) - 1
            quantity = int(quantity_choice)
            if product_index < 0 or product_index >= len(products):
                raise ValueError
            order_list.append((products[product_index], quantity))
        except ValueError:
            print("Error adding product!")
        else:
            print("Product added to list!")

    total_price = best_buy.order(order_list)
    print("********")
    print(f"Order made! Total payment: ${total_price}")


def start(best_buy):
    """Run the main store menu loop."""
    while True:
        choice = show_menu_and_get_choice()

        if choice == 1:
            show_products(best_buy)
        elif choice == 2:
            show_total_amount(best_buy)
        elif choice == 3:
            make_order(best_buy)
        elif choice == 4:
            break


def main():
    """Create the store and start the console application."""
    product_list = [
        Product("MacBook Air M2", price=1450, quantity=100),
        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        Product("Google Pixel 7", price=500, quantity=250),
    ]
    best_buy = Store(product_list)
    start(best_buy)


if __name__ == "__main__":
    main()
