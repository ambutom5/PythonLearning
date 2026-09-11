# 24.Write a program to print all words in a sentence that start with a vowel.

mystring = "This is a python program"

words = mystring.split()

print(words)

for word in words:
   if word[0] in 'aeiouAEIOU':
        print(word)

