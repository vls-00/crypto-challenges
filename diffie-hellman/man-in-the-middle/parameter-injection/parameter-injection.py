from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hashlib
from pwn import *
import json

def is_pkcs7_padded(message):
    padding = message[-message[-1]:]
    return all(padding[i] == len(padding) for i in range(0, len(padding)))


def decrypt_flag(shared_secret: int, iv: str, ciphertext: str):
    # Derive AES key from shared secret
    sha1 = hashlib.sha1()
    sha1.update(str(shared_secret).encode('ascii'))
    key = sha1.digest()[:16]
    # Decrypt
    ciphertext = bytes.fromhex(ciphertext)
    iv = bytes.fromhex(iv)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext)

    if is_pkcs7_padded(plaintext):
        return unpad(plaintext, 16).decode('ascii')
    else:
        return plaintext.decode('ascii')
    
def modular_pow(base, exponent, modulus):
    if modulus == 1:
        return 0
    
    result = 1
    base = base % modulus
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
            
        exponent = exponent // 2
        base = (base * base) % modulus
    
    return result

def json_recv():
    line = r.readline()
    line = line.decode().split('{', 1)[1].strip()
    return json.loads("{" + line)

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)
    
HOST = "socket.cryptohack.org"
PORT = 13371
r = remote(HOST, PORT)

alice_key_exchange = json_recv()
print(f'Alice key exchange: {alice_key_exchange}')

g = int(alice_key_exchange['g'], 16)
p = int(alice_key_exchange['p'], 16)
A = int(alice_key_exchange['A'], 16)

c = 7
C = modular_pow(g, c, p)

malicious_request_to_bob = {
    "p": hex(p),
    "g": hex(g),
    "A": hex(C)
}
json_send(malicious_request_to_bob)

bob_key_exchange = json_recv()
print(f'Bob key exchange: {bob_key_exchange}')

B = int(bob_key_exchange['B'], 16)

shared_secret = modular_pow(A, c, p)

request_to_alice = {
    "B": hex(C)
}

json_send(request_to_alice)

alice_message = json_recv()
print(f'Alice\'s message: {alice_message}')
iv = alice_message["iv"]
ciphertext = alice_message["encrypted_flag"]

print(f'Flag: {decrypt_flag(shared_secret, iv, ciphertext)}')