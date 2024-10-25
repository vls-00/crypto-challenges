### Analysis
This challenge is the same as `RSA OR HMAC` part 1 so what we have to do is sign our custom JWT token by using the RSA public key and HMAC algorithm. The twist in this challenge is that we do not have the public key given. A lot of research was required for this challenge and luckily I stumbled upon a portswigger section about deriving public keys from JWT tokens.
* Portswigger module: `https://portswigger.net/web-security/jwt/algorithm-confusion#deriving-public-keys-from-existing-tokens`
* JWT forgery tool: `https://github.com/silentsignal/rsa_sign2n/blob/release/standalone/jwt_forgery.py`
* Demo video for the tool: `https://asciinema.org/a/390901`
* Blog post explaining the math behind it: `https://blog.silentsignal.eu/2021/02/08/abusing-jwt-public-keys-without-the-public-key/`
* Stack overflow answer mathemtically explaining how to get the modulus from an RSA signature: `https://crypto.stackexchange.com/questions/30289/is-it-possible-to-recover-an-rsa-modulus-from-its-signatures/30301#30301`

### Solution
1. First of all we need to apply the patch at the PyJWT library (`jwt/utils.py` file) as explained by the challenged so it lets us sign a JWT token with HMAC algorithm by using an RSA PUBLIC KEY.
2. We generate 2 JWT tokens from the website API so we can use `jwt_forgery.py` tool to extract the RSA public key for us.
3. We now call `jwt_forgery.py` in a subprocess using these 2 tokens which will make a file in the current directory that includes the RSA public key recovered from the signatures.
4. Next, we do some string manipulation in the tool's output to find the PKCS1 filename and load the public key inside our script.
5. We can now craft our JWT using the RSA PUBLIC KEY recovered from the signatures and exploit the same vulnerability with HMAC and RSA as in `HMAC or RSA` part 1 challenge.
