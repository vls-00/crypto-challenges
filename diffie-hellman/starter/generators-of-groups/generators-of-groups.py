p = 28151

for g in range(2, p):
    H = []
    for n in range (0, p-1):
        H.add(pow(g, n ,p)) 
    
    if len(H) == p - 1:
        print(f'Found it: {g}')
        break