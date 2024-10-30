def phi_for_primes(p, q):
    return (p - 1) * (q - 1)

def modular_m_inverse(exponent, phi_N):
    if exponent == 0:
        return 0, 1

    new_x, new_y = modular_m_inverse(phi_N % exponent, exponent)

    x = new_y - (phi_N//exponent) * new_x
    y = new_x

    return x, y
    

p = 857504083339712752489993810777
q = 1029224947942998075080348647219
e = 65537
phi_N = phi_for_primes(p, q)

print(f'Flag: {modular_m_inverse(e, phi_N)}')