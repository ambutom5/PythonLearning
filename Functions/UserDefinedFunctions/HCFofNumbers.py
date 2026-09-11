def calculate_hcf(x,y):
    if x<y:
        smallest = x
    else:
        smallest = y

    for i in range(1,smallest+1):
        if x % i == 0 and y % i == 0:
            hcf = i

    return hcf

print(calculate_hcf(12,15))