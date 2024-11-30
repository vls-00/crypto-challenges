import json
import requests
from Crypto.Util.Padding import unpad

url = "https://aes.cryptohack.org/triple_des/"

key = "0101010101010101" + "FEFEFEFEFEFEFEFE"

flag = json.loads(requests.get(url + "/encrypt_flag/" + key + "/").content.decode())['ciphertext']
flag = json.loads(requests.get(url + "/encrypt/" + key + "/" + flag + "/").content.decode())['ciphertext']

print(bytes.fromhex(flag))