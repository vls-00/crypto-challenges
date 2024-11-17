## Analysis
We have to make a python script that converts the given hex to base64.

## Solution
1. Copy the hex string from the exercise.
2. Use the `bytes.fromhex(hex)` to convert it to bytes.
3. Wrap that inside `base64.b64encode` to convert the bytes to base64 and get the flag.
