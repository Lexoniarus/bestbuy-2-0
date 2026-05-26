"""Product models for the Best Buy store application."""


class Product:
    """Represent a stocked product that can be sold by the store."""

    def __init__(self, name, price, quantity):
        """Initialize a product with a name, unit price, and quantity."""
        if not name:
            raise ValueError("Product name cannot be empty")
        if price < 0:
            raise ValueError("Product price cannot be negative")
        if quantity < 0:
            raise ValueError("Product quantity cannot be negative")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = quantity > 0
        self.promotion = None

    def get_promotion(self):
        """Return the product promotion, if one is set."""
        return self.promotion

    def set_promotion(self, promotion):
        """Set the product promotion."""
        self.promotion = promotion

    def get_promotion_name(self):
        """Return the promotion name or None when no promotion is set."""
        if self.promotion is None:
            return None
        return self.promotion.get_name()

    def is_active(self):
        """Return whether the product is currently active."""
        return self.active

    def activate(self):
        """Mark the product as active."""
        self.active = True

    def deactivate(self):
        """Mark the product as inactive."""
        self.active = False

    def show(self):
        """Return a readable product description."""
        return f"{self.name}, Price: ${self.price}, Quantity: {self.quantity}"

    def get_price(self):
        """Return the product unit price."""
        return self.price

    def set_price(self, price):
        """Set the product unit price."""
        if price < 0:
            raise ValueError("Product price cannot be negative")
        self.price = price

    def get_quantity(self):
        """Return the current product quantity."""
        return self.quantity

    def set_quantity(self, quantity):
        """Set the current product quantity."""
        if quantity < 0:
            raise ValueError("Product quantity cannot be negative")

        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()
        else:
            self.activate()

    def buy(self, quantity):
        """Sell the requested quantity and return the total purchase price."""
        if quantity <= 0:
            raise ValueError("Invalid Quantity")
        if not self.is_active():
            raise ValueError("Product Inactive")
        if quantity > self.quantity:
            raise ValueError("Quantity larger than what exists")

        if self.promotion is None:
            total_price = self.price * quantity
        else:
            total_price = self.promotion.apply_promotion(self, quantity)

        self.set_quantity(self.quantity - quantity)
        return total_price


class NonStockedProduct(Product):
    """Represent a product that has unlimited stock."""

    def __init__(self, name, price):
        """Initialize a non-stocked product."""
        super().__init__(name, price, 0)
        self.activate()

    def show(self):
        """Return a readable non-stocked product description."""
        return (
            f"{self.name}, Price: ${self.price}, Quantity: Unlimited, "
            f"Promotion: {self.get_promotion_name()}"
        )

    def buy(self, quantity):
        """Return the purchase price without changing stock."""
        if quantity <= 0:
            raise ValueError("Invalid Quantity")
        if self.promotion is None:
            return self.price * quantity
        return self.promotion.apply_promotion(self, quantity)


class LimitedProduct(Product):
    """Represent a product with a maximum quantity per order."""

    def __init__(self, name, price, quantity, maximum):
        """Initialize a limited product."""
        super().__init__(name, price, quantity)
        if maximum <= 0:
            raise ValueError("Product maximum must be positive")
        self.maximum = maximum

    def show(self):
        """Return a readable limited product description."""
        return (
            f"{self.name}, Price: ${self.price}, Quantity: {self.quantity}, "
            f"Limited to {self.maximum} per order!, "
            f"Promotion: {self.get_promotion_name()}"
        )

    def buy(self, quantity):
        """Sell the product while enforcing the per-order limit."""
        if quantity > self.maximum:
            raise ValueError(
                f"Only {self.maximum} is allowed from this product!"
            )
        return super().buy(quantity)
