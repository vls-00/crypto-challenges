### Analysis
This challenge is teaching us about a vulnerability in PyJWT library where you could encode a JWT using HMAC and an RSA public key. 

Then any web server using `PyJWT version <= 1.5.0` that was supporting both RSA and HMAC signature verification had a major vulnerability where the attacker could mix the algorithms and impersonate another.

### Solution
Note: I tried making the public key PEM file locally so I can freely use it but when I used the file with open file mode `rb` to sign my JWT I always got `Signature Verification Error`. What worked for me is copying the whole public key string as returned from the website JSON response. Maybe it had something to do with the `\n` characters. Anyway, you need to use the public key as it is returned inside the JSON from the web server.

1. By looking at the web server code we notice that the decode function accepts both RSA or HMAC algorithms for token verification.
2. We also notice that the secret used for decoding `HMAC` signatures is the RSA public key provided.
3. What we have to do is craft a payload containing the `admin` value set to `True` and sign it with HMAC algorithm while using the RSA public key as our secret.
4. This flaw in the library is already patched, in order to craft the malicious payload you have to modify the `jwt/utils.py` as explained by the challenge so the library let's you `HMAC` encrypt with an RSA PUBLIC KEY.
5. Send the malicious JWT to the server that will verify our signature and return the flag.
6. The JWT used to get the flag is: `eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImFkbWluIiwiYWRtaW4iOnRydWV9.ilYg-wRobcU9pAannICe4ZxmFhfOh1nXcWf8tJ6UyOY`
