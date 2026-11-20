"""Basic checks for the four calculator operations."""

import unittest

from calculator import add, subtract, multiply, divide


class CalculatorTests(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(8, 2), 10)
        self.assertEqual(add(-3, 1), -2)

    def test_subtract(self):
        self.assertEqual(subtract(8, 2), 6)
        self.assertEqual(subtract(2, 8), -6)

    def test_multiply(self):
        self.assertEqual(multiply(8, 2), 16)
        self.assertEqual(multiply(-3, 2), -6)

    def test_divide(self):
        self.assertEqual(divide(8, 2), 4)
        self.assertEqual(divide(5, 2), 2.5)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(5, 0)


if __name__ == "__main__":
    unittest.main()
