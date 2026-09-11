# 11. Write a Python program to reverse a string.

mystring = "program"
r = ""

for i in range(len(mystring)-1,-1,-1):
    r = r + mystring[i]
print(r)

