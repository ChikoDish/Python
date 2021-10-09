def leat_distance(a,b,c):
    numbers = sorted([a,b,c])
    a = numbers[0]
    b = numbers[1]
    c = numbers[2]
    deff1 = abs(c - b)
    deff2 = abs(c - a)
    deff3 = abs(b - a)
    print(deff1 , deff2 , deff3)
    if deff1 < deff2 and deff1 < deff3:
        return deff1
    elif deff1 > deff2 and deff2 < deff3:
        return deff2
    else:
        return deff3
    
print(leat_distance(13,19,25))
    