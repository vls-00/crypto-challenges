import requests as rq
import json
from pwn import xor
import secrets

url = "https://aes.cryptohack.org/symmetry/"

get_flag = json.loads(rq.get(url + "/encrypt_flag/").content.decode())['ciphertext']
iv = get_flag[:32]
flag_ct_part_1 = get_flag[32:64]
flag_ct_part_2 = get_flag[64:96]
flag_ct_part_3 = get_flag[96:]

dummy_pt = secrets.token_hex(16 * 3)
ct = json.loads(rq.get(url + "/encrypt/" + dummy_pt + "/" + iv + "/").content.decode())['ciphertext']

output_iv_block_1 = xor(bytes.fromhex(ct[:32]), bytes.fromhex(dummy_pt[:32]))
output_iv_block_2 = xor(bytes.fromhex(ct[32:64]), bytes.fromhex(dummy_pt[32:64]))
output_iv_block_3 = xor(bytes.fromhex(ct[64:]), bytes.fromhex(dummy_pt[64:]))

flag_part_1 = xor(bytes.fromhex(flag_ct_part_1), output_iv_block_1)
flag_part_2 = xor(bytes.fromhex(flag_ct_part_2), output_iv_block_2)
flag_part_3 = xor(bytes.fromhex(flag_ct_part_3), output_iv_block_3)

print(f"Flag: {flag_part_1 + flag_part_2 + flag_part_3}")
