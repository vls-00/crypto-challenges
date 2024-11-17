## Analysis
In this challenge, a source script is given and we can notice that the exponent used for encryption equals to 1.

From the RSA definition, private key `d` is the modular multiplicative inverse of the exponent `e` and `phi(n)`.

Since the exponent is 1, it doesn't matter what `phi(n)` is because the modular multiplicative inverse will result in 1.

That means `d = 1` and we can easily decrypt the ciphertext.
