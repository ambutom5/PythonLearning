# 13.Write a program to find the first non-repeating character in a string using a
# dictionary.

string = "proposal"
mydict = {}

for char in string:
    if char not in mydict:
        mydict[char] = 1
    else:
        mydict[char] += 1

for key,value in mydict.items():
    if value == 1:
        print(key,":",value)
        break

