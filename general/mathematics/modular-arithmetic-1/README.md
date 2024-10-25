### Analysis
This challenge is an indtroduction to modular arithmetic. 

`a ≡ b mod m -> a mod m = b mod m`

That means that both a and b if they are divided by m they have the same ramainder. That remainder is the smaller possible number for a and b to be congruent modulo.

Example:
* 11 ≡ x mod 6
* 11/6 = 1 with remainder 5
* The smaller `x` for 11 and `x` in order for them to be congruent modulo is 5

### Solution

I took the given numbers which are 11 , 8146798528947 and modulo them with their respective m which is 6, 17.
That gives us 5 for the first one and 4 for the second one. The flag is the smaller of the two.
