'''
bubble_sort.py -- Bubble sort algorithm.

Written by Sergey Torshin @torshin5ergey
'''


def bubble_sort(nums: list[int]) -> None:
    """Bubble sort a list in-place.
    
    Parameter:
    nums (list) -- the list of elements to be sorted
    """
    n = len(nums)
    for i in range(n):
        for j in range(n-1-i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
