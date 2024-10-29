### Analysis
In this challenge we have to calculate the `phi` function of `N`. `N` is the modulus of an RSA encryption which occuprs from the multipliation fo 2 prime numbers (p, q). In the provided article (https://leimao.github.io/article/RSA-Algorithm/) it explained why the `phi` function of a prime number equals to `p - 1`. So `phi(p) = p-1` and `phi(q) = q-1`

### Solution
`phi(N) = phi(p * q) = phi(p) * phi(q) = (p-1)(q-1)`

Note: Every `p` and `q` in RSA are comprimes because they are both prime numbers

### Flag - 20 pts
`882564595536224140639625987657529300394956519977044270821168`