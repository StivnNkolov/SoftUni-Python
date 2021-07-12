from MultilevelInheritance.vehicle import Vehicle


class Car(Vehicle):
    def __init__(self):
        super().__init__()

    def drive(self):
        return "driving..."

car = Car()
print(car.drive())
print(car.move())
