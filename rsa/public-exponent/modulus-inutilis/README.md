## Analysis
In this challenge, from the provided script, we notice that the exponent used for encryption is 3.

This can cause various problems and one of them is that `plaintext ^ e` is smaller than the modulus.

Why is this important? `ciphertext = plaintext ^ e mod n` but if `n` is big enough, then `ciphertext = plaintext ^ e`.
That means if we calculate the e-th root of the ciphertext we can get the plaintext.

That is exactly what happens in this challenge and it can be verified by taking a fake flag of `b"XXXXXXXXXXXXXXXXXXXXXXX"`, and calculate `flag ^ e `.

The resulting number is much smaller than the modulus `n` given by the challenge.

## Solution
Use `root()` function from `sympy` to calculate the e-th root of the ciphertext. We now have the plaintext.
