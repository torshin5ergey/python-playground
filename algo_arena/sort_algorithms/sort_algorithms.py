'''
sort_algorithms.py -- Different sort algorithms

Written by Sergey Torshin @torshin5ergey
'''

def bubble_sort(nums: list) -> None:
    # Sort inplace
    n = len(nums)
    
    for i in range(n):
        for j in range(n-1-i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
