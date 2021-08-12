from mammal.project.mammal import Mammal

import unittest


class TestMammal(unittest.TestCase):

    def setUp(self):
        self.m = Mammal("Test", "cat", "meow")

    def test_initialization(self):
        test_mammal = Mammal("Test", "cat", "meow")
        self.assertEqual("Test", self.m.name)
        self.assertEqual("cat", self.m.type)
        self.assertEqual("meow", self.m.sound)

        self.assertEqual("animals", test_mammal._Mammal__kingdom)

    def test_make_sound(self):
        result = self.m.make_sound()
        self.assertEqual("Test makes meow", result)

    def test_get_kingdom(self):
        self.assertEqual("animals", self.m.get_kingdom())

    def test_info(self):
        result = self.m.info()
        self.assertEqual("Test is of type cat", result)




