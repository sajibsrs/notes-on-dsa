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