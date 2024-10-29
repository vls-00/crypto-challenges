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

def rsa_decrypt(ciphertext, d, N):
    return modular_pow(ciphertext, d, N)
    

e = 65537
N = 882564595536224140639625987659416029426239230804614613279163
d = 121832886702415731577073962957377780195510499965398469843281
ciphertext = 77578995801157823671636298847186723593814843845525223303932

print(f'Flag: {rsa_decrypt(ciphertext, d, N)}')