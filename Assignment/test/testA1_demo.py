import sys
sys.path.append("../")

import nbimporter
import Assignment1 as a1
import unittest


class TestNotebook(unittest.TestCase):
    def test_add(self):
        self.assertEqual(a1.add(3, 3), 6)
        self.assertEqual(a1.add(-1, 3), 2)
        self.assertEqual(a1.add(-3, -4), -7)

    def test_subtract(self):
        self.assertEqual(a1.subtract(3, 3), 0)
        self.assertEqual(a1.subtract(-1, 3), -4)
        self.assertEqual(a1.subtract(-3, -4), 1)

    def test_multiply(self):
        self.assertEqual(a1.multiply(3, 3), 9)
        self.assertEqual(a1.multiply(-1, 3), -3)
        self.assertEqual(a1.multiply(-3, -4), 12)

    def test_divide(self):
        self.assertEqual(a1.divide(3, 3), 1)
        self.assertEqual(a1.divide(-1, 3), -1/3)
        self.assertEqual(a1.divide(-3, -4), 3/4)

        
if __name__ == '__main__':
    main = TestNotebook()

    # This executes the unit test/(itself)
    suite = unittest.TestLoader().loadTestsFromTestCase(TestNotebook)
    unittest.TextTestRunner(verbosity=4,stream=sys.stderr).run(suite)
