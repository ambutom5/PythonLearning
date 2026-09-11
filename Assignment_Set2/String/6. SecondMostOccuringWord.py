# 6. Write a program to find the second most frequently occurring word in a
# string

sentence = ("Python is an OOP language. "
            "Python is simple and is easy to learn and use")

words = sentence.split()
mydict = {}

for word in words:
    mydict[word] = mydict.get(word,0)+1

sortedlist = sorted(mydict.items(),key = lambda x:x[1],reverse=True)
print(sortedlist)

print(f"Second Most Occuring Word is {sortedlist[1][0]} : {sortedlist[1][1]}")


# for word in words:
#     if word not in mydict:
#         mydict[word] = 1
#     else:
#         mydict[word] += 1

# Return nth most frequent (1 = most frequent, 2 = second, etc.)
# n=2
# if n<=len(sortedlist):
#     word, count = sortedlist[n - 1]
#     print(word, ":", count)

