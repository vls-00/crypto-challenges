### Analysis
This challenge is giving us a chains of XORs and we have to use the XOR properties in order to receive the flag.

We will use the `Self-Inverse` property as well as the `Identity` and `Associative` properties.

### Solution

1. We start from `KEY1 XOR KEY2` where we can find `KEY2` by XORing with `KEY1` (Self-Inverse).
2. We also use `KEY2 XOR KEY3` where we can find `KEY3` by XORing with `KEY2` (Self-Inverse).
3. We can now XOR with `KEY1`, `KEY2`, `KEY3` in the last formula to get the flag.
