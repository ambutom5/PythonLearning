# 1. Write a program to find the union of two sets without using the union()
# method.

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

union = set1.copy()
union.update(set2)

print(union)
print(type(union))




