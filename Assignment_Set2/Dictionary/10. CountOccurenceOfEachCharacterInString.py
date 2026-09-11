# 10.Write a program to count the number of occurrences of each character in a
# string using a dictionary.

mystr = "banana"
mydict = {}

for char in mystr:
    if char in mydict:
        mydict[char] += 1
    else:
        mydict[char] = 1

print(mydict)
for key,value in mydict.items():
    print(key,":",value)

