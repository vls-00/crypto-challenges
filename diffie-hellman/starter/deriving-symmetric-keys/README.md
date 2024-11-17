## Analysis
In this challenge we are given a `decrypt.py` which can be used to decrypt AES encrypted ciphertexts that use a Diffie-Hellman key exchange. 

The shared secret from the Diffie-Hellman is used to derive the AES key. Alice also sends the the AES initializing vector (iv) so we can decrypt by using AES.

## Solution
1. Use the same methodology as in `computing-shared-secrets` challenge to compute the shared key.
2. Use the provided functions to dectypt the text and obtain the flag.

