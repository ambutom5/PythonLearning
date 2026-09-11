# 1. Write a program to count the frequency of each element in a tuple.

mytuple = (1,2,3,1,4,5,3,1)
freq = {}

for item in mytuple:
    if item not in freq:
        freq[item] = 1
    else:
        freq[item] += 1

for key,value in freq.items():
    print(key,":",value)

    