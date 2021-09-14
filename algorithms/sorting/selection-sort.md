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
> // TODO: add code explanation

## Efficiency of selection sort

> // TODO: add efficiency / time complexity