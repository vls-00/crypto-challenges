## Analysis & Solution
In this weird elliptic curve we can notice that the modulus `p` is equal to the order of the curve. This is sign of Smart's attack in the curve that is also included in the same paper I used for `smooth-criminal`.

I also found an open-source code on github that already has the attack implemented. Sources below.

Attack information: https://wstein.org/edu/2010/414/projects/novotney.pdf
Code source: https://github.com/jvdsn/crypto-attacks/blob/master/attacks/ecc/smart_attack.py