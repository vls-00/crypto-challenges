### Analysis
In this challenge we will have to sign our own message using RSA. `d` and `N` are given. 

In order to sign the message given by the challenge we first calculate its hash and then sign with out private key `d`. 

Signing with `d` means that we will calculate `H(m) ^ d mod N` which can then be decrypted with the public key and verify both the signature and the message.

### Solution
1. Calculate the SHA-256 hash of the message (`H(m)`).
2. Convert the hash to bytes and the bytes to long because RSA we are only working with numbers.
3. Calculate `H(m) ^ d mod N` using modular exponentiation which is the sign.