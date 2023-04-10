from product import Product

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, product):
        self.items.append(product)

    def remove_item(self, product):
        if product in self.items:
            self.items.remove(product)

    def get_total_price(self):
        total_price = 0
        for item in self.items:
            total_price += item.price
        return total_price
