# 18.Write a program to remove all duplicate words from a sentence while
# maintaining their original order.

sentence = "This is a sample python python program program"
mylist = []
words = sentence.split()

for word in words:
    if word not in mylist:
        mylist.append(word)

print(" ".join(mylist))


