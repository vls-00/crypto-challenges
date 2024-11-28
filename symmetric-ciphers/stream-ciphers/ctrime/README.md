## Analysis
This challenge is encrypting the text using a normal CTR mode stream cipher algorithm so there is no way of decrypting without the key.

Although there is something interesting in the encryption endpoint, we can give a plaintext that will get compressed with the flag before the text gets encrypted.

We can take advantage of this by brute-forcing each letter and based on the ciphertext we can determine if the compress function compressed our letters with the letters from the flag (which means they are the same).

If the characters of our plaintext match the ones of the flag then the length of the ciphertext should stay the same.

## Solution
1. Start with the flag prefix that we already know (`crypto{`) and calculate the length.
2. We brute-force the next character and note which character produces a ciphertext with the length we calculated. This is the next character of the flag because it got compressed and did not increase the size.

After I discovered the flag part `crypto{CRIM` then whatever character I tried, the length was always increasing and I believe this is happening because we pushed some characters of the flag to the next block of the encryption. In order to handle this situation I did the following:

1. Start adding each character to the flag 1, 2, 3, 4, 5 times.
2. If a character produced smaller length than the previous addition, it means it matched the flag character and the compression compressed them all together.
3. If a character is not matching the character flag, then by adding it 1, 2, 3, 4, 5 will always procude the same or higher length.
3. After finding the matching character, we also update the target length for the next iterations.
4. Example:

```
crypto{CRIMa -> length = 100
crypto{CRIMaa -> length = 104
crypto{CRIMaaa -> length = 108
crypto{CRIMaaaa -> length = 112
crypto{CRIMaaaaa -> length = 116
...
crypto{CRIME -> length = 100
crypto{CRIMEE -> length = 104
crypto{CRIMEEE -> length = 98 (<104 because the three 'E' got compressed with the one from the flag)
Found it
```

Note: The execution time is >10 minutes because the server is unstable. 