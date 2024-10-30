import primefac
from sympy import factorint
from Crypto.Util.number import inverse, long_to_bytes

def modular_pow(base, exponent, modulus):
    if modulus == 1:
        return 0
    
    result = 1
    base = base % modulus
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
            
        exponent = exponent // 2
        base = (base * base) % modulus
    
    return result
    
n = 984994081290620368062168960884976209711107645166770780785733
e = 65537
ct = 948553474947320504624302879933619818331484350431616834086273

p, q = factorint(n)
phi = (p - 1) * (q - 1)
d = inverse(e, phi)

decrypted = modular_pow(ct, d, n)

print(f'Flag: {long_to_bytes(decrypted).decode('ascii')}')