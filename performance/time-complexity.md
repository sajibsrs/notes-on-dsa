# Time complexity
Big O notation simply describes not the number of steps an algorithm has, but how the steps increases as the data change ( __growth rate__ ). If an algorithm always takes 2 steps, even if the data increases. The efficiency is always O(1) not O(2). Because the steps are always constant. After a certain amount data count O(1) algorithm is always efficient than O(N), if not fast initially.

For 100 data, if an O(1) algorithm takes 10 steps and O(N) takes 5 steps. For a 1000 data, O(1) will take less steps, as it's always takes 10 steps for any amount of data. But the for O(N) the steps will always increase with the increment of data count.

> Big O notation generally refers to the worst case scenario, unless specified otherwise.

It describes exactly how inefficient an algorithm can get in a worst case scenario and helps to choose the better one.