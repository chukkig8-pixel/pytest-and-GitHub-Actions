import pytest

from inventory import Inventory


@pytest.fixture
def inventory():
    store = Inventory()
    store.add_product("P101", "Laptop", 50000, 10)
    store.add_product("P102", "Mouse", 500, 20)
    return store


def test_add_product(inventory):
    inventory.add_product("P103", "Keyboard", 1000, 5)
    product = inventory.get_product("P103")

    assert product["name"] == "Keyboard"
    assert product["price"] == 1000
    assert product["quantity"] == 5


def test_duplicate_product(inventory):
    with pytest.raises(ValueError, match="already exists"):
        inventory.add_product("P101", "Laptop", 50000, 10)


def test_empty_product_name(inventory):
    with pytest.raises(ValueError, match="cannot be empty"):
        inventory.add_product("P103", "   ", 100, 5)


@pytest.mark.parametrize("price", [-1, -100])
def test_negative_price(inventory, price):
    with pytest.raises(ValueError, match="negative"):
        inventory.add_product("P103", "Keyboard", price, 5)


@pytest.mark.parametrize("quantity", [-1, -10])
def test_negative_initial_quantity(inventory, quantity):
    with pytest.raises(ValueError, match="negative"):
        inventory.add_product("P103", "Keyboard", 1000, quantity)


def test_get_product(inventory):
    product = inventory.get_product("P101")

    assert product["name"] == "Laptop"
    assert product["quantity"] == 10


def test_product_not_found(inventory):
    with pytest.raises(KeyError, match="Product not found"):
        inventory.get_product("P999")


def test_update_stock(inventory):
    inventory.update_stock("P101", 5)
    assert inventory.get_product("P101")["quantity"] == 15


def test_negative_stock_update(inventory):
    with pytest.raises(ValueError, match="negative"):
        inventory.update_stock("P101", -5)


def test_sell_product(inventory):
    inventory.sell_product("P101", 3)
    assert inventory.get_product("P101")["quantity"] == 7


def test_sell_all_available_stock(inventory):
    inventory.sell_product("P101", 10)
    assert inventory.get_product("P101")["quantity"] == 0


def test_sell_more_than_available(inventory):
    with pytest.raises(ValueError, match="Insufficient stock"):
        inventory.sell_product("P101", 11)

    # Failed sales must not change the stock.
    assert inventory.get_product("P101")["quantity"] == 10


@pytest.mark.parametrize("quantity", [0, -1])
def test_invalid_sale_quantity(inventory, quantity):
    with pytest.raises(ValueError, match="must be positive"):
        inventory.sell_product("P101", quantity)


def test_remove_product(inventory):
    inventory.remove_product("P102")
    assert "P102" not in inventory.products


def test_remove_missing_product(inventory):
    with pytest.raises(KeyError, match="Product not found"):
        inventory.remove_product("P999")


def test_total_inventory_value(inventory):
    # (50000 * 10) + (500 * 20)
    assert inventory.total_inventory_value() == 510000
