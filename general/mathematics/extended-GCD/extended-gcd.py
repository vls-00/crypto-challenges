def gcd_extended(a, b):
    if a == 0:
        return 0, 1

    new_x, new_y = gcd_extended(b % a, a)

    x = new_y - (b//a) * new_x
    y = new_x

    return x, y
        
    
print(f'u, v = {gcd_extended(32321, 26513)}')