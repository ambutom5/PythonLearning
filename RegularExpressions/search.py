# Purpose: Finds the first match of a pattern in a string.
# Returns: A match object (or None if not found).
# Use re.search() when you only care about the first occurrence.

import re

sentence = "Introduction to, to, python pgmg"
x = re.search("to",sentence)
y = re.search("hello",sentence)

print(x)
print(y)

print((x.start(),x.end()))

result = re.search(r"[.,]",sentence)
print(result)

