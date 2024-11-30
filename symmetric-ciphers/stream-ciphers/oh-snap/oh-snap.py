import json
import requests
import time
import string
import secrets

def request_timeout_retry(url):
        # Timeouts happen ofter in this challenge and we have to make a lot of requests until we receive the flag
        # So I added a retry request mechanism
        max_retries = 10
        retry_delay = 5
        retry_count = 0
        while True:
            try:
                response = requests.get(url)
                response.raise_for_status()
                return json.loads(response.content.decode())
            except requests.exceptions.Timeout:
                retry_count += 1
                if retry_count > max_retries:
                    break
                print(f"Timeout occurred. Retrying... ({retry_count}/{max_retries})")
                time.sleep(retry_delay)
            except requests.exceptions.RequestException as e:
                print(f"An error occurred: {e}")
        exit()

def xor(arr1, arr2):
    if len(arr1) != len(arr2):
        raise ValueError("Byte arrays must have the same length")

    return bytes([a ^ b for a, b in zip(arr1, arr2)])

# https://kevinliu.me/posts/rc4/
def fms(url):
    curKey = b''
    A = 0

    while True:
        results = []
        for x in range(256):
            # Construct weak IVS
            IV = bytes([A + 3, 255, x])
            
            ct = secrets.token_bytes(32).hex()

            response = request_timeout_retry(url + ct + "/" + IV.hex() + "/")['error']
            pt = response[len("Unknown command: "):]
            
            keystream = xor(bytes.fromhex(ct), bytes.fromhex(pt))
            knownKey = IV + curKey

            # Run KSA iterations with known key bytes
            S = [i for i in range(256)]
            j = 0
            for i in range(A + 3):
                j = (j + S[i] + knownKey[i % len(knownKey)]) % 256
                S[i], S[j] = S[j], S[i]
            i += 1
            # Store the most likely next key byte
            results.append((keystream[0] - j - S[i]) % 256)

        # Next byte of the key should be the most common one
        nextByte = max(set(results), key = results.count)
        curKey += bytes([nextByte])
        print(f'[+] Current Key: {curKey}')
        if b'}' in curKey:
            print("Done!")
            exit()

        # Repeat for the next byte
        A += 1
    
url = "https://aes.cryptohack.org/oh_snap/send_cmd/"
fms(url)