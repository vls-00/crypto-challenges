## Analysis
This challenge is giving us an RSA key in PEM format and we have to extract private key exponent `d` from it.

## Solution

1. We will use the recommended function `RSA.importKey()` to import the key from the PKCS.
2. We can get `d` by accessing field `d` of the object of type `RsaKey` given from the `RSA.importKey()` function.