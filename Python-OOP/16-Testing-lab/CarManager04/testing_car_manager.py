from CarManager04.car_manager import Car

from unittest import TestCase, main


class TestCar(TestCase):
    def setUp(self):
        self.car = Car("Test", "TT", 1.5, 100)

    def test_car_initialization(self):
        self.assertEqual("Test", self.car.make)
        self.assertEqual("TT", self.car.model)
        self.assertEqual(1.5, self.car.fuel_consumption)
        self.assertEqual(100, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

    def test_invalid_make_value_raises(self):
        with self.assertRaises(Exception) as ex:
            car = Car("", "TT", 1.5, 100)

        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_invalid_model_value_raises(self):
        with self.assertRaises(Exception) as ex:
            car = Car("Test", "", 1.5, 100)

        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_invalid_value_for_fuel_consumption_raises(self):
        with self.assertRaises(Exception) as ex:
            car = Car("Test", "TT", -1, 100)

        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_invalid_value_for_fuel_capacity_raises(self):
        with self.assertRaises(Exception) as ex:
            car = Car("Test", "TT", 1, 0)

        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_invalid_value_for_fuel_amount_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = -5

        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_refuel_method_add_the_fuel_to_the_fuel_amount(self):
        self.assertEqual(0, self.car.fuel_amount)
        self.car.refuel(100)
        self.assertEqual(100, self.car.fuel_amount)

    def test_refuel_method_with_invalid_value_for_fuel_raises(self):
        self.assertEqual(0, self.car.fuel_amount)
        with self.assertRaises(Exception) as ex:
            self.car.refuel(-5)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_refuel_method_when_fuel_amount_plus_added_fuel_is_bigger_then_fuel_capacity(self):
        self.assertEqual(0, self.car.fuel_amount)
        self.car.refuel(101)
        self.assertEqual(100, self.car.fuel_amount)

    def test_drive_method_with_enough_fuel_for_the_distance(self):
        self.assertEqual(0, self.car.fuel_amount)
        self.car.refuel(100)
        self.assertEqual(100, self.car.fuel_amount)

        self.car.drive(5)
        self.assertEqual(99.925, self.car.fuel_amount)

    def test_drive_function_when_we_dont_have_enough_fuel_for_the_distance(self):
        self.assertEqual(0, self.car.fuel_amount)
        with self.assertRaises(Exception) as ex:
            self.car.drive(5)

        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))


if __name__ == '__main__':
    main()
