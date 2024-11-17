from pwn import *
import json
from Crypto.Util.number import bytes_to_long
from pkcs1 import emsa_pkcs1_v15

#Solve for known k and m: m mod n = k
def find_suitable_exponent_and_modulus(result, k):
    e = 1
    while True:
        if result < (k**e // 2):
            return e, k**e - result
        e += 1
    
def json_recv():
    line = r.readline()
    return json.loads(line)

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)
    
HOST = "socket.cryptohack.org"
PORT = 13391
r = remote(HOST, PORT)

r.readline()

get_signature = {
    "option": "get_signature"
}
json_send(get_signature)

signature = int(json_recv()['signature'], 16)

malory_message = r'I am Mallory and I own CryptoHack.org'
malory_digest = bytes_to_long(emsa_pkcs1_v15.encode(malory_message.encode(), 256))

modified_e, modified_n = find_suitable_exponent_and_modulus(malory_digest, signature)

calculated_digest = pow(signature, modified_e, modified_n)

assert malory_digest == calculated_digest

get_flag = {
    "option": "verify",
    "msg": malory_message,
    "N": hex(modified_n),
    "e": hex(modified_e)
}
json_send(get_flag)

print(f"Flag: {json_recv()['msg']}")