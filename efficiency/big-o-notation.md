# Big O notation
Big O notation is a fancy term to determine the efficiency of algorithms.

If an algorithm has __N__ steps, the efficiency of that algorithm is __O(N)__.

> __O(N)__ is also known as _linear time_ algorithm.

Reading from an array is __1__ step. So it has a efficiency of __O(1)__. Any algorithm that has efficiency of __O(1)__ is the fastest.

> Big O notation simply describes not the number of steps an algorithm has, but how the steps increases as the data change.

If an algorithm always takes __2__ steps, even if the data increases. The efficiency is always __O(1)__ not __O(2)__.

After a certain amount data any __O(1)__ algorithm is efficient than __O(N)__. For __100__ data if an __O(1)__ algorithm takes __10__ steps and __O(N)__ takes __5__ steps. For a __1000__ data __O(1)__ will take less steps, as it's always takes __10__ steps and never changes. But the for __O(N)__ the step will always increase with the increment of data count.

## Efficiency of different algorythims