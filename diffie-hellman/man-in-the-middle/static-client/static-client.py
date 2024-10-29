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
PORT = 13373
r = remote(HOST, PORT)

alice_key_exchange = json_recv()
print(f'Alice key exchange: {alice_key_exchange}')

g = int(alice_key_exchange['g'], 16)
p = int(alice_key_exchange['p'], 16)
A = int(alice_key_exchange['A'], 16)

# We don't care about this
bob_key_exchange = json_recv()

alice_message = json_recv()
print(f'Alice\'s message: {alice_message}')
iv_alice = alice_message["iv"]
ciphertext_alice = alice_message["encrypted"]

malicious_request_to_bob = {
    "p": hex(p),
    "g": hex(A),
    "A": hex(5)
}
json_send(malicious_request_to_bob)

bob_key_exchange_2 = json_recv()
print(f'Bob special key exchange 2: {bob_key_exchange_2}')
special_B = int(bob_key_exchange_2['B'], 16)

shared_secret = special_B

# We don't care about this
bob_message_2 = json_recv()

print(f'Flag: {decrypt_flag(shared_secret, iv_alice, ciphertext_alice)}')