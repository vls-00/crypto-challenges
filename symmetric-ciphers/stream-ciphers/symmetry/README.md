## Analysis
This is a challenge in which we have to exploit the an OFB stream cipher property.

Notice that during the ecryption, the IV after going through teh AES block is getting XORed with the plaintext to produce the ciphertext.

For known plaintext, we can calculate the block cipher output of the IV because we also know the ciphertext.
```
block_cipher_encryption_output ^ plaintext = ciphertext
=> block_cipher_encryption_output = ciphertext ^ plaintext
```
We can exploit this to find the block_cipher_encryption_output of the IV used to encrypt the flag. This time what we do not know is the plaintext (flag).

```
block_cipher_encryption_output ^ plaintext = ciphertext
=> plaintext = block_cipher_encryption_output ^ ciphertext
```

We can repeat the same process for all the blocks until we get the whole flag.

## Solution
1) The solution is basically the analysis above
2) The flag in this challenge is splitted into 3 blocks -> 16 + 16 + 1
3) To decrypt the blocks 2,3 the same process is repeated. We just have to use a bigger dummy plaintext so it will be splitted into 3 blocks in order to calculate the `block_cipher_encryption_output` for each one of the 3 blocks.