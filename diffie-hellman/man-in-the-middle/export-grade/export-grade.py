from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import hashlib
from pwn import *
from sympy.ntheory import discrete_log
import json

def json_recv():
    line = r.readline()
    line = line.decode().split('{', 1)[1].strip()
    return json.loads("{" + line)

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)
    
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

def resolve_secret(p, g, A, B):
    a = discrete_log(p, A, g)
    return modular_pow(B, a, p)
    
HOST = "socket.cryptohack.org"
PORT = 13379
r = remote(HOST, PORT)

alice_algorithm_support = json_recv()
print(f'Alice\'s algorithm support: {alice_algorithm_support}')

# Intercept the request and tell Bob that alice supports only the algorithm withthe smallest key
malicious_request_to_bob = {
    "supported": [alice_algorithm_support['supported'][-1]]
}
json_send(malicious_request_to_bob)

bob_chosen_algorithm = json_recv()
print(f'Bob chosen algorithm: {bob_chosen_algorithm}')

# Send the chosen algorithm from Bob to Alice
json_send(bob_chosen_algorithm)

# Receive p, g, A from Alice
alice_key_exchange = json_recv()
print(f'Alice key exchange: {alice_key_exchange}')
g = int(alice_key_exchange['g'], 16)
p = int(alice_key_exchange['p'], 16)
A = int(alice_key_exchange['A'], 16)

# Receive B from Bob
bob_key_exchange = json_recv()
print(f'Bob key exchange: {bob_key_exchange}')
B = int(bob_key_exchange['B'], 16)

# Receive Alice's message with the IV and the ciphertext
alice_message = json_recv()
print(f'Alice\'s message: {alice_message}')
iv = alice_message["iv"]
ciphertext = alice_message["encrypted_flag"]

shared_secret = resolve_secret(p, g, A, B)
print(f'Calculated secret: {shared_secret}')

print(f'Flag: {decrypt_flag(shared_secret, iv, ciphertext)}')