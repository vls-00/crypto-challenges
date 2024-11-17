## Analysis
In this challenge, we are provided a very very big exponent `e` and by looking at the source code we can notice the private key `d` is small(256 bits).

After a little bit of searching, having a big `e` and a small `d` are the prerequisites to apply a wiener attack on RSA https://en.wikipedia.org/wiki/Wiener%27s_attack

You can also read this article from cryptohack about the wiener attack that explains both the thorem and the attack in details: https://cryptohack.gitbook.io/cryptobook/untitled/low-private-component-attacks/wieners-attack

For the challenge we can use the provided library from the article that has an implementation of the wiener attack https://github.com/orisano/owiener

## Solution
1. Install the owiener python library: `pip3 install owiener`.
2. Attack the given `n` and `e` using the wiener attack to find `d`.
3. Decrypt the flag using `d`.
