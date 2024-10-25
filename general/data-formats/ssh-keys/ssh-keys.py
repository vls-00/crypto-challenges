from Crypto.PublicKey import RSA

rsa_key = open("bruce-rsa.pub", 'rb')

key = RSA.importKey(rsa_key.read())
print(f'Modulus: {key.n}')