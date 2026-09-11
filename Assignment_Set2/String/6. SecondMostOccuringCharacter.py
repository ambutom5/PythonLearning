# 6. Write a program to find the second most frequently occurring character in a
# string

mystring = "programmming"
mydict = {}

for char in mystring:
    if char not in mydict:
        mydict[char] = 1
    else:
        mydict[char] += 1

# for key,value in mydict.items():
#     print(key,":",value)

sort = sorted(mydict.items(),key = lambda x:x[1],reverse=True)
print(sort)

print(f"Second Most Occuring Char is {sort[1][0]} : {sort[1][1]}")

# mostfreqw = None
# mostfreqf = 0
# secondfreqw = None
# secondfreqf = 0
#
# for char in mydict:
#     if mydict[char] > mostfreqf:
#         secondfreqf = mostfreqf
#         secondfreqw = mostfreqw
#
#         mostfreqf = mydict[char]
#         mostfreqw = char
#
#     elif mydict[char] > secondfreqf and mydict[char] != mostfreqf:
#         secondfreqf = mydict[char]
#         secondfreqw = char
#
# print()
# print(secondfreqw,":",secondfreqf)





