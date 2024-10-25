import jwt
import requests as rq
import json

url = "https://web.cryptohack.org/rsa-or-hmac"
session_response = json.loads(rq.get(url + "/create_session/admin").content.decode())
token = session_response["session"]

PUBLIC_KEY = json.loads(rq.get(url + "/get_pubkey/").content.decode())["pubkey"]

payload = jwt.decode(token, options={"verify_signature": False})
# Payload modification to impersonate the admin
payload['admin'] = True

new_key = jwt.encode(payload, PUBLIC_KEY, 'HS256')

authorise = rq.get(url + "/authorise/" + new_key + "/")

print(f'Flag: {authorise.content.decode('utf-8')}')