def least_distance(a,b,c):
    numbers = sorted([a,b,c])
    a = numbers[0]
    b = numbers[1]
    c = numbers[2]
    deff1 = abs(c - b)
    deff2 = abs(c - a)
    deff3 = abs(b - a)
    return min(deff1, deff2, deff3)
    
print(least_distance(1,19,5))
    
