import unittest
from classwork import Pokemon


class Test_Pokemon(unittest.TestCase):
    def test_bulba(self):
        actual = str(Pokemon("Bulbasaur", "grass"))
        expected = "Bulbasaur/grass"
        self.assertEqual(actual, expected)
