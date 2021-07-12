from Zoo02.animal import Animal


class Reptile(Animal):
    def __init__(self, name):
        super().__init__(name)


# test_reptile = Reptile("Croco")
# print(test_reptile.name)