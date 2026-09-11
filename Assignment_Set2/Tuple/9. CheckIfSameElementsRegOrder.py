# 9. Write a program to check whether two tuples contain the same elements
# regardless of order.

tuple1 = (1,2,3,4,5)
tuple2 = (5,3,4,2,1)

if set(tuple1) == set(tuple2):
    print("Same Elements")
else:
    print("Different elements")
