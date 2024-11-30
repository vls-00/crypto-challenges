import json
from pwn import *

MAX_RESET_TRIES = 50

def json_recv():
    line = r.recvline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)

def brute_force_password(password_length):
    for i in range(0, 255):
        password = password_length * chr(i)
        authenticate = {
            "option": "authenticate",
            "password": password
        }
        json_send(authenticate)
        response = json_recv()['msg']
        if "admin" in response:
            print(f"Flag: {response}")
            exit()
    
HOST = "socket.cryptohack.org"
PORT = 13399
r = remote(HOST, PORT)
print(r.recvline())

token = 32 * "01"
password_length = (len(token) - 32) // 2 - 4
password_length=12

for i in range(1, MAX_RESET_TRIES + 1):
    print(f"[+] Try no.{i}:")
    password_reset = {
        "option": "reset_password",
        "token": token
    }
    json_send(password_reset)
    
    print(r.recvline())
    brute_force_password(password_length)
