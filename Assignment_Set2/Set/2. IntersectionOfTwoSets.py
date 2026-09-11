# 2. Write a program to find the intersection of two sets without using the
# intersection() method.

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

intersection = {item for item in set1 if item in set2}
print(intersection)

