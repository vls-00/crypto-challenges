## Analysis
This challenge is the same padding oracle attack as the pad-thai but with a twitst. Every time we get the padding result, the result is getting logical XORed with a random value with this code `return {"result": good | (rng.random() > 0.4)}`. 

Let's break down the possible results:

- Our padding is correct and random value is True: `True || True = True`
- Our padding is correct and random value is False: `True || False = True`
- Our padding is wrong and random value is True: `False || True = True` (false positive)
- Our padding is wrong and random value is false: `False || False = False`

If our padding is correct, then whatever is the random value, the result will always be correct.

If our padding is wrong, then we might get a false positive. In order to handle the false positives, we will make a lot of requests per byte candidate and if one of them is `False` then it means our padding is wrong. 

We also cannot make too many requests because if we exceed the 12.000 we will not get the flag (source code restriction).

Be careful though, with a small number of requests (suppsoe 10), the false positive might occur 10 times in a row and the algorithm will not work because we will have a false byte inside our zeroing_iv.

## Solution
1. I used the same padding oracle algorithm as in `pad-thai` challenge.
2. I changed the `oracle()` function to make 20 requests per call just to be sure we do not get a false positive result. More specifically, when the oracle gets a `False` I immediately break the loop so it will not run 20 times. The oracle will only make 20 requests only for the CORRECT candidates.

- Note 1: 20 requests per CORRECT candidate worked fine for me (most of the times), as you decrease you will fall in a lot of false positive traps.
 
- Note 2: We could also pre-set the first 7 bytes of the zeroing-iv because we know that plaintext starts with `crypto{` but number 20 works fine without it.

- Note 3: Max iterations for 20 requests per candidate might seem a lot but for bad paddings the loop is cut very early most of the times  (~5 requests) so we do not need to worry. This will fail only if all zeroing IV bytes are above the number `0xaa` (170 in decimal).