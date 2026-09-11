# 4. Inverted Pyramid Pattern

row = int(input("Enter the number of rows: "))

for i in range(row,0,-1):
    for s in range(row-i):
        print(" ",end=" ")
    for j in range(2*i-1):
        print("*",end=" ")
    print()

