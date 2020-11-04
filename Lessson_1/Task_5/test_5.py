import unittest

from sub_array import Sub_array
"""
    Test to find sum of sub-array that is equal or lower k
"""

class test_4(unittest.TestCase):
    def setUp(self):
        self.otvet = Sub_array()
    
    def test_sum_1(self):
        self.assertEqual(self.otvet.max_length([1, 3, -1, -3, 5, 3, 6, 7],3), 16)
    
    def test_sum_2(self):
        self.assertEqual(self.otvet.max_length([7, 4, -15, -4, 9, 2, 6, -1],5), 9)
    


if __name__ == '__main__':
    unittest.main()


