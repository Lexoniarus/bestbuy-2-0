"""Tests for the Product class."""

import pytest

from products import Product


def test_create_normal_product():
    """Test that creating a normal product works."""
    product = Product("MacBook Air M2", price=1450, quantity=100)

    assert product.name == "MacBook Air M2"
    assert product.price == 1450
    assert product.get_quantity() == 100
    assert product.is_active() is True


def test_create_product_with_invalid_details_raises_exception():
    """Test that invalid product details raise an exception."""
    with pytest.raises(ValueError):
        Product("", price=1450, quantity=100)

    with pytest.raises(ValueError):
        Product("MacBook Air M2", price=-10, quantity=100)


def test_product_becomes_inactive_when_quantity_reaches_zero():
    """Test that a product becomes inactive when its quantity reaches zero."""
    product = Product("MacBook Air M2", price=1450, quantity=100)

    product.set_quantity(0)

    assert product.get_quantity() == 0
    assert product.is_active() is False


def test_buy_product_changes_quantity_and_returns_total_price():
    """Test that buying a product changes quantity and returns total price."""
    product = Product("MacBook Air M2", price=1450, quantity=100)

    total_price = product.buy(2)

    assert total_price == 2900
    assert product.get_quantity() == 98


def test_buy_more_than_available_raises_exception():
    """Test that buying more than available raises an exception."""
    product = Product("MacBook Air M2", price=1450, quantity=100)

    with pytest.raises(ValueError):
        product.buy(101)
