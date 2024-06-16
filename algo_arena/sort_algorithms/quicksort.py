'''
quicksort.py -- Quicksort algorithm.

Written by Sergey Torshin @torshin5ergey
'''


def rightmost_partition(nums: list[int], start: int, end: int) -> int:
    """Partition the list around a pivot element for quicksort.
    
    Parameters:
    nums (list) -- the list of elements to be partitioned
    start (int) -- the starting index of the sublist to partition
    end (int) -- the ending index of the sublist to partition
    
    Return:
    (int) -- the index of the pivot element after partition
    """
    pivot = nums[end]  # Rightmost element pivot
    i = start -1  # Elements on the left are less than pivot

    for j in range(start, end):
        if nums[j] <= pivot:
            i += 1
            nums[j], nums[i] = nums[i], nums[j]
    nums[i+1], nums[end] = nums[end], nums[i+1]
    return i + 1


def quicksort(nums: list[int], start=0, end=None) -> None:
    """Quicksort a list in-place.
    
    Parameters:
    nums (list) -- the list of elements to be sorted.
    start (int, optional) -- the starting index of the sublist to be sorted (default is 0)
    end (int, optional) -- the ending index of the sublist to be sorted (default is None, which will be set to the last index of the list)
    """
    if end is None:  # For end default value (last element)
        end = len(nums)-1
    # Empty array
    if not nums:
        return

    if start < end:
        pi = rightmost_partition(nums, start, end)
        quicksort(nums, start, pi - 1)
        quicksort(nums, pi+1, end)
