## Analysis
In this challenge we are up against another CTR mode stream cipher which is once again not implemented correctly.

The nonce (or IV) is nto provided into the counter, thus the bytes that go into the block cipher encryption is only the counter which starts from 0, 1, 2, etc.

The real problem lies in the reuse of the IV not on the values themselves. So just because the same IV is used for every encryption, by knowing a plaintext we can derive the block output just by XORing with the ciphertext.

The challenge only provides an endpoint that returns ciphertexts. We also know that every plaintext that gets encrypted is a "TEXT", so they must be english words or sentences.

Do we know any of the plaintexts? We only know the flag prefix (7 bytes) which can help us derive a part of the block output, but how do we know which ciphertext is the flag ciphertext? We can try all ciphertext and calculate all possible block outputs, we can then use that to XOR with the rest of the ciphertexts and the output must be ASCII for all of them in order to be the correct one.

## Solution
1. Make requests to the server and store them in an array until he has returned a message that we already have, 100 times in a row. This way we will have very high chances of receiving all the possible ciphertexts including the flag.
2. For every ciphertext calculate every possible block output, the one that will provide ASCII characters for every other ciphertext is the correct one.

At this point, I tried brute-forcing every possible byte value as the next byte in the block output and see if that will produce an ASCII character in all other ciphertexts. This did not work at all because the ciphertexts we have are only 22 and the chances of a byte producing an ASCII character in all of them are pretty high.
I managed to do it for the next 4 characters of the block output by reducing some punctuation characters from the possible ASCII characters. You can try it if you want, I left the code commented out. You will have to remove the "+" character from the possible characters list, in order to see the next 4.

3. From this point on I used the 7 + 4 characters I have to decode the first 11 letters of all 22 ciphertexts. The only way to continue at this point is by guessing letters.
4. Guessing is made easy here because the texts are normal english sentences and we already know the first 11 letters of them. It is pretty easy guessing letter by letter in one of the setences each time. My guesses are in the end of the script, you can also see the rest of the texts printed after each guess.