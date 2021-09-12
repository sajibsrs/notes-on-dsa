# Big O notation
## Introduction
Big O notation is a fancy term to determine the efficiency of algorithms.

If an algorithm has __N__ steps, the efficiency of that algorithm is __O(N)__. __O(N)__ is also known as _linear time_ algorithm.

Reading from an array is __1__ step. So it has a efficiency of __O(1)__.

> Any algorithm that has efficiency of __O(1)__ is the fastest.

## Comparison
> Big O notation simply describes not the number of steps an algorithm has, but how the steps increases as the data change.

If an algorithm always takes __2__ steps, even if the data increases. The efficiency is always __O(1)__ not __O(2)__.

After a certain amount data __O(1)__ algorithm is always efficient than __O(N)__.

For __100__ data, if an __O(1)__ algorithm takes __10__ steps and __O(N)__ takes __5__ steps. For a __1000__ data, __O(1)__ will take less steps, as it's always takes __10__ steps for any amount of data. But the for __O(N)__ the steps will always increase with the increment of data count.

> Big O notation generally refers to the worst case scenario, unless specified otherwise.

It describes exactly how inefficient an algorithm can get in a worst case scenario and helps to choose the right algorithm.

## Time complexity
An algorithm like __binary search__ can't be described as __O(1)__, neither __O(N)__, as it takes much less steps than it's data count.

> The worst case scenario for a __binary search__ algorithm is __7__ steps for __100__ elements.

