# Big O and logarithm

An algorithm like binary search can't be described as O\(1\) or O\(N\), as it takes much less steps than it's data count, and it's definitely not O\(1\). The worst case scenario for a binary search algorithm is 7 steps for 100 elements.

In Big O terms, this situation described as having time complexity of O\(log N\). Pronounce as "Oh of log N".

An algorithm that increases one step each time the data is doubled is O\(log N\) in term of Big O.

> Logarithm is the inverse function to exponentiation.

Here is an example:

If 2 has a exponent 3 the result is 8.

23 = 8

log is the opposite. If we have a value 8, what would be 2's exponent to get 8? The answer is 3.

log2 8 = 3

As we are working with binary logarithm, the base is 2. The above statement means.

If we have an array of 8 items, the worst case scenario to find an item will be 3 \( `2 x 2 x 2 = 8` \) steps, as we had to multiply 2 to itself 3 times.

