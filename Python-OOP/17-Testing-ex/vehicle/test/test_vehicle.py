from vehicle.project.vehicle import Vehicle

from unittest import TestCase


class TestVehicle(TestCase):
    def setUp(self):
        self.v = Vehicle(100, 50)

    def test_initialization(self):
        fuel = 100
        hp = 50
        capacity = fuel
        fuel_consumption = 1.25
        self.assertEqual(fuel, self.v.fuel)
        self.assertEqual(hp, self.v.horse_power)
        self.assertEqual(capacity, self.v.capacity)
        self.assertEqual(fuel_consumption, self.v.fuel_consumption)

    def test_drive_with_enough_fuel(self):
        self.v.drive(3)
        self.assertEqual(96.25, self.v.fuel)

    def test_drive_not_enough_fuel_raises(self):
        with self.assertRaises(Exception) as ex:
            self.v.drive(100)

        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_refuel(self):
        self.v.fuel -= 20
        self.v.refuel(10)

        self.assertEqual(90, self.v.fuel)

    def test_refuel_with_more_than_capacity_raises(self):
        with self.assertRaises(Exception) as ex:
            self.v.refuel(10)
        self.assertEqual("Too much fuel", str(ex.exception))

    def test_str_method(self):
        result = str(self.v)

        self.assertEqual(f"The vehicle has {self.v.horse_power} horse power"
                         f" with {self.v.fuel} fuel left"
                         f" and {self.v.fuel_consumption} fuel consumption", result)
