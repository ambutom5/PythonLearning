# 9. Write a program to check whether a string is a palindrome without using
# slicing.

mystring = "madame"
mystring = mystring.lower()

length = len(mystring)
flag = 1

for i in range(length//2):
    if mystring[i] != mystring[length - i - 1]:
        print("Not Palindrome!")
        break
else:
    print("Palindrome!")


