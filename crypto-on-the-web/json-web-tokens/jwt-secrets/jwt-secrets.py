import jwt
import json
import requests as rq

url = "https://web.cryptohack.org/jwt-secrets"
session_response = json.loads(rq.get(url + "/create_session/admin").content.decode())
token = session_response["session"]

key = "secret"
payload = jwt.decode(token, key, algorithms="HS256")
payload['admin'] = True

new_key = jwt.encode(payload, key, "HS256")

authorise = rq.get(url + "/authorise/" + new_key + "/")

print(f'Flag: {authorise.content.decode('utf-8')}')