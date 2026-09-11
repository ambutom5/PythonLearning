# 15. Inverted Number Pyramid in Python

# 1 2 3 4 5 4 3 2 1
#   1 2 3 4 3 2 1
#     1 2 3 2 1
#       1 2 1
#         1

row = int(input("Enter the number of rows: "))

for i in range(row,0,-1):
    for s in range(row-i):
        print(" ",end=" ")
    for j in range(1,i+1):
        print(j,end=" ")
    for j in range(i-1,0,-1):
        print(j,end=" ")
    print()