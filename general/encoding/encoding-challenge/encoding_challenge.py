from pwn import *
import json
from Crypto.Util.number import *
import codecs

r = remote('socket.cryptohack.org', 13377, level = 'debug')

def json_recv():
    line = r.recvline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)

response = json_recv()
decoded = ""

for i in range (100):
    type = response["type"]
    encoded = response["encoded"]
    
    if type == "base64":
            decoded = base64.b64decode(encoded).decode('ascii')
    elif type == "hex":
            decoded = bytes.fromhex(encoded).decode('ascii')
    elif type == "rot13":
            decoded = codecs.decode(encoded, 'rot_13')
    elif type == "bigint":
            decoded = long_to_bytes(int(encoded, 16)).decode('ascii')
    elif type == "utf-8":
            decoded = "".join(chr(b) for b in encoded)
    
    request = {
        "decoded": "".join(decoded)
    }
    
    # Uncomment below to see more details about each iteration
    # print(f"Iteration: {i} | Type: {type} | Encoded: {encoded} | Decode Attempt: {decoded}")
    
    json_send(request)
    response = json_recv()