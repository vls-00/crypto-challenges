## Analysis
In this challenge we have to provide a message that has the structure `pad + null_byte + "VOTE FOR PEDRO"`. Although it is not that simple because the server is applying `message^3 mod n` to our input. 

`n` is a lot bigger than the exponent `e` and the byte presentation of our message `b'\00VOTE FOR PEDRO'`. So we do not have to care about the modulo `n` in general because `message^3 mod n = message^3`.

One thing we could do is take the cubic root of `bytes_to_long(b'\00VOTE FOR PEDRO')`. But, the server is converting our input to an integer, that means our message must have a perfect cubic root.

We could theoretically take the number from our message and pad numbers in the front until we find a number that has a perfect cubic root. For example we want a number that has the desired suffix which is `bytes_to_long(b'\00VOTE FOR PEDRO')` in our case and has a perfect cubic root. This can be done but it is very computationally expensive because we might need to check trillions+ of numbers.

In order to make this computation less expensive, we can exploit a property of mathematical powers which is:
>If we add digits to the front of the base of a power, the suffix digits will not change.

Example: 12^3 = 1728, 112^3=1404928, 23112=12,345,610,940,928

Notice that adding numbers in the front does not change the suffix of the result which is 28.

In order to exploit this we can make a function that is calculating cubes for each number added in the front (0-9) until we find the desired suffix digit by digit.

Let's say we want the suffix 88:
* 1^3=1, 2^3=8
* we keep 2
* 12^3=1728, 22^3=10648, 32^3=32768, 42^3=74088
* we keep 4
* result = 42

## Solution
**Note:** The first function I made is working with integers which are in decimal form and better for me to understand but working with integers is a problem because of how the integers are converted into bytes and saved into the memory. If you have 2 integers with the same suffix and you convert them to bytes, they won't have the same byte presentation suffix. To solve this, I converted my function to work with hexadecimal numbers and strings. The old function for the integers is still inside the script and called `create_power_with_target_suffix_decimal()` if you want to take a look.

1. Take the hexadecimal form of `b'pad\00VOTE FOR PEDRO'`
2. For each hexadecimal digit of the desired message starting from the end, iterate through all possible hexadecimal digits and see if the `result ^ 3` gives us the desired length.
3. The desired length with each iteration is `1, 2, 3, ..., target_length`. Like in the small example I provided above. 
4. In order to compare the suffixes we use modular arithmetics. To take the last `n` digits of a number you can calculate `number mod (base^n)`. Base is 16 for our example because we work with hexadecimals. For integers we use base=10 (e.g `1432 mod (10^3) = 432`).
5. Now, when the server will calculate the integer number of our hex presentation will have our desired byte presentation because we worked with hexadecimal numbers which is an exact byte presentation, just a bit more compact.

