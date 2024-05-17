import unittest
from my_calculator.calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        self.assertEqual(self.calculator.add(3, 4), 7)

    def test_multi(self):
        self.assertEqual(self.calculator.multi(3, 4), 12)
    
    def test_divide(self):
        self.assertEqual(self.calculator.divide(8, 2), 4)
        with self.assertRaises(ValueError):
            self.calculator.divide(6, 0)
    
    def test_subtract(self):
        self.assertEqual(self.calculator.subtract(10, 5), 5)