## Analysis
JACK11 hash algorithm has an output of 11 bits so 2 ^ 11 = 2048 different hash values in total.

This may seem like a birthday paradox problem at first but the challenge is giving us a specific value for Jack's hash that we need to match,
therefore the birthday paradox equation is not suitable here.

## Solution
1. The propability of not finding a collision using 1 secret is `2047/2048`.
2. The propability of not finding a collision using n secrets is `(2047/2048)^n`.
3. Therefore the propability of finding one collision in n secrets is `1 - (2047/2048)^n`.
4. We want the propability to be bigger than 0.5 so we solve `1 - (2047/2048)^n = 0.5`:
    
    =>`(2047/2048)^n = 0.5`

    =>`n = log(0.5, (2047/2048)`

    =>`n = approx. 1419.21`

    =>`ceiling(1419.21)`
