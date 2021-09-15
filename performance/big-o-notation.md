# Big O notation
Big O notation is a mathematical family of notations to describe the efficiency of algorithms with the data growth. In programming it's an asymptotic notation to represent the time or space complexity. 

## Time complexity
Time complexity is most commonly estimated by counting the number of elementary steps performed by any algorithm to finish execution. If an algorithm has N steps, the time complexity of that algorithm is O(N). Reading from an array is 1 step. So it has a time complexity of O(1).

> Any algorithm that has efficiency of O(1) is considered the fastest.

[Read more about time complexity](efficiency/time-complexity.md)

## Space complexity
Space complexity refers to determining how much memory an algorithm consumes during its runtime. It becomes a crucial factor where memory is limited. If an algorithm has an array of N items and that creates another array of the same size for its execution, the space complexity of that algorithm would be O(N), as the algorithm uses the same amount of additional memory as its input array.

[Read more about space complexity](efficiency/space-complexity.md)

[Look here for complexities performance table](efficiency/references/complexities-table.md)

## Trade-offs between time and space complexity
> // TODO: add details
