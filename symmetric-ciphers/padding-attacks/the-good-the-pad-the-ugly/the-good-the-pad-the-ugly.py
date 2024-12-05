import json
from pwn import *
        
MAX_LUCKY_CHECKS = 20

def json_recv():
    line = r.readline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)

def oracle(iv , ct):
    check_padding_req = {
            "option":"unpad",
            "ct": iv.hex() + ct
    }
    for i in range(MAX_LUCKY_CHECKS):
        json_send(check_padding_req)

        if json_recv()["result"] == False:
            return False
    return True

def single_block_attack(block, BLOCK_SIZE):
    # zeroing_iv starts out nulled. each iteration of the main loop will add
    # one byte to it, working from right to left, until it is fully populated,
    # at which point it contains the result of DEC(ct_block)
    # zeroin_iv is block cipher output
    zeroing_iv = [0] * BLOCK_SIZE

    for pad_val in range(1, BLOCK_SIZE+1):
        padding_iv = [pad_val ^ b for b in zeroing_iv]

        for candidate in range(256):
            padding_iv[-pad_val] = candidate
            iv = bytes(padding_iv)
            if oracle(iv, block):
                if pad_val == 1:
                    padding_iv[-2] ^= 1
                    iv = bytes(padding_iv)
                    if not oracle(iv, block):
                        continue # false positive; keep searchin
                break
        else:
            raise Exception("no valid padding byte found (is the oracle working correctly?)")

        zeroing_iv[-pad_val] = candidate ^ pad_val
        print(zeroing_iv)

    return zeroing_iv

def full_attack(iv, ct, BLOCK_SIZE):
    assert len(iv) == BLOCK_SIZE and len(ct) % BLOCK_SIZE == 0

    msg = iv + ct
    blocks = [msg[i:i+BLOCK_SIZE] for i in range(0, len(msg), BLOCK_SIZE)]
    result = b''

    # loop over pairs of consecutive blocks performing CBC decryption on them
    iv = blocks[0]
    for ct in blocks[1:]:
        dec = single_block_attack(ct.hex(), BLOCK_SIZE)
        pt = bytes(iv_byte ^ dec_byte for iv_byte, dec_byte in zip(iv, dec))
        result += pt
        iv = ct

    return result

HOST = "socket.cryptohack.org"
PORT = 13422
r = remote(HOST, PORT)

# ignore first message
r.readline()

encrypt_req = {
    "option":"encrypt"
}
json_send(encrypt_req)

response = json_recv()["ct"]
original_iv = response[:32]
ct = response[32:]

pt = full_attack(bytes.fromhex(original_iv), bytes.fromhex(ct), 16)
message = bytes.fromhex(pt.decode('utf-8'))

check = {
    "option":"check",
    "message": message.hex()
}
json_send(check)

print(f"Flag: {json_recv()}")