class Product:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def decrease(self, quantity):
        if self.quantity - quantity >= 0:
            self.quantity -= quantity

    def increase(self, quantity):
        self.quantity += quantity

# test = Product("Kure", 65)
# print(test.quantity, test.name)
#
# test.decrease(90)
# print(test.quantity)
