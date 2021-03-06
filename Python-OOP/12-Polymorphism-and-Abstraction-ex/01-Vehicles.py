from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass


class Car(Vehicle):
    air_condition_consumption = 0.9

    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance):
        liters_needed_for_the_distance = (self.fuel_consumption + Car.air_condition_consumption) * distance
        if liters_needed_for_the_distance <= self.fuel_quantity:
            self.fuel_quantity -= liters_needed_for_the_distance

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    air_condition_consumption = 1.6

    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance):
        liters_needed_for_the_distance = (self.fuel_consumption + Truck.air_condition_consumption) * distance
        if liters_needed_for_the_distance <= self.fuel_quantity:
            self.fuel_quantity -= liters_needed_for_the_distance

    def refuel(self, fuel):
        self.fuel_quantity += fuel * 0.95


car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)

truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)
