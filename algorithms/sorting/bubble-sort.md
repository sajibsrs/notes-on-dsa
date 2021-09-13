# Bubble sort
[//]: # (add description)

```python
# bubble sort example in python

def bubble_sort(array):
    upper_bound = len(array) - 1
    done = False

    while not done:
        done = True

        for i in range(upper_bound):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                done = False
        upper_bound -= 1

    return array


print(bubble_sort([10, 30, 15, 11, 22]))
```
## Efficiency of bubble sort

With a array of 5 elements we'd need a total of:

4 + 3 + 2 + 1 = 10 comparisons

For N number of elements that is:

(N - 1) + (N - 2) + (N - 3) ... + 1 comparisons

As we got the comparisons count for the bubble sort. Let's look at the number of swaps we need. For the worst case scenario we'd need swaps for every comparison, when the array component orders are exactly the opposite of a sorted array.

For the worst case, swaps count would be 10 for an array with 5 elements. That is same as the swap count. So, the total steps for bubble sort would be:

10 comparisons + 10 swaps = 20 steps for a 5 items array.

If we make a growth table with different data count for bubble sort, then the results would be:

| Data count N | Number of steps | N<sup>2</sup> |
| ------------ | --------------- | ------------- |
| 5            | 20              | 25            |
| 10           | 90              | 100           |
| 20           | 380             | 400           |
| 30           | 870             | 900           |
| 40           | 1560            | 1600          |
| 50           | 2450            | 2500          |

As we can see from the growth table the growth of steps as number of data N increases. It's approximately by N<sup>2</sup> for N data.

So, we can say the bubble sort algorithm has efficiency or time complexity of N<sup>2</sup>.