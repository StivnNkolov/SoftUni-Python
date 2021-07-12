from Shop05.product import Product


class Drink(Product):
    def __init__(self, name):
        super().__init__(name, quantity=10)



