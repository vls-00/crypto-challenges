## Analysis
This challenge is giving us a vulnerable backend source code and we must try to exploit it by using a maliciously crafted JWT token in order to get the flag.

## Solution
1. Make a JWT token with username `admin` where we can extract the payload and modify it.
2. Modify the payload setting the `admin` value to `True`
4. Encode the modified JWT using `"none"` as algorithm. The key must also be `None` (key is not needed for "None" algorithms)
6. Send the forged JWT to the server to get the flag
