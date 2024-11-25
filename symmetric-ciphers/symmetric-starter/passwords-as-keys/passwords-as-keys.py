import requests as rq
import json
import hashlib

url = "https://aes.cryptohack.org/passwords_as_keys/"

encrypted_flag = json.loads(rq.get(url + "/encrypt_flag/").content.decode())
ct = encrypted_flag["ciphertext"]

with open("CRYPTO\symmetric-ciphers\symmetric-starter\passwords-as-keys\words.txt") as f:
    words = [w.strip() for w in f.readlines()]

for word in words:
    key = hashlib.md5(word.encode()).digest()
    decrypted = json.loads(rq.get(url + "/decrypt/" + ct + "/" + key.hex() + "/").content.decode())
    flag = bytes.fromhex(decrypted['plaintext'])
    if b'crypto{' in flag:
        print(f'Flag:{flag}')
        break
