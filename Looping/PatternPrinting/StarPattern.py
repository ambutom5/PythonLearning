# RightTrianglePattern
# Enter number of rows: 5
# *
# * *
# * * *
# * * * *
# * * * * *

row = int(input("Enter number of rows: "))
for i in range(1,row+1):
    print("* " *i)