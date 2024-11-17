## Analysis
In this challenge, we explore why using only the same prime for `p` and `q`.From the RSA definition we know `n = p * q`, if we use the same prime that transforms into `p ^ 2`. 
* That means we can easily calculate the prime `p`:

`n = p * p`

`square_root(n) = p`

* Now that we know `p`, we can calculate `phi(n)`:

`phi(n) = p * (p-1)`

Note: when `p = q` then `phi(n)` is not `(p-1) * (p-1)` but rather `p * (p-1)`.

## Solution
1. Calculate `p = sqrt(n)` using gmpy2.
2. Calculate `phi(n) = p * (p-1)`.
3. Calculate the private key which is the modular multiplicative inverse `d = e^−1 mod phi(N)`.
4. Decrypt the ciphertext with the formula `ciphertext^d mod N`.