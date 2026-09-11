# 4 Write a program to check whether two strings are anagrams.

string1 = input("Enter a string: ")
string2 = input("Enter another string: ")

# string1 = string1.replace(" ","").lower()
# string2 = string2.replace(" ","").lower()

string1 = sorted(string1)
string2 = sorted(string2)

if string1 == string2:
    print("The two strings are Anagrams")
else:
    print("The two strings are not Anagrams")