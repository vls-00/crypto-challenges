## Analysis
For this challenge we need to find the element `d` so that `3*d ≡ 1 (mod 13)`. We notice that 13 is a prime and cannot divide 3 so we can apply fermat's little theorem.

* Resource for finding the inverse element: `https://www.geeksforgeeks.org/fermats-little-theorem/`

## Solution
From Fermat's little theorem we have:
* `3 ^ (13-1) ≡ 1 (mod 13)`
* `3 ^ (13-2) ≡ 3 ^ (-1) (mod 13)`

Thus, the inverse element is `3 ^ (13-2) = 3 ^ 11`

So `d = (3 ^ 11) % 13 = 9`
