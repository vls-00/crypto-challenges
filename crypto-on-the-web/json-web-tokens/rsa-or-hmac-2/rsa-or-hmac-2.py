import jwt
import requests as rq
import json
import subprocess

url = "https://web.cryptohack.org/rsa-or-hmac-2"
session_response1 = json.loads(rq.get(url + "/create_session/admin").content.decode())
token1 = session_response1["session"]
session_response2 = json.loads(rq.get(url + "/create_session/user").content.decode())
token2 = session_response2["session"]

print(f'[+] Initial token 1: {token1}\n')
print(f'[+] Initial token 2: {token2}\n')


jwt_forgery_result = subprocess.run(['python3', 'jwt-forgery.py', token1, token2], capture_output=True, text=True)

pem_files = []
for line in jwt_forgery_result.stdout.splitlines():
    # Find the lines from the output that include the .pem filenames
    if line.startswith("[+] Written to"):
        pem_files.append(line)

# Find the PKCS1 file which is the public key because the programm makes 2 .pem files
for file in pem_files:
    if "pkcs1" in file:
        # Throw the first 15 characters from the output so we keep only the filename
        pkcs1_filename = file[15:]

PUBLIC_KEY = open(pkcs1_filename, 'rb').read()
payload = {'username': "admin", 'admin': True}

new_token = jwt.encode(payload, PUBLIC_KEY, 'HS256')
print(f'[+] Forged token using the public key: {new_token}\n')

authorise = rq.get(url + "/authorise/" + new_token + "/")

print(f'[$] Flag: {authorise.content.decode('utf-8')}')