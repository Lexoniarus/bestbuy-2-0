"""Promotion models for the Best Buy store application."""

from abc import ABC, abstractmethod


class Promotion(ABC):
    """Base class for product promotions."""

    def __init__(self, name):
        """Initialize a promotion with a display name."""
        if not name:
            raise ValueError("Promotion name cannot be empty")
        self.name = name

    @abstractmethod
    def apply_promotion(self, product, quantity):
        """Return the promoted price for buying a product quantity."""


class SecondHalfPrice(Promotion):
    """Every second item is sold for half price."""

    def apply_promotion(self, product, quantity):
        """Apply a half-price discount to every second item."""
        regular_price = product.price * quantity
        discount = (quantity // 2) * product.price * 0.5
        return regular_price - discount


class ThirdOneFree(Promotion):
    """Every third item is free."""

    def apply_promotion(self, product, quantity):
        """Apply a free-item discount to every third item."""
        regular_price = product.price * quantity
        discount = (quantity // 3) * product.price
        return regular_price - discount


class PercentDiscount(Promotion):
    """Apply a percentage discount to the whole purchase."""

    def __init__(self, name, percent):
        """Initialize a percentage discount promotion."""
        if percent < 0 or percent > 100:
            raise ValueError("Discount percent must be between 0 and 100")
        super().__init__(name)
        self.percent = percent

    def apply_promotion(self, product, quantity):
        """Apply the configured percentage discount."""
        regular_price = product.price * quantity
        return regular_price * (1 - self.percent / 100)
