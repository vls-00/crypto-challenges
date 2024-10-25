### Analysis
This challenge is giving us a hex value and tells that it has been XORed with 1 random byte that we do not know.

1. We can brute force with each possible value a byte can take.
2. A byte can be 255 different values, from 00000000 to 11111111
3. In order to avoid forging bytes, we can just iterate through the numbers 0 and 255 -> convert them to bytes -> get all possible byte values for 1 byte

### Solution

1. We start a for-loop from number 0 to number 255
2. We convert each number to bytes of length 1 and XOR with the encoded text.
3. We know the FLAG is in the format `crypto{____}`
4. For each decoded text we convert to ASCII and if the decoded string contains the string `crypto{` it means we found the flag and succesfully decoded the text.
