from pwn import *
import json
from Crypto.Util.number import bytes_to_long, long_to_bytes
from sympy import integer_nthroot
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
import gmpy2
    
def json_recv():
    line = r.readline()
    return json.loads(line)

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)
        
def create_power_with_target_suffix_decimal(target, e):
    length = len(str(target))
    
    result = ""
    for i in range(1, length+1):
        for j in range(0, 10):
            if i == 1:
                if pow(j, e, 16**i) == pow(target, 1, 10**i):
                    result = f"{j}"
                    break
            else:
                int_result = int(f"{j}{result}")
                if pow(int_result, e, 10**i) == pow(target, 1, 10**i):
                    result = f"{j}{result}"
                    break
            
    if len(result) != length:
        print("Error: Cannot find a base with this power that has the desired suffix.")
        return
    return int(result)

def create_power_with_target_suffix_hexadecimal(target, e):
    length = len(target)
    
    result = ""
    for i in range(1, length + 1):
        for j in "0123456789abcdef":
            if i == 1:
                if pow(int(j, 16), e, 16**i) == pow(int(target, 16), 1, 16**i):
                    result = f"{j}"
                    break
            else:
                hex_result = f"{j}{result}"
                if pow(int(hex_result, 16), e, 16**i) == pow(int(target, 16), 1, 16**i):
                    result = hex_result
                    break
    
    if len(result) != length:
        print("Error: Cannot find a base with this power that has the desired suffix.")
        return
    return result
            
HOST = "socket.cryptohack.org"
PORT = 13375
r = remote(HOST, PORT)

# Ignore the first message
r.readline()

n = 22266616657574989868109324252160663470925207690694094953312891282341426880506924648525181014287214350136557941201445475540830225059514652125310445352175047408966028497316806142156338927162621004774769949534239479839334209147097793526879762417526445739552772039876568156469224491682030314994880247983332964121759307658270083947005466578077153185206199759569902810832114058818478518470715726064960617482910172035743003538122402440142861494899725720505181663738931151677884218457824676140190841393217857683627886497104915390385283364971133316672332846071665082777884028170668140862010444247560019193505999704028222347577
e = 3

vote = b'pad\00VOTE FOR PEDRO'

cubic_root = create_power_with_target_suffix_hexadecimal(vote.hex(), e)

assert cubic_root != None
assert int(cubic_root, 16) ** 3 < n

send_vote = {
    "option": "vote",
    "vote": cubic_root
}
json_send(send_vote)
print(f"Flag: {json_recv()}")
