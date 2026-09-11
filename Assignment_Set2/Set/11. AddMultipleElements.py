# 11.Write a program to add multiple elements to a set without using the update()
# method.

myset = {1,2,3,4,5}
elements = [5,6,7]

myset = myset | {x for x in elements}

print(myset)

