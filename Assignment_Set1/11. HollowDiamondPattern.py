# 11. Hollow Diamond pattern in Python

row = int(input("Enter the number of rows: "))

for i in range(1,row+1):
    for s in range(row-i):
        print(" ",end=" ")
    for j in range(2*i-1):
        if j == 0 or j == 2*i-2:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

for i in range(row-1,0,-1):
    for s in range(row-i):
        print(" ",end=" ")
    for j in range(2*i-1):
        if j == 0 or j == 2 * i - 2:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()