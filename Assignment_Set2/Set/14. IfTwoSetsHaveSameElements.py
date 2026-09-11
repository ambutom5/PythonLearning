# 14.Write a program to check whether two sets contain exactly the same elements.

set1 = {1, 2, 3, 4}
set2 = {3, 4, 1, 2}

flag = True

if len(set1) != len(set2):
    flag = False
else:
    for item in set1:
        if item not in set2:
            flag = False

print(flag)

# OR
# sameornot = ({x for x in set1 if x in set2} & {y for y in set2 if y in set1})
# print(sameornot)
#
# if len(sameornot) == len(set1) == len(set2):
#     print("Sets have Exact Same Elements!")
# else:
#     print("Sets are Not Equal")
#

# OR


# issameornot = ({x for x in set1 if x in set2} == set1) and ({y for y in set2 if y in set1}==set2)
# print(issameornot)




