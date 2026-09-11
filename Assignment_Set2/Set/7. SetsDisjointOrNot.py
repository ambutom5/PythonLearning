# 7. Write a program to check whether two sets are disjoint.

set1 = {7, 8, 5, 6}
set2 = {1, 2, 3, 4}

union = {x for x in set1 if x in set2}
print(union)

if(len(union)==0):
    print("The sets are disjoint")
else:
    print("The sets are not disjoint")


