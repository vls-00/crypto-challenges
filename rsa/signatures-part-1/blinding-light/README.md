## Analysis
In this challenge in order to get the flag we have to sign and verify the ADMIN_TOKEN but the server has some countermeasures in place.

1. First countermeasure: the server is not letting you sign the ADMIN_TOKEN. This is done by checking the byte presentation of the message provided for signing but this can be bypassed.
2. Second countermeasure: the server is not letting you verify a message that is bigger than `n` or smaller than `0`. I actually don't know what is the purpose of this because the message we give is not getting any modulo applied so there is not a way of verifying the `ADMIN_TOKEN` with a manipulated message.

## Solution
1.  To bypass the `ADMIN_TOKEN` sign check: instead of sending `msg = ADMIN_TOKEN`, we send `msg = ADMIN_TOKEN + n`. The byte presentation of `msg = ADMIN_TOKEN + n` is another random byte string (not matching the token one) but when it will get signed it will give us the signature for `ADMIN_TOKEN`:

* `x mod n = (x + n) mod n`

2. Steps: `ADMIN_TOKEN` -> convert bytes to long -> add `n` -> convert it back to bytes -> give it to the server -> receive siganture.
3. Verify the signature received and provide the original `ADMIN_TOKEN` as a message to receive the flag.

