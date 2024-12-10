import requests as rq
import json

url = "https://web.cryptohack.org/digestive"

username = "admin"
signature = json.loads(rq.get(url + "/sign/" + username + "/").content.decode())['signature']

msg = '{"admin": false, "username": "' + username + '", "admin": true}'

verify = json.loads(rq.get(url + "/verify/" + msg + "/" + signature + "/").content.decode())
print(f'Flag: {verify['flag']}')