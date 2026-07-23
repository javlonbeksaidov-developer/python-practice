import pytest
from fixture import ShoppingCart


@pytest.fixture
def filled_cart():
    cart = ShoppingCart()
    cart.add_item("Olma", 5000)
    cart.add_item("Banan", 12000)
    cart.add_item("Sut", 8000)
    return cart


def test_get_total(filled_cart):
    assert filled_cart.get_total() == 25000


def test_item_count(filled_cart):
    assert len(filled_cart.show_item()) == 3


def test_add_new_item(filled_cart):
    filled_cart.add_item("non", 3000)
    assert filled_cart.get_total() == 28000
