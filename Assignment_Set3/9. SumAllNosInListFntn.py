# 9. Write a Python function to sum all the numbers in a list.

from functools import reduce

def sumofnumbers(numbers):
    sum = 0
    for items in numbers:
        sum += items
    return sum

print(sumofnumbers([1,2,3,4,5]))

# OR

list1 = [1,2,3,4,5]
print(reduce(lambda x,y:x+y,list1))
