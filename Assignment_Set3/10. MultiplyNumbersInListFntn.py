# 10. Write a Python function to multiply all the numbers in a list.
from functools import reduce

def multiply(numbers):
    m = 1
    for item in numbers:
        m *= item
    return m

print(multiply([1,2,3,4,5]))

mylist = [1,2,3,4,5]
m = reduce(lambda x,y:x*y,mylist)
print(m)



