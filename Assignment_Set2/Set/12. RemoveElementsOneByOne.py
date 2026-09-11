# 12.Write a program to remove all elements from a set one by one.

myset = {1,2,3,4,5}
print(myset)

for item in list(myset):
    myset.remove(item)

print(myset)







# Why list(my_set) is used
# When you iterate directly over a set (or any collection)
# and modify it at the same time, Python raises a RuntimeError
# because the set’s size changes during iteration.
#
# To avoid this, we make a copy of the set first:
# list(my_set) creates a separate list containing the same elements.
# We then safely loop over that list while removing elements from the original set.