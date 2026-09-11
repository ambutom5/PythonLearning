mylist = [1,2,3,4,5]
square =[]

squares = [num ** 2 for num in mylist]
print(squares)

cubes = [num ** 3 for num in mylist]
print(cubes)

nextnum = [num + 1 for num in mylist]
print(nextnum)

nextnum1 = [num * 5 for num in mylist]
print(nextnum1)