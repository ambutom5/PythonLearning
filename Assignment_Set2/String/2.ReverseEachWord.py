# 2. Write a program to reverse each word in a sentence without
#    changing the order of the words.

sentence = "This is a Sentence"
words = sentence.split()
print(words)

reversedwords = [word[::-1] for word in words]
print(reversedwords)

print("Original sentence is : ",sentence)
print("Reversed sentence is : ",
      " ".join(reversedwords))


# OR
#
# sentence = "Python Is Easy To Learn and Use"
#
# mysentence = " ".join(word[::-1] for word in sentence.split())
#
# print(mysentence)





