import unittest

from Max_Min import Min_Max

test_file = "numbers.txt"
#find_maximum_and_minimum("numbers.txt")
class test_3(unittest.TestCase):
    def setUp(self):
        self.chisla = Min_Max()

    def test_max_min(self):
        """
        Test to find right min and max integers
        """
        self.assertEqual(self.chisla.find_maximum_and_minimum(test_file), (45,90))


if __name__ == '__main__':
    unittest.main()
