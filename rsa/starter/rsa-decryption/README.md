## Analysis
This challenge is a simple RSA decryption. To decrypt an RSA encrypted message we have to calculate `m ^ d mod N` for an encrypted message m.

 More info on why this works: https://el.wikipedia.org/wiki/RSA

Note: We are once again going to use modular exponentiation for this calculation (the numbers are too big to handle).