# 13.Write a program to convert a tuple into a list, sort it, and convert it back into
# a tuple.

mytuple = (8,2,3,5,1,4,7,6)
mylist = sorted(list(mytuple))
# mylist.sort(reverse=True)                           # For Sorting in Descending Order
print(mylist)

newtuple = tuple(mylist)
print(newtuple)

# OR                                                  # For Sorting in Descending Order

# mytuple = (8,2,3,5,1,4,7,6)
# mylist = list(mytuple)
#
# mylist.sort(reverse=True)
# print(mylist)
#
# newtuple = tuple(mylist)
# print(newtuple)
