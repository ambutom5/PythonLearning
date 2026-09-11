# Number Patterns
# Enter number of rows: 5
# 1 2 3 4 5
# 2 3 4 5
# 3 4 5
# 4 5
# 5

rows = int(input("Enter number of rows: "))
for i in range(1,rows+1):
    for j in range(i,rows+1):
        print(j, end = " ")
    print()