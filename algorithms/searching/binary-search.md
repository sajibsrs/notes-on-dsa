# Binary search

Binary search is the search algorithm that eliminates half of possible items and works with the other half.

> To perform binary search the array must be sorted.

[//]: # (add an example)

```python
sorted_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def binary_search(array, value):
    lower_bound = 0
    upper_bound = len(array) - 1

    while lower_bound <= upper_bound:
        mid_point = math.floor((upper_bound + lower_bound) / 2)
        mid_point_val = array[mid_point]

        if value == mid_point_val:
            return mid_point
        elif value < mid_point_val:
            upper_bound = mid_point_val - 1
        elif value > mid_point_val:
            lower_bound = mid_point + 1

    return False


binary_search(sorted_array, 4)
```
> It took `3` steps to find value 4.

> For a array / list with `100` ordered items it would take `7` steps maximum to find a value.

## Required steps for specific operation

### Best case

> If the guess is just right, then only `1` step is needed. Which is rare scenario.

### Worst case
