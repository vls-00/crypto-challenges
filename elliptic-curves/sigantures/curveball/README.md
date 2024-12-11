## Analysis
In this challenge we have to match the public key for `www.bing.com` by providing our own `G` and private key `d`.

Everything could be easy if we could jsut copy the poinT `A` and give `d = 1` but the server does not allow us.

Although, we know that in a finite field a point is cycling through all the possible values it can produce, just like modular arithmetics in decimal numbers. In elliptic curves, a point can produce as many different values as its order (that's what order is) and then it will cycle back.

So if we provide `d = order(A) + 1` will be like providing `d = 1` because point `A` will have cycled back to the first value which is `1 * A`.

## Solution
* G = A
* private_key = order(A) + 1
* host: "www.bing.com"
* curve: *whatever*