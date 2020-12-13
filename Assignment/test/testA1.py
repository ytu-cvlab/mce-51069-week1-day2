import sys
sys.path.append("..")

import nbimporter
import Assignment1 as a1
import unittest
from Assignment1 import Calculator as Cal


class TestNotebook(unittest.TestCase):

    def test_calculator(self):
        self.assertEqual(a1.calculator(3, 3, 'add'), 6)
        self.assertEqual(a1.calculator(3, 3, 'subtract'), 0)
        self.assertEqual(a1.calculator(3, 3, 'multiply'), 9)
        self.assertEqual(a1.calculator(3, 3, 'divide'), 1)
        self.assertEqual(a1.calculator(2, 6, 'add'), 8)
        self.assertEqual(a1.calculator(2, 6, 'subtract'), -4)
        self.assertEqual(a1.calculator(2, 6, 'multiply'), 12)
        self.assertEqual(a1.calculator(2, 6, 'divide'), 1/3)
        self.assertEqual(a1.calculator(-3, 4, 'add'), 1)
        self.assertEqual(a1.calculator(-3, 4, 'subtract'), -7)
        self.assertEqual(a1.calculator(-3, 4, 'multiply'), -12)
        self.assertEqual(a1.calculator(-3, 4, 'divide'), -0.75)
        
    def test_triangle_area(self):
        self.assertEqual(a1.triangle_area(3, 4), 6)
        self.assertEqual(a1.triangle_area(3.5, 4), 7.0)
        self.assertEqual(a1.triangle_area(5, 12), 30)
        self.assertEqual(a1.triangle_area(8, 15), 60)

    def test_mean_square_error(self):
        self.assertEqual(a1.mean_square_error(3, 4), 0.5)
        self.assertEqual(a1.mean_square_error(3.5, 4), 0.125)
        self.assertEqual(a1.mean_square_error(-3.5, -3.5), 0)
        self.assertEqual(a1.mean_square_error(3.5, -3.5), 24.5)

    def test_fizzbuzz(self):
        self.assertEqual(a1.fizzbuzz(5), ['1', '2', 'Fizz', '4', 'Buzz'])
        self.assertEqual(a1.fizzbuzz(17), ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz", "16", "17"])
        
    def test_class(self):
        cal = Cal(2, 5)
        cal1 = Cal(-4, 2)
        cal2 = Cal(0.5, 2)
        
        self.assertEqual(cal.add(), 7)
        self.assertEqual(cal.subtract(), -3)
        self.assertEqual(cal.multiply(), 10)
        self.assertEqual(cal.divide(), 0.4)
        self.assertEqual(cal1.add(), -2)
        self.assertEqual(cal1.subtract(), -6)
        self.assertEqual(cal1.multiply(), -8)
        self.assertEqual(cal1.divide(), -2)
        self.assertEqual(cal2.add(), 2.5)
        self.assertEqual(cal2.subtract(), -1.5)
        self.assertEqual(cal2.multiply(), 1)
        self.assertEqual(cal2.divide(), 0.25)

        
if __name__ == '__main__':
    main = TestNotebook()

    # This executes the unit test/(itself)
    suite = unittest.TestLoader().loadTestsFromTestCase(TestNotebook)
    unittest.TextTestRunner(verbosity=4,stream=sys.stderr).run(suite)
