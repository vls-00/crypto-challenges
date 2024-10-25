### Analysis
This challenge is an introduction to Fermat's little theorem. We need to calculate `(27324678765 ^ 65536) % 65537`.
* We are given that `65537` is a prime number
* From Fermat's little theorem we have that:
    * if the base is not divisable by the exponent
    * `exponent = prime` 
Then:

    * `a^(p-1) ≡ 1 (mod p) => a^(p-1) mod p = 1 mod p => a^(p-1) mod p = 1`

### Solution
1. Exponent = `65536`.
2. We notice that `65536 = 65537 - 1` where `65537` is prime.
3. For `p = 65537` the above equation results to 1.

