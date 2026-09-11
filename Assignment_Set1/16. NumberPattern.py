# 54321
# 5432
# 543
# 54
# 5

row = 5
for i in range(row,0,-1):
    for j in range(row,row-i,-1):
        print(j,end="")
    print()


s = "54321"
for i in range(5,0,-1):
    print(s[0:i])


