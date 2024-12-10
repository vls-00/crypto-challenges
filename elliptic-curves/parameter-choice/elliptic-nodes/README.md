## Analysis & Solution
In this challenge the parameters a, b are hidden from us, but as long as we have 2 poitns on the curve we can solve the equation and recover them.

I used the utility function from https://github.com/jvdsn/crypto-attacks/blob/master/attacks/ecc/singular_curve.py to calculate a, b.

As soon as I got the parameters I tried making the elliptic curve on sage and calculate the order but I got the following error:

```
ArithmeticError: y^2 = x^3 + 64186688762130075872648727143532923412208390610536286437268423112*x + 32579945572763798990069104934898692239152360555014084068553395172709029894 defines a singular curve
```

A singular curve is not an elliptic curve and the discrete logarithm problem becomes trivial. You can read a very good mathematical explanation about how it happens here: https://crypto.stackexchange.com/questions/61302/how-to-solve-this-ecdlp/61434#61434.

I also used the singular curve attack from https://github.com/jvdsn/crypto-attacks/blob/master/attacks/ecc/singular_curve.py to calculate the private key `n`.

The private key `n` is the flag bytes converted to long (look at the source code) so all we have to do is convert it back to bytes to receive the flag.