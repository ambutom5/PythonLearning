# 2. Write a program to merge two tuples without using the + operator.

tuple1 = (1,2,3,4,5)
tuple2 = (6,7,8,9,10)

list1 = list(tuple1)
list2 = list(tuple2)

list1.extend(list2)
print(list1)
print(tuple(list1))


