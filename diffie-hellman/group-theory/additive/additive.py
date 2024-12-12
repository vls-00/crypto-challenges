from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hashlib
import json
from pwn import *

def is_pkcs7_padded(message):
    padding = message[-message[-1]:]
    return all(padding[i] == len(padding) for i in range(0, len(padding)))

def decrypt_flag(shared_secret: int, iv: str, ciphertext: str):
    # Derive AES key from shared secret
    sha1 = hashlib.sha1()
    sha1.update(str(shared_secret).encode('ascii'))
    key = sha1.digest()[:16]
    # Decrypt flag
    ciphertext = bytes.fromhex(ciphertext)
    iv = bytes.fromhex(iv)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext)

    if is_pkcs7_padded(plaintext):
        return unpad(plaintext, 16).decode('ascii')
    else:
        return plaintext.decode('ascii')
    
HOST = "socket.cryptohack.org"
PORT = 13380

r = remote(HOST, PORT)

#ignore first message
alice_message = json.loads(r.readline()[len("Intercepted from Alice: "):])
bob_message = json.loads(r.readline()[len("Intercepted from Bob: "):])
aes_params_message = json.loads(r.readline()[len("Intercepted from Alice: "):])

p = int(alice_message['p'], 16)
A = int(alice_message['A'], 16)
g = int(alice_message['g'], 16)

B = int(bob_message['B'], 16)

iv = aes_params_message['iv']
ct = aes_params_message['encrypted']

print(f"A: {A}")
print(f"B: {B}")
print(f"g: {g}")
print(f"p: {p}")

b = B // 2
secret = (A * b) % p

print(decrypt_flag(secret, iv, ct))