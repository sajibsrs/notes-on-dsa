# Big O notation
## Introduction
Big O notation is a fancy term to determine the efficiency of algorithms. If an algorithm has N steps, the efficiency of that algorithm is O(N). O(N) is also known as _linear time_ algorithm. Reading from an array is 1 step. So it has a efficiency of O(1).

> Any algorithm that has efficiency of O(1) is the fastest.

## Comparison
> Big O notation simply describes not the number of steps an algorithm has, but how the steps increases as the data change.

If an algorithm always takes 2 steps, even if the data increases. The efficiency is always O(1) not O(2). After a certain amount data O(1) algorithm is always efficient than O(N).

For 100 data, if an O(1) algorithm takes 10 steps and O(N) takes 5 steps. For a 1000 data, O(1) will take less steps, as it's always takes 10 steps for any amount of data. But the for O(N) the steps will always increase with the increment of data count.

> Big O notation generally refers to the worst case scenario, unless specified otherwise.

It describes exactly how inefficient an algorithm can get in a worst case scenario and helps to choose the right one.

## Time complexity
An algorithm like binary search can't be described as O(1), neither O(N), as it takes much less steps than it's data count.

> The worst case scenario for a binary search algorithm is 7 steps for 100 elements.

