## Analysis
In this challenge we are able to send a malicious message to Bob. After reading the prompt it says `Bob connects to you, send him some parameters`. So we can send some new parameters to Bob and Bob will give us his `B` so we can talk with him. We can now impersonate Alice and talk with Bob but Bob's decrypted message is: `Hey what's up, I generated some random numbers did you see?` which is no use to us, the flag is probably contained inside Alice's message.

* Let's take a step back and think, what will Bob calculate when we send him the parameters? Bob will calculate `g ^ b mod p` which is his public key `B` and then he is gonna send it to us.
* What is Bob's secret key with Alice? Bob will calculate `A ^ b mod p` in order to talk with Alice.
* We know Alice's `A` because we intercepted the messages.
* What if we sent `A` in place of `g`? Bob will calculate `g ^ b mod p` which is his public key `B` but now will calculate `A ^ b mod p` because we sent him the wrong `g`.
* So Bob will calculate the shared secret key he used with Alice for us, and send it to us as his public key `B`.

## Solution
1. We fetch the first message from Alice and save `g, p, A`
2. We fetch the first message from Bob which includes his public key `B` with Alice but it is no use to us.
3. We get the encrypted message from Alice and save it.
4. We now send the malicious request to Bob with: `g = A`, `p = p`, `A = (whatever number you want)`
5. Bob calculates the secret key he used with Alice and sends it back as his public key `B`.
6. We decrypt Alice's message using the special `B` Bob sent us.
