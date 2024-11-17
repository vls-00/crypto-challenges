## Analysis
In this challenge we are given a server that supports 2 important functions.
* A function that is giving us an encrypted secret (which was encrypted with the private key using RSA)
* A function that is able to sign any message as the server.

As we already know RSA can be used for encryption using the public key so it can only be decrypted with the private key and for signatures where the message is encrypted with the private key and can only get decrypted with the public key so anyone can verify the signature.

In this challenge we can exploit this because the server is using the same keys for encryption and signing by receiving the encrypted secret and then use the "sign" option to sign it which means this will get the secret dectypted because the server will use the private key to sign it.

## Solution
1. We fetch the secret from the server using the option "get_secret".
2. We sign the received secret using the option "sign".
3. Receive the signature and decode it to reveal the secret.

