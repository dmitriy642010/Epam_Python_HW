import unittest

from four import Poisk
"""
    Test to find sum of 4 int that could give zero in sum
"""

class test_4(unittest.TestCase):
    def setUp(self):
        self.otvet = Poisk()
    
    def test_sum(self):
        self.assertEqual(self.otvet.check_sum_of_four([200,150], [-150,300], [200,-300], [150,-200]), 1)



if __name__ == '__main__':
    unittest.main()
