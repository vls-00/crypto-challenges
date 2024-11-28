import requests
import json
import time
from pwn import xor
import string

MAX_CLONE_VALUES_RETURNED = 100
MAX_MATCHING_TEXTS = 50
POSSIBLE_CHARACTERS = string.ascii_letters + string.digits + " " + string.punctuation

def request_timeout_retry():
        # Timeouts happen ofter in this challenge and we have to make a lot of requests until we receive the flag
        # So I added a retry request mechanism
        max_retries = 10
        retry_delay = 5
        retry_count = 0
        while True:
            try:
                response = requests.get(url + "/encrypt/")
                response.raise_for_status()
                return json.loads(response.content.decode())['ciphertext']
            except requests.exceptions.Timeout:
                retry_count += 1
                if retry_count > max_retries:
                    break
                print(f"Timeout occurred. Retrying... ({retry_count}/{max_retries})")
                time.sleep(retry_delay)
            except requests.exceptions.RequestException as e:
                print(f"An error occurred: {e}")
        exit()

def find_matching_byte(ciphertexts, block_output_prefix):
    for possible_byte in range(256):
        candidate = block_output_prefix + bytes([possible_byte])
        for test_ct in ciphertexts:
            try:
                plaintext = xor(candidate, bytes.fromhex(test_ct)[:len(candidate)]).decode('ascii')
                for char in plaintext:
                    if char not in POSSIBLE_CHARACTERS:
                        raise Exception
                if test_ct == ciphertexts[-1]:
                    return possible_byte
            except:
                break
        
def find_block_output_prefix(ciphertexts, known):
    for ct in ciphertexts:
        possible_block_output_prefix = xor(known.encode()[:len(bytes.fromhex(ct))], bytes.fromhex(ct)[:len(known)])
        for test_ct in ciphertexts:
            try:
                test_ct_bytes = bytes.fromhex(test_ct)
                if len(possible_block_output_prefix) > len(test_ct_bytes):
                    print(f"[+] Updated block output prefix: {possible_block_output_prefix}")
                    return possible_block_output_prefix, ct
                plaintext = xor(possible_block_output_prefix, test_ct_bytes[:len(possible_block_output_prefix)]).decode('ascii')
                for char in plaintext:
                    if char not in POSSIBLE_CHARACTERS:
                        raise Exception
                if test_ct == ciphertexts[-1]:
                    print(f"[+] Updated block output prefix: {possible_block_output_prefix}")
                    return possible_block_output_prefix, ct
            except:
                break

def print_plaintext_progress(ciphertexts, block_output_prefix):
    for ct in ciphertexts:
        print(xor(bytes.fromhex(ct)[:len(block_output_prefix)], block_output_prefix[:len(ct)]))
        
def guess_text_and_print_plaintexts(text, ciphertexts):
    block_output_prefix, _ = find_block_output_prefix(ciphertexts, text)
    print_plaintext_progress(ciphertexts, block_output_prefix)
    
url = "https://aes.cryptohack.org/stream_consciousness"
ciphertexts = []

# Fill the array with all possible ciphertexts
ct_copy_counter = 0
while ct_copy_counter < MAX_CLONE_VALUES_RETURNED:
    time.sleep(1)
    ct = request_timeout_retry()
    if ct not in ciphertexts:
        ciphertexts.append(ct)
        ct_copy_counter = 0
    ct_copy_counter += 1

ciphertexts = sorted(ciphertexts, key=len, reverse=True)
flag_prefix = "crypto{"
block_output_prefix, flag_ct = find_block_output_prefix(ciphertexts, flag_prefix)

print_plaintext_progress(ciphertexts, block_output_prefix)

# Uncomment to brute-force and see the next 4 characters
# for index in range(len(block_output_prefix) + 1, 17):
#     matching_char = find_matching_byte(ciphertexts, block_output_prefix)
#     if matching_char == None:
#         break
#     block_output_prefix += bytes([matching_char])
    
guess_text_and_print_plaintexts("crypto{k3y5", ciphertexts)
guess_text_and_print_plaintexts("What a nasty", ciphertexts)
guess_text_and_print_plaintexts("Love, probabl", ciphertexts)
guess_text_and_print_plaintexts("Love, probably", ciphertexts)
guess_text_and_print_plaintexts("But I will show", ciphertexts)
guess_text_and_print_plaintexts("Dolly will think", ciphertexts)
guess_text_and_print_plaintexts("Three boys running", ciphertexts)
guess_text_and_print_plaintexts("Would I have believ", ciphertexts)
guess_text_and_print_plaintexts("It can't be torn out", ciphertexts)
guess_text_and_print_plaintexts("I'm unhappy, I deserve", ciphertexts)
guess_text_and_print_plaintexts("I'm unhappy, I deserve ", ciphertexts)
guess_text_and_print_plaintexts("I shall lose everything ", ciphertexts)
guess_text_and_print_plaintexts("The terrible thing is that", ciphertexts)
guess_text_and_print_plaintexts("I shall, I'll lose everything", ciphertexts)
guess_text_and_print_plaintexts("Love, probably? They don't know", ciphertexts)
guess_text_and_print_plaintexts("Dolly will think that I'm leaving", ciphertexts)
