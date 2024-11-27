import requests as rq
import json
from pwn import xor
import secrets
from Crypto.Cipher import AES
import os

url = "https://aes.cryptohack.org/bean_counter/"

encrypted = json.loads(rq.get(url + "/encrypt/").content.decode())['encrypted']

#https://en.wikipedia.org/wiki/PNG
png_image_header = "89504e470d0a1a0a0000000d49484452"

key = xor(bytes.fromhex(png_image_header), bytes.fromhex(encrypted[:32]))

image = b''

for i in range(1, len(encrypted) // 32 + 1):
    start = 32 * (i - 1)
    end = 32 * i
    image += xor(key, bytes.fromhex(encrypted[start:end]))

with open("./flag.png", "wb") as png_file:
    png_file.write(image)