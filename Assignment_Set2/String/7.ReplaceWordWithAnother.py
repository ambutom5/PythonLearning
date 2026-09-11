# 7 Write a program to replace all occurrences of a given word with another word in a sentence
# without using the replace() method.

sentence = "Java is a high level language"
newsentn = ""
oldw = "Java"
neww = "Python"

words = sentence.split()

for i in range(len(words)):
    if words[i] == oldw:
        words[i] = neww

newsentn = " ".join(words)
print(newsentn)


