row = int(input("Enter number of rows: "))
for i in range(row,0,-1):
    for s in range(row-i):
        print(" ",end = " ")
    for j in range(2*i-1):
        print("*", end = " ")
    print()

# OR

# for i in range(row):
#     for s in range(i):
#         print(" ",end = " ")
#     for j in range(2*(row-i)-1):
#         print("*", end = " ")
#     print()