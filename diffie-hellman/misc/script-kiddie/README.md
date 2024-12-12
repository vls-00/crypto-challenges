## Analysis & Solution
This challenge's key point is a typo mistake in `generate_public_int` and `generate_shared_secret` functions.

The symbol `^` is used to power numbers but this symbol XORs in python.

So, the server in order to calculate the public key B will xor `b` and `g`. We also know that `b < p` from the source code so not even the modulo operation is applied after the XOR.

## Solution
1. Calculate `b`: `b = B XOR g`
2. Copy the faulty `generate_shared_secret` from the source code and use it to calculate the shared secret.
3. Copy the AES decrypt function from the server and decrypt the flag.
