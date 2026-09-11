# 2.Inverted Right-Angled Triangle in Python
# * * * * *
# * * * *
# * * *
# * *
# *

row = int(input("Enter the number of rows: "))

for i in range(1,row+1):
    for j in range(i,row+1):
        print("*",end=" ")
    print()
