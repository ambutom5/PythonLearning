# 4. Write a program to find the symmetric difference without using the
# symmetric_difference() method.

set1 = {3, 4, 5, 6}
set2 = {1, 2, 3, 4}

symmdiff = {x for x in set1 if x not in set2} | {y for y in set2 if y not in set1}

print(symmdiff)

