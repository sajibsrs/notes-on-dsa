# Array
The `array` is one of the most basic data structure. The `array` is simply a list of __data elements__. In __python__ an array of animals would look like this:

```python
animals = ["dog", "cat", "cow", "goat", "sheep"]
```
## Size
The `size` of an array determined by how many items the array holds. In our case the length of __animals__ array is __5__.

## Index
The `index` of an _array item_ is, it's position in the array expressed in number. Array index starts with the number `0`. So, the position of the first emelemnt/item of the array is `0`.

> Last item index in an array is always ( `n - 1` ). Where the size of array is `n` _( n represents any integer )_. As array index starts with `0`.

## Required steps for specific operation on an array

### Reading
> #### Required step = 1. Item in any position

### Searching
> #### Required steps best = 1, when it's the first item

> #### Required steps worst = n, when it's the last item

### Insertion
> #### Required steps best = 1, when it's the last item

> #### Required steps worst = n + 1, when it's the first item

### Deletetion
> #### Required steps best = 1, when it's the last item

> #### Required steps worst = n, when it's the first item