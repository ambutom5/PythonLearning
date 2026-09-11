# 23.Write a program to check whether two strings are equal without using the ==
# operator.

string1 = "This is a python program"
string2 = "This is a python program"
flag = True

if len(string1) != len(string2):
    flag = False
else:
    for i in range(len(string1)):
        if string1[i]!=string2[i]:
            break

if flag == True:
    print("Strings are equal!")
else:
    print("Strings are not equal!")
    