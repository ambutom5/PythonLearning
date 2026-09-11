# 4. Write a program to find the frequency of each element in a list.

mylist = [1,2,3,2,4,5,1,3,1,1]
freq ={}

for item in mylist:
    if item not in freq:
        freq[item] = 1
    else:
        freq[item] += 1

for key,value in freq.items():
    print(key,":",value)
