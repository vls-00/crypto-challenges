## Analysis & Solution
In this challenge we are given P and we need to find Q such that P + Q = O. 

For elliptic curves, in order to satisfy this equation, Q is the inverse of P.

For `P = (x, y) => Q = (x, -y)`. But because we work on a finite field: `Q = (x, -y mod p)`