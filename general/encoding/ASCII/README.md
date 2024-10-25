### Analysis
This challenge is giving us an array of ordinals that we have to convert to ASCII.
We need to parse each ordinal separately, convert it to ASCII and concatenate all together to ge tthe flag.

### Solution

1. Copy the ordinal array from the exercise.
2. Use the `chr()` function to convert the ordinals to characters.
3. Join every converted character in order to get the flag
