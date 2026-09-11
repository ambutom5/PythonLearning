# Number Patterns
# Enter number of rows: 5
# 1 1 1 1 1
# 2 2 2 2
# 3 3 3
# 4 4
# 5

rows = int(input("Enter number of rows: "))
for i in range(1,rows+1):
    for j in range(i,rows+1):
        print(i, end = " ")
    print()