

- Bubble Sort (Сортировка пузырьком)
- Selection Sort (Сортировка выбором)
- Insertion Sort (Сортировка вставками)
- Merge Sort (Сортировка слиянием)
- Quick Sort (Быстрая сортировка)
- Heap Sort (Сортировка кучей)
- Counting Sort (Сортировка подсчетом)
- Radix Sort (Поразрядная сортировка)


### Bubble Sort

![bubble sort Wiki visualisation](https://upload.wikimedia.org/wikipedia/commons/c/c8/Bubble-sort-example-300px.gif)

- Time complexity: **O(n^2)**
- Memory complexity: **O(1)**

[Bubble sort](https://en.wikipedia.org/wiki/Bubble_sort) (sinking sort), is a simple sorting algorithm that repeatedly steps through the input list element by element, comparing the current element with the one after it, swapping their values if needed. These passes through the list are repeated until no swaps have to be performed during a pass, meaning that the list has become fully sorted. The algorithm, which is a comparison sort, is named for the way the larger elements "bubble" up to the top of the list.

**Algorithm:**

1. Start from the first element (index 0) and compare it with the next element.
2. If the current element is greater than the next element, swap them.
3. Move to the next pair of elements and repeat the comparison and swapping process until you reach the end of the array.
4. After the first iteration, the largest element will be at the end of the array.
5. Repeat steps 1-4 for the remaining elements until the entire array is sorted.
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

### Quick Sort

- Time complexity: 
    - Worst-case: **O(n^2)**
    - Average: **O(n log n)**
- Memory complexity:
    - Worst-case: **O(log n)**
    - Average: **O(n)**

### Heap Sort

- Time complexity: **O(n log n)**
- Memory complexity: **O(1)**

### Counting Sort

- Time complexity: **O(n+k)** (k - non-negatives range)
- Memory complexity: **O(n+k)**

### Radix Sort

- Time complexity: **O(n * w)** (n - number of keys, w - key length)
- Memory complexity: **O(n + w)**