# NumberPattern
# 15 14 13 12 11
# 10 9 8 7
# 6 5 4
# 3 2
# 1

row = int(input("Enter the limit: "))
num = 15
for i in range(1,row+1):
    for j in range(i,row+1):
        print(num,end=" ")
        num -= 1
    print()