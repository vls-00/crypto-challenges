## Analysis & Solution
This challenge's title called "MOVing problems" gave a hint that it is probably referring to the MOV elliptic curve attack which can be enabled when the curve embedding degree is small (<100).

In order to confirm the hint I calculated the curve's embedding degree which was found to be 2. So we can use MOV attack againt the curve and Bob's public key to find his private number `n`.

Attack code source: https://github.com/jvdsn/crypto-attacks/blob/master/attacks/ecc/mov_attack.py
Paper about the MOV attack: https://eprint.iacr.org/2018/307.pdf