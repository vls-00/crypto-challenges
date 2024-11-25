import requests as rq
import json

url = "https://aes.cryptohack.org/block_cipher_starter/"

encrypted_flag = json.loads(rq.get(url + "/encrypt_flag/").content.decode())
ct = encrypted_flag["ciphertext"]

decrypt = json.loads(rq.get(url + "/decrypt/" + ct + "/").content.decode())

print(f'Flag: {bytes.fromhex(decrypt['plaintext'])}')