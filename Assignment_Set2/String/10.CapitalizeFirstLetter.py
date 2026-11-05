# 10.Write a program to capitalize the first letter of each word without using the
# title() method.

sentence = "python is a high level language"
words = sentence.split()
capitalwords = []

for word in words:
    capitalwords.append(word[0].upper()+word[1:])
print(" ".join(capitalwords))

result = " ".join(word[0].upper()+word[1:] for word in sentence.split())
print(result)


# OR

for i in range(len(words)):

    words[i]=words[i].capitalize()

print(" ".join(words))