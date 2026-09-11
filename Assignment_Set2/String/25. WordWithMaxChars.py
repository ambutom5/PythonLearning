# Write a program to find the word with the maximum number of characters in
# a sentence.

sentence = "This is a pythonnnn program"
words = sentence.split()
max = 0
maxword = None


for word in words:
    if len(word)> max:
        max = len(word)
        maxword = word

print(maxword,max)