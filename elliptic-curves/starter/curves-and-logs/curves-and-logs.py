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

a = 497
b = 1768
p = 9739

G = (1804,5368)
n = 1829

QA = (815,3190)

result = scalar_mult(QA, n=n, a=a, p=p)
print(f"Shared secret point: {result}")

x, _ = result
print(f"SHA-1 hash: {hashlib.sha1(str(x).encode()).hexdigest()}")