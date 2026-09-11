import re

sentence = "Pyttthon is a hhigh levell pgmng langauge"
pattern = r"([a-zA-Z0-9])\1{2}"   # match a character repeated 3 times

matches = list(re.finditer(pattern, sentence))

if matches:
    for m in matches:
        print(m.group(0))   # full match, e.g. "ttt"
        print(m.group(1))   # just the repeating character, e.g. "t"
else:
    print(-1)


# For two repeats: ([a-zA-Z0-9])\1
# For three repeats: ([a-zA-Z0-9])\1{2}
# For n repeats: ([a-zA-Z0-9])\1{n-1}