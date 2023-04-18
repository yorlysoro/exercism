import unittest

from lasagna import (
    EXPECTED_BAKE_TIME,
    preparation_time_in_minutes,
    elapsed_time_in_minutes,
    bake_time_remaining
)


class MyTestCase(unittest.TestCase):
    def test_back_time_const(self):
        self.assertEqual(EXPECTED_BAKE_TIME, 40)

    def test_bake_time_remaining(self):
        expected = 10
        minutes = 30
        self.assertEqual(bake_time_remaining(minutes), expected)

    def test_preparation_time_in_minutes(self):
        expected = 4
        number_of_layers = 2
        self.assertEqual(preparation_time_in_minutes(number_of_layers), expected)

    def test_elapsed_time_in_minutes(self):
        expected = 26
        number_of_layers = 3
        minutes = 20
        self.assertEqual(elapsed_time_in_minutes(number_of_layers, minutes), expected)


if __name__ == '__main__':
    unittest.main()
