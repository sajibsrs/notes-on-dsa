# Big O notation
## Introduction
Big O notation is a fancy term to determine the efficiency of algorithms. It's an asymptotic notation to represent the time complexity. Time complexity is most commonly estimated by counting the number of elementary steps performed by any algorithm to finish execution. If an algorithm has N steps, the time complexity of that algorithm is O(N). __O(N) is also known as linear time algorithm__. Reading from an array is 1 step. So it has a efficiency of O(1).

> Any algorithm that has efficiency of O(1) is the fastest.

## Little in-depth
> Big O notation simply describes not the number of steps an algorithm has, but how the steps increases as the data change.

If an algorithm always takes 2 steps, even if the data increases. The efficiency is always O(1) not O(2). After a certain amount data O(1) algorithm is always efficient than O(N).

For 100 data, if an O(1) algorithm takes 10 steps and O(N) takes 5 steps. For a 1000 data, O(1) will take less steps, as it's always takes 10 steps for any amount of data. But the for O(N) the steps will always increase with the increment of data count.

> Big O notation generally refers to the worst case scenario, unless specified otherwise.

It describes exactly how inefficient an algorithm can get in a worst case scenario and helps to choose the better one.

## Big O and logarithm
An algorithm like binary search can't be described as O(1) or O(N), as it takes much less steps than it's data count, and it's definitely not O(1). The worst case scenario for a binary search algorithm is 7 steps for 100 elements.

In Big O terms, this situation described as having time complexity of O(log N). Pronounce as "Oh of log N".

An algorithm that increases one step each time the data is doubled is O(log N) in term of Big O.

> Logarithm is the inverse function to exponentiation.

Here is an example:

If 2 has a exponent 3 the result is 8.

2 <sup>3</sup> = 8

log is the opposite. If we have a value 8, what would be 2's exponent to get 8? The answer is 3. 

log <sub>2</sub> 8 = 3

As we are working with binary logarithm, the base is 2. The above statement means.

If we have an array of 8 items, the worst case scenario to find an item will be 3 ( `2 x 2 x 2 = 8` ) steps, as we had to multiply 2 to itself 3 times.

That is what O(log N) means.

## Summery
### Different Big O time complexities
1. O(1)
2. O(N)
3. O(log N)