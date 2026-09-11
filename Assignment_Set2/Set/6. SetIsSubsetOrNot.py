# 6. Write a program to check whether one set is a subset of another.

set1 = {3, 4}
set2 = {1, 2, 3, 4}

issubset = all(item in set2 for item in set1)
print(issubset)



