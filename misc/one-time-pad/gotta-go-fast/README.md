## Analysis
In this challenge, we can notice in the server source code that the flag is getting XORed byte to byte with the current server time in bytes.

Of course we can abuse this by calculating the time locally using the same time function as the server and then brute-force the key with values for the next 10 seconds (although the server will do the calculation 1 or 2 seconds after our calculation).

It is also very helpful that the server is using a time function that calculates time in seconds since the Epoch and not milliseconds, that means we have less values to brute-force.

## Solution
1. Calculate the time using the same time function locally.
2. Send the Request.
3. For all possible time values of current time until current time + 10 seconds, calculate the key.
4. The key is calculating by taking the time bytes converted to long and then hashed with SHA256, do this for every possible time value.
5. Do the XOR operation per byte with the ciphertext and if a ciphertext begins with `crypto{`, it means we have found the flag and brute-forced the key.
