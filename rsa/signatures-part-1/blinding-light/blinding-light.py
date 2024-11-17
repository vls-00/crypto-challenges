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
PORT = 13376
r = remote(HOST, PORT)

# Ignore the first message
r.readline()

get_pub_key = {
    "option": "get_pubkey"
}
json_send(get_pub_key)

pub_key = json_recv()
n = int(pub_key['N'], 16)
e = int(pub_key['e'], 16)

ADMIN_TOKEN = b"admin=True"
admin_token_long = bytes_to_long(ADMIN_TOKEN)
admin_token_plus_N = admin_token_long + n
admin_token_masked = long_to_bytes(admin_token_plus_N)

sign_request = {
    "option": "sign",
    "msg": admin_token_masked.hex()
}
json_send(sign_request)

signature = json_recv()['signature']

verify_request = {
    "option": "verify",
    "msg": ADMIN_TOKEN.hex(),
    "signature": signature
}
json_send(verify_request)

print(f"Flag: {json_recv()}")
