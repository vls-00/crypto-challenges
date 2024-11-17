## Analysis
In this challenge, we are provided the modulus `n` and the private key `d`. We can use these two to factorize the `n` into `p` and `q` by using the algorithm from the suggested website https://www.di-mgt.com.au/rsa_factorize_n.html.

I did a raw implementation of the algorithm but did not use a random `g` in every iteration. Instead, I used every prime number starting from 2 and upwards because the article suggests this kind of approach if we are dealing with big numbers (read `#Code to do this with large integers`).

## Solution
1. Factorize `n` into `p` and `q` using the new algorithm.
2. Calculate `phi(n)`.
3. Initialize the friend keys in an array in reverse order because each key is used one after another in the original order to encode the plaintext.
4. Our friends used 5 different `e` to encode the message so we will need to calculate a new private key `d` for each `e` so that:
   
    `d*e = 1 mod phi(N)` for each one.
5. As a last step we use each new `d` to calculate `ct ^ d mod n` and after all the keys have been applied, we should receive the plaitext.
