### Analysis
In this challenge we are able to manipulate the parameter negotiation message from Alice to Bob. In the first message from Alice we can see that she supports `DH64` which is Diffie-Hellman with 64 bit parameters. 

The keys of `DH64` can be brute forced using a commodity PC nowadays within seconds.

### Solution
1. We intercept the first message from Alice which includes a lot of Diffie-Hellman algorithms with different key lengths.
2. We throw away all other algoriths and only keep the one with the smallest key. This is the last elemnt in the list and is the `DH64`.
3. Now we have forced Bob to talk we Alice using 64 bit keys so alice will send us the `p, g, A` we need to have in order to break the `DH`.
4. Bob will also send public key `B` which we need in order to calculate the shared secret key after we have brute-forced Alice's secret key `a`

<span style="color:orange">Note:</span> Trying to find the discrete algorithm directly on your PC might cause a memory error (happened to me).
It will only work if you make the required optimizations which is a lot of math to understand. Maybe it is better to use a ready-to-go function from a library.
I used the `discrete_log` function from `sympy`.

5. Calculate the discrete log of `A` with modulus `p` and base `g`. This will give you Alice's secret key `a`.
6. Now that we have `a` we can calculate the shared secret key using Bob's `B` (`key = (B ^ a) mod p`)
7. We use the provided function for AES decryption gived by the challenge to decrypt the message and get the flag.

