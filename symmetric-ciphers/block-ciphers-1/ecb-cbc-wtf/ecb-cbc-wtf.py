import requests as rq
import json
from pwn import xor

url = "https://aes.cryptohack.org/ecbcbcwtf/"

encrypt_flag = json.loads(rq.get(url + "/encrypt_flag/").content.decode())
ct = encrypt_flag["ciphertext"]

iv = ct[:32]
block_1 = ct[32:64]
block_2 = ct[64:]

decrypted_1 = json.loads(rq.get(url + "/decrypt/" + block_1 + "/").content.decode())['plaintext']
decrypted_2 = json.loads(rq.get(url + "/decrypt/" + block_2 + "/").content.decode())['plaintext']

plaintext_1 = xor(bytes.fromhex(decrypted_1), bytes.fromhex(iv))
plaintext_2 = xor(bytes.fromhex(decrypted_2), bytes.fromhex(block_1))
print(f'Flag: {plaintext_1.decode('utf-8')}{plaintext_2.decode('utf-8')}')