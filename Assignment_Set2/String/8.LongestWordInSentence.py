# 8. Write a program to find the longest word in a sentence.

sentence = "Java is a high level language"
words = sentence.split()

length = 0
longest = ""
for word in words:
    if len(word) > length:
        length = len(word)
        longest = word
print(longest)


# OR


# mydict = {}
# length = 0
#
# for word in words:
#     if len(word) > length:
#         mydict[word] = len(word)
#         length = len(word)
#
# for key,value in mydict.items():
#     if value == length:
#         print(key)








