row = int(input("Enter number of rows: "))
for i in range(1,row+1):
    for s in range(row-i):
        print(" ",end = " ")
    for j in range(2*i-1):
        print("*", end = " ")
    print()