def phi_for_primes(p, q):
    return (p - 1) * (q - 1)

p = 857504083339712752489993810777
q = 1029224947942998075080348647219

print(f'Flag: {phi_for_primes(p, q)}')