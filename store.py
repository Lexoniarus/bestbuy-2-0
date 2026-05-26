"""Store model for the Best Buy console application."""

from products import Product


class Store:
    """Represent a store that manages and sells products."""

    def __init__(self, product_list):
        """Initialize a store with a list of products."""
        self.products = list(product_list)

    def add_product(self, product):
        """Add a product to the store."""
        if not isinstance(product, Product):
            raise TypeError("Only Product instances can be added")
        self.products.append(product)

    def remove_product(self, product):
        """Remove a product from the store."""
        self.products.remove(product)

    def get_total_quantity(self):
        """Return the total quantity of all products in the store."""
        return sum(product.get_quantity() for product in self.products)

    def get_all_products(self):
        """Return all active products in the store."""
        return [
            product
            for product in self.products
            if product.is_active()
        ]

    def order(self, list_of_items):
        """Process an order and return the total purchase price."""
        total_price = 0

        for product, quantity in list_of_items:
            try:
                total_price += product.buy(quantity)
            except Exception:
                print("Error while making order!")

        return total_price
