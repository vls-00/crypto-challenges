from Crypto.PublicKey import RSA

file = open("privacy-enhanced-mail.pem", 'r')
key = RSA.importKey(file.read())
print(f'Private key d (flag): {key.d}')