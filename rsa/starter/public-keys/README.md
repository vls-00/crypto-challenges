### Analysis
This challenge is a simple RSA encryption of the number 12. We calculate `N` modulus which is `p * q` and then apply the RSA encryption as:
`12 ^ e mod N`. In RSA we work with very big numbers so modular exponentiation is a must.

### Solution
1. Calculate `N = p * q = 391`
2. `e = 65537` is given.
3. Use modular exponentiation to ecrypt number 12: `12 ^ 65537 mod 391`.

### Flag - 15 pts
`301`