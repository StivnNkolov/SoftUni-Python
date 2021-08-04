from project.product import Product


class Drink(Product):
    _QUANTITY = 10

    def __init__(self, name):
        super().__init__(name, Drink._QUANTITY)



