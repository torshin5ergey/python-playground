'''
test_sort_algorithms.py -- Test for different sort algorithms

Wirtten by Sergey Torshin @torshin5ergey
'''

import unittest
from sort_algorithms import *

class TestSortAlgo(unittest.TestCase):
    def setUp(self) -> None:
        self.inputs = [
            [5, 3, 8, 1, 2, 7],
            [9, 1, 5, 3, 7, 2],
            [4, 6, 2, 8, 1, 3]
        ]
        self.outputs = [
            [1, 2, 3, 5, 7, 8],
            [1, 2, 3, 5, 7, 9],
            [1, 2, 3, 4, 6, 8]
        ]

    def test_bubble_sort(self):
        for unsorted, sorted in zip(self.inputs, self.outputs):
            bubble_sort(unsorted)
            self.assertEqual(unsorted, sorted)
    
    
if __name__ == "__main__":
    unittest.main()