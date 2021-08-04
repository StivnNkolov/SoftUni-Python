from project.product import Product


class Food(Product):
    _QUANTITY = 15

    def __init__(self, name):
        super().__init__(name,Food._QUANTITY)

