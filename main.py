"""Command line interface for the Best Buy store application."""

import products
import store


def setup_store():
    """Create and return the default Best Buy store."""
    product_list = [
        products.Product("MacBook Air M2", price=1450, quantity=100),
        products.Product(
            "Bose QuietComfort Earbuds",
            price=250,
            quantity=500,
        ),
        products.Product("Google Pixel 7", price=500, quantity=250),
    ]
    return store.Store(product_list)


def show_menu():
    """Show the main menu."""
    print()
    print("Store Menu")
    print("----------")
    print("1. List all products in store")
    print("2. Show total amount in store")
    print("3. Make an order")
    print("4. Quit")


def list_products(store_instance):
    """Print all active products with item numbers."""
    product_list = store_instance.get_all_products()

    if not product_list:
        print("No active products available.")
        return

    for index, product in enumerate(product_list, start=1):
        print(f"{index}. {product.show()}")


def show_total_quantity(store_instance):
    """Print the total product quantity in the store."""
    total_quantity = store_instance.get_total_quantity()
    print(f"Total quantity in store: {total_quantity}")


def get_selected_quantity(product, shopping_list):
    """Return the quantity already selected for a product."""
    return sum(
        quantity
        for selected_product, quantity in shopping_list
        if selected_product is product
    )


def make_order(store_instance):
    """Collect order items from the user and place the order."""
    product_list = store_instance.get_all_products()

    if not product_list:
        print("No active products available.")
        return

    shopping_list = []
    list_products(store_instance)

    while True:
        product_number = input("Product number: ")
        if product_number == "":
            break

        try:
            product_index = int(product_number) - 1
            if product_index < 0 or product_index >= len(product_list):
                print("Invalid product number.")
                continue
        except ValueError:
            print("Please enter a valid product number.")
            continue

        amount = input("Amount: ")

        try:
            quantity = int(amount)
        except ValueError:
            print("Please enter a valid amount.")
            continue

        if quantity <= 0:
            print("Amount must be greater than zero.")
            continue

        selected_product = product_list[product_index]
        selected_quantity = get_selected_quantity(
            selected_product,
            shopping_list,
        )
        available_quantity = selected_product.get_quantity() - selected_quantity

        if quantity > available_quantity:
            print("Not enough products in stock.")
            continue

        shopping_list.append((selected_product, quantity))
        print("Product added to order.")

    if not shopping_list:
        print("No products selected. Order cancelled.")
        return

    try:
        total_price = store_instance.order(shopping_list)
    except Exception as error:
        print(f"Order failed: {error}")
        return

    print(f"Order made! Total payment: ${total_price}")


def start(store_instance):
    """Run the main menu until the user quits."""
    while True:
        show_menu()
        choice = input("Please choose a number: ")

        if choice == "1":
            list_products(store_instance)
        elif choice == "2":
            show_total_quantity(store_instance)
        elif choice == "3":
            make_order(store_instance)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid menu choice.")


def main():
    """Set up the store and start the command line interface."""
    store_instance = setup_store()
    start(store_instance)


if __name__ == "__main__":
    main()
