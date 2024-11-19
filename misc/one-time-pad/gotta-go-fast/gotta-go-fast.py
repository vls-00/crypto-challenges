import time
from Crypto.Util.number import long_to_bytes
import hashlib
from pwn import *
import json

def json_recv():
    line = r.readline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)

HOST = "socket.cryptohack.org"
PORT = 13372

r = remote(HOST, PORT)

#ignore first message
r.readline()

current_time = int(time.time())

get_flag = {
    "option":"get_flag"
}
json_send(get_flag)

ciphertext = json_recv()['encrypted_flag']
ciphertext = bytes.fromhex(ciphertext)
flag_prefix = b'crypto{'

for i in range(current_time, current_time+10):
    key = hashlib.sha256(long_to_bytes(i)).digest()
    plaintext = b''
    for j in range(0, len(ciphertext)):
        plaintext += bytes([ciphertext[j] ^ key[j]])
    if flag_prefix in plaintext:
        print(f"Flag: {plaintext}")