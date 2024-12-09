def point_addition(P, Q, a, n):
    if P == (None, None):
            return Q
    if Q == (None, None):
        return P
        
    px, py = P
    qx, qy = Q
    
    if px == qx and py == -qy % n:
        return (None, None)
    
    if px == qx and py == qy:
        k = ((3 * px**2 + a) * pow(2 * py, -1, n)) % n
    else:
        k = ((qy - py) * pow(qx - px, -1, n)) % n
    
    rx = (k**2 - px - qx) % n
    ry = (k*(px - rx) - py) % n
    return (rx, ry)

a = 497
b = 1768
p = 9739

P = (493, 5564)
Q = (1539, 4742)
R = (4403, 5202)

A = point_addition(P, P, a, p)
B = point_addition(A, Q, a, p)
C = point_addition(B, R, a, p)
print(f"{C}")