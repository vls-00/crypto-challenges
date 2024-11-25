## Analysis
In this challenge we are provided an encrypt endpoint which encrypts the flag using CBC and another endpoint which decrypts a ciphertext using ECB.

They key point here is that the only difference between these 2 algorithms is just an XOR before the plaintext goes into the AES cipher block.

We can take advantage of this to decrypt the ciphertext and just do the XOR manually.

Note 1: The initilization vector (iv) is given in the response of the encrypt endpoint. It is the first 16 bytes (32 hex characters).
Note 2: The output from the encrypt endpoint is 96 hex characters, the iv is 32 of them so the plaintext is 64 hex characters (32 bytes). That means the plaintext is getting encrypted in 2 blocks, one per 16 bytes.

## Solution
1. Take the ciphertext from the encrypt endpoint and split it into the 2 blocks of the plaintext and the iv
2. Send the 2 encrypted blocks of the plaintext into the decrypt endpoint separately
3. We XOR the first block of the decrypted plaintext with the IV to get the first half of the flag
4. For the second block of the decrypted plaintext, we need to XOR it with the first block of the encrypted text (CBC chain decryption).

Note: The initialization vector for each iteration is the ciphertext of the previous iteration except the first iteration in which the original IV is used. Take alook at the picture in https://aes.cryptohack.org/ecbcbcwtf/ to understand the CBC concept better.