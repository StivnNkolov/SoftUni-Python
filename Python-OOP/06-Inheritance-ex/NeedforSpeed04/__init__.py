from NeedforSpeed04.vehicle import Vehicle
from NeedforSpeed04.family_car import FamilyCar

if __name__ == '__main__':



    vehicle = Vehicle(50, 150)
    print(Vehicle.DEFAULT_FUEL_CONSUMPTION)
    print(vehicle.fuel)
    print(vehicle.horse_power)
    print(vehicle.fuel_consumption)
    vehicle.drive(100)
    print(vehicle.fuel)
    family_car = FamilyCar(150, 150)
    family_car.drive(50)
    print(family_car.fuel)
    family_car.drive(50)
    print(family_car.fuel)
    print(family_car.__class__.__bases__[0].__name__)

