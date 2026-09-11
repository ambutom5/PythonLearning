# 7. Hollow Right-Angled Triangle in Python
# HollowRightAngledTriangle
# Enter the number of rows: 5
# *
# * *
# *   *
# *     *
# * * * * *

row = int(input("Enter the number of rows: "))

for i in range(1,row+1):
    for j in range(1,i+1):
        if j == 1 or j == i or i == row:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
    