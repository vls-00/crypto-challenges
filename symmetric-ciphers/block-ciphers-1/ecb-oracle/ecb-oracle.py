import requests as rq
import json
from Crypto.Util.Padding import pad

def find_pad_border(original_size):
    test_hex = "ff"
    border = 1
    while True:
        size_test = json.loads(rq.get(url + "/encrypt/" + test_hex + "/").content.decode())
        if original_size < len(size_test["ciphertext"]):
            break
        test_hex += "ff"
        border += 1
    return border

url = "https://aes.cryptohack.org/ecb_oracle/"

size_test = json.loads(rq.get(url + "/encrypt/ff").content.decode())
ct_size = len(size_test["ciphertext"])

pad_border = find_pad_border(ct_size)

# border + flag_legth = 17 chars (34 hex chars) => flag_length = 17 - border
flag_size = (ct_size - pad_border * 2) // 2

possible_characters = "abcdefghijklmnopqrstuvwxyz0123456789_"
lookup = {}
flag = "}"
block_number = 1

# Add 1 more to the border because we already know that the last character is '}', so we start by pushing 2 characters
pad_border += 1


for i in range(flag_size - len("crypto{}")):
    # Build the lookup table for each character
    for char in possible_characters:
        candidate = pad(char.encode() + flag.encode() , 16)
        response = bytes.fromhex(json.loads(rq.get(url + "/encrypt/" + candidate.hex() + "/").content.decode())["ciphertext"])
        lookup[response[:16]] = char
    
    # Add pad to push the next flag character into the next block
    pad_border += 1
    prefix = ""
    for j in range(pad_border):
        prefix += "ff"
    
    response = bytes.fromhex(json.loads(rq.get(url + "/encrypt/" + prefix + "/").content.decode())["ciphertext"])
    
    # Take the corresponding character from the dictionary that matches the last 16 bytes of the response (pushed flag characters)
    flag = lookup[response[32:48]] + flag

    print(f"[+] Current flag: {flag}")
    lookup.clear()
    
print("----Done!----")
print("Flag: crypto" + "{" + flag)

