def gcd(a, b):
    big = a
    small = b
    
    if a < b:
        big = b
        small = a
        
    while(1):
        remainder = big % small
        
        if remainder == 0:
            return small
        
        big = small
        small = remainder
        
    
print(gcd(66528, 52920))