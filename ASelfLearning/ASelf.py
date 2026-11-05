sentence = "This is a pythonnnn program"
words = sentence.split()
longestw = ""

for word in words:
    if len(word) > len(longestw):
        longestw = word

print(longestw)