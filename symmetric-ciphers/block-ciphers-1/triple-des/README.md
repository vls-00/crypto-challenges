## Analysis
The interesting part in this challenge is that we can manipulate the key of 3DES. This should not be possible under normal circumstances, so I supposed the solution had something to do with that. After a little bit of reaserch I found a wiki articla saying that 3DES has some weak key pairs that make the encryption work like a decryption.

More information on:
- https://en.wikipedia.org/wiki/Weak_key

## Solution
1. Choose a weak key pair from the article (some of them are not working, trial and error is needed)
2. Encrypt the flag
3. Use the encryption endpoint to encrypt the flag again with the same weak key, this will result in the flag decryption