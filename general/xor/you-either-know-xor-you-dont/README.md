### Analysis
This challenge is giving us an encoded value which is the result of the flag XORed with a secret key. We already know that the flags of cryptohack have the `crypto{` prefix. So we can use this information to obtain the first 7 characters of the key based on the XOR associative property.

### Solution
1. We take the first 14 chracters of the encoded value which are the first 7 bytes of the flag (2 hex characters = 1 byte)
2. We encode the already known prefix `crypto{` to bytes.
3. We XOR those two to get the first 7 characters of the key which are `myXORke`.
4. We can now guess that the key is `myXORkey` so if we XOR the encoded text bytes with this key we can get the flag.
