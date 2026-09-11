# 3. Write a program to find the difference between two sets.

set1 = {3, 4, 5, 6}
set2 = {1, 2, 3, 4}

difference = {item for item in set1 if item not in set2}
print(difference)

