## Analysis
In this challenge the DH key exchange is happening over an additive group instead of the original multiplicative group.

Here is a quick glance at the algorithm over an additive group:
```
1. Alice picks private number a
2. Alice calculates: g * a mod p
3. Sends it to Bob
4. Alice receives Bob's B
5. Alice calculates: a * B mod p
6. Bob does the same
7. They now have the same shared secret
```

For this algorithm to be kind of safe, the modulo arithmetics must apply which means that:
1. `g * a > p => a > p / 2`
2. `g * b > p => b > p / 2`

The first thing I tried is to see if someone from Alice or Bob picked a small number so podulo `p` is not applied to the equation at all.

Indeed I found that Bob picked a small number so that `2 * b < p`, which means that `b = B / g = B / 2`. This can be verified because the secret I got from `b * A mod p` let me decrypt the encrypted message.

Note: Alice's private key was big enough.


