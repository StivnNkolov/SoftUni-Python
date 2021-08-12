from List03.extended_list import IntegerList

from unittest import TestCase, main


class TestIntegerList(TestCase):
    def setUp(self):
        self.integer_list = IntegerList(5, 6, 7)

    def test_integer_list_initialization(self):
        self.assertEqual([5, 6, 7], self.integer_list._IntegerList__data)

    def test_integer_list_initialization_with_non_integer_values(self):
        test_list = IntegerList(5, 6, 7.3)
        self.assertEqual([5, 6], test_list._IntegerList__data)

    def test_if_add_method_add_number_and_return_the_data(self):
        self.assertEqual([5, 6, 7], self.integer_list._IntegerList__data)
        result = self.integer_list.add(100)
        self.assertEqual([5, 6, 7, 100], result)

    def test_if_adding_non_integer_type_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.integer_list.add(5.5)

        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_remove_index_method_removes_the_value_and_returns_it(self):
        self.assertEqual([5, 6, 7], self.integer_list._IntegerList__data)

        result = self.integer_list.remove_index(0)
        self.assertEqual(5, result)
        self.assertEqual([6, 7], self.integer_list._IntegerList__data)

    def test_remove_index_with_invalid_index_raises(self):
        with self.assertRaises(IndexError) as ex:
            self.integer_list.remove_index(3)

        self.assertEqual("Index is out of range", str(ex.exception))

    def test_get_method_return_the_value_we_want(self):
        result = self.integer_list.get(0)

        self.assertEqual(5, result)

    def test_get_method_with_invalid_index_raises(self):
        with self.assertRaises(IndexError) as ex:
            self.integer_list.get(3)

        self.assertEqual("Index is out of range", str(ex.exception))

    def test_if_insert_method_inserts_the_value_on_te_desired_place(self):
        self.integer_list.insert(0, 100)
        self.assertEqual([100, 5, 6, 7], self.integer_list._IntegerList__data)

    def test_insert_method_with_invalid_index_raises(self):
        with self.assertRaises(IndexError) as ex:
            self.integer_list.insert(5, 100)

        self.assertEqual("Index is out of range", str(ex.exception))

    def test_insert_method_with_non_integer_value(self):
        with self.assertRaises(ValueError) as ex:
            self.integer_list.insert(0, 1.1)

        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_get_biggest_number_returns_the_biggest_number_in_the_list(self):
        result = self.integer_list.get_biggest()
        self.assertEqual(7, result)

    def test_get_index_returns_the_desired_value(self):
        result = self.integer_list.get_index(5)

        self.assertEqual(0, result)


if __name__ == '__main__':
    main()
