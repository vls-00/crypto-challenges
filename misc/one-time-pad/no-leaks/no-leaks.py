import base64
import json
from pwn import *

def json_recv():
    line = r.readline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)

HOST = "socket.cryptohack.org"
PORT = 13370

r = remote(HOST, PORT)

#ignore first message
r.readline()

rejected_values = {}
for i in range(7, 19):
    rejected_values[i] = set()

#If we get extra unlucky the flag returned will not be correct, just add 1k+ iterations if you want to be sure
#Although this will take much more time to complete as we are talking with the server through a web socket
iterations = 2000
for k in range(iterations):
    try:
        request = {
            "msg":"request"
        }
        json_send(request)
        ciphertext = json_recv()['ciphertext']
        ciphertext = base64.b64decode(ciphertext)
        
        for i in range(7, 19):
            byte = ciphertext[i]
            rejected_values[i].add(byte)
    except:
        continue

flag = "crypto{"
for i in range(7, 19):
    #These are the only characters a cryptohack flag can contain
    for char in "abcdefghijklmnopqrstuvwxyz0123456789_":
        if ord(char) in rejected_values[i]:
            continue
        else:
            flag += char
flag += "}"

print(f"Flag:{flag}")
    