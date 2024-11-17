## Analysis
In this challenge, we explore why using only a single prime, `p`, for RSA encryption breaks the security. RSA encryption relies on the computational difficulty of factoring the product of two distinct primes. However, if we use a single prime then the RSA cryptosystem breaks down because anyone can easily calculate `phi`. 

`phi(n) = p - 1`

Note: we only have a single prime so `p = n`

## Solution
1. Calculate `phi(n) = p - 1`.
2. Calculate the private key which is the modular multiplicative inverse `d = e^−1 mod phi(N)`.
3. Decrypt the ciphertext with the formula `ciphertext^d mod N`.
