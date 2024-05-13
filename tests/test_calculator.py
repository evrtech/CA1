import unittest
from my_calculator.calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        self.assertEqual(self.calculator.add(3, 4), 7)

    def test_multi(self):
        self.assertEqual(self.calculator.multi(3, 4), 12)
