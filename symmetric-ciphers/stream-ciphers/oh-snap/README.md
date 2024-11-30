## Analysis
This challenge is a recreation of famous Fluhrer, Mantin, Shamir(fms) attack on the RC4 algorithm, which was also used to attack the WEP wireless protocol.

Resources for more information:
- https://en.wikipedia.org/wiki/RC4
- https://en.wikipedia.org/wiki/Fluhrer,_Mantin_and_Shamir_attack
- https://kevinliu.me/posts/rc4/

## Solution
>Note: Two bytes from the flag are not guessed correctly from the algortithm but can be guessed by looking at the rest of the flag.

1. I used the attack algorithm from https://kevinliu.me/posts/rc4/
2. In the article the attack is on the pure keystream while the original algorithm is XORing the keystream with the ciphertext to receive the plaintext.
3. We need to modify the algorithm a little bit calculate the keystream for our standards:
```
keystream ^ ciphertext = plaintext
=> keystream = ciphertext ^ plaintext
```

We know what the ciphertext is (we send it in the request) and we also know what the plaintext is because it is returned in the response (unless it is equivalent to `b'ping'` x.x)