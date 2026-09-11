# 21. Create a function to generate a list of squares of numbers from 1 to n using list
# comprehension.

def squares(x):
    sq = [x**2 for x in range(1,x+1)]
    return sq

print(squares(10))

