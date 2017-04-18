import unittest
from odd_avg import *

class TestCountAverage(unittest.TestCase):
    def test_odd_average(self):
        average = CountAverage()
        self.assertEqual(average.odd_average([2, 3, 4, 5]), 4)

    def test_odd_average_emptylist(self):
        average = CountAverage()
        self.assertEqual(average.odd_average([]), "ZeroDivisionError, please do not enter empty list")

    def test_odd__average_one_even_element_in_list(self):
        average = CountAverage()
        self.assertEqual(average.odd_average([2]), "ZeroDivisionError, element is even in list")

    def test_odd__average_one_odd_element_in_list(self):
        average = CountAverage()
        self.assertEqual(average.odd_average([3]), 3)


if __name__ == '__main__':
    unittest.main()
