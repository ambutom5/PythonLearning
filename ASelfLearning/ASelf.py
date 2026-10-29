sentence = "Python is a high high level level language."

words = sentence.split()

freq = {}

# for word in words:
#     if word not in freq:
#         freq[word] = 1
#     else:
#         freq[word] += 1

for word in words:
    freq[word] = freq.get(word,0)+1

print(freq)
