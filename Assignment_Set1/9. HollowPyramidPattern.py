# 9. Hollow Pyramid pattern in Python

row = int(input("Enter the number of rows: "))

for i in range(1,row+1):
    for s in range(row-i):
        print(" ",end=" ")
    for j in range(1,2*i):
        if j == 1 or j == 2*i-1 or (i==row and j%2==1) :
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
