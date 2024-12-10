import hashlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import hashlib
from sage.all import EllipticCurve
from sage.all import Qq
from sage.all import ZZ

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

# Convert a field element to a p-adic number.
def _gf_to_qq(n, qq, x):
    return ZZ(x) if n == 1 else qq(list(map(int, x.polynomial())))


# Lift a point to the p-adic numbers.
def _lift(E, p, Px, Py):
    for P in E.lift_x(Px, all=True):
        if (P.xy()[1] % p) == Py:
            return P


def smart_attack(G, P):
    """
    Solves the discrete logarithm problem using Smart's attack.
    More information: Smart N. P., "The Discrete Logarithm Problem on Elliptic Curves of Trace One"
    More information: Hofman S. J., "The Discrete Logarithm Problem on Anomalous Elliptic Curves" (Section 6)
    :param G: the base point
    :param P: the point multiplication result
    :return: l such that l * G == P
    """
    E = G.curve()
    assert E.trace_of_frobenius() == 1, f"Curve should have trace of Frobenius = 1."

    F = E.base_ring()
    p = F.characteristic()
    q = F.order()
    n = F.degree()
    qq = Qq(q, names="g")

    # Section 6.1: case where n == 1
    E = EllipticCurve(qq, [_gf_to_qq(n, qq, a) + q * ZZ.random_element(1, q) for a in E.a_invariants()])
    Gx, Gy = _gf_to_qq(n, qq, G.xy()[0]), _gf_to_qq(n, qq, G.xy()[1])
    Gx, Gy = (q * _lift(E, p, Gx, Gy)).xy()
    Px, Py = _gf_to_qq(n, qq, P.xy()[0]), _gf_to_qq(n, qq, P.xy()[1])
    Px, Py = (q * _lift(E, p, Px, Py)).xy()
    l = ZZ(((Px / Py) / (Gx / Gy)) % p)

    if n > 1:
        # Section 6.2: case where n > 1
        G0 = p ** (n - 1) * G
        G0x, G0y = _gf_to_qq(n, qq, G0.xy()[0]), _gf_to_qq(n, qq, G0.xy()[1])
        G0x, G0y = (q * _lift(E, p, G0x, G0y)).xy()
        for i in range(1, n):
            Pi = p ** (n - i - 1) * (P - l * G)
            if Pi.is_zero():
                continue

            Pix, Piy = _gf_to_qq(n, qq, Pi.xy()[0]), _gf_to_qq(n, qq, Pi.xy()[1])
            Pix, Piy = (q * _lift(E, p, Pix, Piy)).xy()
            l += p ** i * ZZ(((Pix / Piy) / (G0x / G0y)) % p)

    return int(l)

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

iv = "719700b2470525781cc844db1febd994"
ciphertext = "335470f413c225b705db2e930b9d460d3947b3836059fb890b044e46cbb343f0"

p = 0xa15c4fb663a578d8b2496d3151a946119ee42695e18e13e90600192b1d0abdbb6f787f90c8d102ff88e284dd4526f5f6b6c980bf88f1d0490714b67e8a2a2b77
a = 0x5e009506fcc7eff573bc960d88638fe25e76a9b6c7caeea072a27dcd1fa46abb15b7b6210cf90caba982893ee2779669bac06e267013486b22ff3e24abae2d42
b = 0x2ce7d1ca4493b0977f088f6d30d9241f8048fdea112cc385b793bce953998caae680864a7d3aa437ea3ffd1441ca3fb352b0b710bb3f053e980e503be9a7fece

E = EllipticCurve(GF(p), [a, b])
G = E(0x39f15e024d44228fd11c58a71c312fd64167c7d249d5677da0dfb4b9c3ed0f90701837a5e77b5a2b74433d7fbe027cd0c73b5aa7b300f7384521af0dc283dc6d,
      0x5f3636a89167a6fbb7b7d1ad97d11c70756835b5f1273e20c06d9e022d74648ec22a3f92c378196d137c3f2027a67381be79e1c0d65cd9b61211a77a3842c8b2)

A = E(0x5aa8b5cf3124c552881ba67c14c863bb2ff30d960fe41b61123d2025cdddf0ea75e92d76326be9fb09b9a32373fc278ac8d5cf5ca83b9e517ce347c6879bef51,
      0x2e3ddec1b35930b1039351b2814252186b30ce27ce15eda4351428868ae8593ab8c61c034ba10041cce205d7f7102c292f30ac5f3d2a2c2f3a463d837df070cd)

B = (int("0x7f0489e4efe6905f039476db54f9b6eac654c780342169155344abc5ac90167adc6b8dabacec643cbe420abffe9760cbc3e8a2b508d24779461c19b20e242a38", 16), 
  int("0xdd04134e747354e5b9618d8cb3f60e03a74a709d4956641b234daa8a65d43df34e18d00a59c070801178d198e8905ef670118c15b0906d3a00a662d3a2736bf", 16))

na = smart_attack(G, A)
secret, _ = scalar_mult(B, n=na, a=a, p=p)

print(decrypt_flag(secret, iv, ciphertext))
