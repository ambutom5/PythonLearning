# Purpose: Finds all matches and returns them as a list of strings.
# Use re.findall() when you want all matches, but only the text itself(not positions).

import re

sentence = "Introduction to to python pgmg"
x = re.findall("to",sentence)
y = re.findall("is",sentence)
print(x)
print(y)

result = re.findall(r"\d","A0B1 B078")                         # Find all digits
print(result)

result = re.findall(r"\w+","A0B1 B078")                        # Find all words
print(result)

result = re.findall(r"([a-zA-Z])","A0BB1 B078")                # Find letters
print(result)

result = re.findall(r"([a-zA-Z])\1","A0BB1 B078")              # Find repeating letters
print(result)