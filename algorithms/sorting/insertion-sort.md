# Insertion sort
> // TODO: add intro

## How it works
> // TODO: add graphical explanation 

## Code example
```python
# insertion sort in python

def insertion_sort(array):
    for index in range(1, len(array)):
        # put current element in temp variable
        temp = array[index]
        # set position to previous index
        position = index - 1

        # when previous element is bigger than current element
        while position >= 0 and array[position] > temp:
            # move previous element to current element position
            array[position + 1] = array[position]
            # move position backward
            position -= 1
            # move current element value to previous element position
            array[position + 1] = temp
    return array


print(insertion_sort([10, 30, 15, 11, 22]))
```

## Efficiency of insertion sort
> // TODO: add efficiency / time complexity

## Efficiency comparison table:
| N elements | Steps in bubble sort | Steps in selection sort | Steps in insertion sort |
| :--------: | :------------------: | :---------------------: | :---------------------: |
|     5      |          20          |           14            |           10            |
|     10     |          90          |           45            |           45            |
|     20     |         380          |           209           |           190           |
|     30     |         870          |           464           |           435           |
|     40     |         1560         |           819           |           780           |
|     50     |         2450         |          1274           |          1225           |

Insertion sort also has an efficiency of N<sup>2</sup>.
