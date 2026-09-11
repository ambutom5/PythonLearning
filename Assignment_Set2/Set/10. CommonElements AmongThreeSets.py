# 10.Write a program to find the common elements among three sets.

set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}
set3 = {5, 6, 7, 8, 9}

common = {x for x in set1 if x in set2 and x in set3}

print(common)

