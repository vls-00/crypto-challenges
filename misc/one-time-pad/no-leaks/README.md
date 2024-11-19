## Analysis
In this challenge every time we request the flag it is getting XORed with a random 20 byte sequence which has the length of the flag (the flag is 20 characters).

This is completely secure because an XOR with a random one time pad for every request can never be guessed. What makes the encoding insecure is these 2 lines:
```
for c, p in zip(xored, flag_ord):
    assert c != p
```

This line ensures that the bytes from the ciphertext are not the same with the bytes of the plaintext (per position index).

We can take advantage of this and receive a ciphertext so many times that if we track all the characters received per byte position we can reject most of the alphabet except the correct character. Just because the correct flag character will never be in the ciphertext in its position.

## Solution
1. Make a dictionary of sets to keep track of all the rejected bytes per position
2. We only need to check the bytes in positions 7 to 18 because we only that the prefix of the flag is `crypto{` and the suffix `}`
3. Receive 2000 cipherexts and add the rejected characters for each position in the dictionary
4. Warning: If we are extra unlucky, 2000 iterations might not be sufficient. 5000 will surely do the work but it takes over 5 minutes to complete.
5. Finally, check the dictionary for all the rejected characters per position and that should leave us with 1 available character for each character in the flag (except the prefix and the suffix which we already know)
6. We only iterate through lowercase characters, numbers and _ because they are the only characters a cryptoflag flag can contain.

Note: Checking for all ASCII characters plus checking for all 20 bytes of the flag can still work, but it takes a lot more time. Checking for all ASCII characters means that the iterations must be >50000 for this to work because there are hundreds more characters that we need to reject. So just use the flag form knowledge to your advantage.
