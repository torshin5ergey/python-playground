# Iterative Binary Search Algorythm

A simple and efficient iterative binary search algorithm.

## Description

[Binary search](https://en.wikipedia.org/wiki/Binary_search_algorithm) is a classic algorithm used to efficiently **find a target value in a sorted list**. It works by repeatedly dividing the search interval in **half**. If the target value is equal to the middle element of the interval, the search is successful. Otherwise, the algorithm continues to search in the appropriate half of the list until the target value is found or the interval is empty.

## Algorithm

1. **Initialization**. Start with the left pointer `l` at the beginning of the list and the right pointer `r` at the end of the list.
2. **Iteration**. Calculate the middle index `mid` as the average of `l` and `r` while `l` is less than or equal to `r`:
    - If the middle element `arr[mid]` is equal to the target value `value`, return `True`.
    - If `arr[mid]` is less than value, move the left pointer `l` to `mid + 1`.
    - If `arr[mid]` is greater than value, move the right pointer `r` to `mid - 1`.
3. **Completion**. If the loop exits without finding the value, return `False`.

The binary search algorithm has a time complexity of **O(log n)**.

### Variations

- **Iterative Binary Search**. The standard form, using a while loop.
- **Recursive Binary Search**. An alternative form using recursion.
- **Finding the First or Last Occurrence**. Modified versions to find the first or last occurrence of a value in a list with duplicates.

## Usage

Binary search is commonly used in scenarios where efficient lookups in sorted data are required, such as:
- Database searching
- Real-time search systems
- Algorithmic problem solving

## How to run

1. Clone this repository
```bash
git clone https://github.com/torshin5ergey/python-playground.git
```
2. Go to this project directory
```bash
cd python-playground/algo_arena/binary_search
```
3. Run unit tests file
```bash
python -m unittest test_rabin_karp.py
```
This will run the unit tests and display the results.
4. Or use it in your project.
```python
from binary_search import iterative_binary_search
```

### Unit tests

**Test class**: `TestBinarySearch`

**Included tests:**
- `test_element_found`: True for existing elements.
- `test_element_not_found`: False for non-existing elements.
- `test_empty_array`: False for an empty array.
- `test_single_element_array`: Correct work with a single-element array.
- `test_large_array`: Correct work with large arrays efficiently.

## Usage example

```python
from binary_search import iterative_binary_search

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
value = 4
print(iterative_binary_search(arr, value))  # Output: True
```

## Exercises

### Ex1. Iterative Binary Search 1

You have a sorted array of integers `arr` and a target integer `value`. Write the function `iterative_binary_search` to determine if the target integer `value` exists in the array `arr`. Return `True` if the target is found, otherwise return `False`.

## Author

Sergey Torshin [@torshin5ergey](https://github.com/torshin5ergey)