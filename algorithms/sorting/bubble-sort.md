# Bubble sort

> // TODO: add intro

## How it works

> // TODO: add graphical explanation

## Code example

```python
# bubble sort in python

def bubble_sort(array):
    # set upper bound
    upper_bound = len(array) - 1
    done = False

    while not done:
        done = True

        for i in range(upper_bound):
            # compare current index with its next index
            if array[i] > array[i+1]:
                # if current index is greater swap position
                array[i], array[i+1] = array[i+1], array[i]
                # we are not done yet
                done = False
        # after one iteration the largest item will go to the
        # last position and we'll exclude it every time
        upper_bound -= 1

    return array


print(bubble_sort([10, 30, 15, 11, 22]))
```

## Efficiency of bubble sort

With a array of 5 elements we'd need a total of:

4 + 3 + 2 + 1 = 10 comparisons

For N number of elements that is:

\(N - 1\) + \(N - 2\) + \(N - 3\) ... + 1 comparisons

As we got the comparisons count for the bubble sort. Let's look at the number of swaps we need. For the worst case scenario we'd need swaps for every comparison, when the array component orders are exactly the opposite of a sorted array. For the worst case, swaps count would be 10 for an array with 5 elements. That is same as the swap count. So, the total steps for bubble sort would be:

10 comparisons + 10 swaps = 20 steps for a 5 items array

## Efficiency comparison table:

| Data count N | Number of steps | N2 |
| :---: | :---: | :---: |
| 5 | 20 | 25 |
| 10 | 90 | 100 |
| 20 | 380 | 400 |
| 30 | 870 | 900 |
| 40 | 1560 | 1600 |
| 50 | 2450 | 2500 |

For N amount of data step increment is approximately N2. So, we can say the bubble sort algorithm has efficiency or time complexity of N2.

