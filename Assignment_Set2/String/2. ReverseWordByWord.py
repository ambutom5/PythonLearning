string = "I am a developer"
s = ""
words = string.split()
for i in range(len(words)-1,-1,-1):
    s = s + words[i] + " "
print(s.strip())

print(" ".join(string.split()[::-1]))

print(" ".join(reversed(string.split())))
