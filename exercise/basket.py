class Basket:
    item_prices = {
        "apple": 1.0,
        "banana": 0.5,
        "grapes": 0.75,
    }

    def __init__(self):
        self.items = {}

    def add_item(self, item, quantity):
        if item not in Basket.item_prices:
            return False
        current_quantity = self.items.get(item, 0)
        self.items[item] = current_quantity + quantity
        return True

    def remove_item(self, item, quantity):
        if item not in self.items:
            return False

        current_quanity = self.items.get(item, 0)
        if current_quanity - quantity <= 0:
            del self.items[item]
            return True

        self.items[item] -= quantity
        return True

    def calculate_price(self):
        total = 0.0
        for item, quantity in self.items.items():
            price_per_item = Basket.item_prices[item]
            total += price_per_item * quantity
        return total

    def clear_basket(self):
        self.items = {}
        return True