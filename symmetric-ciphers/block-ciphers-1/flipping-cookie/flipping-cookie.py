import requests as rq
import json
from pwn import xor

url = "https://aes.cryptohack.org/flipping_cookie/"

cookie = json.loads(rq.get(url + "/get_cookie").content.decode())['cookie']
iv = cookie[:32]
ct = cookie[32:]
cookie_first_16 = b'admin=False;expi'
cookie_modified_first_16 = b'admin=True;;expi'

# block_1_output ^ iv = cookie_first_16
block_output = xor(bytes.fromhex(iv), cookie_first_16)

# block_1_output ^ modified_iv = cookie_modified_first_16
modified_iv = xor(cookie_modified_first_16, block_output)

print(json.loads(rq.get(url + "/check_admin/" + ct + "/" + modified_iv.hex() +"/").content.decode()))
