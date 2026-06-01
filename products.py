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
        self.promotion = None

    def get_promotion(self):
        """Return the assigned promotion, if there is one."""
        return self.promotion

    def set_promotion(self, promotion):
        """Assign a promotion to this product."""
        self.promotion = promotion

    def get_quantity(self):
        """Return the current product quantity."""
        return self.quantity

    def get_promotion_name(self):
        """Return the promotion name or None when no promotion is set."""
        if self.promotion:
            return self.promotion.name
        return "None"

    def set_quantity(self, quantity):
        """Set the product quantity and deactivate it when it reaches zero."""
        if quantity < 0:
            raise ValueError("Product quantity cannot be negative")

        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()
        else:
            self.activate()

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
        return (
            f"{self.name}, Price: ${self.price}, Quantity: {self.quantity}, "
            f"Promotion: {self.get_promotion_name()}"
        )

    def buy(self, quantity):
        """Buy a quantity, reduce stock, and return the total price."""
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero")
        if quantity > self.quantity:
            raise ValueError("Quantity cannot exceed current stock")
        if not self.is_active():
            raise ValueError("Inactive products cannot be bought")

        self.set_quantity(self.quantity - quantity)
        if self.promotion:
            return self.promotion.apply_promotion(self, quantity)

        total_price = float(self.price * quantity)
        return total_price


class NonStockedProduct(Product):
    """Represent a product with unlimited stock."""

    def __init__(self, name, price):
        """Initialize a non-stocked product."""
        super().__init__(name, price, quantity=0)
        self.activate()

    def set_quantity(self, quantity):
        """Keep non-stocked products at quantity zero."""
        self.quantity = 0
        self.activate()

    def show(self):
        """Return a readable non-stocked product description."""
        return (
            f"{self.name}, Price: ${self.price}, Quantity: Unlimited, "
            f"Promotion: {self.get_promotion_name()}"
        )

    def buy(self, quantity):
        """Buy a non-stocked product without changing stock."""
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero")
        if not self.is_active():
            raise ValueError("Inactive products cannot be bought")

        if self.promotion:
            return self.promotion.apply_promotion(self, quantity)
        return float(self.price * quantity)


class LimitedProduct(Product):
    """Represent a product with a maximum quantity per order."""

    def __init__(self, name, price, quantity, maximum=1):
        """Initialize a limited product."""
        super().__init__(name, price, quantity)
        if maximum <= 0:
            raise ValueError("Maximum must be greater than zero")
        self.maximum = maximum

    def show(self):
        """Return a readable limited product description."""
        return (
            f"{self.name}, Price: ${self.price}, Limited to {self.maximum} "
            f"per order!, Promotion: {self.get_promotion_name()}"
        )

    def buy(self, quantity):
        """Buy a product only when it is within the order limit."""
        if quantity > self.maximum:
            raise ValueError(
                f"Only {self.maximum} is allowed from this product!"
            )
        return super().buy(quantity)
