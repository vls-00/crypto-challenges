## Analysis
In this challenge we have to do a MITM attack in Alice's and Bob's key exchange messages. More specifically we will pick our secret, call is `c`, and trick both Bob and Alice into crafting a shared secret key with us.

## Solution
1. Pick a random prime number `c` as our secret (let's say 7)
2. The first message we receive is from Alice and includes `p`, `g`, `A`.
3. We will calculate our public key `C` using the `p`, `g` parameters and we will send it to Bob. Bob will now calculate the same shared key with us.
4. Bob will respond with his public key `B` but we will intercept it and send our crafted public key `C` to Alice instead of Bob's `B`.
5. Now Alice will also calculate the same shared key with us.
6. We calculate the same shared key with alice using modular exponentiation from the previous challenges. We also need Alice's public key A in order to make the shared secret key that will decrypt Alice's messages.
7. We can now decrypt Alice's message she encrypted with the shared key we also have. For the decryption we will use the AES decryption method provided in the previous challenge.

Note: If we also wanted to decrypt Bob's messages we would have to calculate another shared key using Bob's public key `B`.

