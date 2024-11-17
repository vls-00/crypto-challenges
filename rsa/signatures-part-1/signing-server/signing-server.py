from pwn import *
import json
from Crypto.Util.number import bytes_to_long, long_to_bytes

def json_recv():
    line = r.readline()
    return json.loads(line)

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)
    
HOST = "socket.cryptohack.org"
PORT = 13374
r = remote(HOST, PORT)

r.readline()

get_secret = {
    "option": "get_secret"
}
json_send(get_secret)

secret = json_recv()
print(secret)

sign_secret = {
    "option": "sign",
    "msg": secret['secret']
}
json_send(sign_secret)

signed_secret = json_recv()['signature']

print(f'Secret message: {long_to_bytes(int(signed_secret, 16)).decode("utf-8")}')