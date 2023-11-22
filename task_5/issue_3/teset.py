import unittest
from main import fit_transform


class TestFitTransform(unittest.TestCase):
    def test_four_cities(self):
        cities = [
            "Moscow",
            "New York",
            "Moscow",
            "London",
        ]
        exp_transformed_cities = [
            ("Moscow", [0, 0, 1]),
            ("New York", [0, 1, 0]),
            ("Moscow", [0, 0, 1]),
            ("London", [1, 0, 0]),
        ]
        self.assertEqual(fit_transform(cities), exp_transformed_cities)

    def test_empty_list(self):
        self.assertEqual(fit_transform([]), [])

    def test_sum(self):
        cities = [
            "Moscow",
            "New York",
            "Moscow",
            "London",
        ]
        sums_list = [sum(i[1]) for i in fit_transform(cities)]
        self.assertNotIn(0, sums_list)

    def test_length(self):
        cities = [
            "Moscow",
            "New York",
            "Moscow",
            "London",
        ]
        lengths_list = [
            len(i[1]) == len(set(cities)) for i in fit_transform(cities)
        ]
        print(lengths_list)
        self.assertTrue(all(lengths_list))

    def test_exception(self):
        self.assertRaises(TypeError, fit_transform, 1)
