## Analysis & Solution
In this challenge we are provided a poor chosen elliptic curve that we have to break.

Why is the elliptic curve poor chosen? Because the order of the curve (number of points over a finite field) is not a prime number. We can calculate the order using the following code in sage:

```python
E = EllipticCurve(GF(p), [a, b])
assert is_prime(E.order())
```

So now that we know the order of the curve is not prime, we can use the Pohlig-Hellman algorithm to solve the discrete logarithm for Bob's public key and find his `n`.

Source: https://wstein.org/edu/2010/414/projects/novotney.pdf