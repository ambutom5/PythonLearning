# 3. Write a program to count the frequency of each word in a sentence using a
# dictionary.

sentence = "Python is a high high level level language."
words = sentence.title().split()
freq = {}

for word in words:
    if word not in freq:
        freq[word] = 1
    else:
        freq[word] += 1

for key,value in freq.items():
    print(key,":",value)


