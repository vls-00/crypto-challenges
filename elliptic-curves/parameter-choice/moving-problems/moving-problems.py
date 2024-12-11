import hashlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import hashlib
from sage.all import *

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

def get_embedding_degree(q, n, max_k):
    """
    Returns the embedding degree k of an elliptic curve.
    Note: strictly speaking this function computes the Tate-embedding degree of a curve.
    In almost all cases, the Tate-embedding degree is the same as the Weil-embedding degree (also just called the "embedding degree").
    More information: Maas M., "Pairing-Based Cryptography" (Section 5.2)
    :param q: the order of the curve base ring
    :param n: the order of the base point
    :param max_k: the maximum value of embedding degree to try
    :return: the embedding degree k, or None if it was not found
    """
    for k in range(1, max_k + 1):
        if q ** k % n == 1:
            return k

    return None

def mov_attack(P, R, max_k=6, max_tries=10):
    """
    Solves the discrete logarithm problem using the MOV attack.
    More information: Harasawa R. et al., "Comparing the MOV and FR Reductions in Elliptic Curve Cryptography" (Section 2)
    :param P: the base point
    :param R: the point multiplication result
    :param max_k: the maximum value of embedding degree to try (default: 6)
    :param max_tries: the maximum amount of times to try to find l (default: 10)
    :return: l such that l * P == R, or None if l was not found
    """
    E = P.curve()
    q = E.base_ring().order()
    n = P.order()
    assert gcd(n, q) == 1, "GCD of base point order and curve base ring order should be 1."

    k = get_embedding_degree(q, n, max_k)
    if k is None:
        return None

    Ek = E.base_extend(GF(q ** k))
    Pk = Ek(P)
    Rk = Ek(R)
    for i in range(max_tries):
        Q_ = Ek.random_point()
        m = Q_.order()
        d = gcd(m, n)
        Q = (m // d) * Q_
        if Q.order() != n:
            continue

        if (alpha := Pk.weil_pairing(Q, n)) == 1:
            continue

        beta = Rk.weil_pairing(Q, n)
        l = beta.log(alpha)
        return int(l)

    return None

iv = "eac58c26203c04f68d63dc2c58d79aca"
ciphertext = "bb9ecbd3662d0671fd222ccb07e27b5500f304e3621a6f8e9c815bc8e4e6ee6ebc718ce9ca115cb4e41acb90dbcabb0d"

p = 1331169830894825846283645180581
a = -35
b = 98

E = EllipticCurve(GF(p), [a,b])

A= E(1110072782478160369250829345256, 800079550745409318906383650948)
G = E(479691812266187139164535778017, 568535594075310466177352868412)
B = E(1290982289093010194550717223760, 762857612860564354370535420319)

order = E.order()
k = 1
while (p**k - 1) % order:
    k += 1
    if k > 100:
        print("The degree is over 100...")
        break
print(f"Embedding degree: {k}")

assert k < 100

nb = mov_attack(G, B)
secret, _ = scalar_mult(A, n=nb, a=a, p=p)
print(decrypt_flag(secret, iv, ciphertext))