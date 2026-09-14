import numpy

arr = [1,2,3,4,5]

def arrays(arr):
    rev = arr[::-1]
    b = numpy.array(rev,float)
    return b

result = arrays(arr)
print(result)