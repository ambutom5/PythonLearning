# 8. Write a Python function to find the maximum of three numbers.

maximum = lambda x,y,z:x if(x > y and x > z) else y if(y > z) else z
print(maximum(5,9,7))

def maxi(x,y,z):
    if x > y and x >z:
        return x
    elif y > z:
        return y
    else:
        return z
print(maxi(5,9,7))