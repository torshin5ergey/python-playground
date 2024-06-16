
# Sorting Algorithms

Various implementations of sorting algorithms. 

## Description

Each sorting algorithm is implemented in a separate module, and the directory includes a test script.

Algorithms:
- [Bubble Sort](#bubble-sort)
- [Quicksort](#quicksort)

### Bubble Sort

![bubble sort Wiki visualisation](https://upload.wikimedia.org/wikipedia/commons/c/c8/Bubble-sort-example-300px.gif)

- Time complexity: **O(n^2)**
- Memory complexity: **O(1)**

[Bubble sort](https://en.wikipedia.org/wiki/Bubble_sort) (sinking sort), is a simple sorting algorithm that repeatedly steps through the input `nums` array element by element, comparing the current element with the one after it, swapping their values if needed. These passes through the `nums` array are repeated until no swaps have to be performed during a pass, meaning that the array has become fully sorted. The algorithm, which is a comparison sort, is named for the way the larger elements "bubble" up to the top of the list.

**Algorithm:**

1. Start from the first element (index 0) and compare it with the next element.
2. If the current element is greater than the next element, swap them.
3. Move to the next pair of elements and repeat the comparison and swapping process until you reach the end of the array.
4. After the first iteration, the largest element will be at the end of the `nums` array.
5. Repeat steps 1-4 for the remaining elements until the entire `nums` array is sorted.
6. Continue this process until no more swaps are needed, indicating that the array is fully sorted.

### Selection Sort

- Time complexity: **O(n^2)**
- Memory complexity: **O(1)**

### Insertion Sort

- Time complexity: **O(n^2)**
- Memory complexity: **O(1)**

### Merge Sort

- Time complexity: **O(n log n)**
- Memory complexity: **O(n)**

### Quicksort
![quicksort Wiki visualisation](https://upload.wikimedia.org/wikipedia/commons/6/6a/Sorting_quicksort_anim.gif)

- Time complexity: 
    - Worst-case: **O(n^2)**
    - Average: **O(n log n)**
- Memory complexity:
    - Worst-case: **O(log n)**
    - Average: **O(n)**

[Quick sort](https://en.wikipedia.org/wiki/Quicksort) is a highly efficient sorting algorithm. It is based on partitioning arrays into smaller sub-arrays. It works by selecting a `pivot` element from the array and partitioning the other elements into two sub-arrays according to whether they are less than or greater than the `pivot`. The sub-arrays are then recursively sorted. The **key operation in quicksort is the partitioning process**, which rearranges the elements around the `pivot`. The efficiency of quick sort heavily depends on the choice of the `pivot` element.

**Algorithm:**
1. *Choose a `pivot` element from the `nums` array.
2. Reorder the `nums` array so that all elements with values less than the `pivot` come before it, and all elements with values greater than the `pivot` come after it (equal values can go either way). After this partitioning, the `pivot` is in its final position.
3. Recursively apply these steps to the sub-array of elements with smaller values and separately to the sub-array of elements with greater values.
4. Continue partitioning and sorting the sub-arrays recursively until the entire `nums` array is sorted.

***Pivot selection methods:**
- **Leftmost of rightmost (first or last) element**. Inefficient performance on already sorted or nearly sorted arrays.
- **Random element**. Choosing a random element from the array as the pivot helps in reducing the chance of worst-case scenarios. This approach is simple to implement and effective in practice.

### Heap Sort

- Time complexity: **O(n log n)**
- Memory complexity: **O(1)**

### Counting Sort

- Time complexity: **O(n+k)** (k - non-negatives range)
- Memory complexity: **O(n+k)**

### Radix Sort

- Time complexity: **O(n * w)** (n - number of keys, w - key length)
- Memory complexity: **O(n + w)**

## Contents

- `bubble_sort.py` - Bubble sort algorithm.
- `quicksort.py` - Quicksiort algorithm.
- `test_sort_algorithms.py` - Test for different sort algorithms.

## Author

Torshin Sergey [@torshin5ergey](https://github.com/torshin5ergey)