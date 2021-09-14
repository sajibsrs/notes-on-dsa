# Big O notation
Big O notation is a mathematical family of notations to describe the efficiency of algorithms with the data growth. In programming it's an asymptotic notation to represent the time or space complexity. 

## Time complexity
Time complexity is most commonly estimated by counting the number of elementary steps performed by any algorithm to finish execution. If an algorithm has N steps, the time complexity of that algorithm is O(N). Reading from an array is 1 step. So it has a time complexity of O(1).

> Any algorithm that has efficiency of O(1) is the fastest.

[Read more about time complexity](/efficiency/time-complexity.md)

## Space complexity
Space complexity refers to determine how much memory an algorithm consumes during its runtime. It becomes a crucial factor where memory is limited. If an algorithm has an array of N items and that creates another array of the same size for its execution, the space complexity of that algorithm would be O(N), as the algorithm uses the same amount of additional memory as its input array.

[Read more about space complexity](/efficiency/space-complexity.md)

## Different complexities
|  Pos  |      Function       |     Name     |  Pos  |     Function     |    name     |
| :---: | :-----------------: | :----------: | :---: | :--------------: | :---------: |
|   1   |        O(1)         |   Constant   |   7   | O(N<sup>2</sup>) |  Quadratic  |
|   2   |       O(logN)       | Logarithmic  |   8   | O(N<sup>3</sup>) |    Cubic    |
|   3   | O(log<sup>2</sup>N) |  Log-square  |   9   | O(N<sup>4</sup>) |   Quartic   |
|   4   |     O(&Sqrt;N)      |    Root-N    |  10   | O(2<sup>N</sup>) | Exponential |
|   5   |        O(N)         |    Linear    |  11   | O(e<sup>N</sup>) | Exponential |
|   6   |      O(NlogN)       | Linearithmic |  12   |      O(N!)       | N-Factorial |