# Set
A set is very similar to array, except set doesn't allow _duplicate values_. There are different types of sets, but we'll discuss about _array-based_ set.

For this example we'll be using the same example from the array. This array is a set as all of it's items are unique.

```python
animals = ["dog", "cat", "cow", "goat", "sheep"]
```

## Required steps for specific operation on a set.

### Reading
> #### Required step = 1. Item in any position.

## Searching
> #### Required steps `best` = 1, when it's the first item.
> #### Required steps `worst` = n, when it's the last item.

### Insertion
> #### Required steps `best` = n + 1, when it's the last item.
> #### Required steps `worst` = 2n + 1, when it's the first item.

### Deletetion
> #### Required steps `best` = 1, when it's the last item.
> #### Required steps `worst` = n, when it's the first item.