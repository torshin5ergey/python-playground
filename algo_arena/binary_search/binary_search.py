"""
binary_search.py -- Binary search for sorted list.

Written by Sergey Torshin @torshin5ergey
"""


from typing import List
import unittest


def iterative_binary_search(arr: List, value: int) -> bool:
    # Empty array check
    if not arr:
        return False
    
    # Left and right pointers
    l, r, = 0, len(arr)-1
    
    while l <= r:
        # Middle value index
        mid = (r + l) // 2
        
        if arr[mid] == value:
            return True
        
        # Relocate pointers
        elif arr[mid] < value:
            l = mid + 1
        else:
            r = mid - 1
            
    return False


class TestBinarySearch(unittest.TestCase):
    def test_element_found(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(iterative_binary_search(arr, 4), True)
        self.assertEqual(iterative_binary_search(arr, 1), True)
        self.assertEqual(iterative_binary_search(arr, 9), True)

    def test_element_not_found(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(iterative_binary_search(arr, 10), False)
        self.assertEqual(iterative_binary_search(arr, -1), False)
        self.assertEqual(iterative_binary_search(arr, 0), False)

    def test_empty_array(self):
        arr = []
        self.assertEqual(iterative_binary_search(arr, 1), False)

    def test_single_element_array(self):
        arr = [1]
        self.assertEqual(iterative_binary_search(arr, 1), True)
        self.assertEqual(iterative_binary_search(arr, 0), False)

    def test_large_array(self):
        arr = list(range(1000000))
        self.assertEqual(iterative_binary_search(arr, 999999), True)
        self.assertEqual(iterative_binary_search(arr, 500000), True)
        self.assertEqual(iterative_binary_search(arr, 0), True)
        
if __name__ == "__main__":
    unittest.main()