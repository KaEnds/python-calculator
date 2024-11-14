import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)
        self.assertEqual(self.calc.add(5, 7), 12)

    def test_substract(self):
        self.assertEqual(self.calc.subtract(9, 1), -8)
        self.assertEqual(self.calc.subtract(7, 2), -5)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(-5, 5), -25)

    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 2), 0)
        self.assertEqual(self.calc.divide(5, 20), 4)

    def test_modulo(self):
        self.assertEqual(self.calc.modulo(5, 3), 2)
        self.assertEqual(self.calc.modulo(10, 4), 2)


    

    # Add the following test methods to the TestCalculator class:

if __name__ == '__main__':
    unittest.main()