import jwt
import requests as rq
import json

url = "https://web.cryptohack.org/no-way-jose"
session_response = json.loads(rq.get(url + "/create_session/admin").content.decode())
token = session_response["session"]


payload = jwt.decode(token, options={"verify_signature": False})

# Payload modification to impersonate the admin
payload['admin'] = True

new_token = jwt.encode(payload, None, algorithm='none')
print(f'Forged token: {new_token}\n')

authorise = rq.get(url + "/authorise/" + new_token + "/")

print(f'Flag: {authorise.content.decode('utf-8')}')