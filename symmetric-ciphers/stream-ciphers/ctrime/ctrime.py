import requests as rq
import json
import requests
import time
import string

def request_timeout_retry(plaintext):
        # Timeouts happen ofter in this challenge and we have to make a lot of requests until we receive the flag
        # So I added a retry request mechanism
        max_retries = 10
        retry_delay = 5
        retry_count = 0
        while True:
            try:
                response = rq.get(url + "/encrypt/" + plaintext.encode().hex() +"/")
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

url = "https://aes.cryptohack.org/ctrime/"

possible_characters = string.ascii_letters + string.digits + "_}"
flag = "crypto{"

initial_ct = request_timeout_retry(flag)
target_length = len(initial_ct)

while True:
    for char in possible_characters:
        plaintext = flag + char

        time.sleep(1)
        ct = request_timeout_retry(plaintext)
        
        if len(ct) == target_length:
            flag += char
            print("[+] Current flag: " + flag)
            if (char == "}"):
                exit()
            break
        elif len(ct) != target_length and char == "}":
            for char in possible_characters:
                previous_ct_len = 0
                break_outer = False
                for i in range(1, 6):
                    plaintext = flag + (i * char)
                    time.sleep(1)
                    ct = request_timeout_retry(plaintext)

                    if len(ct) < previous_ct_len:
                        flag += char
                        print("[+] Current flag: " + flag)
                        time.sleep(1)
                        target_length = len(request_timeout_retry(flag))
                        print(f"New target length: {target_length}")
                        break_outer = True
                        break
                    previous_ct_len = len(ct)
                if break_outer:
                    break
