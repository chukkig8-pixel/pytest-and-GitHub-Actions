"""Inventory management application logic."""


class Inventory:
    def __init__(self):
        self.products = {}

    def add_product(self, product_id, name, price, quantity):
        if product_id in self.products:
            raise ValueError("Product already exists")

        if not name.strip():
            raise ValueError("Product name cannot be empty")

        if price < 0:
            raise ValueError("Price cannot be negative")

        if quantity < 0:
            raise ValueError("Quantity cannot be negative")

        self.products[product_id] = {
            "name": name,
            "price": price,
            "quantity": quantity,
        }

    def get_product(self, product_id):
        if product_id not in self.products:
            raise KeyError("Product not found")

        return self.products[product_id]

    def update_stock(self, product_id, quantity):
        product = self.get_product(product_id)

        if quantity < 0:
            raise ValueError("Quantity cannot be negative")

        product["quantity"] += quantity

    def sell_product(self, product_id, quantity):
        product = self.get_product(product_id)

        if quantity <= 0:
            raise ValueError("Sale quantity must be positive")

        if product["quantity"] < quantity:
            raise ValueError("Insufficient stock")

        product["quantity"] -= quantity

    def remove_product(self, product_id):
        if product_id not in self.products:
            raise KeyError("Product not found")

        del self.products[product_id]

    def total_inventory_value(self):
        return sum(
            product["price"] * product["quantity"]
            for product in self.products.values()
        )
