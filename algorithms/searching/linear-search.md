# Linear search

**Linear search** is the simplest way of searching for something inside a _collection_. It simply compares a value with every items inside a collection. It searches in a _linear direction_, until it finds the desired value.

```python
# linear search example in python

animals = ["dog", "cat", "cow", "goat", "sheep"]


def linear_search(array, value):
    for item in array:
        if item == value:
            return array.index(item) # return the index of the item
    return False # return False if item not found


print(linear_search(animals, "cow"))
```

> Output: 2

## Required steps for specific operation

### Best case

> It takes just `1` step if the item is the first item of the collection.

### Worst case

> It takes `n` steps to find the item, if the item is the last element of that collection.

