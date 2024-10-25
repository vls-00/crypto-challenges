### Analysis
In this challenge we are given all the required components in order to calculate a shared secret for bob. From the Diffie-Hellman algorithm definition all we have to do is take Alice's Public value `A` and calculate `A ^ b mod p`. This will result in the Diffie-Hellman secret. More information on why this works: https://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange

### Solution
1. Use the same function for modular exponentiation as in `computing-public-values` challenge.
2. Use `A` as base `b` as exponent and `p` as modulus. This is the Diffie-Hellman algorithm :)

