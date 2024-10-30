### Analysis
In this challenge we have to calculate the private key `d` of an RSA encryption. The private key `d` is the modular multiplicative inverse of `e mod phi(N)`.

 We have already seen multiplicative inverses in mathematics chapter of the general section (see general/mathematics/extended-gcd). The Extended Euclidean Algorithm is what we need to find multiplicative inverses. Specifically:

`d = e^-1 mod phi(N) =>`

`d X e = 1 mod phi(N) =>`

`d * e + phi(N) * k = 1`

This is where Extended Euclidean Algorithm shines.

### Solution
1. We apply the extended euclidean algorithm python script for `e` and `phi(n)`
2. This will result in two numbers which are `d`, `k` (see analysis).
3. `k` has no use to us for now, we only need `d` which is the private key.