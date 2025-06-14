import unittest
from simple_calculator import SimpleCalculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = SimpleCalculator()

    def test_addition(self):
        self.assertEqual(self.calc.add(0,5),5)
        self.assertEqual(self.calc.add(-2,-5),-7)
        self.assertEqual(self.calc.add(2,-5),-3)

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(0,5),-5)
        self.assertEqual(self.calc.subtract(-2,-5),3)
        self.assertEqual(self.calc.subtract(2,-5),7)

    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(0,5),0)
        self.assertEqual(self.calc.multiply(-2,-5),10)
        self.assertEqual(self.calc.multiply(2,-5),-10)

    def test_division(self):
        self.assertEqual(self.calc.divide(0,5),0)
        self.assertEqual(self.calc.divide(-2,-5),0.4)
        self.assertEqual(self.calc.divide(2,0),None)



if __name__ == "__main__":
    unittest.main()