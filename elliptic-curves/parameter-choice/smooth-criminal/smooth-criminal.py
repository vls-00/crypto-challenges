import hashlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import hashlib

def point_addition(P, Q, a, p):
    if P == (None, None):
            return Q
    if Q == (None, None):
        return P
        
    px, py = P
    qx, qy = Q
    
    if px == qx and py == -qy % p:
        return (None, None)
    
    if px == qx and py == qy:
        k = ((3 * px**2 + a) * pow(2 * py, -1, p)) % p
    else:
        k = ((qy - py) * pow(qx - px, -1, p)) % p
    
    rx = (k**2 - px - qx) % p
    ry = (k*(px - rx) - py) % p
    return (rx, ry)

def scalar_mult(P, n, a, p):
    R = (None, None)
    Q = P

    while n > 0:
        if n % 2 == 1:
            R = point_addition(R, Q, a, p)

        Q = point_addition(Q, Q, a, p)
        n //= 2

    return R

def is_pkcs7_padded(message):
    padding = message[-message[-1]:]
    return all(padding[i] == len(padding) for i in range(0, len(padding)))


def decrypt_flag(shared_secret: int, iv: str, ciphertext: str):
    # Derive AES key from shared secret
    sha1 = hashlib.sha1()
    sha1.update(str(shared_secret).encode('ascii'))
    key = sha1.digest()[:16]
    # Decrypt flag
    ciphertext = bytes.fromhex(ciphertext)
    iv = bytes.fromhex(iv)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext)

    if is_pkcs7_padded(plaintext):
        return unpad(plaintext, 16).decode('ascii')
    else:
        return plaintext.decode('ascii')

iv = "07e2628b590095a5e332d397b8a59aa7"
ciphertext = "8220b7c47b36777a737f5ef9caa2814cf20c1c1ef496ec21a9b4833da24a008d0870d3ac3a6ad80065c138a2ed6136af"

a = 2
b = 3
p = 310717010502520989590157367261876774703

# Use below code in sage math to calculate Bob's nb
# E = EllipticCurve(GF(p), [a,b])
# G = E(179210853392303317793440285562762725654,105268671499942631758568591033409611165)
# QA = E(280810182131414898730378982766101210916, 291506490768054478159835604632710368904)
# QB = E(272640099140026426377756188075937988094, 51062462309521034358726608268084433317)
# nb = G.discrete_log(QB)

QA = (280810182131414898730378982766101210916, 291506490768054478159835604632710368904)
nb = 23364484702955482300431942169743298535

secret, _ = scalar_mult(QA, n=nb, a=a, p=p)

print(decrypt_flag(secret, iv, ciphertext))