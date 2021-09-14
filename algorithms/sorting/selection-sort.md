# Selection sort
> // TODO: add intro

## How it works
> // TODO: add graphical explanation 

## Code example
```python
# selection sort example in python

def selection_sort(array):

    # visit all array elements
    for i in range(len(array)):

        # find the minimum element
        min_idx = i
        for j in range(i+1, len(array)):
            if array[min_idx] > array[j]:
                min_idx = j

        # swap the found minimum element with the first element
        array[i], array[min_idx] = array[min_idx], array[i]
    return array


array = [5, 4, 3, 2, 1]
print(selection_sort(array))

```
## Efficiency of selection sort

> // TODO: add efficiency / time complexity

Efficiency comparison table:

| N elements | Steps in bubble sort | Steps in selection sort |
| :--------: | :------------------: | :---------------------: |
|     5      |          20          |           14            |
|     10     |          90          |           45            |
|     20     |         380          |           209           |
|     30     |         870          |           464           |
|     40     |         1560         |           819           |
|     50     |         2450         |          1274           |

For N items bubble sort take almost N<sup>2</sup> and for selection sort it's N<sup>2</sup>/2.

> Big O notation ignores constants.

That's why efficiency of selection sort described as O(N<sup>2</sup>). It's the same as bubble sort.
