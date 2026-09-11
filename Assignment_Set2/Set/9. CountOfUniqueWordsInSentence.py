# 9. Write a program to count the number of unique words in a sentence.

sentence = "This is is a a python program"
words = sentence.upper().split()

unique = set(words)
print(unique)
print("Number of unique words: ",len(unique))


