from OpenSSL import crypto
from Crypto.PublicKey import RSA

der_file = open("2048b-rsa-example-cert.der", 'rb')

certificate = crypto.load_certificate(crypto.FILETYPE_ASN1, der_file.read())
pem_certificate = crypto.dump_certificate(crypto.FILETYPE_PEM, certificate)

rsa_key = crypto.dump_publickey(crypto.FILETYPE_PEM, certificate.get_pubkey())

key = RSA.importKey(rsa_key)
print(f'Modulus: {key.n}')