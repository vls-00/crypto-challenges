from Crypto.Util.number import long_to_bytes
import sage.all

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

# https://github.com/jvdsn/crypto-attacks/blob/master/attacks/ecc/parameter_recovery.py
def recover_a_b(p, x1, y1, x2, y2):
    """
    Recovers the a and b parameters from an elliptic curve when two points are known.
    :param p: the prime of the curve base ring
    :param x1: the x coordinate of the first point
    :param y1: the y coordinate of the first point
    :param x2: the x coordinate of the second point
    :param y2: the y coordinate of the second point
    :return: a tuple containing the a and b parameters of the elliptic curve
    """
    a = pow(x1 - x2, -1, p) * (pow(y1, 2, p) - pow(y2, 2, p) - (pow(x1, 3, p) - pow(x2, 3, p))) % p
    b = (pow(y1, 2, p) - pow(x1, 3, p) - a * x1) % p
    return int(a), int(b)

# https://github.com/jvdsn/crypto-attacks/blob/master/attacks/ecc/singular_curve.py
def singular_curve_attack(p, a2, a4, a6, Gx, Gy, Px, Py):
    """
    Solves the discrete logarithm problem on a singular curve (y^2 = x^3 + a2 * x^2 + a4 * x + a6).
    :param p: the prime of the curve base ring
    :param a2: the a2 parameter of the curve
    :param a4: the a4 parameter of the curve
    :param a6: the a6 parameter of the curve
    :param Gx: the base point x value
    :param Gy: the base point y value
    :param Px: the point multiplication result x value
    :param Py: the point multiplication result y value
    :return: l such that l * G == P
    """
    x = GF(p)["x"].gen()
    f = x ** 3 + a2 * x ** 2 + a4 * x + a6
    roots = f.roots()

    # Singular point is a cusp.
    if len(roots) == 1:
        alpha = roots[0][0]
        u = (Gx - alpha) / Gy
        v = (Px - alpha) / Py
        return int(v / u)

    # Singular point is a node.
    if len(roots) == 2:
        if roots[0][1] == 2:
            alpha = roots[0][0]
            beta = roots[1][0]
        elif roots[1][1] == 2:
            alpha = roots[1][0]
            beta = roots[0][0]
        else:
            raise ValueError("Expected root with multiplicity 2.")

        t = (alpha - beta).sqrt()
        u = (Gy + t * (Gx - alpha)) / (Gy - t * (Gx - alpha))
        v = (Py + t * (Px - alpha)) / (Py - t * (Px - alpha))
        return int(v.log(u))

    raise ValueError(f"Unexpected number of roots {len(roots)}.")

p = 4368590184733545720227961182704359358435747188309319510520316493183539079703

ax = 2582928974243465355371953056699793745022552378548418288211138499777818633265
ay = 2421683573446497972507172385881793260176370025964652384676141384239699096612

gx = 8742397231329873984594235438374590234800923467289367269837473862487362482
gy = 225987949353410341392975247044711665782695329311463646299187580326445253608

a, b = recover_a_b(p, ax, ay, gx, gy)

discriminant = 16 * (4 * a**3 + 27 * b**2)
assert discriminant % p == 0

n = singular_curve_attack(p, 0, a, b, gx, gy, ax, ay)

print(long_to_bytes(n).decode('ascii'))