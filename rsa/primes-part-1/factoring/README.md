## Analysis
This challenge we have to factorise an 150-bit number. 

This is a very trivial calculation for a modern PC expecially with the modern optimized algorithms for the factorization. 
It is also why its so important using primes of 4096 bit size or more for RSA.

## Solution
Use the `factorint()` function from sympy to factorize the number. 

It seems like the `primefac` library proposed by the challenge is too outdated, I could not make it work.