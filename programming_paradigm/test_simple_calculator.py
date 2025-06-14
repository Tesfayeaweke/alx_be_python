import unittest
from simple_calculator import SimpleCalculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = SimpleCalculator()

    def test_add(self):
        self.assertEqual(self.calculator.add(0,5),5)
        self.assertEqual(self.calculator.add(-2,-5),-7)
        self.assertEqual(self.calculator.add(2,-5),-3)

    def test_subtract(self):
        self.assertEqual(self.calculator.subtract(0,5),-5)
        self.assertEqual(self.calculator.subtract(-2,-5),3)
        self.assertEqual(self.calculator.subtract(2,-5),7)

    def test_multiply(self):
        self.assertEqual(self.calculator.multiply(0,5),0)
        self.assertEqual(self.calculator.multiply(-2,-5),10)
        self.assertEqual(self.calculator.multiply(2,-5),-10)

    def test_divide(self):
        self.assertEqual(self.calculator.divide(0,5),0)
        self.assertEqual(self.calculator.divide(-2,-5),0.4)
        self.assertEqual(self.calculator.divide(2,0),None)



if __name__ == "__main__":
    unittest.main()