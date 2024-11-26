import requests as rq
import json
from pwn import xor
import secrets

url = "https://aes.cryptohack.org/lazy_cbc/"

c0 = secrets.token_hex(16)
c1 = secrets.token_hex(16)

decrypt_1 = json.loads(rq.get(url + "/receive/" + c0 + c1 + "/").content.decode())['error']

message_len = len("Invalid plaintext: ")
p1 = decrypt_1[message_len : message_len + 32]
p2 = decrypt_1[message_len + 32 : message_len + 64]

decrypt_2 = json.loads(rq.get(url + "/receive/" + c1 + "/").content.decode())['error']
p2_ = decrypt_2[message_len : message_len + 32]

modified_iv = xor(bytes.fromhex(p2), bytes.fromhex(p2_), bytes.fromhex(c0))

get_flag = json.loads(rq.get(url + "/get_flag/" + modified_iv.hex() +"/").content.decode())['plaintext']

print(f"Flag: {bytes.fromhex(get_flag).decode('utf-8')}")
