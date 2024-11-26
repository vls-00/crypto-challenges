## Analysis
In this challenge we are only provided an encryption endpoint where we can give a plaintext of bytes that will be prepended before the flag before it gets encrypted.

The padding is in blocks of 16 bytes. We also know that ECB has no chain encryption and the plaintext is splitted into blocks of 16 bytes and encrypted separately.

We can take advantage of that in 3 ways:
1) Calculate the flag length by adding a byte to the prefix until the output becomes 16 bytes longer
2) Give the endpoint a prefix of each aphanumeric character padded to 16 bytes (with the same pad function used) and then observe the encrypted output of the first block. Our block will get encrypted separately from the others. That way we can make a dictionary and note how each alphanumeric character padded looks like after encryption. Example for character 'a': "try: a\x0f\x0f\x0f... -> save the first 16 bytes of the encrypted output to the dictionary".
3) Give the endpoint a random pad (based on the flag length) in order to push each character of the flag to the last block of the encrypted text. The padded flag will look something like (3 blocks):
```
\xff\xff\xff\xff.... (our prefix pad)
crypto{?????????
}\x0f\x0f\x0f\x0f... (the pad() function pad and the last flag character)
```

After step 3, we can match the encrypted text of the last block with the dictionary we made in step 1 and based on the encrypted bytes, find what character corresponds to this 16-byte encrypted text.

## Algorithm Example
flag: crypto{test}

Iteration 1:
* We calculate the length: 12
* Make a dictionary by sending requests with: pad('a', 16), pad('b', 16), pad('c', 16)....
* Save each character with its corresponding encrypted block of the ciphertext (which will be block 1)
* Push the last character to the next block by giving "ffffffffff" (ff x 5) into the endpoint. Note that: 12 + 5 = 17 = 16 + 1
* Take the last block of the encrypted text and look at the dictionary which character matches it. It will be '}'

Iteration 2:
* Make a dictionary by sending requests with: pad('a}', 16), pad('b}', 16), pad('c}', 16)....
* Save each character with its corresponding encrypted block of the ciphertext (which will be block 1)
* Push the last 2 characters to the next block by giving "ffffffffffff" (ff x 6) into the endpoint. Note that: 12 + 6 = 18 = 16 + 2
* Take the last block of the encrypted text and look at the dictionary which character matches it. It will be 't}'

...Do the rest of the iterations by pushing one character more in each iteration

## Solution
The solution is mostly explained above.

Note 1: The flag in the challenge is 25 characters so at some point the blocks will look something like: 
```
\xff\xff\xff\xff....
\xff\xff\xff....crypto{??
????????????????
}\x0f\x0f\x0f\x0f...
```
That means we have to check in the response accordingly and not only in the last block of it.

Note 2: We only check for alphanumeric characters, numbers and '_'. Nothing else can be contained in the flag.

Note 3: The complexity is: possible_characters * length.

Note 4: In this script, we dont check for 'crypto{' characters because we know the flag format, it is also assumed that the lastcharacter is '}'.