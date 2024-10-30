### Analysis
In this challenge we are given an SSH public key and asked to find the modulus.

They key point here is that SSH keys are basically RSA keys so we can just use the same methodology as in `privacy-enhanced-mail` to extract the modulus..

### Solution

We will use the same code from `privacy-enhanced-mail` challenge to get the key and fetch the field `n` of the RSA key which is the modulus.