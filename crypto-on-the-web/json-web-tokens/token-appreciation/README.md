## Analysis
This challenge is giving us a JWT token and is an introduction on how to decode tokens using the PyJWT library.

## Solution
1. use `jwt.decode()` function from the library to decode the JWT and get the data payload.
2. We do not have the key for verifying the signature we must use the option `options={"verify_signature": False}` when decoding the token. Verifying the signature is not necessary for JWT tokens, someone can still see the payload data even without it.
3. The flag is inside the token's payload data.
