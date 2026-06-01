"""Store model for the Best Buy store application."""

import products


class Store:
    """Represent a store that manages and sells products."""

    def __init__(self, product_list):
        """Initialize a store with a list of products."""
        self.products = list(product_list)

    def __contains__(self, product):
        """Return whether a product is in the store."""
        return product in self.products

    def __add__(self, other):
        """Combine two stores into a new Store instance."""
        if not isinstance(other, Store):
            return NotImplemented
        return Store(self.products + other.products)

    def add_product(self, product):
        """Add a product to the store."""
        if not isinstance(product, products.Product):
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

    def order(self, shopping_list):
        """Process an order and return the total purchase price."""
        total_price = 0

        for product, quantity in shopping_list:
            total_price += product.buy(int(quantity))

        return total_price
