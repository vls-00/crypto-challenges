### Analysis
We will have to make a python script that converts the long number to bytes and then convert to ASCII.
Better use the `long_to_bytes()` function as proposed by the challenge.

### Solution
1. Copy the long number from the challenge inside the script.
2. Use the `long_to_bytes()` function as proposed to convert the number to bytes.
3. Use `decode('ascii')` to convert the bytes to ASCII and get the flag.
