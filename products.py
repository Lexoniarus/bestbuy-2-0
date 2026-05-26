"""Product model for the Best Buy store application."""


class Product:
    """Represent a product in the store."""

    def __init__(self, name, price, quantity):
        """Initialize a product with name, price, quantity, and status."""
        if not name:
            raise ValueError("Product name cannot be empty")
        if price < 0:
            raise ValueError("Product price cannot be negative")
        if quantity < 0:
            raise ValueError("Product quantity cannot be negative")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self):
        """Return the current product quantity."""
        return self.quantity

    def set_quantity(self, quantity):
        """Set the product quantity and deactivate it when it reaches zero."""
        if quantity < 0:
            raise ValueError("Product quantity cannot be negative")

        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def is_active(self):
        """Return True when the product is active, otherwise False."""
        return self.active

    def activate(self):
        """Set the product status to active."""
        self.active = True

    def deactivate(self):
        """Set the product status to inactive."""
        self.active = False

    def show(self):
        """Return a readable product description."""
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def buy(self, quantity):
        """Buy a quantity, reduce stock, and return the total price."""
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero")
        if quantity > self.quantity:
            raise ValueError("Quantity cannot exceed current stock")
        if not self.is_active():
            raise ValueError("Inactive products cannot be bought")

        total_price = float(self.price * quantity)
        self.set_quantity(self.quantity - quantity)
        return total_price
