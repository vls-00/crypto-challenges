## Analysis
In this challenge the server has a custom CFB-8 encryption and decryption mechanism. The interesting thing here is that we can reset our password to the server by giving out custom ciphertext and custom IV. How can this be manipulated?

After a closer look we can see that the state that gets encrypted is shifted by 1 byte in each iteration:
```
state = state[1:] + bytes([ct[i]])
```
And 1 byte from the ciphertext is added in the end.

As said above, the ciphertext and the IV is an input from us. Can we make the state be the same every time it gets shifted? If we were able to do that, we erase the AES encryption because it will always have the same block output. So we need something that:
```
state[1:] + bytes([ct[i]]) = state[2:] + bytes([ct[i+1]]) = state[3:] + bytes([ct[i+2]]) = ... 
```
To achieve that, we can select a random byte (like 0x01) and make:  `IV = ciphertext = \x01\x01\x01\x01\x01\x01...`

Now every time the state shifts, the same state occurs. That means, the plaintext password that will occur will constists of the same repeated byte of desired length.

We can now brute force the password which will be 1 of 255 possible passwords (all possible byte values).

## Solution
1. Make a token with an IV of 16 bytes and a ciphertext of 16 bytes that all bytes are the same
2. Reset the password using that token
3. Calculate the length of the new password which is 12
4. Make a password of length 12 for each possible bytes cloned 12 times and try to authenticate, one of them must be it.

Warning / Note: The server only accepts an ASCII password input which is then converted into bytes and compared with the actual password. That means we cannot send custom bytes as a password. To avoid that, we only send printable characters as the password. If none is matching, it means we have reset the password into a password with non-printable bytes. We reset the password again and re-try, at some point we should be able to reset the password into a stream of cloned ASCII printable characters.