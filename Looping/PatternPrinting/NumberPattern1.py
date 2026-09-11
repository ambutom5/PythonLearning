# NumberPattern
# Enter the number of rows: 5
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

row = int(input("Enter the number of rows: "))

for i in range(1,row+1):
    for j in range(i):
        print(i,end=" ")
    print()